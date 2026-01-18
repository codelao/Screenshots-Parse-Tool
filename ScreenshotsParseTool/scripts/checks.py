import requests, json
from ScreenshotsParseTool import __version__


def check_internet_connection():
    try:
        requests.get('https://google.com', timeout=1)
        return True
    except:
        return False
        
def check_latest_release():
    headers = {'Accept': 'application/vnd.github+json'}
    check_latest_release = requests.get('https://api.github.com/repos/codelao/Screenshots-Parse-Tool/releases/latest', headers=headers)
    if check_latest_release.status_code == 200:
        latest_release = json.loads(check_latest_release.text)
        if not latest_release['tag_name'] == 'v'+__version__:
            return latest_release['tag_name']
