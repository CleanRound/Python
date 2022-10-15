try:
    for i in range(1, 11):
        print("\n\nMultiplication table for %d\n" % (i))
        for j in range(1, 11):
            print("%-5.d * %5.d    = %5.d"
                  % (i, j, i * j))
except Exception as err:
    print(f'Error: {err}')
finally:
    print('The program has finished')