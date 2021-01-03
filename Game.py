from Stores import Steam


class Game:
    COUNTRY_CODE = "gb"
    CURRENCY = "GBP"

    def __init__(self, name_query):
        # Create object by searching Steam store for title
        # Takes the game's name as a string or the game's steam ID as an integer < 7 digits
        if type(name_query) is int and len(str(name_query)) <= 7:
            self.steam_id = str(name_query)
        else:
            self.steam_id = Steam.get_app_id_by_query(name_query)

        self.title = Steam.get_app_name(self.steam_id)
        self.base_price = Steam.get_base_price(self.steam_id, Game.COUNTRY_CODE)

        self.steam_price = Steam.get_current_price(self.steam_id, Game.COUNTRY_CODE)
        self.steam_discount = Steam.get_discount_amount(self.steam_id, Game.COUNTRY_CODE)
        self.steam_on_sale = self.steam_discount > 0

        self.epic_price = None

        self.gog_price = None

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"[{self.title}, {self.steam_price}]"

    # Get current prices function
    def update(self):
        self.steam_price = Steam.get_current_price(self.steam_id, Game.COUNTRY_CODE)
        self.steam_discount = Steam.get_discount_amount(self.steam_id)
        self.steam_on_sale = self.steam_discount > 0

    # Check against wishlist prices

    # Print all info
    def print_info(self):
        print()
        print(f"Game: {self.title}\tBase price: {self.base_price}")
        print(f"Steam")
        print(f"On sale: {self.steam_on_sale}\tDiscount: {self.steam_discount}\tPrice: {self.steam_price}")
