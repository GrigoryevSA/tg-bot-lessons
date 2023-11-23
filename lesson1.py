import asyncio
import telegram

async def main():
    # Замените <ваш токен> на токен, который вы получили от @BotFather
    async with telegram.Bot(token='<ваш токен>') as bot:
        # Отправляем сообщение с текстом "Hello, World!" себе.
        # свой ID можно получить у бота: https://t.me/getmyuserid_bot
        message = await bot.send_message(chat_id=123456789, text='Hello, World!')

if __name__ == '__main__':
    asyncio.run(main())
