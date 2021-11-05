from fastapi import FastAPI
from instalooter.looters import ProfileLooter

app = FastAPI()


@app.get("/{username}")
async def root(username):
    looter = ProfileLooter(str(username))
    directory = str('pic_'+username)
    looter.download_pictures(directory, media_count=50)
    return 'Download Successful'