import logging

def sendError():
   logging.basicConfig(filename='errorTemp.log')
   logging.warning('Reading Weather API Failed after 6 attempts')
