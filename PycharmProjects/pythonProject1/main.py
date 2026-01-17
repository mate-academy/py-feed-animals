import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
import config
import markups
from db import Database

bot = Bot(token=config.TOKEN)
dp = Dispatcher()
db = Database("users_db.db")

# referral system logic
@dp.message(Command(commands=["start"]))
async def start(message: Message):
    if not db.user_exists(message.from_user.id):
        start_comand = message.text
        referrer_id = str(start_comand[7:])
        print(referrer_id)
        print(message.from_user.id)
        if str(referrer_id) != "" and db.user_exists(referrer_id):
            db.add_user(message.from_user.id, referrer_id)
            try:
                await bot.send_message(referrer_id, "You have a new referral")
            except:
                db.add_user(message.from_user.id)
                pass
        else:
            db.add_user(message.from_user.id)

    await bot.send_message(message.from_user.id, "Hello there!", reply_markup=markups.mainMenu)

# button "profile" returns your ID and Lisf of IDs of your referrals
@dp.message()
async def bot_message(message: Message):
    if message.text == "Profile":
        await message.answer(
            f"ID: {message.from_user.id}\nInvite link:\nhttps://t.me/{config.BOT_NICK}?start={message.from_user.id}\nList of referrals:\n{db.count_referrals(message.from_user.id)}"
        )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
