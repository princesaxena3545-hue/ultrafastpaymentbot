from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
import os

BOT_TOKEN = os.environ["BOT_TOKEN"]
ADMIN_ID = 7796466520

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📸 Payment screenshot bhejo.\nAdmin verify karne ke baad file/link di jayegi."
    )

async def photo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    await context.bot.forward_message(
        chat_id=ADMIN_ID,
        from_chat_id=update.effective_chat.id,
        message_id=update.message.message_id
    )

    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=f"👤 User: @{user.username}\n🆔 ID: {user.id}"
    )

    await update.message.reply_text(
        "✅ Screenshot receive ho gaya.\nVerification ke baad aapko file/link bheji jayegi."
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO, photo_handler))

    print("Bot Started...")
    app.run_polling()

if __name__ == "__main__":
    main()
