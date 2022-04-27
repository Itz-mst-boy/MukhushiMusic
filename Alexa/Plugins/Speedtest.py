import os

import speedtest
import wget
from pyrogram import Client, filters
from pyrogram.types import Message

from Alexa import BOT_ID, SUDOERS, app
from Alexa.Utilities.formatters import bytes

__MODULE__ = "🚅 sᴘᴇᴇᴅᴛᴇsᴛ"
__HELP__ = """

`/speedtest`
- ᴄʜᴇᴄᴋ sᴇʀᴠᴇʀ ʟᴀᴛᴇɴᴄʏ ᴀɴᴅ sᴘᴇᴇᴅ.

- ᴘᴏᴡᴇʀᴅ ʙʏ 😍 ʀᴏᴄᴋs ᴀɴᴅ @mukhushi_official.

"""


@app.on_message(filters.command("speedtest") & ~filters.edited)
async def statsguwid(_, message):
    m = await message.reply_text("ʀᴜɴɴɪɴɢ sᴘᴇᴇᴅ ᴛᴇsᴛ...")
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = await m.edit("ʀᴜɴɴɪɴɢ ᴅᴏᴡɴʟᴏᴀᴅ sᴘᴇᴇᴅᴛᴇsᴛ...")
        test.download()
        m = await m.edit("ʀᴜɴɴɪɴɢ ᴜᴘʟᴏᴀᴅ sᴘᴇᴇᴅᴛᴇsᴛ...")
        test.upload()
        test.results.share()
        result = test.results.dict()
    except Exception as e:
        return await m.edit(e)
    m = await m.edit("sʜᴀʀɪɴɢ sᴘᴇᴇᴅᴛᴇsᴛ ʀᴇsᴜʟᴛs...")
    path = wget.download(result["share"])

    output = f"""**sᴘᴇᴇᴅᴛᴇsᴛ ʀᴇsᴜʟᴛs**
    
<u>**ᴄʟɪᴇɴᴛ:**</u>
**ɪsᴘ:** {result['client']['isp']}
**ᴄᴏᴜɴᴛʀʏ:** {result['client']['country']}
  
<u>**sᴇʀᴠᴇʀ:**</u>
**ɴᴀᴍᴇ:** {result['server']['name']}
**ᴄᴏᴜɴᴛʀʏ:** {result['server']['country']}, {result['server']['cc']}
**sᴘᴏɴsᴏʀ:** {result['server']['sponsor']}
**ʟᴀᴛᴇɴᴄʏ:** {result['server']['latency']}  
**ᴘɪɴɢ:** {result['ping']}"""
    msg = await app.send_photo(
        chat_id=message.chat.id, photo=path, caption=output
    )
    os.remove(path)
    await m.delete()
