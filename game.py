from Stores import steam, epic


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

        epic_api = epic.EpicStoreAPI(country=self.COUNTRY_CODE)
        self.epic_slug = epic_api.get_slug_from_query(self.title)
        if self.epic_slug is not None:
            self.epic_base_price, self.epic_price, self.epic_discount = epic_api.get_price_from_slug(self.epic_slug).values()
            self.epic_on_sale = self.epic_discount > 0

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

    # Print game info. This will be handled by a printer class eventually
    def print_info(self):
        print()
        print(f"Game: {self.title}")
        print(f"Steam (Base price: {self.base_price}{self.CURRENCY})")
        print(f"\tOn sale: {self.steam_on_sale}\tDiscount: {self.steam_discount}%\tPrice: {self.steam_price}{self.CURRENCY}")
        print(f"Epic Store (Base price: {self.epic_base_price}{self.CURRENCY})")
        print(f"\tOn sale: {self.epic_on_sale}\tDiscount: {self.epic_discount}%\tPrice: {self.epic_price}{self.CURRENCY}")