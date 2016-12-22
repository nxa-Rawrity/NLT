# -*- coding: utf-8 -*-
## SET UP LOGGING ##
import logging
logging.basicConfig(filename='debug.log', level=logging.DEBUG)

from PyQt4 import QtCore, QtGui
######-------- CUSTOM VARIABLE DECLARATIONS AND START FUNCTIONS---------##############

import os, sys, shutil, psutil, subprocess, time
import _winreg

logging.info('Declaring Variables')
testConf = 'settings-test.conf'
betaConf = 'settings-beta.conf'
stageConf = 'settings-staging.conf'
defaultConf = 'settings.conf'
envLabel = 'ENV'

extCheck = False
advCheck = False

curDir = os.curdir
confDir = os.path.join(curDir,'conf')

logExt = ['.log', '.log.1', '.log.2', '.log.3']
hostsLoc = 'C:\Windows\System32\drivers\etc\HOSTS'
hostsLocTest = '.\hosts\HOSTS'

##### BETA and STAGING No longer require host settings for extenal machines.
##### '#' has been added to betaHostsOn and stageHostsOn.  Remove the '#' to enable host
betaHostsOn = ['#8.31.102.78 accounts-beta.nexon.net\n',
               '#8.31.102.78 games-beta.nexon.net\n',
               '#8.31.102.78 api-beta.nexon.net\n']

betaHostsOff = ['#8.31.102.78 accounts-beta.nexon.net\n',
                '#8.31.102.78 games-beta.nexon.net\n',
                '#8.31.102.78 api-beta.nexon.net\n']

stageHostsOn = ['#208.85.109.173 games-stage.nexon.net\n',
                '#208.85.109.173 accounts-stage.nexon.net\n',
                '#208.85.109.173 api-stage.nexon.net\n']

stageHostsOff = ['#208.85.109.173 games-stage.nexon.net\n',
                 '#208.85.109.173 accounts-stage.nexon.net\n',
                 '#208.85.109.173 api-stage.nexon.net\n']

cdnHostOn = '208.85.109.165 cdn.nexon.net\n'

cdnHostOff = '#208.85.109.165 cdn.nexon.net\n'

aboutLoc = '.\hosts\ABOUT'
logLoc = '.\debug.log'

appdataLoc = os.getenv('APPDATA')
appdataPath = os.path.join(appdataLoc,'NexonLauncher')
eulafile = 'eula.db'

utilLoc ='.\util'
dfcLoc = os.path.join(utilLoc, 'DFC.bat')

tempContent = 'blank'
showAbout = False
fontPath = '.\css\KlavikaNX-Bold.otf'
showVersion = True

logging.info('Variables Declared')


try:
    logging.info('Obtaining NxL Registry Key')
    root_key=_winreg.OpenKey(_winreg.HKEY_CURRENT_USER, r'SOFTWARE\Nexon Launcher', 0, _winreg.KEY_READ)
    pathname=_winreg.QueryValueEx(root_key,"Install Directory")
    _winreg.CloseKey(root_key)
    logging.info('Key Obtained')
except pathname == "":
    logging.warning('Key Not Obtained')
if "" == pathname:
    raise WindowsError



