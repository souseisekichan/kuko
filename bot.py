from telepot import *
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.namedtuple import InlineQueryResultArticle, InputTextMessageContent


#bot = telebot.TeleBot("316846706:AAF3ipEWyE5l0ASJ5MN-7X6zEchuhhP2uYg")

#----------------------------// TOKEN //-------------------------------
bot = Bot('316846706:AAF3ipEWyE5l0ASJ5MN-7X6zEchuhhP2uYg')
db_api = 'LDX1tde9wZSyJfsh4m80tciZ4gegCoc12EtC5oS7Ibo'
#-----------------------------------------------------------




def command_handle(s):
    d = {}
    with open("dict.json") as f:
        for line in f:
            (key, val) = line.split()
            d[key] = val
        ans = d.get(s)
        if ans == None:
            ans = 'Try again!'
    return ans

def on_message(msg): #answering message! 
    content_type, chat_type, chat_id = glance(msg)
    if msg['text'].lower().find('куко') != -1 or msg['text'].lower().find('кууко') != -1:
        s_str = msg['text'].split()
        ans = command_handle(s_str[2].lower())
        bot.sendMessage(chat_id, ans)



# Keep the program running.
#answerer = telepot.helper.Answerer(bot)
bot.message_loop({'chat': on_message,
                  #'callback_query': on_callback_query,
                  #'inline_query': on_inline_query,
                  #'chosen_inline_result': on_chosen_inline_result
                  },
                 run_forever='Listening ...')

