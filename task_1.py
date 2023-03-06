A = int(input('Введите начальный диапазон: '))
B = int(input('Введите конечный диапазон: '))

range_list = [x for x in range(A, B+1) if x % 2 == 0]

print(range_list)
