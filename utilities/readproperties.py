import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations/config.ini")
class Readconfig:
    @staticmethod
    def getApplicationURL():
       url= config.get('common info','baseurl')

    @staticmethod
    def getUserEmail():
        Email= config.get('common info', 'username')

    @staticmethod
    def getPassword():
        Password = config.get('common info', 'password')
