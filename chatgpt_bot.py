import openai
import telebot

openai.api_key = "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"
bot_token = '6263313761:AAGn5TF27u0JdioU0OReKMSXWTEmh25rB0o'

# Создаем экземпляр бота
bot = telebot.TeleBot(bot_token)

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m):
    user_first_name = str(m.from_user.first_name)
    bot.reply_to(m, f"Здравствуй, {user_first_name}! Высший интелект на связи.")

# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    user_first_name = str(message.chat.first_name)
    message_split = message.text
    chat_id = message.chat.id

    completion = openai.Completion.create(engine="text-davinci-003",
                                          prompt=message_split,
                                          max_tokens=100,
                                          temperature=0.5,
                                          stop=". "
                                          )
    try:
        response_text = completion.choices[0].text.strip()
        bot.reply_to(message, response_text)
    except:
        bot.reply_to(message, "Сервер GPT перегружен")

# Запускаем бота
bot.polling(none_stop=True, interval=0)