# Logger class for youtube_dl
class YTLogger(object):
    def debug(self, msg):
        print(msg)


    def warning(self, msg):
        self.print_wrap("[!] %s" % msg)


    def error(self, msg):
        self.print_wrap("[!!!] %s" % msg)


    # wraps print in border so it's easier to read in the output
    def print_wrap(s):
        print('-'*40)
        print(s)
        print('-'*40)