import logging
from datetime import datetime

def sendError(errText):
   logging.basicConfig(format='%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                       datefmt='%Y-%m-%d:%H:%M:%S',level=logging.DEBUG, filename='{:%Y-%m-%d}.log'.format(datetime.now()))
   logging.debug(errText)
