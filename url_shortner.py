import requests
import urllib
import telepot
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
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
    if content_type == 'text':
        if msg["text"]=="/start":
           bot.sendMessage(chat_id, f"Welcome {msg['from']['first_name']} to this bot. This bot allows you to shorten links. Please send me the link, and I'll shorten it.")
        else:
            re=short(msg["text"])
            if not re=="Error":
                keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Open Link', url=re)]])
                bot.sendMessage(chat_id,"result={}".format(re),reply_markup=keyboard)
            else:
                bot.sendMessage(chat_id,"result={}".format(re))
    else:
        bot.sendMessage(chat_id,"please send text messages only")

bot=telepot.Bot("token")
bot.deleteWebhook()
MessageLoop(bot,{"chat":message}).run_as_thread()
print("runing")
while True:
    pass