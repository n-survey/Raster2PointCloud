# -*- coding: utf-8 -*-

import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QMessageBox
from PyQt5.QtGui import QFont
from PIL import Image

import tkinter
from tkinter import messagebox as tkMessageBox
from tkinter import filedialog as tkFileDialog
from tkinter import messagebox

root = tkinter.Tk()
root.withdraw()

class Dialog(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
#--------------------------------------------------------------------------------------------------------
        self.setObjectName("self")
        self.setEnabled(True)
        self.resize(375, 311)
        self.setMinimumSize(QtCore.QSize(200, 40))
        self.setMaximumSize(QtCore.QSize(400, 400))
        self.gazo = QtWidgets.QPushButton(self)
        self.gazo.setEnabled(True)
        self.gazo.setGeometry(QtCore.QRect(10, 10, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.gazo.setFont(font)
        self.gazo.setWhatsThis("")
        self.gazo.setCheckable(False)
        self.gazo.setAutoExclusive(False)
        self.gazo.setAutoDefault(True)
        self.gazo.setDefault(False)
        self.gazo.setObjectName("gazo")
        self.vbs = QtWidgets.QPushButton(self)
        self.vbs.setEnabled(True)
        self.vbs.setGeometry(QtCore.QRect(10, 280, 111, 21))
        self.vbs.setWhatsThis("")
        self.vbs.setAutoExclusive(False)
        self.vbs.setAutoDefault(True)
        self.vbs.setDefault(False)
        self.vbs.setObjectName("vbs")
        self.label_x = QtWidgets.QLabel(self)
        self.label_x.setGeometry(QtCore.QRect(60, 40, 111, 21))
        self.label_x.setFrameShape(QtWidgets.QFrame.Box)
        self.label_x.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_x.setText("")
        self.label_x.setAlignment(QtCore.Qt.AlignCenter)
        self.label_x.setObjectName("label_x")
        self.label_y = QtWidgets.QLabel(self)
        self.label_y.setGeometry(QtCore.QRect(250, 40, 111, 21))
        self.label_y.setFrameShape(QtWidgets.QFrame.Box)
        self.label_y.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_y.setText("")
        self.label_y.setAlignment(QtCore.Qt.AlignCenter)
        self.label_y.setObjectName("label_y")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(15, 40, 41, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(205, 40, 41, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(15, 70, 41, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(205, 70, 41, 20))
        self.label_4.setObjectName("label_4")
        self.lineEdit_x = QtWidgets.QLineEdit(self)
        self.lineEdit_x.setGeometry(QtCore.QRect(60, 70, 111, 20))
        self.lineEdit_x.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_x.setObjectName("lineEdit_x")
        self.lineEdit_y = QtWidgets.QLineEdit(self)
        self.lineEdit_y.setGeometry(QtCore.QRect(250, 70, 111, 20))
        self.lineEdit_y.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_y.setObjectName("lineEdit_y")
        self.label_file = QtWidgets.QLabel(self)
        self.label_file.setGeometry(QtCore.QRect(90, 10, 271, 21))
        self.label_file.setToolTip("")
        self.label_file.setFrameShape(QtWidgets.QFrame.Box)
        self.label_file.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_file.setText("")
        self.label_file.setObjectName("label_file")
        self.conv = QtWidgets.QPushButton(self)
        self.conv.setEnabled(True)
        self.conv.setGeometry(QtCore.QRect(130, 280, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.conv.setFont(font)
        self.conv.setWhatsThis("")
        self.conv.setCheckable(False)
        self.conv.setAutoExclusive(False)
        self.conv.setAutoDefault(True)
        self.conv.setDefault(False)
        self.conv.setObjectName("conv")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(15, 130, 41, 20))
        self.label_5.setObjectName("label_5")
        self.lineEdit_z = QtWidgets.QLineEdit(self)
        self.lineEdit_z.setGeometry(QtCore.QRect(60, 130, 111, 20))
        self.lineEdit_z.setInputMask("")
        self.lineEdit_z.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_z.setObjectName("lineEdit_z")
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(15, 100, 41, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(205, 100, 41, 20))
        self.label_7.setObjectName("label_7")
        self.lineEdit_dy = QtWidgets.QLineEdit(self)
        self.lineEdit_dy.setGeometry(QtCore.QRect(250, 100, 111, 20))
        self.lineEdit_dy.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_dy.setObjectName("lineEdit_dy")
        self.lineEdit_dx = QtWidgets.QLineEdit(self)
        self.lineEdit_dx.setGeometry(QtCore.QRect(60, 100, 111, 20))
        self.lineEdit_dx.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_dx.setObjectName("lineEdit_dx")
        self.checkBox1 = QtWidgets.QCheckBox(self)
        self.checkBox1.setGeometry(QtCore.QRect(10, 162, 91, 16))
        self.checkBox1.setObjectName("checkBox1")
        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(110, 160, 16, 20))
        self.label_8.setObjectName("label_8")
        self.lineEdit_rh = QtWidgets.QLineEdit(self)
        self.lineEdit_rh.setGeometry(QtCore.QRect(130, 160, 51, 20))
        self.lineEdit_rh.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit_rh.setInputMask("")
        self.lineEdit_rh.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_rh.setObjectName("lineEdit_rh")
        self.label_9 = QtWidgets.QLabel(self)
        self.label_9.setGeometry(QtCore.QRect(200, 160, 16, 20))
        self.label_9.setObjectName("label_9")
        self.lineEdit_gh = QtWidgets.QLineEdit(self)
        self.lineEdit_gh.setGeometry(QtCore.QRect(220, 160, 51, 20))
        self.lineEdit_gh.setInputMask("")
        self.lineEdit_gh.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_gh.setObjectName("lineEdit_gh")
        self.label_10 = QtWidgets.QLabel(self)
        self.label_10.setGeometry(QtCore.QRect(290, 160, 16, 20))
        self.label_10.setObjectName("label_10")
        self.lineEdit_bh = QtWidgets.QLineEdit(self)
        self.lineEdit_bh.setGeometry(QtCore.QRect(310, 160, 51, 21))
        self.lineEdit_bh.setInputMask("")
        self.lineEdit_bh.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_bh.setObjectName("lineEdit_bh")
        self.label_11 = QtWidgets.QLabel(self)
        self.label_11.setGeometry(QtCore.QRect(290, 190, 16, 20))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self)
        self.label_12.setGeometry(QtCore.QRect(200, 190, 16, 20))
        self.label_12.setObjectName("label_12")
        self.lineEdit_gb = QtWidgets.QLineEdit(self)
        self.lineEdit_gb.setGeometry(QtCore.QRect(220, 190, 51, 20))
        self.lineEdit_gb.setInputMask("")
        self.lineEdit_gb.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_gb.setObjectName("lineEdit_gb")
        self.lineEdit_bb = QtWidgets.QLineEdit(self)
        self.lineEdit_bb.setGeometry(QtCore.QRect(310, 190, 51, 21))
        self.lineEdit_bb.setInputMask("")
        self.lineEdit_bb.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_bb.setObjectName("lineEdit_bb")
        self.checkBox2 = QtWidgets.QCheckBox(self)
        self.checkBox2.setGeometry(QtCore.QRect(10, 192, 91, 16))
        self.checkBox2.setObjectName("checkBox2")
        self.label_13 = QtWidgets.QLabel(self)
        self.label_13.setGeometry(QtCore.QRect(110, 190, 16, 20))
        self.label_13.setObjectName("label_13")
        self.lineEdit_rb = QtWidgets.QLineEdit(self)
        self.lineEdit_rb.setGeometry(QtCore.QRect(130, 190, 51, 20))
        self.lineEdit_rb.setInputMask("")
        self.lineEdit_rb.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_rb.setObjectName("lineEdit_rb")
        self.lineEdit_ba = QtWidgets.QLineEdit(self)
        self.lineEdit_ba.setGeometry(QtCore.QRect(310, 220, 51, 21))
        self.lineEdit_ba.setInputMask("")
        self.lineEdit_ba.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_ba.setObjectName("lineEdit_ba")
        self.lineEdit_ga = QtWidgets.QLineEdit(self)
        self.lineEdit_ga.setGeometry(QtCore.QRect(220, 220, 51, 20))
        self.lineEdit_ga.setInputMask("")
        self.lineEdit_ga.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_ga.setObjectName("lineEdit_ga")
        self.label_14 = QtWidgets.QLabel(self)
        self.label_14.setGeometry(QtCore.QRect(200, 220, 16, 20))
        self.label_14.setObjectName("label_14")
        self.lineEdit_ra = QtWidgets.QLineEdit(self)
        self.lineEdit_ra.setGeometry(QtCore.QRect(130, 220, 51, 20))
        self.lineEdit_ra.setInputMask("")
        self.lineEdit_ra.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_ra.setObjectName("lineEdit_ra")
        self.label_15 = QtWidgets.QLabel(self)
        self.label_15.setGeometry(QtCore.QRect(290, 220, 16, 20))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self)
        self.label_16.setGeometry(QtCore.QRect(110, 220, 16, 20))
        self.label_16.setObjectName("label_16")
        self.conv2 = QtWidgets.QPushButton(self)
        self.conv2.setEnabled(True)
        self.conv2.setGeometry(QtCore.QRect(250, 280, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.conv2.setFont(font)
        self.conv2.setWhatsThis("")
        self.conv2.setCheckable(False)
        self.conv2.setAutoExclusive(False)
        self.conv2.setAutoDefault(True)
        self.conv2.setDefault(False)
        self.conv2.setObjectName("conv2")
        self.las_dir = QtWidgets.QPushButton(self)
        self.las_dir.setEnabled(True)
        self.las_dir.setGeometry(QtCore.QRect(10, 250, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.las_dir.setFont(font)
        self.las_dir.setWhatsThis("")
        self.las_dir.setCheckable(False)
        self.las_dir.setAutoExclusive(False)
        self.las_dir.setAutoDefault(True)
        self.las_dir.setDefault(False)
        self.las_dir.setObjectName("las_dir")
        self.label_txt2las = QtWidgets.QLabel(self)
        self.label_txt2las.setGeometry(QtCore.QRect(90, 250, 271, 21))
        self.label_txt2las.setToolTip("")
        self.label_txt2las.setFrameShape(QtWidgets.QFrame.Box)
        self.label_txt2las.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_txt2las.setText("")
        self.label_txt2las.setObjectName("label_txt2las")

        self.lineEdit_x.returnPressed.connect(self.lineEdit_y.setFocus)
        self.lineEdit_y.returnPressed.connect(self.lineEdit_dx.setFocus)
        self.lineEdit_bb.returnPressed.connect(self.lineEdit_ra.setFocus)
        self.lineEdit_dx.returnPressed.connect(self.lineEdit_dy.setFocus)
        self.lineEdit_dy.returnPressed.connect(self.lineEdit_z.setFocus)
        self.lineEdit_rh.returnPressed.connect(self.lineEdit_gh.setFocus)
        self.lineEdit_gh.returnPressed.connect(self.lineEdit_bh.setFocus)
        self.lineEdit_rb.returnPressed.connect(self.lineEdit_gb.setFocus)
        self.lineEdit_gb.returnPressed.connect(self.lineEdit_bb.setFocus)
        self.lineEdit_ra.returnPressed.connect(self.lineEdit_ga.setFocus)
        self.lineEdit_ga.returnPressed.connect(self.lineEdit_ba.setFocus)
        self.lineEdit_ba.returnPressed.connect(self.conv.setFocus)
        self.lineEdit_bh.returnPressed.connect(self.lineEdit_rb.setFocus)
        self.lineEdit_z.returnPressed.connect(self.lineEdit_rh.setFocus)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.setTabOrder(self.gazo, self.lineEdit_x)
        self.setTabOrder(self.lineEdit_x, self.lineEdit_y)
        self.setTabOrder(self.lineEdit_y, self.lineEdit_dx)
        self.setTabOrder(self.lineEdit_dx, self.lineEdit_dy)
        self.setTabOrder(self.lineEdit_dy, self.lineEdit_z)
        self.setTabOrder(self.lineEdit_z, self.checkBox1)
        self.setTabOrder(self.checkBox1, self.lineEdit_rh)
        self.setTabOrder(self.lineEdit_rh, self.lineEdit_gh)
        self.setTabOrder(self.lineEdit_gh, self.lineEdit_bh)
        self.setTabOrder(self.lineEdit_bh, self.checkBox2)
        self.setTabOrder(self.checkBox2, self.lineEdit_rb)
        self.setTabOrder(self.lineEdit_rb, self.lineEdit_gb)
        self.setTabOrder(self.lineEdit_gb, self.lineEdit_bb)
        self.setTabOrder(self.lineEdit_bb, self.lineEdit_ra)
        self.setTabOrder(self.lineEdit_ra, self.lineEdit_ga)
        self.setTabOrder(self.lineEdit_ga, self.lineEdit_ba)
        self.setTabOrder(self.lineEdit_ba, self.conv)
        self.setTabOrder(self.conv, self.conv2)
        self.setTabOrder(self.conv2, self.las_dir)
        self.setTabOrder(self.las_dir, self.vbs)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Raster2PointCloud Ver.2022.03.11"))
        self.gazo.setText(_translate("self", "画像読込"))
        self.vbs.setToolTip(_translate("self", "起動用バッチファイルと、VBScriptを作成します。"))
        self.vbs.setText(_translate("self", "VBS作成"))
        self.label_x.setToolTip(_translate("self", "横のピクセル数"))
        self.label_y.setToolTip(_translate("self", "縦のピクセル数"))
        self.label.setText(_translate("self", "横 (px)"))
        self.label_2.setText(_translate("self", "縦 (px)"))
        self.label_3.setText(_translate("self", "横実寸"))
        self.label_4.setText(_translate("self", "縦実寸"))
        self.lineEdit_x.setToolTip(_translate("self", "横の実寸（m）"))
        self.lineEdit_x.setText(_translate("self", "0"))
        self.lineEdit_y.setToolTip(_translate("self", "縦の実寸（m）"))
        self.lineEdit_y.setText(_translate("self", "0"))
        self.conv.setText(_translate("self", "PointCloud (txt)"))
        self.label_5.setText(_translate("self", "Z 値"))
        self.lineEdit_z.setToolTip(_translate("self", "z値（m）"))
        self.lineEdit_z.setText(_translate("self", "0"))
        self.label_6.setText(_translate("self", "左下X"))
        self.label_7.setText(_translate("self", "左下Y"))
        self.lineEdit_dy.setToolTip(_translate("self", "縦の実寸（m）"))
        self.lineEdit_dy.setText(_translate("self", "0"))
        self.lineEdit_dx.setToolTip(_translate("self", "横の実寸（m）"))
        self.lineEdit_dx.setText(_translate("self", "0"))
        self.checkBox1.setText(_translate("self", "透過色"))
        self.label_8.setText(_translate("self", "R"))
        self.lineEdit_rh.setToolTip(_translate("self", "0～255の整数"))
        self.lineEdit_rh.setText(_translate("self", "255"))
        self.label_9.setText(_translate("self", "G"))
        self.lineEdit_gh.setToolTip(_translate("self", "0～255の整数"))
        self.lineEdit_gh.setText(_translate("self", "255"))
        self.label_10.setText(_translate("self", "B"))
        self.lineEdit_bh.setToolTip(_translate("self", "0～255の整数"))
        self.lineEdit_bh.setText(_translate("self", "255"))
        self.label_11.setText(_translate("self", "B"))
        self.label_12.setText(_translate("self", "G"))
        self.lineEdit_gb.setToolTip(_translate("self", "0～255の整数"))
        self.lineEdit_gb.setText(_translate("self", "0"))
        self.lineEdit_bb.setToolTip(_translate("self", "0～255の整数"))
        self.lineEdit_bb.setText(_translate("self", "0"))
        self.checkBox2.setText(_translate("self", "線色変更"))
        self.label_13.setText(_translate("self", "R"))
        self.lineEdit_rb.setToolTip(_translate("self", "0～255の整数"))
        self.lineEdit_rb.setText(_translate("self", "0"))
        self.lineEdit_ba.setToolTip(_translate("self", "0～255の整数"))
        self.lineEdit_ba.setText(_translate("self", "0"))
        self.lineEdit_ga.setToolTip(_translate("self", "0～255の整数"))
        self.lineEdit_ga.setText(_translate("self", "0"))
        self.label_14.setText(_translate("self", "G"))
        self.lineEdit_ra.setToolTip(_translate("self", "0～255の整数"))
        self.lineEdit_ra.setText(_translate("self", "255"))
        self.label_15.setText(_translate("self", "B"))
        self.label_16.setText(_translate("self", "R"))
        self.conv2.setText(_translate("self", "LAS (laz)"))
        self.las_dir.setText(_translate("self", "txt2las_dir"))
#--------------------------------------------------------------------------------------------------------

        # Raster2PointCloud.iniより設定復元
        sfname = os.path.dirname(__file__) + u'/Raster2PointCloud.ini'
        if not os.path.exists(sfname):
            txt = 'txt2las_dir='
            f = open(sfname, 'w')
            f.write(txt)
            f.close()

        try:
            for line in open(sfname, 'r'):
                dat = line.replace('\n','').split('=')
                if 'txt2las_dir' in line:
                    self.label_txt2las.setText(dat[1])
        except:
            pass

        self.gazo.clicked.connect(self.gazo_open)
        self.conv.clicked.connect(self.convert)
        self.conv2.clicked.connect(self.convert2)
        self.las_dir.clicked.connect(self.LasDir)
        self.vbs.clicked.connect(self.make_vbs)

        if sys.platform == "win32":
            self.vbs.setEnabled(True)
            if self.label_txt2las.text() != "":
                self.label_txt2las.setEnabled(True)
        else:
            self.vbs.setEnabled(False)
            self.label_txt2las.setEnabled(False)

        self.show()

    # 画像読込
    def gazo_open(self):
        gazo_file = tkFileDialog.askopenfilename(filetypes = [(u'画像ファイル','*.*')])
        if not gazo_file:
            return
        dirpath = os.path.dirname(gazo_file)
        filename = os.path.basename(gazo_file)
        fn, ext = os.path.splitext(filename)
        PointCloud_name = os.path.dirname(__file__) + '/' + fn + '.txt'
        img = Image.open(gazo_file)
        rgb_img = img.convert('RGB')
        size = rgb_img.size
        self.label_file.setText(gazo_file)
        self.label_x.setText(str(size[0]))
        self.label_y.setText(str(size[1]))
        self.lineEdit_x.setText(str(size[0]))
        self.lineEdit_y.setText(str(size[1]))
        # ワールドファイルがある場合は、実寸と左下座標を計算する
        # 元データにワールドファイルがある場合は、縦横の実寸・左下座標を計算する
        wf1 = dirpath + '/' + fn + '.wld'                    #wld
        wf2 = dirpath + '/' + fn + ext + 'w'                 #pngw,tifw,jpgw...
        wf3 = dirpath + '/' + fn + ext[0:2] + ext[-1:] + 'w' #pgw,tfw,jgw...
        w = 0
        if os.path.exists(wf1):
            w = 1
        if os.path.exists(wf2):
            w = 2
        if os.path.exists(wf3):
            w = 3
        # ワールドファイルが複数あった場合、QGISの優先順位に会わせる
        # wf1(pgw,tfw,jgw...)→wf2(pngw,tifw,jpgw...)→wf3(wld)
        if w != 0:
            if w == 1:
                world_file = wf1
            if w == 2 :
                world_file = wf2
            if w == 3:
                world_file = wf3
            n = 1
            with open(world_file) as f:
                for line in f:
                    if n == 1:
                        xd = float(line)
                    if n == 4:
                        yd = float(line)
                    if n == 5:
                        yt = float(line)
                    if n == 6:
                        xt = float(line)
                    n = n + 1
            xx = xd * size[0]
            yy = yd * size[1]
            xb = xt + yy
            self.lineEdit_x.setText(str(xx))
            self.lineEdit_y.setText(str(abs(yy)))
            self.lineEdit_dx.setText(str(xb))
            self.lineEdit_dy.setText(str(yt))
        self.lineEdit_x.setFocus()

    # PointCloud 変換
    def convert(self):
        gazo_file = self.label_file.text()

        if gazo_file == '':
            return
        if self.label_x.text() == '':
            return
        if self.label_y.text() == '':
            return
        if self.lineEdit_x.text() == '':
            self.lineEdit_x.setText('0')
        if self.lineEdit_y.text() == '':
            self.lineEdit_y.setText('0')
        if self.lineEdit_z.text() == '':
            self.lineEdit_z.setText('0')
        dirpath = os.path.dirname(gazo_file)
        filename = os.path.basename(gazo_file)
        fn, ext = os.path.splitext(filename)
        PointCloud_name = os.path.dirname(__file__) + '/' + fn + '.txt'
        img = Image.open(gazo_file)
        rgb_img = img.convert('RGB')
        size = rgb_img.size
        txt = ''
        xm = float(self.lineEdit_x.text())
        ym = float(self.lineEdit_y.text())
        dx = float(self.lineEdit_dx.text())
        dy = float(self.lineEdit_dy.text())
        rh = self.lineEdit_rh.text()
        gh = self.lineEdit_gh.text()
        bh = self.lineEdit_bh.text()
        rb = self.lineEdit_rb.text()
        gb = self.lineEdit_gb.text()
        bb = self.lineEdit_bb.text()
        ra = self.lineEdit_ra.text()
        ga = self.lineEdit_ga.text()
        ba = self.lineEdit_ba.text()

        z = self.lineEdit_z.text()
        if os.path.exists(PointCloud_name):
            os.remove(PointCloud_name)
        f = open(PointCloud_name, 'a')
        for x in range(size[0]):
            for y in range(size[1]):
                r,g,b = rgb_img.getpixel((x,y))
                y = int(size[1]) - y
                xn = x / (float(self.label_x.text()) /xm) + dy
                yn = y / (float(self.label_y.text()) /ym) + dx
                if self.checkBox1.isChecked():
                    if rh != str(r) and gh != str(g) and bh != str(b):
                        if self.checkBox2.isChecked():
                            if rb == str(r) and gb == str(g) and bb == str(b):
                                txt = str(xn) + ',' + str(yn) + ',' + z + ',' + ra + ',' + ga + ',' + ba
                            else:
                                txt = str(xn) + ',' + str(yn) + ',' + z + ',' + str(r) + ',' + str(g) + ',' + str(b)
                        else:
                            txt = str(xn) + ',' + str(yn) + ',' + z + ',' + str(r) + ',' + str(g) + ',' + str(b)
                else:
                    if self.checkBox2.isChecked():
                        if rb == str(r) and gb == str(g) and bb == str(b):
                            txt = str(xn) + ',' + str(yn) + ',' + z + ',' + str(r) + ',' + str(g) + ',' + str(b)
                        else:
                            txt = str(xn) + ',' + str(yn) + ',' + z + ',' + ra + ',' + ga + ',' + ba
                    else:
                        txt = str(xn) + ',' + str(yn) + ',' + z + ',' + str(r) + ',' + str(g) + ',' + str(b)
                print(txt, file = f)
        f.close()
        QMessageBox.information(self, u'完了', PointCloud_name + u'を作成しました。')

    # Las 変換
    def convert2(self):
        self.convert()
        gazo_file = self.label_file.text()
        dirpath = os.path.dirname(gazo_file)
        filename = os.path.basename(gazo_file)
        fn, ext = os.path.splitext(filename)
        PointCloud_name = os.path.dirname(__file__) + '/' + fn + '.txt'
        if not os.path.exists(PointCloud_name):
            return
        Las_name = os.path.dirname(__file__) + '/' + fn + '.laz'
        bat_name = os.path.dirname(__file__) + '/las.bat'
        cmd = self.label_txt2las.text() + "txt2las.exe -parse xyzRGB -i " + PointCloud_name + " -o " + Las_name
        f = open(bat_name, 'w')
        f.write(cmd)
        f.close()
        os.system(bat_name)
        QMessageBox.information(self, u'完了', Las_name + u'を作成しました。')

    # txt2las.exe選択
    def LasDir(self):
        txt2las_dir = tkFileDialog.askopenfilename(filetypes = [(u'txt2las.exe選択','txt2las.exe')], initialdir = '')
        if not txt2las_dir:
            return
        self.label_txt2las.setText(str(txt2las_dir).replace('txt2las.exe',''))
        sfname = os.path.dirname(__file__) + u'/Raster2PointCloud.ini'
        txt = 'txt2las_dir=' + self.label_txt2las.text()
        f = open(sfname,'w')
        f.write(txt)
        f.close()

    # 起動用バッチファイル
    def make_vbs(self):
        python_path = tkFileDialog.askopenfilename(filetypes = [(u'python.exe選択','python.exe')], initialdir = '')
        if not python_path:
            return
        batname = os.path.dirname(__file__) + '/run.bat'
        bat_text = '"' + python_path.replace('/', '\\') + '"' + ' ' + '"' + os.path.dirname(__file__) + u'\\convert.py' + '"'
        fname = open(batname, 'w')
        fname.write(bat_text)
        fname.close()
        vbsname = os.path.dirname(__file__) + '/Raster2PointCloud.vbs'
        vbs_text = 'Dim oShell\n'
        vbs_text = vbs_text + 'Set oShell = WScript.CreateObject (' + '"' + 'WSCript.shell' + '"' + ')\n'
        vbs_text = vbs_text + 'oShell.run ' +  '"' + batname.replace('/', '\\') + '"' + ',0\n'
        vbs_text = vbs_text + 'Set oShell = Nothing'
        fname = open(vbsname, 'w')
        fname.write(vbs_text)
        fname.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Dialog()
    sys.exit(app.exec_())
