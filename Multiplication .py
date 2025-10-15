for i in range(1, 11):
    print(f"23 x {i} = {23 * i}")




    n = int(input("Enter number of Rows: "))
    for i in range(1, n+1):
        for j in range(i):
            print('*', end=' ')
        print()