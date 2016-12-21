from urllib.request import Request, urlopen
from urllib.parse import urlencode
from pathlib import Path
from shutil import copyfile
import json
import yaml


class Authentication:

    def __init__(self):
        self.url = ''
        self.token = ''
        self.body = {}

    def getConfig(self):
        parameters_file = Path("apiclient/parameters.yml")
        if parameters_file.is_file() is False:
            copyfile('apiclient/parameters.yml.dist', 'apiclient/parameters.yml')

        stream = open("apiclient/parameters.yml", "r")
        config = yaml.load_all(stream)
        for parameters in config:
            for key, value in parameters.items():
                if key == 'url':
                    self.url = value
                else:
                    self.body[key] = value
        self.body['grant_type'] = 'password'

    '''
    Authentication
    '''
    def auth(self):
        self.getConfig()
        authUrl = self.url + '/oauth/v2/token'
        request = Request(authUrl, urlencode(self.body).encode())
        response = urlopen(request)
        code = response.getcode()
        body = response.read().decode()
        data = {'code': code, 'body': json.loads(body)}

        self.token = data['body']['access_token']

    '''
    Make a request
    '''
    def request(self, url, body=None, method='GET'):
        self.auth()
        url = self.url+url
        header = {
            'Authorization': 'Bearer '+self.token,
            'Content-Type': 'application/json',
            'Accept-Language': 'fr_FR'
        }
        if method == 'GET':
            request = Request(url, None, header, method)
        elif method == 'POST':
            content = json.dumps(body).encode('utf8')
            request = Request(url, content, header, 'POST')

        response = urlopen(request, timeout=30)
        body = response.read().decode()

        return json.loads(body)
