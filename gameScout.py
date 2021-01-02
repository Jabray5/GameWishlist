import steam

class Game():

    country_code="gb"

    def __init__(self, query):
        self.steam_id = steam.get_app_id_by_query(query)
        self.title = steam.get_app_name(self.steam_id)
        self.price = steam.get_app_price(self.steam_id, Game.country_code)

    def __str__(self):
        print(self.title)

    # Get current prices function

    # Check against wishlist prices


class Wishlist():

    def __init__(self, wishlist=list):
        self.wishlist = wishlist

    def wishlist_add(self, game_title):
        game_to_add = Game(game_title)
        self.wishlist.append(game_to_add)

    def print_wishlist(self):
        print(self.wishlist)





g = Game("Sam and Max save the world")

print(g.steam_id)
print(g.title)
print(g.price)