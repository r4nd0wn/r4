import json
import time
from PyQt5.QtCore import QTimer, QSettings
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from threading import Thread
from irc import IRC
import datetime
import random
import hashlib



class Ui_MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 692)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalWidget.setGeometry(QtCore.QRect(0, 0, 601, 631))
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.PlainTextEdit = QtWidgets.QPlainTextEdit(self.horizontalWidget)
        self.PlainTextEdit.setObjectName("PlainTextEdit")
        self.verticalLayout.addWidget(self.PlainTextEdit)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.line = QtWidgets.QFrame(self.horizontalWidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.horizontalWidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.lcdNumber = QtWidgets.QLCDNumber(self.horizontalWidget)
        self.lcdNumber.setMinimumSize(QtCore.QSize(50, 0))
        self.lcdNumber.setMaximumSize(QtCore.QSize(16777215, 100))
        self.lcdNumber.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setObjectName("lcdNumber")
        self.verticalLayout_2.addWidget(self.lcdNumber)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(100, 25))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(200, 25))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_2.addWidget(self.lineEdit_3, 0, QtCore.Qt.AlignTop)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_3.setMaximumSize(QtCore.QSize(200, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3, 0, QtCore.Qt.AlignTop)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_4.setMaximumSize(QtCore.QSize(200, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_5.setMaximumSize(QtCore.QSize(200, 25))
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_2.addWidget(self.pushButton_5)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 30))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuInfo = QtWidgets.QMenu(self.menubar)
        self.menuInfo.setObjectName("menuInfo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSafe_Settings = QtWidgets.QAction(MainWindow)
        self.actionSafe_Settings.setObjectName("actionSafe_Settings")
        self.actionReload = QtWidgets.QAction(MainWindow)
        self.actionReload.setObjectName("actionReload")
        self.actionDeveloper_Info = QtWidgets.QAction(MainWindow)
        self.actionDeveloper_Info.setObjectName("actionDeveloper_Info")
        self.actionApplication_Info = QtWidgets.QAction(MainWindow)
        self.actionApplication_Info.setObjectName("actionApplication_Info")
        self.menuSettings.addAction(self.actionSafe_Settings)
        self.menuSettings.addAction(self.actionReload)
        self.menuInfo.addAction(self.actionDeveloper_Info)
        self.menuInfo.addAction(self.actionApplication_Info)
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuInfo.menuAction())
        self.centralwidget.setLayout(self.horizontalLayout)



        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Current Viewers"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.menuSettings.setTitle(_translate("MainWindow", "File"))
        self.menuInfo.setTitle(_translate("MainWindow", "Info"))
        self.actionSafe_Settings.setText(_translate("MainWindow", "Edit Settings"))
        self.actionReload.setText(_translate("MainWindow", "Reload"))
        self.actionDeveloper_Info.setText(_translate("MainWindow", "Developer Info"))
        self.actionApplication_Info.setText(_translate("MainWindow", "Application Info"))

    def set_viewercount(self):
        global viewername
        self.lcdNumber.display(int(get_viewercount(get_clientId(viewername))))

    def set_chat(self):
        global chat1


app = QApplication(sys.argv)
settings = QSettings("r4" "r4nd0wn")
settings.setValue("username", "skadoodle")
settings.
window = Ui_MainWindow()
window.show()
print("xD")

text_area = window.PlainTextEdit

username = "rTsFetcher"
oauth = "oauth:efhn2jfl093dyrdv94rd91vad3zdoy"
channel = "skadoodle"

chat1 = IRC(channel, username, oauth)
chat1.connect()

userlist = []
colorid = []
stimer = QTimer()
new_messages = []
def fetch_new_messages():
    while True:
        response = chat1.get_splitted_message()

        if response:
            new_messages.append(response)


thread = Thread(target=fetch_new_messages, daemon=True)
thread.start()

def display_new_messages():
    while new_messages:
        message = new_messages.pop(0)
        prefix = """<b><span style="color: """ + getUserColor(message[1]) + """;">"""
        postfix = "</span></b>"
        print(message)
        text_area.appendHtml("<small>" + message[0] + "</small>" + " " + prefix + message[1] + postfix + ": " + message[2])

def send_message():
    try:
        chat1.send(window.lineEdit.text())
        timestamp = datetime.datetime.now()
        fullmessage = "<small>" + chat1.timestamp() + "</small>" + " " + """<b><span style="color: #00BFFF;">""" + username + "</span>" + ": " + "</b>" + window.lineEdit.text()

        text_area.appendHtml(fullmessage)
        window.lineEdit.clear()

    except Exception as e:
        print(e)

def getUserColor(usr):
    color = "#" + str(hashlib.sha512(usr.encode("UTF-8")).hexdigest())[0:6]
    return color

def random_color():
    color = "#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
    return color

def create_user(username):
    userlist.append(username)
    colorid.insert(userlist.index(username), random_color())

def get_clientId(channelname):

    try:
        headers = {
            'Accept': 'application/vnd.twitchtv.v5+json',
            'Client-ID': 'zc4jzl9wci2c16d2zir99z0jz7lxpw',
        }

        params = (
            ('login', channelname),
        )

        response = requests.get('https://api.twitch.tv/kraken/users', headers=headers, params=params)

        json_obj = json.loads(response.text)
        user = json_obj.get("users", "")
        user = user[0]
        id = user.get("_id", "")
        return id
    except Exception as e:
        print(e)
def get_viewercount(id):
    import requests

    headers = {
        'Accept': 'application/vnd.twitchtv.v5+json',
        'Client-ID': 'zc4jzl9wci2c16d2zir99z0jz7lxpw',
        'Authorization': 'OAuth m9aomgcvgacww3ybeo07m2pu162c0y',
    }

    response = requests.get('https://api.twitch.tv/kraken/streams/' + id, headers=headers)
    json_obj = json.loads(response.text)
    stream = json_obj.get("stream", "")
    viewcount = stream.get("viewers", "")
    return viewcount

def startviewercount():
    try:
        stimer.stop()
    except:
        print("timer already started")
    global viewername
    viewername = window.lineEdit_3.text()
    window.lineEdit_3.clear()
    window.set_viewercount()

    stimer.timeout.connect(window.set_viewercount)
    stimer.start(10000)


window.lineEdit.returnPressed.connect(send_message)
ftimer = QTimer()
ftimer.timeout.connect(display_new_messages)
ftimer.start(100)
window.lineEdit_3.returnPressed.connect(startviewercount)




app.exec_()