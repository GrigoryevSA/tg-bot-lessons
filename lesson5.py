from telegram import ForceReply, Update
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, ContextTypes, MessageHandler, filters

import config

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import ReplyKeyboardMarkup, KeyboardButton


async def reply_keyboard_sender(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    button1 = KeyboardButton("Button 1")
    button2 = KeyboardButton("Button 2")
    button3 = KeyboardButton("Button 3")

    keyboard = [[button1, button2], [button3]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    # Отправляем сообщение с клавиатурой
    await update.message.reply_text('Выберите кнопку:', reply_markup=reply_markup)

def main() -> None:
    # Создаём приложение и передаём ему токен нашего бота
    application = Application.builder().token(config.token).build()

    # Для состоящих из текста и не являющихся командами добавляем echo как обработчик
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_keyboard_sender))

    # Запускаем бота до тех пор пока пользователь не нажмёт ctrl+C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()