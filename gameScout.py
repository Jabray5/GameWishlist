import steam


class Game:
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
        self.base_price = steam.get_base_price(self.steam_id, Game.COUNTRY_CODE)

        self.steam_price = steam.get_current_price(self.steam_id, Game.COUNTRY_CODE)
        self.steam_discount = steam.get_discount_amount(self.steam_id, Game.COUNTRY_CODE)
        self.steam_on_sale = self.steam_discount > 0

        self.epic_price = None

        self.gog_price = None

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"[{self.title}, {self.steam_price}]"

    # Get current prices function
    def update(self):
        self.steam_price = steam.get_current_price(self.steam_id, Game.COUNTRY_CODE)
        self.steam_discount = steam.get_discount_amount(self.steam_id)
        self.steam_on_sale = self.steam_discount > 0

    # Check against wishlist prices

    # Print all info
    def print_info(self):
        print("*************************")
        print(f"Game: {self.title}\tBase price: {self.base_price}")
        print()
        print(f"Steam")
        print(f"On sale: {self.steam_on_sale}\tDiscount: {self.steam_discount}\tPrice: {self.steam_price}")
        print("*************************")


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


w = Wishlist()

w.wishlist_add("Gears 5")
w.wishlist_add("Warhammer total war")
w.wishlist_add(1139900)
w.wishlist_add("Persona 4")

print(w)

w.print_all_game_info()
