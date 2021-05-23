import time
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from pyrogram import Client

select = " "

docs = """\n𓆩 SOURCE ICSS - STRING SESSION 𓆪"""

tutor = """
~ When you finish steps  
~ You will find it in your Telegram save msg
~ Dev - @rruuurr
~ For Sources Icss - Userbot
"""

template = """
𓆩 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 -  𝑺𝑻𝑹𝑰𝑵𝑮 𝑺𝑬𝑺𝑺𝑰𝑶𝑵 𓆪
𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻 
<code>{}</code>
𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻
⌔∮ كود التيرمكس الخاص بك.
⌔∮ المطور - @rruuurr"""

print(docs)

while select != ("kimo"):
    select = input("\n~ Enter kimo - ").lower()
    if select == "kimo":
        print("""\n~ Telethon selected\n~ Running script...""")
        time.sleep(1)
        print(tutor)
        API_KEY = int(input("⌔∮ Enter API_KEY - "))
        API_HASH = input("⌔∮ Enter API_HASH - ")

        with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
            session_string = client.session.save()
            saved_messages_template = template.format(session_string)
            print("\nGenerating String Session...\n")
            client.send_message("me", saved_messages_template, parse_mode="html")
        break
    
    else:
        print("\n~ please Type kimo - To get String Session: \n")
        time.sleep(1.5)
