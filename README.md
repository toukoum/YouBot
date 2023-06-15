**This bot work perfectly but some update come in a short time**   
**You may check these out in the meanwhile**:

![alt text](https://github.com/[toukoum]/[YouBot]/blob/[master]/banner.png?raw=true)

# Youtube-Shorts-Bot
 This Python Bot Scrape Videos from Pexels, & Add a Random Song from Songs Folder, Then You Can Auto Upload The Videos To Your Youtube Channel

 Watch How I create this Bot:  <a href="https://www.youtube.com/watch?v=vp1v5mBG7rA&ab_channel=Toukoum">click here<a> [youtube video]

---

- [Youtube-Shorts-Bot](#youtube-shorts-bot)
- [1. Set up the Bot](#1-set-up-the-bot)
  - [Install](#install)
  - [Youtube Studio Account](#youtube-studio-account)
  - [Change music for your shorts](#change-music-for-your-shorts)
  - [Change the content of Short created](#change-the-content-of-short-created)
- [2. Run the Bot](#2-run-the-bot)


-------------

# 1. Set up the Bot

## Install

Download or clone this GitHub repository
Install requirements with:

```sh
python3 -m venv venv
. venv/bin/activate
pip3 install -r requirements.txt
```
## Youtube Studio Account

Go to `YouBot/youtubeShortsBot/upload.py`

and set  Your youtube Studio account Url at this line:

    49  driver.get('[your_url]')


## Change music for your shorts


Change or modify the song inside the `songs/` folder <br>


## Change the content of Short created

Go to `youtubeShortsBot/make_video.py`

and you can modify these two lines:

    38   Liste_phrases = ["[Title]: [Content]", ...]

and:

    101 url = "[url of pexel video in 9:16 ratio]"
i.e: 

https://www.pexels.com/search/videos/historycal/?orientation=portrait


# 2. Run the Bot

Go to `YouBot` folder and run:

    python3 scrape.py

this will create as many vids in the `videos/` folder as different content you set

and finally, run:

    python3 upload.py

this will upload all video one by one, so it may take a while.


 


