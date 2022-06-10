"""項目6:複数代入アンパック."""

if __name__ == "__main__":
    snack_calories = {"chips": 140, "popcorn": 80, "nuts": 190}
    items = tuple(snack_calories.items())
    print(items)
