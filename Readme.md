# TikTok Video Converter

A small utility to speed-up my meme generation pipeline. 

It can convert videos with **squared** proportion (*classic instagram post*) to a **vertical** video (*TikTok, Instagram stories, Instagram Reels*).

## How does it work

The script takes a folder as input and convert all the file with the extension *.mp4 into a vertical format.

It simply add padding upside and downside.

The image below gives a roughly idea of how the script works:

![VideoConverter](/mnt/F8AEE8A5AEE85D9E/Users/Fitec/Documents/Progetti/VerticalVideoConverter/images/VideoConverter.png)

## How to use it

### Dependencies

To install all the requirements just type:

```bash
pip install -r requirements.txt
```

### Usage

To run the script simply put in the root directory all the folder containing the files that you need to convert and then type:

```
python convertTikTok.py
```

You will find all the vertical files inside the folder named **Tiktok**

