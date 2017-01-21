from telepot import *
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.namedtuple import InlineQueryResultArticle, InputTextMessageContent
import random

#bot = telebot.TeleBot("316846706:AAF3ipEWyE5l0ASJ5MN-7X6zEchuhhP2uYg")

#----------------------------// TOKEN //-------------------------------
bot = Bot('316846706:AAF3ipEWyE5l0ASJ5MN-7X6zEchuhhP2uYg')
db_api = 'LDX1tde9wZSyJfsh4m80tciZ4gegCoc12EtC5oS7Ibo'
#-----------------------------------------------------------


def command_handle(s):
    d = {}
    with open('dict.json') as data_file:
    	d = json.load(data_file)
    	ans = d.get(s)
    if ans == None:
        pass
    return ans


def on_message(msg): #answering message! 
    content_type, chat_type, chat_id = glance(msg)

    '''bot.sendMessage('278278709', msg['from'])
                bot.sendMessage('278278709', msg['text'])'''
    #==============================================
    if msg['text'].lower().find('roll') != -1 :
    	try:
    		s = int(msg['text'].lower().split()[1])
    		bot.sendMessage(chat_id, random.randint(0, s))
    	except:
    		bot.sendMessage(chat_id, 'Сообщение должно содержать только roll и одну цифру, бвака!')
    #================================================
    
    elif command_handle(msg['text'].lower()) != None :
    	bot.sendMessage(chat_id, command_handle(msg['text'].lower()), parse_mode = 'Markdown', reply_to_message_id = msg)




# Keep the program running.
#answerer = telepot.helper.Answerer(bot)
bot.message_loop({'chat': on_message,
                  #'callback_query': on_callback_query,
                  #'inline_query': on_inline_query,
                  #'chosen_inline_result': on_chosen_inline_result
                  },
                 run_forever='Listening ...')


