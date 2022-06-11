"""項目9:for と while の後に else は使わない."""


def _coprime(a: int, b: int) -> bool:
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            return False
    return True


def _coprime_2(a: int, b: int) -> bool:
    is_coprime = True
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            is_coprime = False
            break
    return is_coprime


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

    # break で抜けると else は実行されない
    for i in range(3):
        print(f"For Loop {i}")
        if i == 1:
            break
    else:
        print("For Else block")
    print("-" * 50)

    # else が即実行される
    for i in []:
        print("Never runs")
    else:
        print("For Else block!!!!")

    # while の先頭で終了しても else が実行
    while False:
        print("Never runs")
    else:
        print("While Else block!!!")
    print("-" * 50)

    # 2つの数が互いに素数か判定する
    a = 4
    b = 9

    for i in range(2, min(a, b) + 1):
        print(f"Testing {i}")
        if a % i == 0 and b % i == 0:
            print("Not coprime")
            break
    else:
        print("Coprime")
    print("-" * 50)

    print(f"{_coprime(4, 9)=}")
    print(f"{_coprime_2(3, 6)=}")
    print("-" * 50)
