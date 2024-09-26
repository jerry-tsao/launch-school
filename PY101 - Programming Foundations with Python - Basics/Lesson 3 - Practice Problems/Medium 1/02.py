def factors(number):
    divisor = number
    result = []
    while divisor > 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result

# The purpose of number % divisor == 0 is to determine whether or not the
# divisor is a factor. If there is no remainder, the divisor is a factor.