###########-------------- END CUSTOM VARIABLES AND START FUNCTIONS-------##############
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(QtGui.QWidget):
    #####--------- INTIALIZER --------------#####
    def __init__(self):
        logging.info('Initializing QWidget')
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        logging.info('QWidget Initialized')


    def setupUi(self, Form):
        logging.info('Setting up UI')
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(354, 189)
        Form.setMinimumSize(QtCore.QSize(354, 189))
        Form.setMaximumSize(QtCore.QSize(354, 189))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        font.setPointSize(8)
        Form.setFont(font)

        nxFont = QtGui.QFontDatabase.addApplicationFont(fontPath)

        if nxFont < 0:
            logging.info('unable to load font')

        logging.info('Obtaining CSS')
        css = './css/darkorange.stylesheet.txt'
        with open(css, 'r') as cssFile:
            Form.setStyleSheet(cssFile.read())
        logging.info('CSS Applied')

        self.verticalLayout_4 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.MainSection = QtGui.QVBoxLayout()
        self.MainSection.setObjectName(_fromUtf8("MainSection"))
        self.Title_LBL = QtGui.QLabel(Form)
        titleFont = QtGui.QFont()
        titleFont.setFamily("Century Gothic")
        titleFont.setPointSize(20)
        self.Title_LBL.setFont(titleFont)
        self.Title_LBL.setAlignment(QtCore.Qt.AlignCenter)
        self.Title_LBL.setObjectName(_fromUtf8("Title_LBL"))
        self.Title_LBL.setFixedSize(QtCore.QSize(334,33))
        self.MainSection.addWidget(self.Title_LBL)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(48, -1, -1, -1)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.EnvText_LBL = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        font.setPointSize(10)
        self.EnvText_LBL.setFont(font)
        self.EnvText_LBL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.EnvText_LBL.setObjectName(_fromUtf8("EnvText_LBL"))
        self.horizontalLayout_2.addWidget(self.EnvText_LBL)
        self.Env_LBL = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Env_LBL.setFont(font)
        self.Env_LBL.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Env_LBL.setObjectName(_fromUtf8("Env_LBL"))
        self.Env_LBL.setStyleSheet('color: #ffaa00')
        self.horizontalLayout_2.addWidget(self.Env_LBL)
        self.Restart_BTN = QtGui.QPushButton(Form)
        self.Restart_BTN.setMaximumSize(QtCore.QSize(22, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Restart_BTN.setFont(font)
        self.Restart_BTN.setToolTip(_fromUtf8(""))
        self.Restart_BTN.setIconSize(QtCore.QSize(16, 16))
        self.Restart_BTN.setObjectName(_fromUtf8("Restart_BTN"))
        self.horizontalLayout_2.addWidget(self.Restart_BTN)
        self.MainSection.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.EnvSelect_LBL = QtGui.QLabel(Form)
        self.EnvSelect_LBL.setMaximumSize(QtCore.QSize(10000, 15))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        font.setPointSize(16)
        self.EnvSelect_LBL.setFont(font)
        self.EnvSelect_LBL.setFrameShape(QtGui.QFrame.NoFrame)
        self.EnvSelect_LBL.setLineWidth(0)
        self.EnvSelect_LBL.setAlignment(QtCore.Qt.AlignCenter)
        self.EnvSelect_LBL.setObjectName(_fromUtf8("EnvSelect_LBL"))
        self.verticalLayout_2.addWidget(self.EnvSelect_LBL)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.Test_BTN = QtGui.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Test_BTN.setFont(font)
        self.Test_BTN.setObjectName(_fromUtf8("Test_BTN"))
        self.Test_BTN.setFixedSize(QtCore.QSize(80,22))
        self.horizontalLayout_3.addWidget(self.Test_BTN)
        self.Beta_BTN = QtGui.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Beta_BTN.setFont(font)
        self.Beta_BTN.setObjectName(_fromUtf8("Beta_BTN"))
        self.Beta_BTN.setFixedSize(QtCore.QSize(80,22))
        self.horizontalLayout_3.addWidget(self.Beta_BTN)
        self.Stage_BTN = QtGui.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Stage_BTN.setFont(font)
        self.Stage_BTN.setObjectName(_fromUtf8("Stage_BTN"))
        self.Stage_BTN.setFixedSize(QtCore.QSize(80,22))
        self.horizontalLayout_3.addWidget(self.Stage_BTN)
        self.Live_BTN = QtGui.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Live_BTN.setFont(font)
        self.Live_BTN.setObjectName(_fromUtf8("Live_BTN"))
        self.Live_BTN.setFixedSize(QtCore.QSize(80,22))
        self.horizontalLayout_3.addWidget(self.Live_BTN)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.ExtMachine_BOX = QtGui.QCheckBox(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        self.ExtMachine_BOX.setFont(font)
        self.ExtMachine_BOX.setObjectName(_fromUtf8("ExtMachine_BOX"))
        self.horizontalLayout_4.addWidget(self.ExtMachine_BOX)
        self.ClearLog_BOX = QtGui.QCheckBox(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        self.ClearLog_BOX.setFont(font)
        self.ClearLog_BOX.setObjectName(_fromUtf8("ClearLog_BOX"))
        self.horizontalLayout_4.addWidget(self.ClearLog_BOX)
        self.Location_DRP = QtGui.QComboBox(Form)
        self.Location_DRP.setObjectName(_fromUtf8("Location_DRP"))
        self.Location_DRP.addItem(_fromUtf8(""))
        self.Location_DRP.addItem(_fromUtf8(""))
        self.Location_DRP.addItem(_fromUtf8(""))
        self.horizontalLayout_4.addWidget(self.Location_DRP)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.MainSection.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.MainSection)
        self.HostsSection = QtGui.QVBoxLayout()
        self.HostsSection.setObjectName(_fromUtf8("HostsSection"))
        self.line = QtGui.QFrame(Form)
        self.line.setLineWidth(2)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.HostsSection.addWidget(self.line)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.AdvSettings_BOX = QtGui.QCheckBox(Form)
        self.AdvSettings_BOX.setObjectName(_fromUtf8("checkBox"))
        self.horizontalLayout.addWidget(self.AdvSettings_BOX)
        self.HostsSection.addLayout(self.horizontalLayout)
        self.advSettingsTabs = QtGui.QTabWidget(Form)
        self.advSettingsTabs.setTabPosition(QtGui.QTabWidget.North)
        self.advSettingsTabs.setTabShape(QtGui.QTabWidget.Rounded)
        self.advSettingsTabs.setObjectName(_fromUtf8("advSettingsTabs"))
        self.files = QtGui.QWidget()
        self.files.setObjectName(_fromUtf8("files"))
        self.hostsTextEdit = QtGui.QPlainTextEdit(self.files)
        self.hostsTextEdit.setEnabled(True)
        self.hostsTextEdit.setGeometry(QtCore.QRect(0, 40, 329, 270))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hostsTextEdit.sizePolicy().hasHeightForWidth())
        self.hostsTextEdit.setSizePolicy(sizePolicy)
        self.hostsTextEdit.setMaximumSize(QtCore.QSize(329, 270))
        self.hostsTextEdit.setAutoFillBackground(True)
        self.hostsTextEdit.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.hostsTextEdit.setBackgroundVisible(True)
        self.hostsTextEdit.setCenterOnScroll(True)
        self.hostsTextEdit.setObjectName(_fromUtf8("hostsTextEdit"))
        self.adjFiles_DRP = QtGui.QComboBox(self.files)
        self.adjFiles_DRP.setGeometry(QtCore.QRect(0, 10, 131, 21))
        self.adjFiles_DRP.setAcceptDrops(False)
        self.adjFiles_DRP.setEditable(False)
        self.adjFiles_DRP.setObjectName(_fromUtf8("adjFiles_DRP"))
        self.adjFiles_DRP.addItem(_fromUtf8(""))
        self.adjFiles_DRP.addItem(_fromUtf8(""))
        self.adjFiles_DRP.addItem(_fromUtf8(""))
        self.Apply_BTN = QtGui.QPushButton(self.files)
        self.Apply_BTN.setGeometry(QtCore.QRect(230, 10, 100, 22))
        self.Apply_BTN.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Apply_BTN.setObjectName(_fromUtf8("Apply_BTN"))
        self.advSettingsTabs.addTab(self.files, _fromUtf8(""))
        self.logs = QtGui.QWidget()
        self.logs.setObjectName(_fromUtf8("logs"))
        self.logs_DRP = QtGui.QComboBox(self.logs)
        self.logs_DRP.setGeometry(QtCore.QRect(0, 10, 151, 22))
        self.logs_DRP.setObjectName(_fromUtf8("logs_DRP"))
        self.logs_DRP.addItem(_fromUtf8(""))
        self.logs_DRP.addItem(_fromUtf8(""))
        self.logs_DRP.addItem(_fromUtf8(""))
        self.logs_DRP.addItem(_fromUtf8(""))
        self.logViewer = QtGui.QPlainTextEdit(self.logs)
        self.logViewer.setGeometry(QtCore.QRect(0, 40, 329, 270))
        self.logViewer.setMaximumSize(QtCore.QSize(329,270))
        self.logViewer.setObjectName(_fromUtf8("Log Viewer"))
        self.advSettingsTabs.addTab(self.logs, _fromUtf8(""))
        self.utils = QtGui.QWidget()
        self.utils.setObjectName(_fromUtf8("utils"))
        self.utilitiesSpace = QtGui.QScrollArea(self.utils)
        self.utilitiesSpace.setGeometry(QtCore.QRect(0, 0, 329, 305))
        self.utilitiesSpace.setWidgetResizable(True)
        self.utilitiesSpace.setObjectName(_fromUtf8("utilitiesSpace"))
        self.utilitiesContents = QtGui.QWidget()
        self.utilitiesContents.setGeometry(QtCore.QRect(0, 0, 329, 305))
        self.utilitiesContents.setObjectName(_fromUtf8("utilitiesContents"))
        self.line_2 = QtGui.QFrame(self.utilitiesContents)
        self.line_2.setGeometry(QtCore.QRect(10, 80, 311, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.dfcTitle_LBL = QtGui.QLabel(self.utilitiesContents)
        self.dfcTitle_LBL.setGeometry(QtCore.QRect(10, 10, 121, 16))
        self.dfcTitle_LBL.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.dfcTitle_LBL.setObjectName(_fromUtf8("dfcTitle_LBL"))
        self.CreateDummy_BTN = QtGui.QPushButton(self.utilitiesContents)
        self.CreateDummy_BTN.setGeometry(QtCore.QRect(10, 30, 311, 23))
        self.CreateDummy_BTN.setObjectName(_fromUtf8("CreateDummy_BTN"))
        self.refreshSpace_BTN = QtGui.QPushButton(self.utilitiesContents)
        self.refreshSpace_BTN.setGeometry(QtCore.QRect(10, 60, 311, 23))
        self.refreshSpace_BTN.setObjectName(_fromUtf8("refreshSpace_BTN"))
        self.Free_LBL = QtGui.QLabel(self.utilitiesContents)
        self.Free_LBL.setGeometry(QtCore.QRect(280, 10, 41, 20))
        self.Free_LBL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Free_LBL.setObjectName(_fromUtf8("Free_LBL"))
        self.gbCount_LBL = QtGui.QLabel(self.utilitiesContents)
        self.gbCount_LBL.setGeometry(QtCore.QRect(230, 10, 41, 20))
        self.gbCount_LBL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.gbCount_LBL.setObjectName(_fromUtf8("gbCount_LBL"))
        self.utilitiesSpace.setWidget(self.utilitiesContents)
        self.advSettingsTabs.addTab(self.utils, _fromUtf8(""))
        self.automation = QtGui.QWidget()
        self.automation.setObjectName(_fromUtf8("automation"))
        self.LBL_zzz_image = QtGui.QLabel(self.automation)
        self.LBL_zzz_image.setGeometry(QtCore.QRect(100, 30, 131, 121))
        self.LBL_zzz_image.setAutoFillBackground(False)
        self.LBL_zzz_image.setText(_fromUtf8(""))
        self.LBL_zzz_image.setPixmap(QtGui.QPixmap(_fromUtf8("./css/zzz.jpg")))
        self.LBL_zzz_image.setScaledContents(True)
        self.LBL_zzz_image.setObjectName(_fromUtf8("LBL_zzz_image"))
        self.LBL_comingSoonText = QtGui.QLabel(self.automation)
        self.LBL_comingSoonText.setGeometry(QtCore.QRect(70, 160, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.LBL_comingSoonText.setFont(font)
        self.LBL_comingSoonText.setText(_fromUtf8("Under Construction..."))
        self.LBL_comingSoonText.setScaledContents(False)
        self.LBL_comingSoonText.setObjectName(_fromUtf8("LBL_comingSoonText"))
        self.advSettingsTabs.addTab(self.automation, _fromUtf8(""))
        self.HostsSection.addWidget(self.advSettingsTabs)
        self.version_LBL = QtGui.QLabel(Form)
        self.version_LBL.setMaximumSize(QtCore.QSize(354, 16))
        self.version_LBL.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.version_LBL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.version_LBL.setObjectName(_fromUtf8("version_LBL"))
        self.HostsSection.addWidget(self.version_LBL)
        self.verticalLayout_4.addLayout(self.HostsSection)

        self.retranslateUi(Form)
        self.advSettingsTabs.setCurrentIndex(0)
        self.adjFiles_DRP.setCurrentIndex(0)
        self.logs_DRP.setCurrentIndex(0)
        self.advSettingsTabs.setDisabled(True)
        self.advSettingsTabs.setVisible(False)
        QtCore.QMetaObject.connectSlotsByName(Form)
        #self.hostsTextEdit.setDisabled(False)
        #self.hostsTextEdit.setVisible(True)
        self.version_LBL.setVisible(False)
        #self.adjFiles_DRP.setDisabled(True)
        #self.Apply_BTN.setDisabled(True)
        logging.info('UI Setup Completed')

    def retranslateUi(self, Form):
        logging.info('Setting Specific UI Binding')
        Form.setWindowTitle(_translate("Form", "NLT", None))
        self.Title_LBL.setText(_translate("Form", "Nexon Launcher Tool", None))
        self.EnvText_LBL.setText(_translate("Form", "Current Environment:  ", None))
        self.Env_LBL.setText(_translate("Form", "ENV", None))
        self.Restart_BTN.setText(_translate("Form", "R", None))
        self.EnvSelect_LBL.setText(_translate("Form", "Switch Environment", None))
        self.Test_BTN.setText(_translate("Form", "Test", None))
        self.Beta_BTN.setText(_translate("Form", "Beta", None))
        self.Stage_BTN.setText(_translate("Form", "Staging", None))
        self.Live_BTN.setText(_translate("Form", "Live", None))
        self.ExtMachine_BOX.setText(_translate("Form", "Ext. Machine", None))
        self.ClearLog_BOX.setText(_translate("Form", "Clear Logs", None))
        self.Location_DRP.setItemText(0, _translate("Form", "Select Location...", None))
        self.Location_DRP.setItemText(1, _translate("Form", "Install Location", None))
        self.Location_DRP.setItemText(2, _translate("Form", "APPDATA Folder", None))
        self.AdvSettings_BOX.setText(_translate("Form", "Adv Settings", None))
        self.adjFiles_DRP.setItemText(0, _translate("Form", "Host Settings", None))
        self.adjFiles_DRP.setItemText(1, _translate("Form", "Settings.conf", None))
        self.adjFiles_DRP.setItemText(2, _translate("Form", "EULA.db", None))
        self.Apply_BTN.setText(_translate("Form", "Apply", None))
        self.advSettingsTabs.setTabText(self.advSettingsTabs.indexOf(self.files), _translate("Form", "Adjustable Files", None))
        self.advSettingsTabs.setTabToolTip(self.advSettingsTabs.indexOf(self.files), _translate("Form", "Adjust HOSTS file, settings.conf, and other files", None))
        self.logs_DRP.setItemText(0, _translate("Form", "Runtime Log", None))
        self.logs_DRP.setItemText(1, _translate("Form", "Runtime Debug", None))
        self.logs_DRP.setItemText(2, _translate("Form", "Updater Debug", None))
        self.logs_DRP.setItemText(3, _translate("Form", "NLT Debug", None))
        self.advSettingsTabs.setTabText(self.advSettingsTabs.indexOf(self.logs), _translate("Form", "Logs", None))
        self.advSettingsTabs.setTabToolTip(self.advSettingsTabs.indexOf(self.logs), _translate("Form", "View log files", None))
        self.dfcTitle_LBL.setToolTip(_translate("Form", "Fills up HD with an empty file.  Use to test Hard Drive Space handling.", None))
        self.dfcTitle_LBL.setText(_translate("Form", "Dummy File Creator", None))
        self.CreateDummy_BTN.setToolTip(_translate("Form", "Creates a Dummy file that fills up the Hard Drive.  Be sure to remove when finished.", None))
        self.CreateDummy_BTN.setText(_translate("Form", "Run Utility", None))
        self.refreshSpace_BTN.setToolTip(_translate("Form", "", None))
        self.refreshSpace_BTN.setText(_translate("Form", "Calculate Free Space", None))
        self.Free_LBL.setToolTip(_translate("Form", "Fills up HD with an empty file.  Use to test Hard Drive Space handling.", None))
        self.Free_LBL.setText(_translate("Form", "GB Free", None))
        self.gbCount_LBL.setToolTip(_translate("Form", "Fills up HD with an empty file.  Use to test Hard Drive Space handling.", None))
        self.gbCount_LBL.setText(_translate("Form", "0", None))
        self.advSettingsTabs.setTabText(self.advSettingsTabs.indexOf(self.utils), _translate("Form", "Utilities", None))
        self.advSettingsTabs.setTabToolTip(self.advSettingsTabs.indexOf(self.utils), _translate("Form", "Utilities to help you out", None))
        self.advSettingsTabs.setTabText(self.advSettingsTabs.indexOf(self.automation), _translate("Form", "Automation", None))
        self.version_LBL.setText(_translate("Form", "v.05", None))

#########------- START BINDING ----------########
        self.Env_LBL.setText(_translate("Form", self.SetEnvLabel(os.path.join(pathname[0], 'settings.conf')), None))
        self.Test_BTN.clicked.connect(self.SetTestEnv)
        self.Test_BTN.clicked.connect(lambda: self.EnvLabelDynamic(self.Env_LBL))
        self.Stage_BTN.clicked.connect(self.SetStageEnv)
        self.Stage_BTN.clicked.connect(lambda: self.EnvLabelDynamic(self.Env_LBL))
        self.Beta_BTN.clicked.connect(self.SetBetaEnv)
        self.Beta_BTN.clicked.connect(lambda: self.EnvLabelDynamic(self.Env_LBL))
        self.Live_BTN.clicked.connect(self.SetLiveEnv)
        self.Live_BTN.clicked.connect(lambda: self.EnvLabelDynamic(self.Env_LBL))
        self.Location_DRP.activated['QString'].connect(self.OpenLocation)
        self.ExtMachine_BOX.stateChanged.connect(lambda: self.DisableTestButton(self.Test_BTN))
        self.Restart_BTN.clicked.connect(self.RestartLauncher)
        self.AdvSettings_BOX.stateChanged.connect(lambda: self.DisplayTabs(self.advSettingsTabs,Form, self.version_LBL))
        self.adjFiles_DRP.activated['QString'].connect(self.DisplayFile)
        self.logs_DRP.activated['QString'].connect(self.DisplayFile)
        self.Apply_BTN.clicked.connect(lambda: self.ApplyTextToFile(self.adjFiles_DRP.currentIndex(),
                                                                    self.hostsTextEdit))
        self.CreateDummy_BTN.clicked.connect(self.RunDFC)
        self.CreateDummy_BTN.clicked.connect(lambda: self.SpaceLabelDynamic(self.gbCount_LBL))
        self.refreshSpace_BTN.clicked.connect(lambda: self.SpaceLabelDynamic(self.gbCount_LBL))
        self.version_LBL.mousePressEvent = self.AboutInfo

        logging.info('UI Elements Properly Bound')
        self.Startup()

    def Startup(self):
        logging.info('### Starting up NLT ###')
        self.ScanHosts()
        self.EnableDebug()
        self.CopyLogs()
        logging.info('### Startup Complete ###')
        self.SpaceLabelDynamic(self.gbCount_LBL)
        logging.info('# HD Space Scan Complete #')

    def AboutInfo(self, event):
        if self.version_LBL.text() == 'v.05':
            self.version_LBL.setText('Created by Gerald Hardin 2016.  ghardin@nexon.net')
        else:
            self.version_LBL.setText('v.05')


    def ScanHosts(self):
        logging.info('### Starting Host Scan ###')
        with open(hostsLoc, 'r+') as h:
            lines = h.readlines()
            h.seek(0)
            h.truncate()
            betaOff0Found = False
            betaOn0Found = False
            betaOff1Found = False
            betaOn1Found = False
            betaOff2Found = False
            betaOn2Found = False

            stageOff0Found = False
            stageOn0Found = False
            stageOff1Found = False
            stageOn1Found = False
            stageOff2Found = False
            stageOn2Found = False

            cdnOffFound = False
            cdnOnFound = False

            for line in lines:
                line.rstrip()
                ###### Scan for Beta Hosts #######

                if betaHostsOff[0] in line:
                    betaOff0Found = True

                if betaHostsOff[1] in line:
                    betaOff1Found = True

                if betaHostsOff[2] in line:
                    betaOff2Found = True

                if betaHostsOn[0] in line:
                    betaOn0Found = True

                if betaHostsOn[1] in line:
                    betaOn1Found = True

                if betaHostsOn[2] in line:
                   betaOn2Found = True


                ###### Scan for Staging Hosts #######
                if stageHostsOff[0] in line:
                    stageOff0Found = True

                if stageHostsOff[1] in line:
                    stageOff1Found = True

                if stageHostsOff[2] in line:
                    stageOff2Found = True

                if stageHostsOn[0] in line:
                    stageOn0Found = True

                if stageHostsOn[1] in line:
                    stageOn1Found = True

                if stageHostsOn[2] in line:
                    stageOn2Found = True

                #### Scan for CDN hosts #####
                if cdnHostOff in line:
                    cdnOffFound = True

                if cdnHostOn in line:
                    cdnOnFound = True

                ##### Empty Line and non-NxL Host Lines ####
                if not line.strip():
                    h.write('\n')

                else:
                    h.write(line)

            ####### Add host Settings if not already found #######

            ##### Add Beta hosts if not already found #####
            if not betaOff0Found and not betaOn0Found:
                h.write('\n')
                h.write('#### added by NLT ####\n')
                h.write(betaHostsOff[0])
                logging.info(betaHostsOff[0] + ' was added to HOST setting')
            if not betaOff1Found and not betaOn1Found:
                h.write('\n')
                h.write('#### added by NLT ####\n')
                h.write(betaHostsOff[1])
                logging.info(betaHostsOff[1] + ' was added to HOST setting')
            if not betaOff2Found and not betaOn2Found:
                h.write('\n')
                h.write('#### added by NLT ####\n')
                h.write(betaHostsOff[2])
                logging.info(betaHostsOff[2] + ' was added to HOST setting')

            ##### Add Staging Hosts if not already found ######
            if not stageOff0Found and not stageOn0Found:
                h.write('\n')
                h.write('#### added by NLT ####\n')
                h.write(stageHostsOff[0])
                logging.info(stageHostsOff[0] + ' was added to HOST setting')
            if not stageOff1Found and not stageOn1Found:
                h.write('\n')
                h.write('#### added by NLT ####\n')
                h.write(stageHostsOff[1])
                logging.info(stageHostsOff[1] + ' was added to HOST setting')
            if not stageOff2Found and not stageOn2Found:
                h.write('\n')
                h.write('#### added by NLT ####\n')
                h.write(stageHostsOff[2])
                logging.info(stageHostsOff[2] + ' was added to HOST setting')

            ###### Add CDN Hosts if not already found #####
            if not cdnOffFound and not cdnOnFound:
                h.write('\n')
                h.write('#### added by NLT ####\n')
                h.write(cdnHostOff)
                logging.info(cdnHostOff + ' was added to HOST setting')
        h.close()
        logging.info('### Completed Host Scan ###')


    def SetHosts(self, env):
        if env == 'beta':
            logging.info('Setting hosts setting for %s', env)
            with open(hostsLoc, 'r+') as h:
                lines = h.readlines()
                h.seek(0)
                h.truncate()
                for line in lines:
                    found = False
                    line.rstrip()
                    ###### enables Beta Hosts #######
                    if betaHostsOff[0] in line:
                        h.write(betaHostsOn[0] if betaHostsOff[0] in line else line)
                        found = True
                    if betaHostsOff[1] in line:
                        h.write(betaHostsOn[1] if betaHostsOff[1] in line else line)
                        found = True
                    if betaHostsOff[2] in line:
                        h.write(betaHostsOn[2] if betaHostsOff[2] in line else line)
                        found = True


                    ####### enable CDN host ########
                    if cdnHostOff in line:
                        line = line.replace(cdnHostOff, cdnHostOn)

                    ######## disables Staging Hosts ######
                    if stageHostsOn[0] in line:
                        h.write(stageHostsOff[0] if stageHostsOn[0] in line else line)
                        found = True
                    if stageHostsOn[1] in line:
                        h.write(stageHostsOff[1] if stageHostsOn[1] in line else line)
                        found = True
                    if stageHostsOn[2] in line:
                        h.write(stageHostsOff[2] if stageHostsOn[2] in line else line)
                        found = True
                    if not found:
                        h.write(line)
                h.close()
        if env == 'stage':
            logging.info('Setting hosts setting for %s', env)
            with open(hostsLoc, 'r+') as h:
                lines = h.readlines()
                h.seek(0)
                h.truncate()
                for line in lines:
                    found = False
                    line.rstrip()
                    ###### Disable Beta Hosts #######
                    if betaHostsOn[0] in line:
                        h.write(betaHostsOff[0] if betaHostsOn[0] in line else line)
                        found = True
                    if betaHostsOn[1] in line:
                        h.write(betaHostsOff[1] if betaHostsOn[1] in line else line)
                        found = True
                    if betaHostsOn[2] in line:
                        h.write(betaHostsOff[2] if betaHostsOn[2] in line else line)
                        found = True
                    ####### enable CDN host ########
                    if cdnHostOff in line:
                        line = line.replace(cdnHostOff, cdnHostOn)

                    ######## Enable Staging Hosts ######
                    if stageHostsOff[0] in line:
                        h.write(stageHostsOn[0] if stageHostsOff[0] in line else line)
                        found = True
                    if stageHostsOff[1] in line:
                        h.write(stageHostsOn[1] if stageHostsOff[1] in line else line)
                        found = True
                    if stageHostsOff[2] in line:
                        h.write(stageHostsOn[2] if stageHostsOff[2] in line else line)
                        found = True
                    if not found:
                        h.write(line)
                h.close()
        if env == 'live':
            logging.info('Disabling Host Settings for %s Env', env)
            with open(hostsLoc, 'r+') as h:
                lines = h.readlines()
                h.seek(0)
                h.truncate()
                for line in lines:
                    found = False
                    line.rstrip()
                    ###### Disable Beta Hosts #######
                    if betaHostsOn[0] in line:
                        h.write(betaHostsOff[0] if betaHostsOn[0] in line else line)
                        found = True
                    if betaHostsOn[1] in line:
                        h.write(betaHostsOff[1] if betaHostsOn[1] in line else line)
                        found = True
                    if betaHostsOn[2] in line:
                        h.write(betaHostsOff[2] if betaHostsOn[2] in line else line)
                        found = True

                    ####### enable CDN host ########
                    if cdnHostOn in line:
                        h.write(cdnHostOff if cdnHostOn in line else line)
                        found = True

                    ######## Disable Staging Hosts ######
                    if stageHostsOn[0] in line:
                        h.write(stageHostsOff[0] if stageHostsOn[0] in line else line)
                        found = True
                    if stageHostsOn[1] in line:
                        h.write(stageHostsOff[1] if stageHostsOn[1] in line else line)
                        found = True
                    if stageHostsOn[2] in line:
                        h.write(stageHostsOff[2] if stageHostsOn[2] in line else line)
                        found = True
                    if not found:
                        h.write(line)
                h.close()
        logging.info('Host File Closed')

    def DisplayFile(self, text):
        self.Apply_BTN.setDisabled(False)
        if text == 'Host Settings':

            file = open(hostsLoc).read()
            self.hostsTextEdit.setPlainText(file)

        if text == 'Settings.conf':
            try:
                file = open(os.path.join(pathname[0], defaultConf)).read()
                self.hostsTextEdit.setPlainText(file)
            except:
                logging.info('No Settings File')
                self.Apply_BTN.setDisabled(True)
                self.hostsTextEdit.setPlainText('No settings.conf file found')

        if text == 'EULA.db':
            try:
                file = open(os.path.join(appdataPath, eulafile)).read()
                self.hostsTextEdit.setPlainText(file)
            except:
                logging.info('EULA.db not found')
                self.hostsTextEdit.setPlainText('EULA not found')

        if text == 'Runtime Log':
            try:
                self.Apply_BTN.setDisabled(True)
                log = open(os.path.join(pathname[0], 'nexon_runtime.log')).read()
                self.logViewer.setPlainText(log)
            except:
                self.logViewer.setPlainText('No Runtime log found')

        if text == 'Runtime Debug':
            try:
                self.Apply_BTN.setDisabled(True)
                log = open(os.path.join(pathname[0], 'nexon_runtime_debug.log')).read()
                self.logViewer.setPlainText(log)
            except:
                self.logViewer.setPlainText('No Runtime Debug log found')

        if text == 'Updater Debug':
            try:
                self.Apply_BTN.setDisabled(True)
                log = open(os.path.join(pathname[0], 'nexon_updater_debug.log')).read()
                self.logViewer.setPlainText(log)
            except:
                self.logViewer.setPlainText('No Updater Debug log found')

        if text == 'NLT Debug':
            try:
                log = open(logLoc).read()
                self.logViewer.setPlainText(log)
            except:
                self.logViewer.setPlainText('No NLT Debug log found')


    def ApplyTextToFile(self, index, text):
            global showAbout
            if index == 0:
                with open(hostsLoc, 'w') as hostFile:
                    hostFile.write(str(text.toPlainText()))
                hostFile.close()
                self.DisplayFile('Host Settings')

            if index == 1:
                settingsPath = os.path.join(pathname[0], defaultConf)
                with open(settingsPath, 'w') as settingsFile:
                    settingsFile.write(str(text.toPlainText()))
                settingsFile.close()
                self.DisplayFile('Settings.conf')

            if index == 2:
                eulapath = os.path.join(appdataPath, eulafile)
                with open(eulapath, 'w') as eulaDbFile:
                    eulaDbFile.write(str(text.toPlainText()))
                eulaDbFile.close()
                self.DisplayFile('EULA.db')

            if index == 5:
                aboutContent = open(aboutLoc).read()
                self.hostsTextEdit.setPlainText(aboutContent)


    def DisplayTabs(self, editor, form, label):
        ##### Enable and display text editor #####
        global advCheck
        advCheck = not advCheck
        if advCheck == True:
            editor.setDisabled(False)
            editor.setVisible(True)
            form.setMaximumSize(354,556)
            form.setMinimumSize(354,556)
            form.resize(354, 556)
            label.setVisible(True)
        if advCheck == False:
            editor.setDisabled(True)
            editor.setVisible(False)
            form.setMaximumSize(354,189)
            form.setMinimumSize(354,189)
            form.resize(354, 189)
            label.setVisible(False)

    def DisableTestButton(self, button):
        global extCheck
        extCheck = not extCheck
        if extCheck == True:
            button.setDisabled(True)
        if extCheck == False:
            button.setDisabled(False)


    def EnvLabelDynamic(self, label):
        conf = os.path.join(pathname[0], 'settings.conf')
        if os.path.exists(conf):
            if "test" in open(conf).read():
                label.setText('Test')
            if "beta" in open(conf).read():
                label.setText('Beta')
            if "stage" in open(conf).read():
                label.setText('Staging')
        else:
            label.setText('Live')


    def SetEnvLabel(self, conf):
        env = ''
        if os.path.exists(conf):
            if "test" in open(conf).read():
                self.env = 'Test'
                return 'Test'
            if "beta" in open(conf).read():
                self.env = 'Beta'
                return 'Beta'
            if "stage" in open(conf).read():
                self.env = 'Staging'
                return 'Staging'
        else:
            self.env = 'Live'
            return 'Live'
        logging.info('!!! Env Label set to %s !!!', env)



    def EnableDebug(self):
        debugLocation = os.path.join(pathname[0], 'enable_debug')
        if os.path.isfile(debugLocation) is False:
            logging.info('Creating enable_debug File')
            file = open(debugLocation, 'w')
            file.close()
        else:
            logging.info('enable_debug Found')

    def CopyLogs(self):
        if self.ClearLog_BOX.isChecked():
            for filename in os.listdir(pathname[0]):
                 if filename.endswith(tuple(logExt)):
                    srcPath = os.path.join(pathname[0], filename)
                    destPath = os.path.join(curDir, 'logs', filename)
                    shutil.copy(srcPath, destPath)
                    logging.info('%s copied to %s', srcPath, destPath)
                    os.remove(srcPath)
                    logging.info('%s removed from %s', srcPath, curDir)

    def KillLauncher(self):
        processName = 'nexon_runtime.exe'
        for process in psutil.process_iter():
            listedName = process.name()
            if listedName == processName:
                logging.info('%s found.', processName)
                process.kill()
                logging.info('Launcher Process Killed')


    def StartLauncher(self):
        execName = 'nexon_launcher.exe'
        execLoc = os.path.join(pathname[0], execName)
        subprocess.Popen(execLoc)
        logging.info('Launcher Started!')


    def SetTestEnv(self):
        logging.info('!!!!!!!!!! Switching to Test Env !!!!!!!!!!')
        if not extCheck:
            self.KillLauncher()
            if self.ExtMachine_BOX.isChecked():
                self.SetHosts('beta')
            else:
                self.SetHosts('live')
            time.sleep(2)
            self.CopyLogs()
            confLocation = os.path.join(confDir, testConf)
            destName = os.path.join(pathname[0], 'settings.conf')
            shutil.copyfile(confLocation, destName)
            self.StartLauncher()
            self.SetEnvLabel(destName)
            logging.info('!!!!!!!!!! Launcher now on Test !!!!!!!!!!')

    def SetBetaEnv(self):
        logging.info('!!!!!!!!!! Switching to Beta Env !!!!!!!!!!')
        self.KillLauncher()
        if self.ExtMachine_BOX.isChecked():
            self.SetHosts('beta')
        else:
            self.SetHosts('live')
        time.sleep(2)
        self.CopyLogs()
        confLocation = os.path.join(confDir, betaConf)
        destName = os.path.join(pathname[0], 'settings.conf')
        shutil.copyfile(confLocation, destName)
        self.StartLauncher()
        self.SetEnvLabel(destName)
        logging.info('!!!!!!!!!! Launcher now on Beta !!!!!!!!!!')

    def SetStageEnv(self):
        logging.info('Switching to Stage Env')
        self.KillLauncher()
        if self.ExtMachine_BOX.isChecked():
            self.SetHosts('stage')
        else:
            self.SetHosts('live')
        time.sleep(2)
        self.CopyLogs()
        confLocation = os.path.join(confDir, stageConf)
        destName = os.path.join(pathname[0], 'settings.conf')
        shutil.copyfile(confLocation, destName)
        self.StartLauncher()
        self.SetEnvLabel(destName)
        logging.info('!!!!!!!!!! Launcher now on Staging !!!!!!!!!!')

    def SetLiveEnv(self):
        logging.info(' !!!!!!!!!! Switching to Live Env !!!!!!!!!!')
        self.KillLauncher()
        self.SetHosts('live')
        time.sleep(2)
        self.CopyLogs()
        destName = os.path.join(pathname[0], 'settings.conf')
        if os.path.exists(destName):
            os.remove(destName)
        self.StartLauncher()
        self.SetEnvLabel(destName)
        logging.info('!!!!!!!!!! Launcher now on Live !!!!!!!!!!')

    def OpenLocation(self, text):
        if text == 'Install Location':
            try:
                os.startfile(pathname[0])
            except:
                logging.info('unable to open Install Location')

        if text == 'APPDATA Folder':
            try:
                os.startfile(appdataPath)
            except:
                logging.info('unable to open APPDATA Folder')

    def RunDFC(self):

        try:
            from subprocess import Popen
            Popen(dfcLoc, creationflags=subprocess.CREATE_NEW_CONSOLE)
            #file.communicate()
        except:
            logging.info('Unable to load Dummy File Creator.  Ensure it can be found in '+ dfcLoc)

    def SpaceLabelDynamic(self, label):
        logging.info('# Scanning HD Space #')
        freeSpace = psutil.disk_usage('/')
        convertedSpace= freeSpace.free / 1024 / 1024 / 1024
        label.setText(str(convertedSpace))


    def RestartLauncher(self):
        logging.info('Restarting Launcher')
        self.KillLauncher()
        time.sleep(2)
        self.StartLauncher()
        self.EnvLabelDynamic(self.Env_LBL)
        logging.info('Launcher Restarted')

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex =Ui_Form()
    ex.show()
    sys.exit(app.exec_())


#######-------- END CUSTOMIZING --------------##############