from __future__ import unicode_literals
import youtube_dl

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        print("[!] %s" % msg)

    def error(self, msg):
        print("[!] %s" % msg)

def my_hook(d):
    if d['status'] == 'finished':
        print('[+] Done downloading, now converting...')

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

urls = [line.rstrip() for line in open("urls.txt")]
print(urls)
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(urls)

print("[+] Total MP3's: %d" % len(urls))
print("[+] All Done =) \007")