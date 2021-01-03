from Wishlist import Wishlist


def main():
    w = Wishlist()

    w.wishlist_add("Gears 5")
    w.wishlist_add("Warhammer total war")
    w.wishlist_add(1139900)
    w.wishlist_add("Persona 4")
    w.wishlist_add("Cyberpunk")

    w.print_all_game_info()


if __name__ == "__main__":
    main()
