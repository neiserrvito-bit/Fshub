from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)
from config import BOT_TOKEN, CHANNEL_USERNAME


# 🔥 FUNCTION CEK MEMBER
async def is_user_joined(bot, user_id):
    try:
        member = await bot.get_chat_member(CHANNEL_USERNAME, user_id)
        return member.status in ["member", "administrator", "creator"]
    except:
        return False


# 🚀 START COMMAND
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_id = user.id

    joined = await is_user_joined(context.bot, user_id)

    if joined:
        await update.message.reply_text(
            f"✅ Halo {user.first_name}!\nLu udah join, silakan akses file 🔥"
        )
    else:
        keyboard = [
            [InlineKeyboardButton(
                "📢 Join Channel",
                url=f"https://t.me/{CHANNEL_USERNAME.replace('@','')}"
            )],
            [InlineKeyboardButton(
                "🔄 Coba Lagi",
                callback_data="check_join"
            )]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text(
            "🚫 Lu harus join channel dulu ya!\n\nKlik tombol bawah 👇",
            reply_markup=reply_markup
        )


# 🔄 BUTTON CEK ULANG
async def check_join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id
    joined = await is_user_joined(context.bot, user_id)

    if joined:
        await query.edit_message_text(
            "✅ Mantap! Lu udah join.\nSekarang akses file kebuka 🔥"
        )
    else:
        await query.answer("❌ Masih belum join bro 😅", show_alert=True)


# 🚀 MAIN APP
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(check_join))

    print("🤖 Bot jalan...")
    app.run_polling()


if __name__ == "__main__":
    main()
