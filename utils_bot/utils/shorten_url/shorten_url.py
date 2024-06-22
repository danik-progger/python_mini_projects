import pyshorteners

def shorten_url(long_url):
    type_tiny = pyshorteners.Shortener()
    short_url = type_tiny.tinyurl.short(long_url)
    return short_url

if __name__ == "__main__":
    link = input()
    print(shorten_url(link))