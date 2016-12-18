from apiclient import apiclient
from multiprocessing import Pool


class ApiRoute:

    def __init__(self):
        self.client = apiclient.ApiClient()

    def getProperty(self):
        url = 'http://api2.squarebreak.local/properties/70'

        while True:
            result = self.client.request(url)
            self.client.log(result)

    def multi(self):
        p = Pool(5)
        p.map(self.getProperty())
