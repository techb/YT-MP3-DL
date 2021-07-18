# YouTube to MP3 GUI Tool
GUI tool to download a single or list of YouTube videos as MP3s. Simply copy and paste your desired YouTube videos url, separated by a new line. Select the destination folder and click convert. If there is an issue, usually cause by videos becoming unavailable in your country or the video being removed by the author, you will be givin a list of failed urls.

![App Screenshot](img/screenshot.png)

## Install and Run
- `$ git clone git@github.com:techb/YT-MP3-DL.git`
- `$ pipenv shell`
- `$ pipenv install`
- `$ python yt-to-mp3.py`

## Requires
- PySimpleGUI
- youtube_dl

## Download from bookmark folder
- Right click the desired folder containing youtube urls
- Paste into URL list
- Remove non youtube url label


![Copy Bookmark Folder](img/copy-bookmark.png)
![Remove Header Label in List](img/copy-bookmark2.png)
![Correct list](img/copy-bookmark3.png)