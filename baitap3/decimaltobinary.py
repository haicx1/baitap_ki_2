def decimal_to_binary(num):
    if num >= 1:
        decimal_to_binary(num // 2)
    print(num % 2, end='')


list_num = list(map(int, input().split()))
for num in list_num:
    decimal_to_binary(num)
    print('\n')
