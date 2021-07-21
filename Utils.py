# new lines to make output box prettier
def padd(n=0):
    print('\n'*n)


# wraps error messages in !
# if passed a list <l> will wrap the list in !
def print_error(s, l=None, hz=42):
    print(f'!'*42)
    print(s)
    if l:
        for e in l:
            print(e)
        print('!'*hz)
    else:
        print('!'*hz)
        print(s)
        print('!'*hz)


# prints a title border to output
def print_title(s):
    print(f'------------ {s} ------------')


# Hook to say when youtube_dl is done dowloading from url
# Then webm is converted to MP3 and move on to the next url in its list
def status_hook(d):
    if d['status'] == 'finished':
        padd()
        print_title('Converting to MP3')