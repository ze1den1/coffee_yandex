# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddForm(object):
    def setupUi(self, AddForm):
        AddForm.setObjectName("AddForm")
        AddForm.resize(439, 573)
        self.gridLayout_2 = QtWidgets.QGridLayout(AddForm)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.volume = QtWidgets.QSpinBox(AddForm)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.volume.setFont(font)
        self.volume.setMaximum(999999999)
        self.volume.setObjectName("volume")
        self.gridLayout.addWidget(self.volume, 6, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(AddForm)
        self.label_3.setMinimumSize(QtCore.QSize(0, 50))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 1, 1, 1)
        self.roasting_edit = QtWidgets.QLineEdit(AddForm)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.roasting_edit.setFont(font)
        self.roasting_edit.setObjectName("roasting_edit")
        self.gridLayout.addWidget(self.roasting_edit, 4, 1, 1, 1)
        self.id_edit = QtWidgets.QLineEdit(AddForm)
        self.id_edit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.id_edit.setFont(font)
        self.id_edit.setObjectName("id_edit")
        self.gridLayout.addWidget(self.id_edit, 2, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel(AddForm)
        self.label_5.setMinimumSize(QtCore.QSize(0, 50))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 1, 1, 1)
        self.name_edit = QtWidgets.QLineEdit(AddForm)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.name_edit.setFont(font)
        self.name_edit.setObjectName("name_edit")
        self.gridLayout.addWidget(self.name_edit, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(AddForm)
        self.label_2.setMinimumSize(QtCore.QSize(0, 50))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.price = QtWidgets.QSpinBox(AddForm)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.price.setFont(font)
        self.price.setMaximum(999999999)
        self.price.setObjectName("price")
        self.gridLayout.addWidget(self.price, 6, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(AddForm)
        self.label_4.setMinimumSize(QtCore.QSize(0, 50))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(AddForm)
        self.label_6.setMinimumSize(QtCore.QSize(0, 50))
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 1, 1, 1)
        self.coffee_type = QtWidgets.QRadioButton(AddForm)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.coffee_type.setFont(font)
        self.coffee_type.setObjectName("coffee_type")
        self.gridLayout.addWidget(self.coffee_type, 9, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(AddForm)
        self.label_7.setMinimumSize(QtCore.QSize(0, 50))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 7, 0, 1, 2)
        self.label = QtWidgets.QLabel(AddForm)
        self.label.setMinimumSize(QtCore.QSize(0, 50))
        self.label.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.taste = QtWidgets.QTextEdit(AddForm)
        self.taste.setMinimumSize(QtCore.QSize(0, 200))
        self.taste.setMaximumSize(QtCore.QSize(16777215, 400))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.taste.setFont(font)
        self.taste.setObjectName("taste")
        self.gridLayout.addWidget(self.taste, 8, 0, 1, 2)
        self.execute = QtWidgets.QPushButton(AddForm)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.execute.setFont(font)
        self.execute.setObjectName("execute")
        self.gridLayout.addWidget(self.execute, 9, 1, 1, 1)
        self.check = QtWidgets.QLineEdit(AddForm)
        self.check.setMaximumSize(QtCore.QSize(0, 0))
        self.check.setObjectName("check")
        self.gridLayout.addWidget(self.check, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(AddForm)
        QtCore.QMetaObject.connectSlotsByName(AddForm)

    def retranslateUi(self, AddForm):
        _translate = QtCore.QCoreApplication.translate
        AddForm.setWindowTitle(_translate("AddForm", "Add or Edit"))
        self.label_3.setText(_translate("AddForm", "Степень обжарки"))
        self.label_5.setText(_translate("AddForm", "Объём (мл)"))
        self.label_2.setText(_translate("AddForm", "Название сорта"))
        self.label_4.setText(_translate("AddForm", "Цена (р)"))
        self.label_6.setText(_translate("AddForm", "ID, которого нет в таблице."))
        self.coffee_type.setText(_translate("AddForm", "Молотый (1), в зернах (0)"))
        self.label_7.setText(_translate("AddForm", "Описание вкуса"))
        self.label.setText(_translate("AddForm", "ID изменяемого кофе ИЛИ"))
        self.execute.setText(_translate("AddForm", "Применить"))
