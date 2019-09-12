import sys
import time
import json
from riotwatcher import RiotWatcher, ApiError
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import threading
import logging

from PyQt5 import QtCore, QtGui, QtWidgets
# ***HTML Skeleton***#
html_upper = """
<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <title></title>
  <meta name="author" content="r4nd0wn">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta http-equiv="refresh" content="5">
  <link rel = "stylesheet"
   type = "text/css"
   href = "styles.css" />
</head>

<body>
"""

chat_upper = """
<html>
  <head>
    <title></title>
    <meta content="">
    <style></style>
  </head>
  <body>
  	<iframe frameborder="0"
        scrolling="no"
        id="chat_embed"
        src="https://www.twitch.tv/embed/
"""
chat_lower = """
/chat"
        height="460"
        width="300">
	</iframe>

  </body>
</html>
"""


gids = []
apikey = 'RGAPI-43a35a08-8b30-4a9c-b7c7-0612007c59e0'
accountid = 'esyeZI7W2HbdAlIRf9lPvZ9h3pIdM1-BawqWI3TIUGleKDM'
region = 'euw1'
matches = []
ownchampion = []
enemychampions = []
alllanes = []
username_twitch = 'r4nd0wn'

with open('champion.json') as champion_file:
	champions = json.load(champion_file)


class Fenster(QWidget):
	def __init__(self):
		super().__init__()
		self.initMe()

	def initMe(self):


		self.setGeometry(0,30,530,150)
		self.setFixedSize(530, 150)

		self.setWindowTitle("r4 - created by r4nd0wn.")
		self.setWindowIcon(QIcon("ressources/pictures/r4.svg"))

		self.apibutton = QPushButton('Set API Key', self)
		self.apibutton.setGeometry(400, 20, 110, 23)
		self.apibutton.clicked.connect(self.apichanged)

		self.accountbutton = QPushButton('Set AccountID', self)
		self.accountbutton.setGeometry(400, 60, 110, 23)
		self.accountbutton.clicked.connect(self.accchanged)

		self.startbutton = QPushButton("Start the API Script", self)
		self.startbutton.setGeometry(20, 110, 230, 23)
		self.startbutton.clicked.connect(startthread)

		self.stopbutton = QPushButton("Stop the API Script", self)
		self.stopbutton.setGeometry(280, 110, 230, 23)
		self.stopbutton.clicked.connect(stopthread)

		self.apiinsert = QLineEdit("Insert API Key here", self)
		self.apiinsert.setGeometry(20, 20, 340, 23)

		self.accinsert = QLineEdit('Insert AccountID here', self)
		self.accinsert.setGeometry(20, 60, 340, 23)

		self.show()

	def apichanged(self):
		global apikey
		apikey = self.apiinsert.text()

	def accchanged(self):
		global accountid
		print(accountid)
		accountid = self.accinsert.text()
		print(accountid)

class User:
	def __init__(self, accountid, watcher, region):
		self.accountid = accountid
		self.watcher = watcher
		self.region = region
	def get_matchids(self):

		with open('champion.json') as champion_file:
			champions = json.load(champion_file)

		# ***GET THE MATCH ID***#

		matchlist = self.watcher.match.matchlist_by_account(self.region, self.accountid)
		onlymatches = matchlist['matches']

		for x in onlymatches:
			if x['queue'] == 420:
				gids.append(x['gameId'])
		return gids
	def get_partids(self, matchid):
		self.matchid = matchid
		matchinfo = self.watcher.match.by_id(self.region, matchid)
		print(matchinfo)

	def get_user_info(self, matchid, rich):
		self.matchid = matchid
		self.rich = rich
		matchinfo = self.watcher.match.by_id(self.region, matchid)
		participants = matchinfo['participants']
		pl = matchinfo['participantIdentities']
		for z in pl:
			pi = z['player']
			if pi['accountId'] == self.accountid:
				partID = z['participantId']
		for a in participants:

			# ***HIER MATCHSPEZIFISCHE INFOS ÜBER KAXM ACCOUNT***#

			if a['participantId'] == partID:
				championId_own = a['championId']
				try:
					championname_own = champions[str(championId_own)]
				except Exception as e:
					print(e)
					print("Der Champion mit der ID " + str(championId_own) + " ist leider nicht mehr verfügbar")

				stats = a['stats']
				for b in stats:
					if b == "kills":
						kills = stats[b]
					if b == "deaths":
						deaths = stats[b]
					if b == "assists":
						assists = stats[b]
					if b == "win":
						result = stats[b]
					if b == "totalMinionsKilled":
						cs = stats[b]
				time = a['timeline']
				for c in time:
					if c == "lane":
						lane = time[c]
		if result == True:
				rresult = """<div style="color:blue">Win</div>"""
		elif result == False:
			rresult = """<div style="color:red">Defeat</div>"""
		if self.rich == True:
			return rresult, lane, championId_own, championname_own, kills, deaths, assists, cs
		if self.rich == False:
			return rresult, championId_own, championname_own
	def get_enemyinfo(self, matchid, lane):
		self.matchid = matchid
		self.lane = lane
		matchinfo = self.watcher.match.by_id(self.region, matchid)
		participants = matchinfo['participants']
		pl = matchinfo['participantIdentities']
		for z in pl:
			pi = z['player']
			if pi['accountId'] == self.accountid:
				partID = z['participantId']
		for d in participants:
			enemystats = d['stats']
			enemytime = d['timeline']
			for f in enemytime:
				if enemytime[f] == lane:
					if d['participantId'] != partID:
						partIDenemy = d['participantId']
						championId_enemy = d['championId']
						try:
							print(championId_enemy)
							championname_enemy = champions[str(championId_enemy)]
						except Exception as e:
							print(e)
							print("Der Champion mit der ID " + str(championId_enemy) + " ist leider nicht mehr verfügbar")
		return championId_enemy, championname_enemy

