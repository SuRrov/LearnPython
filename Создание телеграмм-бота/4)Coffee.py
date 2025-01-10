#Импорт библиотек и иниализация Телеграмм Бота 
import requests
import telebot  
TOKEN = "7133728602:AAE8EZ0pRsI2Wd54-I8iXl9M-89V6nsY-ao"
bot = telebot.TeleBot(TOKEN)

#Хендлер 
@bot.message_handler(content_types=["text"])
def get_message (messages):
    r = requests.get('https://coffee.alexflipnote.dev/random', headers={'Content-Type': 'image/jpeg'})       
    bot.send_photo(messages.from_user.id, r.content)   
    

#Постоянное обновление бота в поисках входящих сообщений
bot.polling(non_stop=True, interval=0)

