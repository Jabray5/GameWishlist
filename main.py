from wishlist import Wishlist


def main():
    w = Wishlist()

    w.wishlist_add("Death stranding")
    w.wishlist_add("Cyberpunk 2077")
    w.wishlist_add("Grand Theft Auto V")

    w.print_all_game_info()


if __name__ == "__main__":
    main()
