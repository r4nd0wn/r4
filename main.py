from riotwatcher import RiotWatcher
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
   href = "style.css" />
</head>

<body>
"""
timeless = round(time.time() * 1000) - 43200000 * 2
gids = []
apikey = 'RGAPI-ebe77482-0b14-4670-9885-145c954b3a6e'
fetchnigga = RiotWatcher(apikey)
currentregion = 'euw1'


def apihandler():
    with open('champion.json') as champion_file:
        champions = json.load(champion_file)

    # ***GET THE MATCH ID***#

    me = fetchnigga.summoner.by_name(currentregion, 'R 4 N D 0 W N')

    matchlist = fetchnigga.match.matchlist_by_account(currentregion, "esyeZI7W2HbdAlIRf9lPvZ9h3pIdM1-BawqWI3TIUGleKDM")

    onlymatches = matchlist['matches']
    for x in onlymatches:
        if x['timestamp'] > timeless:
            gids.append(x['gameId'])
    print('I found the following matches which are completed within the last 12 hours:')
    print(gids)

    matches = []
    for y in gids:
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
                    print("Der Champion mit der ID " + str(championId) + " ist leider nicht mehr verfügbar")

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
    rresult = "empty"
    f = open('index.html', 'w')
    f.write(html_upper)
    championname_current = "lappen"
    championname_enemy = "lulu"

    f.write("<p>mit " + championname_current + " gegen " + championname_enemy + " " + rresult + "</p>")

    f.write("</body></html>")


while True:
    apihandler()
    time.sleep(100)
