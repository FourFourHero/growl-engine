from basemodel import BaseModel
from attribute import Attribute
from developer import Developer
from game import Game
from player import Player
from playerattribute import PlayerAttribute
from playerresource import PlayerResource
from playerskill import PlayerSkill
from playertrait import PlayerTrait
from resource import Resource
from skill import Skill
from skillgroup import SkillGroup
from trait import Trait

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
