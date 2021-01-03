from Game import Game


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

    def __str__(self):
        result = ""
        for item in self.wishlist:
            result += ", " + item.__repr__()
        return (result.lstrip(", "))

    def print_game_info(self, index=int):
        self.wishlist[index].print_info()

    def print_all_game_info(self):
        for game in self.wishlist:
            game.print_info()

