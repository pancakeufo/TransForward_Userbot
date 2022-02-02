from pyrogram import Client, Filters, Message, MessageHandler
from googletrans import Translator
import asyncio, os
os.system("clear")

# ID DEGLI ADMIN
admin = [123456]
# ID DEL CANALE DA CONTROLLARE
channel_id = None
# ID DEL GRUPPO DOVE INVIARE
group_id = None

bot = Client("userbot")

# PING USERBOT
@bot.on_message(Filters.user(admin) & Filters.command('on', prefixes=['.', '>', ';', '/', '#']))
async def ping(bot: bot, message: Message):
    await message.reply("Userbot online")

# TRADUZIONE E INVIO
@bot.on_message(Filters.channel & Filters.chat(channel_id))
async def sendTranslation(bot: bot, message: Message):
    translator = Translator()
    translation = translator.translate(message.text, dest='it', src='auto')
    if hasattr(translation, 'text'):
        await bot.send_message(group_id, translation.text, disable_web_page_preview=True)

# RUN
async def main():
    await bot.start()
    await bot.idle()

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
