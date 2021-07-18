from __future__ import unicode_literals
import youtube_dl
from youtube_dl.utils import GeoRestrictedError
import PySimpleGUI as sg
import threading


# new lines to make output box prettier
def padd():
    print('\n\n')


# Logger class for youtube_dl
class MyLogger(object):
    def debug(self, msg):
        print(msg)

    def warning(self, msg):
        print('-'*40)
        print("[!] %s" % msg)
        print('-'*40)

    def error(self, msg):
        print('-'*40)
        print("[!!!] %s" % msg)
        print('-'*40)


# Hook to say when youtube_dl is done
def my_hook(d):
    if d['status'] == 'finished':
        padd()
        print('------------ Converting to MP3 ------------')


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
        print('!'*40)
        print('Videos not converted. Please check the urls and try again.')
        for e in err:
            print(e)
        print('!'*40)

    padd()
    print("------------ All Done =) ------------")


# Width of urls input and debug output text boxes
INPUT_X_SIZE = 50
INPUT_Y_SIZE = 10

# Define the gui layout
layout = [
    [sg.Text("List of YouTube Urls"), sg.Text('Output', pad=(260, 0))],
    [sg.Multiline(size=(INPUT_X_SIZE, INPUT_Y_SIZE), key='-INPUT-', autoscroll=True), sg.Output(size=(INPUT_X_SIZE, INPUT_Y_SIZE))],
    [sg.FolderBrowse(key='-FOLDER-'), sg.Text('Selected Folder: ', key='-SEL_FOLDER-', size=(INPUT_X_SIZE, 1))],
    [sg.Button('Convert'), sg.Button('Quit')],
]


# Init window and bring into focus
window = sg.Window('YouTube to MP3', layout, icon='img/favicon.ico')
window.Finalize()
window.BringToFront()

# Main Loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

    # Convert button clicked
    if event == 'Convert':
        urls = []
        for line in  values['-INPUT-'].split('\n'):
            if line != '':
                urls.append(line.rstrip().replace(',', '')) # If CSV, remove commas

        # Config for youtube_dl, set output to user selected folders
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': values['-FOLDER-']+'/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'logger': MyLogger(),
            'progress_hooks': [my_hook],
        }
        # Start new thread to download everything
        print('------------ Starting Downloads ------------')
        threading.Thread(target=download_mp3, args=(ydl_opts, urls), daemon=True).start()


# Kill everything and exit
window.close()