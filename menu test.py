import json
import time
from PyQt5.QtCore import QTimer, QSettings, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from threading import Thread
from irc import IRC
import datetime
import random
import hashlib
import os
from riotwatcher import RiotWatcher, ApiError


def startRiotwatcher():
    if window.rtcheck.isChecked == True:

        try:
            threadname = Thread(target=riotwatcher, daemon=True)
            riotthread.append(threadname)
            threadname.start()

        except Exception as e:
            print(e)
            print("faultinthreadstareter")

    else:
        print("Checkbox is not chekced")


def startRiotwatcher():
    threadname = Thread(target=riotwatcher, daemon=True)
    riotthread.append(threadname)
    threadname.start()

class Ui_MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)



    def setupUi(self, r4):
        r4.setObjectName("r4")
        r4.resize(640, 692)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/r4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        r4.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(r4)
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
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.horizontalWidget)
        self.plainTextEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
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
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        self.label = QtWidgets.QLabel(self.horizontalWidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)

        self.lcdNumber = QtWidgets.QLCDNumber(self.horizontalWidget)
        self.lcdNumber.setMinimumSize(QtCore.QSize(50, 0))
        self.lcdNumber.setMaximumSize(QtCore.QSize(16777215, 100))
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber.setLineWidth(0)
        self.lcdNumber.setDigitCount(6)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setProperty("intValue", 1337)
        self.lcdNumber.setObjectName("lcdNumber")
        self.verticalLayout_3.addWidget(self.lcdNumber)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(0, 0, -1, -1)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.rtcheck = QtWidgets.QCheckBox(self.horizontalWidget)
        self.rtcheck.setObjectName("checkBox")
        self.verticalLayout_4.addWidget(self.rtcheck)
        self.rtcheck.stateChanged.connect(startRiotwatcher)
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_4.setMaximumSize(QtCore.QSize(200, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        #self.pushButton_4.pressed.connect(startRiotwatcher)
        self.pushButton_4.clicked.connect(startRiotwatcher)
        self.verticalLayout_4.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_3.setMaximumSize(QtCore.QSize(200, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_4.addWidget(self.pushButton_3)
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_5.setMaximumSize(QtCore.QSize(200, 25))
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_4.addWidget(self.pushButton_5)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        r4.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(r4)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 30))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuInfo = QtWidgets.QMenu(self.menubar)
        self.menuInfo.setObjectName("menuInfo")
        r4.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(r4)
        self.statusbar.setObjectName("statusbar")
        r4.setStatusBar(self.statusbar)
        self.actionSettings = QtWidgets.QAction(r4)
        self.actionSettings.setObjectName("actionSettings")
        self.actionSettings.triggered.connect(self.infodialog)
        self.actionReload = QtWidgets.QAction(r4)
        self.actionReload.setObjectName("actionReload")
        self.actionDeveloper_Info = QtWidgets.QAction(r4)
        self.actionDeveloper_Info.setObjectName("actionDeveloper_Info")
        self.actionApplication_Info = QtWidgets.QAction(r4)
        self.actionApplication_Info.setObjectName("actionApplication_Info")
        self.menuSettings.addAction(self.actionSettings)
        self.menuSettings.addAction(self.actionReload)
        self.menuInfo.addAction(self.actionDeveloper_Info)
        self.menuInfo.addAction(self.actionApplication_Info)
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuInfo.menuAction())
        self.centralwidget.setLayout(self.horizontalLayout)
        self.retranslateUi(r4)
        QtCore.QMetaObject.connectSlotsByName(r4)

    def retranslateUi(self, r4):
        _translate = QtCore.QCoreApplication.translate
        r4.setWindowTitle(_translate("r4", "r4\'s Streaming Suite"))
        self.label.setText(_translate("r4", "Current Viewers"))
        self.pushButton_4.setText(_translate("r4", "riotwatchme"))
        self.pushButton_3.setText(_translate("r4", "PushButton3"))
        self.pushButton_5.setText(_translate("r4", "PushButton5"))
        self.menuSettings.setTitle(_translate("r4", "File"))
        self.menuInfo.setTitle(_translate("r4", "Info"))
        self.actionSettings.setText(_translate("r4", "Settings"))
        self.actionReload.setText(_translate("r4", "Reload"))
        self.actionDeveloper_Info.setText(_translate("r4", "Developer Info"))
        self.actionApplication_Info.setText(_translate("r4", "Application Info"))
        self.rtcheck.setText(_translate("r4", "RiotWatcher"))

    def set_viewercount(self):
        global views
        self.lcdNumber.display(int(views))

    def infodialog(self):
        d = Ui_Settings()
        d.show()
        d.exec_()
        # os.execv(__file__, sys.argv)



class Ui_Settings(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Settings")
        Dialog.resize(314, 334)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setMaximumSize(QtCore.QSize(300, 25))
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setMinimumSize(QtCore.QSize(300, 1))
        self.line.setMaximumSize(QtCore.QSize(300, 1))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setMaximumSize(QtCore.QSize(300, 25))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(200, 25))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(300, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setMaximumSize(QtCore.QSize(300, 1))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMaximumSize(QtCore.QSize(200, 25))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setMinimumSize(QtCore.QSize(200, 25))
        self.lineEdit.setMaximumSize(QtCore.QSize(300, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(200, 25))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(300, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setMaximumSize(QtCore.QSize(300, 25))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout.addWidget(self.lineEdit_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 25))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.pressed.connect(self.writesettings)
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_5.setText(_translate("Dialog", "<b>League of Legends Settings</b>"))
        self.label_2.setText(_translate("Dialog", "Summoner Name"))
        self.label_6.setText(_translate("Dialog", "<b>Twitch Settings</b>"))
        self.label.setText(_translate("Dialog", "Username"))
        self.label_3.setText(_translate("Dialog", "OAuth"))
        self.label_4.setText(_translate("Dialog", "Channel"))
        self.pushButton.setText(_translate("Dialog", "Save"))

    def writesettings(self):
        setusern = self.lineEdit.text()
        setoauth = self.lineEdit_3.text()
        setchann = self.lineEdit_4.text()
        print(setusern)
        print(setoauth)
        print(setchann)
        if setusern == "":
            text_area.appendPlainText("username is fucking empty")
        else:
            settings.setValue("username", self.lineEdit.text())
        if setchann == "":
            text_area.appendPlainText("channel is fucking empty")
        else:
            settings.setValue("oauth", self.lineEdit_3.text())
        if setoauth == "":
            text_area.appendPlainText("OAuth is fucking empty")
        else:
            settings.setValue("channel", self.lineEdit_4.text())

        settings.setValue("summonername", "DER Kax 59")



        self.close()
        print(settings.value("channel", "dumb error"))



app = QApplication(sys.argv)
settings = QSettings("r4" "r4nd0wn")
window = Ui_MainWindow()
window.show()
print("xD")

text_area = window.plainTextEdit

stanusername = "rTsFetcher"
stanoauth = "oauth:efhn2jfl093dyrdv94rd91vad3zdoy"
stanchannel = "r4f1xD"

chat1 = IRC(settings.value("channel", stanchannel), settings.value("username", stanusername),
            settings.value("oauth", stanoauth))
chat1.connect()

userlist = []
colorid = []
stimer = QTimer()
new_messages = []
riotthread = []



def riotwatcher():
    try:
        watcher = RiotWatcher('RGAPI-6afbce6a-761d-4116-b2f2-089a6b8f8798')
        my_region = 'euw1'
        summonername = "Der KAX 59"
        me = watcher.summoner.by_name(my_region, 'Der KAX 59')
        accountId = me.get("accountId")
        id = me.get("id")
        leagueinfoall = watcher.league.by_summoner(my_region, id)
        leagueinfosoloduo = leagueinfoall[0]
        leagueinfoflex = leagueinfoall[1]
        leagueinfotft = leagueinfoall[2]
        # print(type(leagueinfosoloduo))
        mydivision = leagueinfosoloduo.get("tier")
        myrank = leagueinfosoloduo.get("rank")
        mylp = leagueinfosoloduo.get("leaguePoints")
        mywinsthisseason = leagueinfosoloduo.get("wins")
        mylosesthisseason = leagueinfosoloduo.get("losses")

        matchlist = watcher.match.matchlist_by_account(my_region, accountId)
        matches = matchlist.get("matches")
        lastgame = matches[0]
        gameidlastgame = lastgame.get("gameId")
        mychamplastgame = lastgame.get("champion")
        matchinfo = watcher.match.by_id(my_region, gameidlastgame)

        participantIdentities = matchinfo.get("participantIdentities")
        for i in participantIdentities:
            player = i.get("player")
            if summonername == player.get("summonerName"):
                mypartid = i.get("participantId")
        participants = matchinfo.get("participants")
        myinfo = participants[mypartid - 1]
        print(myinfo)
        myteamidlastgame = myinfo.get("teamId")
        print(myteamidlastgame)

        teams = matchinfo.get("teams")
        print(teams)
        for j in teams:
            if myteamidlastgame == j.get("teamId"):
                winorloselastgame = j.get("win")
        print(winorloselastgame)
        Victory = "Victory"
        Defeat = "Defeat"
        if winorloselastgame == "Win":
            winlastgame = 1
        else:
            winlastgame = 0
        if winlastgame == 1:
            print(Victory)
        else:
            print("Defeat")
        mystatslastgame = myinfo.get("stats")
        mykillslastgame = mystatslastgame.get("kills")
        mydeathslastgame = mystatslastgame.get("deaths")
        myassistslastgame = mystatslastgame.get("assists")
        myvisionscorelastgame = mystatslastgame.get("visionScore")
        minionskilledlastgame = (mystatslastgame.get("totalMinionsKilled")) + (mystatslastgame.get("neutralMinionsKilled"))
        mylanelastgame = lastgame.get("lane")
        for k in participants:
            timeline = k.get("timeline")
            if myteamidlastgame != k.get("teamId") and mylanelastgame == timeline.get("lane"):
                mylaneenemy = k.get("participantId")
    except Exception as e:
        print(e)


def fetch_new_messages():
    while True:
        response = chat1.get_splitted_message()

        if response:
            new_messages.append(response)


messagethread = Thread(target=fetch_new_messages, daemon=True)
messagethread.start()


def display_new_messages():
    while new_messages:
        message = new_messages.pop(0)
        prefix = """<b><span style="color: """ + getUserColor(message[1]) + """;">"""
        postfix = "</span></b>"
        print(message)
        text_area.appendHtml(
            "<small>" + message[0] + "</small>" + " " + prefix + message[1] + postfix + ": " + message[2])


def send_message():
    try:
        chat1.send(window.lineEdit.text())
        timestamp = datetime.datetime.now()
        fullmessage = "<small>" + chat1.timestamp() + "</small>" + " " + """<b><span style="color: """ + getUserColor(settings.value("username", stanusername)) + """;">""" + settings.value(
            "username", stanusername) + "</span>" + ": " + "</b>" + window.lineEdit.text()

        text_area.appendHtml(fullmessage)
        window.lineEdit.clear()

    except Exception as e:
        print(e)


def getUserColor(usr):
    color = "#" + str(hashlib.sha3_256(usr.encode("UTF-8")).hexdigest())[0:6]
    return color


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


def viewerthread():
    global views
    while True:
        try:

            views = get_viewercount(get_clientId(settings.value("channel", stanchannel)))
            window.set_viewercount()
            time.sleep(15)
        except Exception as e:
            print("error in other thread:")
            print(e)




viewerthread = Thread(target=viewerthread, daemon=True)
viewerthread.start()
window.lineEdit.returnPressed.connect(send_message)
ftimer = QTimer()
ftimer.timeout.connect(display_new_messages)
ftimer.start(100)
stimer.start(10000)

rwTimer = QTimer()
rwTimer.timeout.connect(startRiotwatcher)
rwTimer.start(15000)

app.exec_()
