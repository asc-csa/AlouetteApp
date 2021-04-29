import os.path

class Config:
    LANGUAGES = {'en': 'English', 'fr': 'French'}
    DEFAULT_LANGUAGE = 'fr'
    APP_PREFIX = '/alouette/'
    DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + r'/../../data'
    EN_LINK = '/alouette' #url for the english version
    FR_LINK = '/alouette-fr' #url for the french version