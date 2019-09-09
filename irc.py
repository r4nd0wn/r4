#
# [2016-03-14] Challenge #258 [Easy] IRC: Making a Connection
# https://www.reddit.com/r/dailyprogrammer/comments/4ad23z/20160314_challenge_258_easy_irc_making_a/
#

import socket

HOST = "irc.twitch.tv"
NICK = "r4nd0wn"
PORT = 6667
PASS = "oauth:m9aomgcvgacww3ybeo07m2pu162c0y"
readbuffer = ""
MODT = False
CHANNEL = "r4nd0wn"



PASSWORD = ("PASS " + PASS + "\r\n")
NICKNAME = ("NICK " + NICK + "\r\n")
CHANNELJOIN = ("JOIN #" + CHANNEL + "\r\n")


s = socket.socket()
s.connect((HOST, PORT))
s.send(PASSWORD.encode("utf-8"))
s.send(NICKNAME.encode("utf-8"))
s.send(CHANNELJOIN.encode("utf-8"))

def Parse_message(message):
    print(message)


while True:
    readbuffer = str(s.recv(1024))
    print(readbuffer)
    temp = readbuffer.split("\n")
    username = readbuffer.split("!")[0]
    username = username[3:]
    try:
        tempmessage = readbuffer.split("PRIVMSG #" + CHANNEL +" :")[1]
        content = tempmessage[:-5]
        print(content)
    except:
        print("no real message")
    print(username)
    print(temp)
    if(temp[0] == "PING"):
        print(temp[0])
        print("yes")
    else:
        print(temp[0])
