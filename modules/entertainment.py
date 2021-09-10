import requests
from pyrogram import Client
from config import BOT_USERNAME
from helpers.filters import command


@Client.on_message(command(["lyrics", f"lyrics@{BOT_USERNAME}"]))
async def lirik(_, message):
    try:
        if len(message.command) < 2:
            await message.reply_text("**𝐒𝐨𝐧𝐠 𝐍𝐚𝐦𝐞 𝐏𝐥𝐳!**")
            return
        query = message.text.split(None, 1)[1]
        rep = await message.reply_text("**𝐆𝐞𝐭𝐭𝐢𝐧𝐠 𝐈𝐭!**😍")
        resp = requests.get(f"https://api-tede.herokuapp.com/api/lirik?l={query}").json()
        result = f"{resp['data']}"
        await rep.edit(result)
    except Exception:
        await rep.edit("𝗦𝗮𝗱, 𝗟𝘆𝗿𝗶𝗰𝘀 𝗡𝗼𝘁 𝗙𝗼𝘂𝗻𝗱. 𝗧𝗿𝘆 𝗪𝗶𝘁𝗵 𝗮 𝗩𝗮𝗹𝗶𝗱 𝗡𝗮𝗺𝗲 𝗕𝗿𝘂𝗵!")

@Client.on_message(command(["fakename", f"fakename@{BOT_USERNAME}"]))
async def dare(client, message):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/fakename?country=id_ID").json()
        results = f"{resp['name']}"
        return await message.reply_text(results)
    except Exception:
        await message.reply_text("𝐒𝐨𝐦𝐞𝐭𝐡𝐢𝐧𝐠 𝐰𝐞𝐧𝐭 𝐰𝐫𝐨𝐧𝐠 𝐋𝐎𝐋...😶")
