import logging
from growl.models import Attribute
from growl.caches.attribute import get_attribute_from_cache
from growl.caches.attribute import store_attribute_in_cache

logger = logging.getLogger(__name__)

### Create attribute
def create_attribute(game, name, slug, description, value_min, value_max):
    attribute = Attribute()
    attribute.game = game
    attribute.name = name
    attribute.slug = slug
    attribute.description = description
    attribute.value_min = value_min
    attribute.value_max = value_max
    attribute.save() # post_save stores in cache
    return attribute

### Get attribute
def get_attribute(attribute_id):
    attribute = get_attribute_from_cache(attribute_id)
    if not attribute:
        attribute = Game.objects.get(pk=attribute_id)
        store_attribute_in_cache(attribute)
    return attribute

### Update attribute
def update_attribute(attribute):
    attribute.save() # post_save stores in cache
    return attribute