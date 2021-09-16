import logging
from checkWord import checkWord
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '1997155857:AAG3i7-nHUm9KDZXySOtYuO96iDXYahjYw8'
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("uz_imlo Botiga Xush Kelibsiz. \nBot sizga imlo xatolarni tekshirishga yordam beradi😊")


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply("Botdan foydalanish uchun so'z yuboring")


@dp.message_handler()
async def checkImlo(message: types.Message):
	name = message.from_user.first_name
	last_name = message.from_user.last_name
	user_id = message.from_user.id
	username = message.from_user.username
	words = message.text.split()
	for word in words:
		print(word)
		result = checkWord(word)
		
		if result['available']:
			response = f"✅{word.capitalize()}"
		else:
			response = f"❌{word.capitalize()}\n"
			for text in result['matches']:
				response += f"✅{text.capitalize()}\n"
		print(message.text)
		print(name, last_name, user_id, username)
		await message.answer(response)

if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)