def compute_sum(first_term, last_term):
    total_sum = 0
    for num in range(first_term, last_term + 1):
        total_sum += num
    return total_sum


first_term = int(input("Enter first term number: "))
last_term = int(input("Enter last term number: "))


sum_result = compute_sum(first_term, last_term)
print(f"The sum of the numbers from {first_term} to {last_term} is {sum_result}")

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True