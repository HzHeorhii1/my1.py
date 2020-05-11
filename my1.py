import pyowm
import telebot

owm = pyowm.OWM('Your API', language = "ru")
bot = telebot.TeleBot("Your API")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = owm.weather_at_place( message.text)
    w = observation.get_weather()
    temp = w.get_temperature('celsius')["temp"]

    answer = "В " + message.text + " сейчас " + w.get_detailed_status() +"\n"
    answer += "Температура сейчас: " + str(temp) + " градусов цельсия" +"\n\n"
    if temp < 0:
        answer+="За окном минус " + str(temp) +" Одевай пальто и перчатки, а то замерзнешь"
    elif 0 < temp < 10:
        answer +="Сейчас немножко холодно, одень пальто."
    elif 10 < temp < 20:
        answer +="Сейчас прохладно, одень тонкую куртку."
    elif 20 < temp < 25:
        answer +="Сейчас тепло, одень толстовку."
    elif  temp > 25:
        answer +="Сейчас жарко, футболк - идеальный вариант"
    else:
        answer +="Упсс... у нас сбой! Повторите еще раз))."
    bot.send_message(message.chat.id, answer)

bot.polling(none_stop = True)