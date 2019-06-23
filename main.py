from telethon import TelegramClient, sync
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
import time
from config import *
from utils import *

client = TelegramClient('Volk', api_id, api_hash)
client.start()

prev_time = ''

while True:
    time.sleep(5)
    if time_has_changed(prev_time):
        prev_time = convert_time_to_string(datetime.now())
        client(DeletePhotosRequest(client.get_profile_photos('me')))
        file = client.upload_file('time_images/{}.jpeg'.format(prev_time))
        client(UploadProfilePhotoRequest(file))
