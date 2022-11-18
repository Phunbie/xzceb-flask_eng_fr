
#import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv


load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)

discovery = LanguageTranslatorV3(version = '2018-05-01',
                                authenticator = authenticator)

discovery.set_service_url(url)
discovery.set_disable_ssl_verification(True)

def englishToFrench(english_text):
    """write the code here"""
    if english_text == "":
        french_text = ""
    else:    
        translate =  discovery.translate(
        text = english_text,
        model_id='en-fr').get_result()
        french_text = translate["translations"][0]["translation"]

    return french_text

def frenchToEnglish(french_text):
    """write the code here"""
    if french_text == "":
        english_text = ""
    else:
        translate =  discovery.translate(
        text = french_text,
        model_id='fr-en').get_result()
        english_text = translate["translations"][0]["translation"]

    return english_text
