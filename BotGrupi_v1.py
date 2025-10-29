from telethon import TelegramClient, errors
import asyncio
import random

# 📌 API ID та API Hash з Telegram
API_ID = 21587711  # Введи своє API ID
API_HASH = 'e3c874b8830e229d4aeb903b8d249efd'  # Введи своє API HASH
# 📌 Номер телефону
PHONE_NUMBER = '+380982645731'

# 📌 Створюємо клієнта для Telegram
client = TelegramClient('bot_session', API_ID, API_HASH)

# 🔍 Список варіантів текстів для реклами
messages = [
    # Реклама групи "Всі оголошення України"
    "🌟 **Хей, друже!** 🌟\n🔥 Хочеш **продати**, **купити** або **знайти щось цікаве**? 🔥\n💸 Тут ти знайдеш усе — від авто 🚗 до оренди житла 🏠!\n📢 Приєднуйся прямо зараз 👉 https://t.me/vsi_ogoloshenya_ua\n💬 Тисячі українців вже з нами 🇺🇦",
    "💥 **Гаряча група оголошень України!** 💥\n🛍️ Продаєш? Купуєш? Шукаєш послуги?\n✨ У нас усе просто: публікуй і знаходь за 1 хвилину!\n🚀 Вступай: https://t.me/vsi_ogoloshenya_ua — не пропусти вигідні пропозиції! 💰",
    "📣 **ОГОЛОШЕННЯ УКРАЇНИ!** 🇺🇦\n💎 Товари, послуги, робота — все в одному місці!\n🤝 Знайомся, домовляйся, заробляй 💼\n🔗 Приєднуйся: https://t.me/vsi_ogoloshenya_ua ❤️",
    "🔥 **ТОП-ГРУПА ОГОЛОШЕНЬ!** 🔥\n📦 Купи 🛒 Продай 💬 Знайди 💡\n💥 Без спаму, тільки актуальні оголошення!\n🌍 Приєднуйся 👉 https://t.me/vsi_ogoloshenya_ua\n💖 Твоя вигідна пропозиція вже чекає тебе!",
    "🚨 **Шукаєш щось зараз?** 🚨\n🕵️ Знайди роботу, житло або клієнтів — усього в 1 клік!\n🎯 Реальні люди, реальні угоди ✅\n📲 Вступай: https://t.me/vsi_ogoloshenya_ua",
    # Реклама каналу "Україна Онлайн ⚡"
    "⚡ **Україна Онлайн** ⚡\n📢 Будь в курсі ВСІХ новин України! 📰\n🔥 Оперативні оновлення, гарячі події та корисна інфа 🇺🇦\n🚀 Приєднуйся зараз 👉 https://t.me/+qnWxnEQXppIwYTRi\n💥 З нами ти завжди на хвилі!",
    "📰 **Україна Онлайн ⚡** — твоє джерело новин! \n🌟 Дізнайся першим, що відбувається в Україні та світі! 🌍\n📲 Швидко, правдиво, актуально ✅\n🔗 Вступай: https://t.me/+qnWxnEQXppIwYTRi",
    "🔥 **Україна Онлайн ⚡** — всі новини в одному місці! \n🇺🇦 Гарячі події, важливі оновлення та корисні поради!\n💬 Будь з нами, будь в темі! 👉 https://t.me/+qnWxnEQXppIwYTRi",
    # Комбінована реклама обох каналів
    "🌟 **Два крутих місця для українців!** 🇺🇦\n🛒 **Продаж/покупка?** Приєднуйся до https://t.me/vsi_ogoloshenya_ua — усе від авто до житла! 🚗🏠\n📰 **Хочеш новин?** Лови гарячі оновлення в https://t.me/+qnWxnEQXppIwYTRi ⚡\n💥 Вступай в обидва, щоб бути в темі та в грі!"
]

# 🚀 Функція для отримання списку всіх груп, у яких є бот
async def get_groups():
    dialogs = await client.get_dialogs()
    groups = [dialog.entity for dialog in dialogs if dialog.is_group]
    return groups

# 🚀 Функція для відправки повідомлень у групи
async def send_messages():
    groups = await get_groups()
    print(f'\n🌟 Знайдено {len(groups)} груп для розсилки! Починаємо...\n')
    random.shuffle(groups)
    for group in groups:
        try:
            message = random.choice(messages)
            await client.send_message(group.id, message)
            print(f'✅ Повідомлення надіслано в {group.title} ({group.id})')
        except errors.ChatWriteForbiddenError:
            print(f'🚫 Не можу писати в групу {group.title} ({group.id}) - заборонено')
        except errors.ChatAdminRequiredError:
            print(f'⛔ Бот не має прав писати в {group.title} ({group.id})')
        except errors.UserBannedInChannelError:
            print(f'❌ Бот забанений в {group.title} ({group.id})')
        except Exception as e:
            print(f'⚠️ Інша помилка в {group.title} ({group.id}): {e}')
        await asyncio.sleep(random.randint(10, 30))  # Затримка між повідомленнями

# 🔄 Головна функція
async def main():
    await client.start(PHONE_NUMBER)
    print("\n🚀 Бот підключений! Починаємо розсилку...\n")
    while True:
        await send_messages()
        print('\n⏳ Чекаємо 15 хвилин перед наступним циклом...\n')
        await asyncio.sleep(900)  # Повтор через 15 хвилин

# 🔥 Запуск
with client:
    client.loop.run_until_complete(main())