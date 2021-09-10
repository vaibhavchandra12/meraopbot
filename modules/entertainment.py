import requests
from pyrogram import Client
from config import BOT_USERNAME
from helpers.filters import command
import io
import os
from tswift import Song


@Client.on_message(command(["lyrics", f"lyrics@{BOT_USERNAME}"]))         
async def _(client, message):
    lel = await message.reply("**𝐆𝐞𝐭𝐭𝐢𝐧𝐠 𝐈𝐭!**😍")
    query = message.text
    if not query:
        await lel.edit("𝗦𝗮𝗱, 𝗟𝘆𝗿𝗶𝗰𝘀 𝗡𝗼𝘁 𝗙𝗼𝘂𝗻𝗱. 𝗧𝗿𝘆 𝗪𝗶𝘁𝗵 𝗮 𝗩𝗮𝗹𝗶𝗱 𝗡𝗮𝗺𝗲 𝗕𝗿𝘂𝗵!")
        return

    song = ""
    song = Song.find_song(query)
    if song:
        if song.lyrics:
            reply = song.format()
        else:
            reply = "𝗦𝗮𝗱, 𝗟𝘆𝗿𝗶𝗰𝘀 𝗡𝗼𝘁 𝗙𝗼𝘂𝗻𝗱. 𝗧𝗿𝘆 𝗪𝗶𝘁𝗵 𝗮 𝗩𝗮𝗹𝗶𝗱 𝗡𝗮𝗺𝗲 𝗕𝗿𝘂𝗵!"
    else:
        reply = "𝗦𝗮𝗱, 𝗟𝘆𝗿𝗶𝗰𝘀 𝗡𝗼𝘁 𝗙𝗼𝘂𝗻𝗱. 𝗧𝗿𝘆 𝗪𝗶𝘁𝗵 𝗮 𝗩𝗮𝗹𝗶𝗱 𝗡𝗮𝗺𝗲 𝗕𝗿𝘂𝗵!!"

    if len(reply) > 4095:
        with io.BytesIO(str.encode(reply)) as out_file:
            out_file.name = "lyrics.text"
            await client.send_document(
                message.chat.id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=query,
                reply_to_msg_id=message.message_id,
            )
            await lel.delete()
    else:
        await lel.edit(reply)  # edit or reply
        
        
@Client.on_message(command(["fakename", f"fakename@{BOT_USERNAME}"]))
async def dare(client, message):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/fakename?country=id_ID").json()
        results = f"{resp['name']}"
        return await message.reply_text(results)
    except Exception:
        await message.reply_text("𝐒𝐨𝐦𝐞𝐭𝐡𝐢𝐧𝐠 𝐰𝐞𝐧𝐭 𝐰𝐫𝐨𝐧𝐠 𝐋𝐎𝐋...😶")

        
