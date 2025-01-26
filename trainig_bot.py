from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


# Команда /start для запуску гри
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton(
                text="Play Training Game",
                url="https://oleksandrhubar.github.io/training-game/"  # Замініть на URL вашої гри
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Welcome to the Training Game! Click the button below to start playing:",
        reply_markup=reply_markup
    )


# Основний код для запуску бота
def main():
    app = ApplicationBuilder().token("7694634757:AAFjYakmUnHATXYb5B9NkT_VudUo-KqP8Jc").build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()


if __name__ == "__main__":
    main()
