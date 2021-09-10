from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from helpers.decorators import authorized_users_only
from config import BOT_NAME, BOT_USERNAME, OWNER_NAME, UPDATES_CHANNEL, SUPPORT_GROUP, ASSISTANT_NAME
from modules.play import cb_admin_check


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>𝐇𝐞𝐲 👋 {message.from_user.first_name}

𝐈 𝐚𝐦 𝐂𝐚𝐫𝐯𝐢𝐧𝐚𝐥 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭, 𝐔𝐬𝐞 𝐦𝐞 𝐭𝐨 𝐩𝐥𝐚𝐲 𝐦𝐮𝐬𝐢𝐜 𝐢𝐧 𝐲𝐨𝐮𝐫 𝐠𝐫𝐨𝐮𝐩𝐬 𝐕𝐨𝐢𝐜𝐞 𝐂𝐡𝐚𝐭.
𝐇𝐨𝐬𝐭𝐞𝐝 𝐎𝐧 𝐕𝐏𝐒, 𝐒𝐨 𝐧𝐨 𝐥𝐚𝐠

🥴𝐍𝐞𝐞𝐝 𝐇𝐞𝐥𝐩!
𝐔𝐬𝐞 𝐁𝐮𝐭𝐭𝐨𝐧𝐬 𝐁𝐞𝐥𝐨𝐰 𝐓𝐨 𝐊𝐧𝐨𝐰 𝐌𝐨𝐫𝐞 𝐀𝐛𝐨𝐮𝐭 𝐌𝐞 𝐚𝐧𝐝 𝐌𝐲 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬😁
:-) 𝗙𝗼𝗿 𝗠𝗼𝗿𝗲 𝗜𝗻𝗳𝗼, 𝗦𝗲𝗻𝗱 /help
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "➕ 𝐀𝐝𝐝 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(
                        "𝐇𝐨𝐰 𝐓𝐨 𝐔𝐬𝐞?💎", callback_data="cbhowtouse")
                ],[
                    InlineKeyboardButton(
                         "🤔𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬", url=f"https://t.me/IncognitoNetwork/8"
                    )
                ],[
                    InlineKeyboardButton(
                        "💬 𝐒𝐮𝐩𝐩𝐨𝐫𝐭", url=f"https://t.me/IncognitoOff"
                    ),
                    InlineKeyboardButton(
                        "🔊 𝐔𝐩𝐝𝐚𝐭𝐞𝐬", url=f"https://t.me/IncognitoNetwork"
                ],[
                    InlineKeyboardButton(
                        "𝐒𝐨𝐮𝐫𝐜𝐞 𝐂𝐨𝐝𝐞💞", url="https://t.me/AddyxD"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )





@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""𝐇𝐨𝐰 𝐓𝐨 𝐔𝐬𝐞 𝐌𝐞❓:

1.) ꜰɪʀꜱᴛ, ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
2.) ᴛʜᴇɴ ᴘʀᴏᴍᴏᴛᴇ ᴍᴇ ᴀꜱ ᴀᴅᴍɪɴ ᴀɴᴅ ɢɪᴠᴇ ᴀʟʟ ᴘᴇʀᴍɪꜱꜱɪᴏɴꜱ ᴇxᴄᴇᴘᴛ ᴀɴᴏɴʏᴍᴏᴜꜱ ᴀᴅᴍɪɴ.
3.) ᴀᴅᴅ @{ASSISTANT_NAME} ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴏʀ ᴛʏᴘᴇ /userbotjoin ᴛᴏ ɪɴᴠɪᴛᴇ ʜɪᴍ.
4.) ᴛᴜʀɴ ᴏɴ ᴛʜᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ꜰɪʀꜱᴛ ʙᴇꜰᴏʀᴇ ꜱᴛᴀʀᴛ ᴛᴏ ᴘʟᴀʏ ᴍᴜꜱɪᴄ.

""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🤔𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬", url=f"https://t.me/IncognitoNetwork/8"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🗑 𝗖𝗹𝗼𝘀𝗲", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()


@Client.on_callback_query(filters.regex("cbback"))
async def cbback(_, query: CallbackQuery):
    await query.edit_message_text(
        "**𝗛𝗲𝗿𝗲 𝗶𝘀 𝘁𝗵𝗲 𝗖𝗼𝗻𝘁𝗿𝗼𝗹 𝗠𝗲𝗻𝘂 𝗢𝗳 𝗕𝗼𝘁:**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⏸ 𝐏𝐚𝐮𝐬𝐞𝐝!", callback_data="cbpause"
                    ),
                    InlineKeyboardButton(
                        "▶️ 𝐑𝐞𝐬𝐮𝐦𝐞𝐝!", callback_data="cbresume"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⏩ 𝐒𝐤𝐢𝐩!", callback_data="cbskip"
                    ),
                    InlineKeyboardButton(
                        "⏹ 𝐄𝐧𝐝!", callback_data="cbend"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🗑 𝗖𝗹𝗼𝘀𝗲", callback_data="close"
                    )
                ]
            ]
        )
    )




@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""𝐇𝐨𝐰 𝐓𝐨 𝐔𝐬𝐞 𝐌𝐞❓:

1.) ꜰɪʀꜱᴛ, ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
2.) ᴛʜᴇɴ ᴘʀᴏᴍᴏᴛᴇ ᴍᴇ ᴀꜱ ᴀᴅᴍɪɴ ᴀɴᴅ ɢɪᴠᴇ ᴀʟʟ ᴘᴇʀᴍɪꜱꜱɪᴏɴꜱ ᴇxᴄᴇᴘᴛ ᴀɴᴏɴʏᴍᴏᴜꜱ ᴀᴅᴍɪɴ.
3.) ᴀᴅᴅ @{ASSISTANT_NAME} ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴏʀ ᴛʏᴘᴇ /userbotjoin ᴛᴏ ɪɴᴠɪᴛᴇ ʜɪᴍ.
4.) ᴛᴜʀɴ ᴏɴ ᴛʜᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ꜰɪʀꜱᴛ ʙᴇꜰᴏʀᴇ ꜱᴛᴀʀᴛ ᴛᴏ ᴘʟᴀʏ ᴍᴜꜱɪᴄ.

""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗑𝗖𝗹𝗼𝘀𝗲", callback_data="cbstart"
                    )
                ]
            ]
        )
    )
