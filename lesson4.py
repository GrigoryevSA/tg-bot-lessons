from telegram import ForceReply, Update
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, ContextTypes, MessageHandler, filters

import config

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async def inline_keyboard_sender(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    button1 = InlineKeyboardButton("Button 1", callback_data='btn1')
    button2 = InlineKeyboardButton("Button 2", callback_data='btn2')
    button3 = InlineKeyboardButton("Button 3", callback_data='btn3')

    keyboard = [[button1, button2], [button3]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Отправляем сообщение с клавиатурой
    await update.message.reply_text('Выберите кнопку:', reply_markup=reply_markup)

def main() -> None:
    # Создаём приложение и передаём ему токен нашего бота
    application = Application.builder().token(config.token).build()

    # Для состоящих из текста и не являющихся командами добавляем echo как обработчик
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, inline_keyboard_sender))

    # Запускаем бота до тех пор пока пользователь не нажмёт ctrl+C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()