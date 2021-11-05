import os

from fastapi import FastAPI
from instalooter.looters import ProfileLooter

app = FastAPI()


@app.get("/{username}")
async def root(username):
    looter = ProfileLooter(str(username))

    directory = str('pic_'+username)
    parent_dir = "home/User/Downloads"
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
    
    looter.download_pictures(directory, media_count=50)