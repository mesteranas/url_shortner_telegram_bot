import requests
import urllib
import message,app
import telegram
from telegram import InlineKeyboardMarkup,InlineKeyboardButton
from telegram.ext import CommandHandler,MessageHandler,filters,ApplicationBuilder
with open("token.bot","r",encoding="utf-8") as file:
    bot=ApplicationBuilder().token(file.read()).build()
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

async def start(update,contextt):
    info=update.effective_user
    await message.Sendmessage(chat_id=info.id,text="welcome " + str(info.first_name) + "to this bot. This bot allows you to shorten links. Please send me the link, and I'll shorten it.")
async def helb(update,contextt):
    links="""<a href="https://t.me/mesteranasm">telegram</a>

<a href="https://t.me/tprogrammers">telegram channel</a>

<a href="https://x.com/mesteranasm">x</a>

<a href="https://Github.com/mesteranas">Github</a>

email:
anasformohammed@gmail.com

<a href="https://Github.com/mesteranas/url_shortner_telegram_bot">visite project on Github</a>
"""
    info=update.effective_user
    await message.Sendmessage(info.id,"""name: {}\nversion: {}\ndescription: {}\n developer: {}\n contect us {}""".format(app.name,str(app.version),app.description,app.developer,links))
async def msg(update,contextt):
    info=update.effective_user
    re=short(update.message.text)
    if not re=="Error":
        keyboard=InlineKeyboardMarkup([[InlineKeyboardButton("open link",url=re)]])
        await message.Sendmessage(info.id,"result=" + str(re),reply_markup=keyboard)
    else:
        await message.Sendmessage(info.id,"result=" + str(re))
print("running")
bot.add_handler(CommandHandler("start",start))
bot.add_handler(CommandHandler("help",helb))
bot.add_handler(MessageHandler(filters.Text(),msg))
bot.run_polling()