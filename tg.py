import telebot
import time
import pyowm

from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = pyowm.OWM('0b605ac7a5dc7be79004ee52491dff4e', config_dict)
mgr = owm.weather_manager()

TOKEN = '5577678555:AAEr-4zy1hetoQJ8pz-TmvqkxWQQwKN5Ztw'

def listener(messages):
	"""
	When new messages arrive TeleBot will call this function.
	"""
	for m in messages:
		chatid = m.chat.id
		if m.content_type == 'text':
			text = m.text
			observation = mgr.weather_at_place(text)
			w = observation.weather
			temp = w.temperature('celsius')["temp"]
			answer = "В городе " + text + " сейчас " + w.detailed_status + ". Воздух: " + str(round(temp, 1)) + "\n"
			tb.send_message(chatid, answer)


tb = telebot.TeleBot(TOKEN)
tb.set_update_listener(listener) #register listener
tb.polling()
#Use none_stop flag let polling will not stop when get new message occur error.
tb.polling(none_stop=True)
# Interval setup. Sleep 3 secs between request new message.
tb.polling(interval=3)

while True: # Don't let the main Thread end.
    pass