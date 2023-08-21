import urllib.request


def check_internet_connection():
        try:
            urllib.request.urlopen('https://google.com', timeout=1)
            return True
        except:
            return False
