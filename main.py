

#Imports
from settings import api_id, api_hash, phone_id
import telethon.sync
from telethon.sync import TelegramClient
from telethon import functions, types, events, utils
from channels_ids import  channels_info2
from modules.image_process import img_txt
import os
import sys
import threading

import re


#prueba del clone




client = TelegramClient('tes', api_id, api_hash)

@client.on(events.NewMessage)
async def my_event_handler(event):
    chat = await event.get_chat()
    print("C/S signal", chat)
    #xxxxxxChat Chat(id=427723780, title='group_test', photo=ChatPhotoEmpty(), participants_count=2, date=datetime.datetime(2020, 11, 17, 0, 12, 6, tzinfo=datetime.timezone.utc), version=1, creator=True, kicked=False, left=False, deactivated=False, migrated_to=None, admin_rights=None, default_banned_rights=ChatBannedRights(until_date=datetime.datetime(2038, 1, 19, 3, 14, 7, tzinfo=datetime.timezone.utc), view_messages=False, send_messages=False, send_media=False, send_stickers=False, send_gifs=False, send_games=False, send_inline=False, embed_links=False, send_polls=False, change_info=False, invite_users=False, pin_messages=False))
    chat_id = event.chat_id

    chat_from = event.chat if event.chat else (await event.get_chat())

    chat_title = utils.get_display_name(chat_from)

    if chat_id in channels_info2.keys():
        #print("estoy en la lista")
        #await client.send_message(-1001265113337, 'este mensaje lo recibi del grupo XXX'+ event.raw_text)
        a = event.raw_text #.split()
        a = a.upper()
        a = re.sub('[!@#$]', ' ', a)



        if (re.findall("SELL|BUY", a) or event.photo) and (len(re.findall("TP", a)) > 0 or len(re.findall("TP", a)) >4) and re.findall("SL", a):

            #print("cumple con los datos basicos")
            #print(chat_title)
            #aca path para guardar imagenes
            if event.photo:
                par = await (client.download_media(event.photo, r"images", ))
                par = img_txt(par)
                print("con signal: ", chat_id)
                print(par)

                #print(a)

                await client.send_message(-1001265113337, chat_title + "\n" +par + "\n" + a)
            else:
                #print("No hay foto")
                #print(a)
                print("Con signal: ", chat_id)
                await client.send_message(-1001265113337,  a)

with client:
    client.run_until_disconnected()

'''

    #     print(a)
    #     if (len(a) == 12):
    #         par = a[0].replace("/", "")
    #         orden =  re.findall("Sell|stays", event.raw_text)
    #         be = a[2]
    #         sl = a[10]
    #         tp1 = a[4]
    #         tp2 = a[6]
    #         tp3 = a[8]
    #         await client.send_message(-1001265113337, par)
    #
    #
    #
    # else:
    #     print("entre en el else por que no estoy en la lista")
    #     print("estoy en la lista")
    #     print('chat id' ,chat_id)
    #     print(channels_info2)
'''

