from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

router = Router()


class Gen(StatesGroup):
    wait = State()

# отлов команды старт
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('привет, создайте свой запрос!!!')
# стоп флуд
@router.message(Gen.wait)
async def stop_flood(message: Message):
    await message.answer('Подождите ваш запрос генерируется!!!')
#   смотрим состояние
@router.message()
async def generating(message: Message, state: FSMContext):
    await state.set_data(Gen.wait)