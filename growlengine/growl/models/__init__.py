from basemodel import BaseModel
from developer import Developer
from game import Game
from player import Player

def model_encode(obj):
    enc = None
    try:
        enc = obj.__json__()
    except:
        enc = None

    if enc:
        return enc

    raise TypeError(repr(obj) + " is not JSON serializable")

def model_encode_verbose(obj):
    enc = None
    try:
        enc = obj.__json_verbose__()
    except Exception, e:
        logging.error(e)
        enc = None

    if enc:
        return enc

    raise TypeError(repr(obj) + " is not JSON serializable")
