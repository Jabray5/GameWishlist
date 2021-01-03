from wishlist import Wishlist


def main():
    w = Wishlist()

    w.wishlist_add("Persona 4")
    w.wishlist_add(1139900)
    w.wishlist_add("Dont Starve")
    w.wishlist_add("Cyberpunk")
    w.wishlist_add("Terraria")

    w.print_all_game_info()


if __name__ == "__main__":
    main()
