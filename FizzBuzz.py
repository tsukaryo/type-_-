for num in range(1, 101):
    string = ''

    # ここから記述

    #3でも5でも割り切れる時はFizzBuzzと出力
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
        continue
    #３のみで割り切れるときは、Fizzと出力
    elif num % 3 == 0:
        print("Fizz")
        continue
    #5のみで割り切れるときはBuzzと出力
    elif num % 5 == 0:
        print("Buzz")
        continue
    #3でも5でも割り切れないときはnumを出力
    else:
        print(num) 
        continue

    # ここまで記述


    print(string)