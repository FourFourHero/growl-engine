import logging
from growl.models import Game
from growl.caches.game import get_game_from_cache
from growl.caches.game import store_game_in_cache

logger = logging.getLogger(__name__)

### Create game
def create_game(developer, name, description=None):
    game = Game()
    game.developer = developer
    game.name = name
    description = description
    game.save() # post_save stores in cache
    return game

### Get game
def get_game(game_id):
    game = get_game_from_cache(game_id)
    if not game:
        game = Game.objects.get(pk=game_id)
        store_game_in_cache(game)
    return game

### Update game
def update_game(game):
    game.save() # post_save stores in cache
    return game