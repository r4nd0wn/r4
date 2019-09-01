from riotwatcher import RiotWatcher, ApiError
import time
import json

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
gids = []
apikey = 'RGAPI-58a57de5-9f35-4563-807d-b9f9628ffa38'
accountid = 'esyeZI7W2HbdAlIRf9lPvZ9h3pIdM1-BawqWI3TIUGleKDM'
region = 'euw1'
fetchnigga = RiotWatcher(apikey)
matches = []
ownchampion = []
enemychampions = []
alllanes = []
with open('champion.json') as champion_file:
	champions = json.load(champion_file)

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
				except:
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
				rresult = "win"
		elif result == False:
			rresult = "lose"
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
							championname_enemy = champions[str(championId_enemy)]
						except:
							print(
								"Der Champion mit der ID " + str(championId_enemy) + " ist leider nicht mehr verfügbar")
		return championId_enemy, championname_enemy




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
	f.write("<p>" + """<img src="./ressources/pictures/champions/""" + str(championId_own) + """.png" style="width:12px;height:12px;">""" + championname_own + " vs " + championname_enemy + "</p>")
	f.write("""<p class="intended">""" + rresult + " " + str(kills) + "/" + str(deaths) + "/" + str(assists) + "   " + str(cs) + "</p>")

	f.write("<p>" + championname_own1 + " vs " + championname_enemy1 + "</p>")
	f.write("""<p class="intended">""" + rresult1 + "</p>")

	f.write("<p>" + championname_own2 + " vs " + championname_enemy2 + "</p>")
	f.write("""<p class="intended">""" + rresult2 + "</p>")

	f.write("</body></html>")

	time.sleep(2)
