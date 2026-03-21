import requests
class Form:
    def __init__(self, login, password, email=None, url=None):
        self.login = login
        self.password = password
        self.email = email
        self.url = url

    def set_web_url(self, url):
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                self.url = url
                return True
            return False
        except requests.exceptions.RequestException:
            return False