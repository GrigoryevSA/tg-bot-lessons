from telegram import ForceReply, Update
from telegram.ext import Application, ContextTypes, MessageHandler, filters

import config


async def reverse_echo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отправляем обратно пользовательское сообщение с обратным порядком символов"""
    text = update.message.text
    # Инвертируем порядок символов
    reversed_text = text[::-1]
    # Отправляем сообщение обратно с инвертированным текстом
    await update.message.reply_text(reversed_text)

def main() -> None:
    # Создаём приложение и передаём ему токен нашего бота
    application = Application.builder().token(config.token).build()

    # Для состоящих из текста и не являющихся командами добавляем echo как обработчик
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reverse_echo_handler))

    # Запускаем бота до тех пор пока пользователь не нажмёт ctrl+C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()