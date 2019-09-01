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
</head>

<body>
"""
gids = []
apikey = 'RGAPI-04bbdc31-af35-4cb8-8051-0dece5a40b6d'
fetchnigga = RiotWatcher(apikey)
currentregion = 'euw1'
matches = []
ownchampion = []
enemychampions = []
alllanes = []


class checker:
    def __init__(self, apikey, accountid):
        self.apikey = apikey
        self.accountid = accountid

def apihandler():
    with open('champion.json') as champion_file:
        champions = json.load(champion_file)

    # ***GET THE MATCH ID***#

    matchlist = fetchnigga.match.matchlist_by_account(currentregion, "esyeZI7W2HbdAlIRf9lPvZ9h3pIdM1-BawqWI3TIUGleKDM")
    onlymatches = matchlist['matches']

    for x in onlymatches:
        if x['queue'] == 420:
            gids.append(x['gameId'])

    print('you played ' + str(len(
        gids)) + ' rank games in the last 100 matches. I will extract the last 3 from all your rank games (sorted by timestamp):')
    del gids[3:]
    print(gids)

    for y in gids:
        print(y)
        ueber = fetchnigga.match.by_id(currentregion, y)
        # print(type(ueber['participantIdentities']))
        pl = ueber['participantIdentities']
        for z in pl:
            pi = z['player']

            # ***HIER ALLGEMEINE INFOS ÜBER KAXM ACCOUNT***#

            if pi['accountId'] == "esyeZI7W2HbdAlIRf9lPvZ9h3pIdM1-BawqWI3TIUGleKDM":
                print("ICH HABE EIN AUTISTEN GEFUNDEN")
                partID = z['participantId']

        parties = ueber['participants']

        for a in parties:

            # ***HIER MATCHSPEZIFISCHE INFOS ÜBER KAXM ACCOUNT***#

            if a['participantId'] == partID:
                championId_played = a['championId']
                try:
                    championname_current = champions[str(championId_played)]
                except:
                    print("Der Champion mit der ID " + str(championId_played) + " ist leider nicht mehr verfügbar")

                stats = a['stats']
                for b in stats:
                    if b == "win":
                        result = stats[b]
                time = a['timeline']
                for c in time:
                    if c == "lane":
                        lane = time[c]

        # ***HIER INFO ÜBER LANE GEGNER***#

        for d in parties:
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

        if result == True:
            rresult = "gewonnen"
        elif result == False:
            rresult = "verloren"
        print(
            "Du hast auf der " + lane + " lane mit " + championname_current + " gegen " + championname_enemy + " gespielt")
        print("Ihr habt " + rresult)

    f = open('index.html', 'w')
    f.write(html_upper)
    f.write("<p>" + championname_current + " vs " + championname_enemy + "</p>")
    f.write("""<p class="intended">""" + rresult + "</p>")

    f.write("</body></html>")


while True:
    apihandler()
    gids.clear()
    print(gids)
    time.sleep(60)
