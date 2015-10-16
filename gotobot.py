import time
import string
import random
import urllib.request
import os.path
import datetime
import queue
from slackclient import SlackClient
#import git
token = "xoxb-10882954435-SMZNaNlnbHilsDWo6fgyuuDT"# found at https://api.slack.com/#auth)
sc = SlackClient(token)
interns = ["Jon", "Yura", "Alex", "Avik", "Derek", "Tommy"]
people = interns + ["Omar", "David", "Alan", "Alison", "Bulent", "Carlos", "Jeff", "Steven", "Thurston", "Linda"]
timestamp = queue.Queue()
last_channel = ""
def startBot():
    print(datetime.datetime.now())
    # g = git.cmd.Git("C:\\Users\\D\\pfpui")
    whiteWrite = open

    whitelist = []
    with open("whitelist.txt", "r") as whiteRead:
         whitelist = whiteRead.read().split(" ")
    #whitelist.remove('')
    # g.pull()
    if sc.rtm_connect():
        while True:
            msg = sc.rtm_read()
            if(len(msg) == 1):
                print(msg)
                msg = msg[0]
                #print("type" in msg and msg["type"] == "message"and "text" in msg)
                if("type" in msg and msg["type"] == "message"and "text" in msg and all(c in string.printable for c in msg["text"].replace("'",""))):
                    #print(1)
                    if(msg["text"].lower() == "~addgrouptowhitelist" and msg['channel'] not in whitelist):
                        whitelist.append(msg["channel"])
                        with open("whitelist.txt", "w") as whiteWrite:
                            whiteWrite.write(" ".join(whitelist))
                    elif(msg["channel"] in whitelist):
                        #print("whitelisted")
                        if("~colorname" in msg["text"].lower()):
                            colorCode(msg)
                        elif("~randomintern" in msg["text"].lower()):
                            last_channel = msg["channel"]
                            sc.rtm_send_message(msg["channel"], random.choice(interns))
                        elif("~catfacts" in msg["text"].lower()):
                            print("cat")
                            request = str(urllib.request.urlopen("http://catfacts-api.appspot.com/api/facts?number=1").read())
                            last_channel = msg["channel"]
                            sc.rtm_send_message(msg["channel"], request[request.find('[') + 2:request.find(']') - 1])
                        elif("~quote" in msg["text"].lower()):
                            print("quote")
                            quote(msg)
                        elif("~startpoll" in msg["text"].lower()):
                            print("poll")
                            startPoll(msg)
                        elif("~stoppoll" in msg["text"].lower()):
                            pass
                            stopPoll(msg)
                        elif("~vote" in msg["text"].lower()):
                            pass
                            vote(msg)
                        elif("~deleteall" in msg["text"].lower()):
                            while not timestamp.empty():
                                ts = timestamp.get()
                                print(ts)
                                sc.api_call("chat.delete",channel=str(ts["channel"]), ts=str(ts["ts"]))
                        elif("~delete" in msg["text"].lower()):
                            if(not timestamp.empty()):
                                ts = timestamp.get()
                                sc.api_call("chat.delete",channel=str(ts["channel"]), ts=str(ts["ts"]))
                        #sc.rtm_send_message(msg["channel"], msg["text"])
                elif("ok" in msg and msg["ok"] == True):
                    timestamp.put({"ts":msg["ts"],"channel":last_channel})
            elif(len(msg) > 1):
                print(msg)
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            time.sleep(.5)
    else:
        print("Connection Failed, invalid token?")


def colorCode(msg):
    print("color")
    name = msg["text"][1 + msg["text"].find(" "):]
    if(name == msg['text']):
        sc.rtm_send_message(msg["channel"], "Invalid arguments")
        return
    # tmp="#"
    # for ch in name[:3]:
    #     tmp += hex(ord(ch))[2:]
    if(name.lower() == "jon"):
        h = "#39FF14"
    elif(name.lower() == "verbose"):
        h = "#b00bee"
    else:
        h = "#" + hex(abs(hash(name)))[2:8]
    last_channel = msg["channel"]
    sc.rtm_send_message(msg["channel"], h)

def quote(msg):
    print(msg)
    args = msg["text"].split(",")
    print(len(args))
    print(args)
    if(len(args) >= 3):
        print(3)
        if(args[1] in people):
            fileName = people[people.index(args[1])] + "Quotes.txt"
            #need to get full quote
            with open(fileName, "a+") as f:
                if(os.path.isfile(fileName)):
                    f.write("," + args[2])
                else:
                    f.write(args[2])
            sc.rtm_send_message(msg["channel"], "Quote added " + args[2])
    elif(len(args) == 2):
        print(2)
        quotes = []
        if(args[1] in people):
            fileName = people[people.index(args[1])] + "Quotes.txt"
            if(os.path.isfile(fileName)):
                with open(fileName, "r") as read:
                    quotes = read.read().split(",")
            if(len(quotes) > 0):
                last_channel = msg["channel"]
                sc.rtm_send_message(msg["channel"], random.choice(quotes))

def startPoll(msg):
    pass

#def send(msg):



startBot()