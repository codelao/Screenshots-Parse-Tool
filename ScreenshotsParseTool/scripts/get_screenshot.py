import os
import random
import string
import datetime
import requests
from lxml import etree
from fake_useragent import UserAgent


def path_generator():
    random_path = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    if not random_path[0] == '0':
        return random_path
    else:
        random_path = random_path.replace('0', '1', 1)
        return random_path

def parser(path):
    headers = {'User-Agent':str(UserAgent().random)}
    link = 'https://prnt.sc/' + path
    get_link = requests.get(link, headers=headers).text
    parser = etree.HTMLParser()
    read = etree.fromstring(get_link, parser)
    find_screenshot_link = read.find('.//img[@id="screenshot-image"]')
    return find_screenshot_link.get('src')

def downloader():
    path = path_generator()
    screenshot_link = parser(path)
    if not screenshot_link[0] == '/':
        headers = {'User-Agent':str(UserAgent().random)}
        get_screenshot_link = requests.get(screenshot_link, headers=headers)
        if not get_screenshot_link.status_code == 404:
            desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
            today = datetime.datetime.today()
            date = today.strftime("%m_%d_%Y")
            filename = path + '.png'
            if os.path.isdir(desktop_path + '/ParsedScreens') == True:
                if os.path.isdir(desktop_path + '/ParsedScreens/' + date) == True:
                    with open(desktop_path + '/ParsedScreens/' + date + '/' + filename, 'wb') as f:
                        f.write(get_screenshot_link.content)
                        f.close()
                else:
                    os.mkdir(desktop_path + '/ParsedScreens/' + date)
                    with open(desktop_path + '/ParsedScreens/' + date + '/' + filename, 'wb') as f:
                        f.write(get_screenshot_link.content)
                        f.close()
            else:
                os.mkdir(desktop_path + '/ParsedScreens')
                os.mkdir(desktop_path + '/ParsedScreens/' + date)
                with open(desktop_path + '/ParsedScreens/' + date + '/' + filename, 'wb') as f:
                    f.write(get_screenshot_link.content)
                    f.close()
        else:
            downloader()
    else:
        downloader()
