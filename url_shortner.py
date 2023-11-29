import requests
import urllib
import telepot
from telepot.loop import MessageLoop
def short(UR):
    link = "http://tinyurl.com/api-create.php"
    try:
        url = link + "?" \
        + urllib.parse.urlencode({"url": UR})
        res = requests.get(url)
        short=res.text
    except:
        short=_("can't short this link")
    return short

def message(msg):
    content_type,chat_type,chat_id=telepot.glance(msg)
    if msg["text"]=="/start":
        bot.sendMessage(chat_id,"welcome to this bot , this bot make you to short the link ,please send me the link and i short it")
    else:
        bot.sendMessage(chat_id,"result={}".format(short(msg["text"])))

bot=telepot.Bot("6940359512:AAEmKJi2G8K7L3cs0ud7g4vjMxq87tvLarU")
MessageLoop(bot,{"chat":message}).run_as_thread()
print("runing")
while True:
    pass