def allinone():
	try:
		global apikey
		global accountId
		global accountid
		fetchnigga = RiotWatcher(apikey)
		abfrage1 = User(accountid, fetchnigga, region)
		while True:
			matchids = abfrage1.get_matchids()
			del matchids[3:]
			rresult, lane, championId_own, championname_own, kills, deaths, assists, cs = abfrage1.get_user_info(matchids[0], True)
			championID_enemy, championname_enemy = abfrage1.get_enemyinfo(matchids[0], lane)

			rresult1, championId_own1, championname_own1 = abfrage1.get_user_info(matchids[1], False)
			championID_enemy1, championname_enemy1 = abfrage1.get_enemyinfo(matchids[1], lane)

			rresult2, championId_own2, championname_own2 = abfrage1.get_user_info(matchids[2], False)
			championID_enemy2, championname_enemy2 = abfrage1.get_enemyinfo(matchids[2], lane)
			
			f = open('index.html', 'w')
			f.write(html_upper)
			f.write("""<table align="center"; style="width:100%">""")
			f.write("<tr>" + "<td>" + """<img src="./ressources/pictures/champions/""" + str(championId_own) + """.png" style="width:16px;height:16px;">""" +  " vs " + """<img src="./ressources/pictures/champions/""" + str(championID_enemy) + """.png" style="width:16px;height:16px;">""" + "</td>" + "</tr>")
			f.write("<tr>" + "<td>" + rresult + "   KDA:" + str(kills) + "/" + str(deaths) + "/" + str(assists) + "   " + "  CS:" + str(cs) + "</td>" + "</tr>")

			f.write("<tr>" + "<td>" + """<img src="./ressources/pictures/champions/""" + str(championId_own1) + """.png" style="width:16px;height:16px;">""" + " vs " + """<img src="./ressources/pictures/champions/""" + str(championID_enemy1) + """.png" style="width:16px;height:16px;">""" + "</td>" +  "</tr>")
			f.write("<tr>" + "<td>" + rresult1 + "</td>" + "</tr>")

			f.write("<tr>" + "<td>" + """<img src="./ressources/pictures/champions/""" + str(championId_own2) + """.png" style="width:16px;height:16px;">"""  + " vs " + """<img src="./ressources/pictures/champions/""" + str(championID_enemy2) + """.png" style="width:16px;height:16px;">""" + "</td>" + "</tr>")
			f.write("<tr>" + "<td>" + rresult2 + "</td>" + "</tr>")

			f.write("</table>")

			f.write("</body></html>")

			time.sleep(12)
	except Exception as e:
		print(e)
		print("error location: allinone")


apithread = threading.Thread(target=allinone)

def startthread():
	global apikey
	global accountid
	if apikey != 'thisisnotavalidapikey' and accountid != 'thisisnotavalidapikey':
		try:
			apithread.start()
		except Exception as e:
			print(e)
			print("error location: startthread")
	
def stopthread():
	try:
		apithread.stop()
	except Exception as e:
		print(e)
		print("error location: stopthread")

app = QApplication(sys.argv)
window = Fenster()


sys.exit(app.exec_())