from apiclient import apiclient
from multiprocessing import Pool


class ApiRoute:

    def __init__(self):
        self.client = apiclient.ApiClient()

    def multi(self):
        p = Pool(5)
        p.map(self.getProperty())

    def getProperty(self):
        url = 'http://api2.squarebreak.local/properties/70'
        result = self.client.request(url)
        # self.client.log(result)

    def createMessage(self):
        body = {
            "userTo": 581,
            "title": "Message TEST title",
            "body": "Guests are COMING!",
            "isImportant": True
        }
        url = 'http://api2.squarebreak.local/messages'
        result = self.client.request(url, body, 'POST')
        self.client.log(result)
