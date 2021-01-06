import random
from wishlist import Wishlist


def random_test(n):

    w = Wishlist()

    with open("Tests/TestList.txt") as file:

        game_list = []
        for line in file:
            game_list.append(line)

        l = len(game_list)

        if n > l:
            raise ValueError(f"{n} is greater than {l}")

        i = 0
        while i < n:
            random_number = random.randrange(0,l)
            game = game_list[random_number]
            game = game.strip()
            print(f"Attempting to add: {game}")
            w.wishlist_add(game)
            print(f"Game added: {w.wishlist[-1].title} / {w.wishlist[-1].epic_slug}")
            print()
            i += 1

    w.print_all_game_info()