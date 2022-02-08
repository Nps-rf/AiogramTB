from aiogram.utils import executor
from create import dp
from ClientSide import activate_handlers

activate_handlers(dp=dp)

executor.start_polling(dp, skip_updates=True)

