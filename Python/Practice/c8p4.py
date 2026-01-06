def sum_of_n_natural_numbers(n):
    if(n==1):
        return 1
    return n + sum_of_n_natural_numbers(n-1)

print(sum_of_n_natural_numbers(5))



