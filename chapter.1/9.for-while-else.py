"""項目9:for と while の後に else は使わない."""


if __name__ == "__main__":
    for i in range(3):
        print(f"For Loop {i}")
    else:
        print("For Else block")
    print("-" * 50)

    index = 0
    while index < 3:
        print(f"While Loop {index}")
        index += 1
    else:
        print("While Else block")
    print("-" * 50)
