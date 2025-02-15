import os
import requests
import telebot
from telebot import types
import datetime
from user_agent import generate_user_agent

user_agent = generate_user_agent()[0]
id = '7160526874'  # Replace This
tok = '7746020300:AAEV8j_mtUDcp6u7Gp4iS4hY5RCBWAHfZ1w'  # Replace This
zzk = 0
bot = telebot.TeleBot(tok)

@bot.message_handler(commands=['start'])
def start(message):
    global zzk
    zzk += 1
    nm = message.from_user.first_name
    id2 = message.from_user.id
    userk = message.from_user.username
    zxu = datetime.datetime.now()
    tt = f'''
A user is using the bot…
—————————————————
User Name: {nm}
Username: @{userk}
User ID: {id2}
User Number: {zzk}
Time: {zxu}
~ @faheem_Ironside'''

    key = types.InlineKeyboardMarkup()
    bot.send_message(id, f"<strong>{tt}</strong>", parse_mode="html", reply_markup=key)
    but1 = types.InlineKeyboardButton(text='- 🔰𝗗𝗘𝗩-FAHEEM', url='https://t.me/faheem_Ironside')
    but2 = types.InlineKeyboardButton(text='- ⚜️ 𝗗𝗘𝗩-ENTITY', url='https://t.me/ientity303')
    add = types.InlineKeyboardButton(text="💌 Create New Email", callback_data='ansh')
    A = types.InlineKeyboardButton(text="💬 Inbox", callback_data='A')
    K = types.InlineKeyboardButton(text="💣 Delete My Account", callback_data='AK')
    
    maac = types.InlineKeyboardMarkup()
    maac.row_width = 2
    maac.add(but1, but2, A, K, add)
    bot.send_message(message.chat.id, f"<strong>Welcome, | {nm} | to the temporary email creation bot for receiving codes and messages. To get your info, use [ /info ]</strong>", parse_mode="html", reply_markup=maac)

@bot.callback_query_handler(func=lambda call: True)
def st(call):
    if call.data == 'ansh':
        nc1 = types.InlineKeyboardMarkup(row_width=2)
        Az = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Click the word [ /gen ]', reply_markup=nc1)
        bot.register_next_step_handler(Az, zd2)
    elif call.data == "A":
        nc1 = types.InlineKeyboardMarkup()
        zd1 = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Click the word [ /get ]', reply_markup=nc1)
        bot.register_next_step_handler(zd1, OZ)
    elif call.data == "AK":
        nc1 = types.InlineKeyboardMarkup(row_width=2)
        MC = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Do you want to delete your account? [ /yes ]', reply_markup=nc1)
        bot.register_next_step_handler(MC, k3)

def zd2(message):
    id2 = str(message.from_user.id)
    ms = message.text
    if '/gen' in ms:
        try:
            os.system(f'rm -rf token{id2}.txt')
            bot.send_message(message.chat.id, f"<strong>Creating email...</strong>", parse_mode="html", reply_markup=types.InlineKeyboardMarkup())
            url = 'https://api.internal.temp-mail.io/api/v3/email/new'
            data = {'name': 'ahmed', 'domain': 'greencafe24.com'}
            headers = {'User-Agent': user_agent}
            response = requests.post(url, data=data, headers=headers)
            result = response.json()
            email = result['email']
            with open(f'token{id2}.txt', 'a') as zaidno:
                zaidno.write(f'{email}')
            z = f"""
Email created successfully:
—————————————————
Email: {email}
—————————————————
You can now send codes to the email and receive them in the inbox section.
To return, press
/start"""
            bot.send_message(message.chat.id, f"<strong>{z}</strong>", parse_mode="html", reply_markup=types.InlineKeyboardMarkup())
        except Exception as e:
            bot.send_message(message.chat.id, f"<strong> ❗ An error occurred</strong>", parse_mode="html", reply_markup=types.InlineKeyboardMarkup())
    else:
        bot.send_message(message.chat.id, f"<strong> ❗ You entered the word incorrectly</strong>", parse_mode="html", reply_markup=types.InlineKeyboardMarkup())

def OZ(message):
    try:
        id2 = message.chat.id
        tx = message.text
        if '/get' in tx:
            token = open(f"token{id2}.txt", "r").read()  
            url = f'https://api.internal.temp-mail.io/api/v3/email/{token}/messages'
            messages = requests.get(url).json()
            if messages:
                for msg in messages:
                    bot.send_message(message.chat.id, f"•<strong>Message: {msg['body_text']}\nSubject: {msg['subject']}</strong>", parse_mode="html", reply_markup=types.InlineKeyboardMarkup())
            else:
                bot.send_message(message.chat.id, "No messages currently.")
        else:
            bot.send_message(message.chat.id, f"<strong>You entered the word incorrectly</strong>", parse_mode="html", reply_markup=types.InlineKeyboardMarkup())
    except Exception as e:
        bot.send_message(message.chat.id, f"<strong>❗ You don’t have an account in the bot</strong>", parse_mode="html", reply_markup=types.InlineKeyboardMarkup())
        print(e)

def k3(message):
    mg = message.chat.id
    try:
        os.system(f'rm -rf token{mg}.txt')
        key = types.InlineKeyboardMarkup()
        bot.send_message(message.chat.id, f"<strong>Your old account has been deleted</strong>", parse_mode="html", reply_markup=key)
    except:
        key = types.InlineKeyboardMarkup()
        bot.send_message(message.chat.id, f"<strong>You don’t have an account in the first place</strong>", parse_mode="html", reply_markup=key)

@bot.message_handler(commands=["info"])
def inf(message):
    global zzk
    zzk += 1
    zxu = datetime.datetime.now()
    nm = message.from_user.first_name
    id2 = message.from_user.id
    userk = message.from_user.username
    bio = bot.get_chat(message.from_user.id).bio
    
    ttg = f'''
—————————————————
User Name: {nm}
Username: @{userk}
User ID: {id2}
User Number: {zzk}
Time: {zxu}
User Bio: {bio}
~ @faheem_Ironside'''
    
    key = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, f"<strong>{ttg}</strong>", parse_mode="html", reply_markup=key) 

while True:
    try:
        bot.infinity_polling()
    except:
        pass