from urllib.request import Request, urlopen
from urllib.parse import urlencode
from pathlib import Path
from shutil import copyfile
import json
import yaml


class ApiClient:

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
        self.body['grant_type'] = 'client_credentials'

    '''
    Authentication
    '''
    def auth(self):
        self.getConfig()
        authUrl = self.url + '/oauth/v2/token'
        data = self.post(authUrl, self.body)
        self.token = data['body']['access_token']
        self.log(data)

    '''
    Make a post request
    '''

    def post(self, url, body):
        request = Request(url, urlencode(body).encode())
        response = urlopen(request)

        code = response.getcode()
        body = response.read().decode()
        result = {'code': code, 'body': json.loads(body)}
        return result

    '''
    Log something
    '''

    def log(self, data):
        with open("logs/prod.log", "a") as myfile:
            myfile.write(str(data) + '\n')
