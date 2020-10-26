from telethon import TelegramClient, events, sync
import os
import random
import shutil

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = XXXXXXX
api_hash = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

path = os.getcwd() + "/images/"
path_uploaded = os.getcwd() + "/uploaded/"
categories = os.listdir(path)

while True:
    folder = random.choice(categories)
    folder_content = os.listdir(path + folder)
    if not folder_content:
        continue
    else:
        remaining = len(folder_content) -1
        remaining_desc = "There's still " + str(remaining) + " images remaining in " + folder"
        imagename = random.choice(folder_content)
        break

path_img = path + folder + '/' + imagename

client = TelegramClient('session_name', api_id, api_hash)
client.start()
client.get_dialogs()

# replace chat_id with the id of the chat you want to upload the image to. To get that id check the readme and run the commented command below
# client.get_entity('telegram.me/joinchat/xxxxxxxxxxxxxxxxxxxxx')
client.send_file(chat_id, path_img, caption=remaining_desc)

move_img = shutil.move(path_img, path_uploaded + imagename)
