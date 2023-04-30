import os, random

memes = []

directory = 'static/memes'

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        memes.append("memes" + "/" + filename)

def pickMeme():
    return random.choice(memes)
