#! /usr/bin/env python3

import threading
import os
from YTLogger import YTLogger
from Utils import *
import youtube_dl
import PySimpleGUI as sg


# Function to do the actual youtube to mp3 work
def download_mp3(opts, urls):
    err = [] # urls that had errors, usually unavailable in our country
    for url in urls:
        try:
            with youtube_dl.YoutubeDL(opts) as ydl:
                ydl.download([url])
        except:
            err.append(url)

    # Show user errors we got
    if len(err) > 0:
        padd()
        print_error('Videos not converted. Please check the urls and try again.', err)

    padd()
    window['Convert'].update(disabled=False)
    print_title('All Done =)')


# Width of urls input and debug output text boxes
INPUT_X_SIZE = 50
INPUT_Y_SIZE = 15

# Define the gui layout
# https://pypi.org/project/PySimpleGUI/
cwd = os.getcwd()
layout = [
    [
        sg.Text("List of YouTube Urls"), sg.Text('Output', pad=(255, 0))
    ],
    [
        sg.Multiline(size=(INPUT_X_SIZE, INPUT_Y_SIZE), key='-INPUT-', autoscroll=True),
        sg.Output(size=(INPUT_X_SIZE, INPUT_Y_SIZE))
    ],
    [
        sg.FolderBrowse(key='-FOLDER-',  pad=((5, 0),(21, 21))),
        sg.Text(cwd , key='-SEL_FOLDER-', size=(INPUT_X_SIZE, 1), pad=((5, 0),(21, 21)))
    ],
    [
        sg.Button('Convert'),
        sg.Button('Quit')
    ],
]


# Init window and bring into focus
sg.theme('DarkBlue3')
window = sg.Window('YouTube to MP3', layout, icon='img/favicon.ico')
window.Finalize()
window.BringToFront()


# Main Loop
if __name__ == "__main__":
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break

        # Convert button clicked
        if event == 'Convert':
            window['Convert'].update(disabled=True)
            urls = []
            for line in values['-INPUT-'].split('\n'):
                if line != '':
                    line = line.rstrip() # remove white space
                    line = line.replace(',', '') # If CSV, remove commas
                    # remove any url params like playlists and time stamps
                    line = line.split('&')[0]
                    urls.append(line)

            # Config for youtube_dl
            ydl_opts = {
                'format': 'bestaudio/best',
                # set output to selected dir
                'outtmpl': values['-FOLDER-']+'/%(title)s.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'logger': YTLogger(),
                'progress_hooks': [status_hook],
            }

            # Start new thread to download everything
            print_title('Starting Downloads')
            threading.Thread(target=download_mp3, args=(ydl_opts, urls), daemon=True).start()


    # Kill everything and exit
    window.close()