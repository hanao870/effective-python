"""項目7:range ではなく enumerate を使う."""
from random import randint

if __name__ == "__main__":
    random_bit = 0
    for i in range(64):
        if randint(0, 1):
            random_bit |= 1 << i

    print(bin(random_bit))
    print("-" * 50)

    favolite_list = ["vanilla", "chocolate", "pecan", "strawberry"]
    for favor in favolite_list:
        print(f"{favor} is delicious")
    print("-" * 50)

    for i in range(len(favolite_list)):
        favor = favolite_list[i]
        print(f"{i + 1}: {favor}")
    print("-" * 50)

    it = enumerate(favolite_list)
    print(next(it))
    print(next(it))
    print("-" * 50)

    for i, favor in enumerate(favolite_list, 1):
        print(f"{i}: {favor}")
