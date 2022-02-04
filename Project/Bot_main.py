from aiogram.utils import executor
from create import dp
from ClientSide import activate_message_handlers

activate_message_handlers(dp=dp)

executor.start_polling(dp, skip_updates=True)

