import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from config import BOT_TOKEN
from handlers.start import router as start_router

logging.basicConfig(
	level=logging.INFO,
	format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

async def main():
	# Создаем бота и диспетчер
	bot = Bot(token=BOT_TOKEN)
	storage = MemoryStorage()
	dp = Dispatcher(storage=storage)

	# Регистрация роутера
	dp.include_router(start_router)

	# Запуск бота
	logger.info("Бот стартует...")
	await dp.start_polling(bot)


if __name__ == "__main__":
	asyncio.run(main())