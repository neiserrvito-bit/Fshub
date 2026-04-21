from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from config import BOT_TOKEN, CHANNEL_USERNAME

# START COMMAND
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_id = user.id

    try:
        member = await context.bot.get_chat_member(CHANNEL_USERNAME, user_id)

        # Kalau user SUDAH join
        if member.status in ["member", "administrator", "creator"]:
            await update.message.reply_text(
                f"✅ Hello {user.first_name}\n\nLu udah join, silakan akses file 🔥"
            )
        else:
            raise Exception("Belum join")

    except:
        # Tombol join
        keyboard = [
            [InlineKeyboardButton("📢 Join Channel", url=f"https://t.me/slengean22('@','')}")],
            [InlineKeyboardButton("🔁 Coba Lagi", callback_data="check_join")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text(
            f"🚫 Hello {user.first_name}\n\nLu harus join channel dulu buat akses file!",
            reply_markup=reply_markup
        )

# BUTTON HANDLER
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id

    try:
        member = await context.bot.get_chat_member(CHANNEL_USERNAME, user_id)

        if member.status in ["member", "administrator", "creator"]:
            await query.edit_message_text(
                "✅ Mantap! Lu udah join.\n\nSekarang akses file terbuka 🔥"
            )
        else:
            raise Exception("Belum join")

    except:
        await query.answer("❌ Masih belum join bro 😅", show_alert=True)

# MAIN
app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

print("Bot jalan...")
app.run_polling()
