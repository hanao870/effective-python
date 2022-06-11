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
