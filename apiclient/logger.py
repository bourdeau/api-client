
"""
Logger
"""


class Logger:

    def log(self, data):
        with open("logs/prod.log", "a") as myfile:
            myfile.write(str(data) + '\n')
