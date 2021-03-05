## GameWishlist

Keeps track of video game prices across multiple stores, and alerts user to sales/discounts.

Currently uses the Steam Store as the groundwork for looking up games, and uses the information from there to fetch prices from other stores.

To implement:
- <s>Steam Store</s>
- <s>Epic Games Store</s>
- GOG Store
- Alert/messaging system via Discord
- Implement Python Threads

Issues:
- Steam sometimes grabs wrong game (e.g. 'Super Meat Boy Forever' instead of 'Super Meat Boy')
- Need to catch when game does not exist in particular store


Unofficial documentation for Steam API from: https://wiki.teamfortress.com/wiki/User:RJackson/StorefrontAPI

Epic Games API based on: https://github.com/SD4RK/epicstore_api
