import sys
import os
import serial
import binascii
import serial.tools.list_ports
import datetime as dt
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ui_demo_1 import Ui_Form
from datetime import datetime

rec_data=''


class Pyqt5_Serial(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(Pyqt5_Serial, self).__init__()
        self.setupUi(self)
        self.init()
        self.setWindowTitle("数据解析")
        self.ser = serial.Serial()
        self.port_check()
        # 接收数据和发送数据数目置零
        self.data_num_received = 0
        self.lineEdit.setText(str(self.data_num_received))
        self.frameNumble='11'
        self.receive_data1 = ''
        self.receive_data2 = ''
        self.right_numble = 0
        self.seconds = 0
        self.list_data1 = []
    def init(self):
        # 串口检测按钮
        self.s1__box_1.clicked.connect(self.port_check)

        # 串口信息显示
        self.s1__box_2.currentTextChanged.connect(self.port_imf)

        # 打开串口按钮
        self.open_button.clicked.connect(self.port_open)

        # 关闭串口按钮
        self.close_button.clicked.connect(self.port_close)

        # 定时器接收数据
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.data_receive)

        #定时存储
        self.save_timer = QTimer(self)
        self.save_timer.timeout.connect(self.currtime)

        #开始接收数据
        self.start_rec.clicked.connect(self.start_receivedata)

        #设置定时器时间
        self.settime.clicked.connect(self.show_lcd)


    #    self.select_button.clicked.connect(self.open_files)

    def show_lcd(self):
        get_time=int(self.timetext.currentText())
        show_time=str(get_time)+ ':' + '0'+'0'
        self.timedisplay.display(show_time)

    def open_files(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)
        if dialog.exec():
            self.filenames = dialog.selectedFiles()
            f = open(self.filenames[0],encoding='utf-8',mode='a')
            f.writelines('\n')


    #开始接收数据
    def start_receivedata(self):
        self.port_open()
        self.start_time = QDateTime.currentDateTime()
        self.save_timer.start(500)
    #    self.timer.start(300)
        self.start_rec.setEnabled(False)
        str_time = self.start_time.toString("hh_mm_ss")
        file_name = self.textEdit.toPlainText()
        desktop_path = "D:\\" + file_name + "\\"
        if not os.path.exists(desktop_path):
            os.makedirs(desktop_path)
    #    os.mkdir(desktop_path)
        self.address1 = desktop_path +  '_' + self.s1__box_2.currentText() + '_' +file_name +  '.txt'
        self.address2 = desktop_path + '_'  +  self.s1__box_2.currentText() + '_raw_data' + '_' + file_name +  '.txt'
        f = open(self.address1, 'a')
        f.close()
        f = open(self.address2, 'a')
        f.close()
    #接收定时器结束
    def currtime(self):

        self.stop_time = QDateTime.currentDateTime()
        str_curr = self.stop_time.toString("yyyy-MM-dd hh:mm:ss")
        str_start = self.start_time.toString("yyyy-MM-dd hh:mm:ss")
        startTime = datetime.strptime(str_start,"%Y-%m-%d %H:%M:%S")
        endTime   = datetime.strptime(str_curr,"%Y-%m-%d %H:%M:%S")
        self.seconds = self.seconds + 1
        toget_time = int(self.timetext.currentText())
        need_time = 120 * toget_time
        if self.seconds > need_time :
            self.save_timer.stop()
            self.timer.stop()
            self.start_rec.setEnabled(True)
        #    f = open(self.address1, 'a')
        #    f.writelines('\n')
        #    f.close()
            self.port_close()
            self.seconds = 0
            QMessageBox.information(self, '提示', '数据读写完成', QMessageBox.Yes , QMessageBox.Yes)
            return

        display_seconds = (self.seconds//2) % 60
        display_minute  = (self.seconds//2) // 60
        show_time = str(display_minute) + ':' + str(display_seconds)
        self.timedisplay.display(show_time)


    # 串口检测
    def port_check(self):
        # 检测所有存在的串口，将信息存储在字典中
        self.Com_Dict = {}
        port_list = list(serial.tools.list_ports.comports())
        self.s1__box_2.clear()
        for port in port_list:
            self.Com_Dict["%s" % port[0]] = "%s" % port[1]
            self.s1__box_2.addItem(port[0])
        if len(self.Com_Dict) == 0:
            self.state_label.setText(" 无串口")

    # 串口信息
    def port_imf(self):
        # 显示选定的串口的详细信息
        imf_s = self.s1__box_2.currentText()
        if imf_s != "":
            self.state_label.setText(self.Com_Dict[self.s1__box_2.currentText()])

    # 打开串口
    def port_open(self):

        self.ser.port = self.s1__box_2.currentText()
        self.ser.baudrate = int(self.s1__box_3.currentText())
        self.ser.bytesize = int(self.s1__box_4.currentText())
        self.ser.stopbits = int(self.s1__box_6.currentText())
        self.ser.parity = self.s1__box_5.currentText()

        try:
            self.ser.open()
        except:
            QMessageBox.critical(self, "Port Error", "此串口不能被打开！")
            return None
        # 打开串口接收定时器，周期为2ms
        self.timer.start(100)
    #    self.get_time()

        if self.ser.isOpen():
            self.open_button.setEnabled(False)
            self.close_button.setEnabled(True)
            self.formGroupBox1.setTitle("串口状态（已开启）")

    # 关闭串口
    def port_close(self):
        self.save_timer.stop()
        self.timer.stop()
        try:
            self.ser.close()
        except:
            pass
        self.open_button.setEnabled(True)
        self.close_button.setEnabled(False)
        self.start_rec.setEnabled(True)
        # 接收数据和发送数据数目置零
        self.seconds = 0
        self.data_num_received = 0
        self.lineEdit.setText(str(self.data_num_received))

        self.formGroupBox1.setTitle("串口状态（已关闭）")


    # 接收数据
    def data_receive(self):
        try:
            num = self.ser.inWaiting()
        except:
            self.port_close()
            return None
        finish_flag = False
        if num > 10:
            data = self.ser.read(num)
            lenth_data = len(data)
            out_s = ''
            for i in range(0, len(data)):
                out_s = out_s + '{:02X}'.format(data[i]) + ' '
            f = open(self.address2, 'a')
            f.writelines(out_s)
            f.close()

            i = 0
            while (i < lenth_data - 8):
                if data[i] == 0xAA and data[i + 1] == 0xAA and data[i + 2] == 0x04 and data[i+3] == 0x80:
                    need_data = 256 * data[i + 5] + data[i + 6]
                    if(need_data > 32768):
                        need_data = need_data -65536
                    self.list_data1 .append(str(need_data))
                elif data[i] == 0xAA and data[i + 1] == 0xAA and data[i+2] == 0x20 and data[i+3]== 0x02 :
                    if data[i+4] == 0x00:
                        finish_flag = True
                    elif data[i+5] != 0x00:
                        self.list_data1 = []
                        self.port_close()
                        self.save_timer.stop()
                        replay = QMessageBox.warning(self, '警告', '接收有无效数据,检查传感器', QMessageBox.Yes,QMessageBox.Yes)
                        if replay == QMessageBox.Yes:
                            self.save_timer.start()
                            self.port_open()
                i = i + 1

            # 统计接收字符的数量
            if finish_flag :
                len_list = len(self.list_data1 )
                f = open(self.address1, 'a')
                j = 0
                while(j<len_list):
                    f.writelines(self.list_data1 [j])
                    f.writelines('\n')
                    j = j +1
                f.close()
                self.list_data1 = []


        #    print(len_list)
            self.data_num_received += num
            self.lineEdit.setText(str(self.data_num_received))
        else:
            pass



    def get_time(self):
        now_time = dt.datetime.now().strftime('%F %T')
        print(now_time)
        f = open('D:/test.txt', 'a')
        f.writelines(now_time+':')
        f.writelines('\n')
        f.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myshow = Pyqt5_Serial()
    myshow.show()
    sys.exit(app.exec_())
