from RedDownloader import RedDownloader
from instagrapi import Client

import time
import os
import random

#download post from reddit
def Getredditpost():
    post = RedDownloader.DownloadBySubreddit("pics", 1, SortBy="new")
    author = post.GetPostAuthors()[0]
    print(f"\nSubreddit: pics")
    print(f"Author: {author}\n")
    return author

#Login to insta
client = Client()
client.login("Username", "Password")

#captons
def CreateCaptions():
    caption = ["Yusuf's first bot post :)", "First bot from Yusuf :)"]

    return random.choice(caption)

#clearing previously downloaded pic from local drive
def ClearFromDrive():
    try:
        os.remove("downloaded/downloaded1.jpeg")
    except:
        pass

while True:
    author = Getredditpost()
    captionA = CreateCaptions()
    caption = f"Reddit User: {author} \n\n{hashtags}"
    try:
        client.photo_upload("downloaded/downloaded1.jpeg", caption)
    except Exception as e:
        print(e)
    finally:
        print(f"\nPosted")
        print(f'Sleeping...')

        ClearFromDrive()
        time.sleep(1800)
