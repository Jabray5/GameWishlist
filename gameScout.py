import steam

class Game():

    COUNTRY_CODE = "gb"
    CURRENCY = "GBP"

    def __init__(self, name_query):
        # Create object by searching Steam store for title
        # Takes the game's name as a string or the game's steam ID as an integer < 7 digits
        if type(name_query) is int and len(str(name_query)) <= 7:
            self.steam_id = str(name_query)
        else:
            self.steam_id = steam.get_app_id_by_query(name_query)
        self.title = steam.get_app_name(self.steam_id)
        self.price = steam.get_app_price(self.steam_id, Game.COUNTRY_CODE)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"[{self.title}, {self.price}]"

    # Get current prices function

    # Check against wishlist prices


class Wishlist:

    def __init__(self, wishlist=None):
        if wishlist is None:
            self.wishlist = []
        else:
            self.wishlist = wishlist

    def wishlist_add(self, game):
        game_to_add = Game(game)
        self.wishlist.append(game_to_add)

    def wishlist_remove(self, game):
        game_to_delete = Game(game)
        for game in self.wishlist:
            if game.steam_id == game_to_delete.steam_id:
                self.wishlist.remove(game)

    def print_wishlist(self):
        print(self.wishlist)

    def __str__(self):
        result = ""
        for item in self.wishlist:
            result += ", " + item.__repr__()
        return(result.lstrip(", "))



w = Wishlist()

w.wishlist_add("Gears 5")
w.wishlist_add("Warhammer total war")
w.wishlist_add(1139900)

w.wishlist_remove("Gears 5")
w.wishlist_remove("Subnautica")

print(w)