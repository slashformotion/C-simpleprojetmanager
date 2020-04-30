# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_win.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(796, 739)
        self.act_Quit = QAction(MainWindow)
        self.act_Quit.setObjectName(u"act_Quit")
        self.act_Deploy = QAction(MainWindow)
        self.act_Deploy.setObjectName(u"act_Deploy")
        self.act_Test = QAction(MainWindow)
        self.act_Test.setObjectName(u"act_Test")
        self.act_Reload = QAction(MainWindow)
        self.act_Reload.setObjectName(u"act_Reload")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.area_main = QFrame(self.centralwidget)
        self.area_main.setObjectName(u"area_main")
        self.area_main.setEnabled(True)
        self.area_main.setGeometry(QRect(10, 10, 771, 671))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.area_main.sizePolicy().hasHeightForWidth())
        self.area_main.setSizePolicy(sizePolicy)
        self.area_main.setFrameShape(QFrame.StyledPanel)
        self.area_main.setFrameShadow(QFrame.Sunken)
        self.horizontalLayoutWidget_2 = QWidget(self.area_main)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(450, 620, 308, 41))
        self.area_workspace_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.area_workspace_2.setObjectName(u"area_workspace_2")
        self.area_workspace_2.setContentsMargins(0, 0, 0, 0)
        self.btn_reload = QPushButton(self.horizontalLayoutWidget_2)
        self.btn_reload.setObjectName(u"btn_reload")

        self.area_workspace_2.addWidget(self.btn_reload)

        self.btn_test = QPushButton(self.horizontalLayoutWidget_2)
        self.btn_test.setObjectName(u"btn_test")

        self.area_workspace_2.addWidget(self.btn_test)

        self.btn_deploy = QPushButton(self.horizontalLayoutWidget_2)
        self.btn_deploy.setObjectName(u"btn_deploy")

        self.area_workspace_2.addWidget(self.btn_deploy)

        self.area_generator = QScrollArea(self.area_main)
        self.area_generator.setObjectName(u"area_generator")
        self.area_generator.setGeometry(QRect(10, 250, 751, 181))
        self.area_generator.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 749, 179))
        self.gridLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 721, 161))
        self.grly_edit = QGridLayout(self.gridLayoutWidget)
        self.grly_edit.setObjectName(u"grly_edit")
        self.grly_edit.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.grly_edit.addItem(self.verticalSpacer, 5, 0, 1, 1)

        self.lied_class0 = QLineEdit(self.gridLayoutWidget)
        self.lied_class0.setObjectName(u"lied_class0")

        self.grly_edit.addWidget(self.lied_class0, 1, 2, 1, 1)

        self.lbl_module_name = QLabel(self.gridLayoutWidget)
        self.lbl_module_name.setObjectName(u"lbl_module_name")

        self.grly_edit.addWidget(self.lbl_module_name, 0, 0, 1, 1)

        self.lied_namespace0 = QLineEdit(self.gridLayoutWidget)
        self.lied_namespace0.setObjectName(u"lied_namespace0")

        self.grly_edit.addWidget(self.lied_namespace0, 1, 1, 1, 1)

        self.lbl__namespace = QLabel(self.gridLayoutWidget)
        self.lbl__namespace.setObjectName(u"lbl__namespace")

        self.grly_edit.addWidget(self.lbl__namespace, 0, 1, 1, 1)

        self.lbl_class_name = QLabel(self.gridLayoutWidget)
        self.lbl_class_name.setObjectName(u"lbl_class_name")

        self.grly_edit.addWidget(self.lbl_class_name, 0, 2, 1, 1)

        self.lied_mod0 = QLineEdit(self.gridLayoutWidget)
        self.lied_mod0.setObjectName(u"lied_mod0")

        self.grly_edit.addWidget(self.lied_mod0, 1, 0, 1, 1)

        self.lied_mod1 = QLineEdit(self.gridLayoutWidget)
        self.lied_mod1.setObjectName(u"lied_mod1")

        self.grly_edit.addWidget(self.lied_mod1, 2, 0, 1, 1)

        self.lied_namespace1 = QLineEdit(self.gridLayoutWidget)
        self.lied_namespace1.setObjectName(u"lied_namespace1")

        self.grly_edit.addWidget(self.lied_namespace1, 2, 1, 1, 1)

        self.lied_class1 = QLineEdit(self.gridLayoutWidget)
        self.lied_class1.setObjectName(u"lied_class1")

        self.grly_edit.addWidget(self.lied_class1, 2, 2, 1, 1)

        self.lied_mod2 = QLineEdit(self.gridLayoutWidget)
        self.lied_mod2.setObjectName(u"lied_mod2")

        self.grly_edit.addWidget(self.lied_mod2, 3, 0, 1, 1)

        self.lied_namespace2 = QLineEdit(self.gridLayoutWidget)
        self.lied_namespace2.setObjectName(u"lied_namespace2")

        self.grly_edit.addWidget(self.lied_namespace2, 3, 1, 1, 1)

        self.lied_class2 = QLineEdit(self.gridLayoutWidget)
        self.lied_class2.setObjectName(u"lied_class2")

        self.grly_edit.addWidget(self.lied_class2, 3, 2, 1, 1)

        self.area_generator.setWidget(self.scrollAreaWidgetContents)
        self.area_mode = QFrame(self.area_main)
        self.area_mode.setObjectName(u"area_mode")
        self.area_mode.setGeometry(QRect(10, 100, 151, 131))
        self.area_mode.setFrameShape(QFrame.Panel)
        self.area_mode.setFrameShadow(QFrame.Sunken)
        self.hrly_setup = QHBoxLayout(self.area_mode)
        self.hrly_setup.setObjectName(u"hrly_setup")
        self.lbl_mode = QLabel(self.area_mode)
        self.lbl_mode.setObjectName(u"lbl_mode")

        self.hrly_setup.addWidget(self.lbl_mode)

        self.cbb_mode = QComboBox(self.area_mode)
        self.cbb_mode.addItem("")
        self.cbb_mode.addItem("")
        self.cbb_mode.setObjectName(u"cbb_mode")

        self.hrly_setup.addWidget(self.cbb_mode)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hrly_setup.addItem(self.horizontalSpacer)

        self.area_workspace = QFrame(self.area_main)
        self.area_workspace.setObjectName(u"area_workspace")
        self.area_workspace.setGeometry(QRect(10, 10, 751, 81))
        self.area_workspace.setFrameShape(QFrame.StyledPanel)
        self.area_workspace.setFrameShadow(QFrame.Sunken)
        self.area_workspace.setLineWidth(1)
        self.horizontalLayout = QHBoxLayout(self.area_workspace)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_workspace = QLabel(self.area_workspace)
        self.lbl_workspace.setObjectName(u"lbl_workspace")
        self.lbl_workspace.setMouseTracking(False)

        self.horizontalLayout.addWidget(self.lbl_workspace)

        self.lbl_path_workspace = QLabel(self.area_workspace)
        self.lbl_path_workspace.setObjectName(u"lbl_path_workspace")
        self.lbl_path_workspace.setStyleSheet(u"border:2;")

        self.horizontalLayout.addWidget(self.lbl_path_workspace)

        self.tbtn_set_path_workspace = QToolButton(self.area_workspace)
        self.tbtn_set_path_workspace.setObjectName(u"tbtn_set_path_workspace")

        self.horizontalLayout.addWidget(self.tbtn_set_path_workspace)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.vfra_modules_existants = QFrame(self.area_main)
        self.vfra_modules_existants.setObjectName(u"vfra_modules_existants")
        self.vfra_modules_existants.setGeometry(QRect(570, 100, 191, 131))
        self.vfra_modules_existants.setFrameShape(QFrame.Panel)
        self.vfra_modules_existants.setFrameShadow(QFrame.Sunken)
        self.verticalLayout = QVBoxLayout(self.vfra_modules_existants)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_modules_existant = QLabel(self.vfra_modules_existants)
        self.lbl_modules_existant.setObjectName(u"lbl_modules_existant")

        self.verticalLayout.addWidget(self.lbl_modules_existant)

        self.liwd_modules_existant = QListWidget(self.vfra_modules_existants)
        self.liwd_modules_existant.setObjectName(u"liwd_modules_existant")

        self.verticalLayout.addWidget(self.liwd_modules_existant)

        self.area_main_file = QFrame(self.area_main)
        self.area_main_file.setObjectName(u"area_main_file")
        self.area_main_file.setGeometry(QRect(170, 100, 381, 131))
        self.area_main_file.setFrameShape(QFrame.Panel)
        self.area_main_file.setFrameShadow(QFrame.Sunken)
        self.hrly_setup_2 = QHBoxLayout(self.area_main_file)
        self.hrly_setup_2.setObjectName(u"hrly_setup_2")
        self.lbl_main_file = QLabel(self.area_main_file)
        self.lbl_main_file.setObjectName(u"lbl_main_file")

        self.hrly_setup_2.addWidget(self.lbl_main_file)

        self.lied_main_file = QLineEdit(self.area_main_file)
        self.lied_main_file.setObjectName(u"lied_main_file")
        self.lied_main_file.setMinimumSize(QSize(70, 0))

        self.hrly_setup_2.addWidget(self.lied_main_file)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hrly_setup_2.addItem(self.horizontalSpacer_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 796, 22))
        self.menuFenetre = QMenu(self.menubar)
        self.menuFenetre.setObjectName(u"menuFenetre")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.cbb_mode, self.area_generator)
        QWidget.setTabOrder(self.area_generator, self.lied_namespace0)
        QWidget.setTabOrder(self.lied_namespace0, self.lied_class0)
        QWidget.setTabOrder(self.lied_class0, self.lied_mod0)
        QWidget.setTabOrder(self.lied_mod0, self.btn_deploy)
        QWidget.setTabOrder(self.btn_deploy, self.lied_namespace1)
        QWidget.setTabOrder(self.lied_namespace1, self.lied_mod1)
        QWidget.setTabOrder(self.lied_mod1, self.lied_class1)
        QWidget.setTabOrder(self.lied_class1, self.lied_namespace2)
        QWidget.setTabOrder(self.lied_namespace2, self.lied_class2)
        QWidget.setTabOrder(self.lied_class2, self.lied_mod2)
        QWidget.setTabOrder(self.lied_mod2, self.btn_test)

        self.menubar.addAction(self.menuFenetre.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menuFenetre.addAction(self.act_Quit)
        self.menuEdit.addAction(self.act_Reload)
        self.menuEdit.addAction(self.act_Test)
        self.menuEdit.addAction(self.act_Deploy)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.act_Quit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
#if QT_CONFIG(shortcut)
        self.act_Quit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.act_Deploy.setText(QCoreApplication.translate("MainWindow", u"Deploy", None))
#if QT_CONFIG(shortcut)
        self.act_Deploy.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
        self.act_Test.setText(QCoreApplication.translate("MainWindow", u"Test", None))
#if QT_CONFIG(shortcut)
        self.act_Test.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+T", None))
#endif // QT_CONFIG(shortcut)
        self.act_Reload.setText(QCoreApplication.translate("MainWindow", u"Reload", None))
#if QT_CONFIG(shortcut)
        self.act_Reload.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.btn_reload.setText(QCoreApplication.translate("MainWindow", u"Reload", None))
        self.btn_test.setText(QCoreApplication.translate("MainWindow", u"Test", None))
        self.btn_deploy.setText(QCoreApplication.translate("MainWindow", u"Deploy", None))
        self.lied_class0.setText("")
        self.lbl_module_name.setText(QCoreApplication.translate("MainWindow", u"Module Name", None))
        self.lied_namespace0.setText("")
        self.lbl__namespace.setText(QCoreApplication.translate("MainWindow", u"Namespace", None))
        self.lbl_class_name.setText(QCoreApplication.translate("MainWindow", u"Class", None))
        self.lied_mod0.setText("")
        self.lbl_mode.setText(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.cbb_mode.setItemText(0, QCoreApplication.translate("MainWindow", u"Create", None))
        self.cbb_mode.setItemText(1, QCoreApplication.translate("MainWindow", u"Add", None))

        self.lbl_workspace.setText(QCoreApplication.translate("MainWindow", u"Workspace : ", None))
        self.lbl_path_workspace.setText(QCoreApplication.translate("MainWindow", u"/path/to/workspace", None))
        self.tbtn_set_path_workspace.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.lbl_modules_existant.setText(QCoreApplication.translate("MainWindow", u"Modules existants", None))
        self.lbl_main_file.setText(QCoreApplication.translate("MainWindow", u"Main File : ", None))
        self.menuFenetre.setTitle(QCoreApplication.translate("MainWindow", u"Fenetre", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
    # retranslateUi

