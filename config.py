import os.path

class Config:
    LANGUAGES = {'en': 'English', 'fr': 'French'}
    DEFAULT_LANGUAGE = 'en'
    APP_PREFIX = '/app/alouette/'
    DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + r'/../../data'
    EN_LINK = '/app/alouette' #url for the english version
    FR_LINK = '/app/alouette-fr' #url for the french version
