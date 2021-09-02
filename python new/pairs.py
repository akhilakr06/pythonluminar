def find_pairs_of_numbers(num_list,n):
    count = 0
    for num1 in num_list:
        for num2 in num_list:
            if (num1 + num2) == n:
                count = count + 1
    return int(count/2)

num_list=[1, 2, 7, 4, 5, 6, 0, 3]
n=6

print(find_pairs_of_numbers(num_list,n))