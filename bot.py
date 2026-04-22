from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from config import *

app = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# 🔍 cek join semua
async def is_joined_all(client, user_id):
    try:
        await client.get_chat_member(CHANNEL_1, user_id)
        await client.get_chat_member(CHANNEL_2, user_id)
        await client.get_chat_member(GROUP, user_id)
        return True
    except:
        return False

# 🚀 START
@app.on_message(filters.command("start"))
async def start(client, message):
    user_id = message.from_user.id

    if not await is_joined_all(client, user_id):
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("ᴊᴏɪɴ ᴅᴜʟᴜ", url=f"https://t.me/{CHANNEL_1.replace('@','')}")], [InlineKeyboardButton("ᴊᴏɪɴ ʟᴀɢɪ", url=f"https://t.me/{CHANNEL_2.replace('@','')}")],
            [InlineKeyboardButton("ᴊᴏɪɴ ʟᴀɢɪ", url=f"https://t.me/{GROUP.replace('@','')}")],
            [InlineKeyboardButton("ᴄᴏʙᴀ ʟᴀɢɪ", callback_data="check_join")]
        ])

        await message.reply_text(
            "Anda harus bergabung di Channel/Grup saya Terlebih dahulu untuk Melihat File yang saya Bagikan

Silakan Join Ke Channel & Group Terlebih Dahulu\nKlik tombol bawah 👇",
            reply_markup=keyboard
        )
    else:
        await message.reply_text("🔥 Mantap! Lu udah join semua, akses kebuka!")

# 🔁 BUTTON CEK ULANG
@app.on_callback_query(filters.regex("check_join"))
async def check_join(client, query: CallbackQuery):
    user_id = query.from_user.id

    if await is_joined_all(client, user_id):
        await query.message.edit_text("🔥 Mantap! Lu udah join semua, akses kebuka!")
    else:
        await query.answer("❌ Masih belum join semua!", show_alert=True)

app.run()
