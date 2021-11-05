N = int(input("Please enter the range (N):\n"))

sum_odd = 0
sum_even = 0
even_count = 0

for i in range(1,N + 1):
    if i % 2 != 0:
        sum_odd += i
    else:
        sum_even += i
        even_count += 1

print(f"The sum of odd numbers in the given range: {sum_odd}")
print(f"The average of even numbers in the given range: {int(sum_even/even_count)}")
