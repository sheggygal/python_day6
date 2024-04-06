number = int(input("Enter the number: "))

divisor_sum = sum([i for i in range(1, number) if number % i == 0])

is_perfect = divisor_sum == number

print(is_perfect)