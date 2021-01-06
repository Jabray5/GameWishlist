from epicstore_api import EpicGamesStoreAPI
from epicstore_api import OfferData


class EpicStoreAPI(EpicGamesStoreAPI):

    def get_slug_from_query(self, query):
        # Grabs slug from the first search result. Could be expanded to iterate through results and check title
        try:
            slug = self.fetch_store_games(count=1, keywords=query)["data"]["Catalog"]["searchStore"]["elements"][0][
            "productSlug"].rstrip("/home")
        except(IndexError):
            return(None)
        return slug

    def get_price_from_slug(self, slug):
        game = self.get_product(slug)
        offers = []
        for page in game['pages']:
            if page.get('offer') is not None:
                try:
                    offers.append(OfferData(page['namespace'], page['offer']['id']))
                except(KeyError):
                    # Ignore it and hope for the best
                    pass

        offers_data = self.get_offers_data(*offers)[0]['data']['Catalog']['catalogOffer']['price']['totalPrice']

        price = {"original": offers_data["originalPrice"] / 100,
                 "discount": offers_data["discountPrice"] / 100,
                 "discount_amt": 100 - round((offers_data["discountPrice"] * 100) / offers_data["originalPrice"])}

        return price


    def print_results(self, query):
        # Just using this for testing results currently
        print(self.fetch_store_games(count=1, keywords=query)["data"]["Catalog"]["searchStore"])