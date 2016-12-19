from apiclient import auth
from multiprocessing import Pool


class Client:

    def __init__(self):
        self.auth = auth.Authentication()

    def multi(self):
        p = Pool(5)
        p.map(self.getProperty())

    def getProperty(self):
        return self.auth.request('/properties/70')
        # self.auth.log(result)

    def createMessage(self):
        body = {
            "userTo": 581,
            "title": "Message TEST title",
            "body": "Guests are COMING!",
            "isImportant": True
        }
        return self.auth.request('/messages', body, 'POST')
