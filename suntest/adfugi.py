def phi(n):
    result = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            while n % i == 0:
                n //= i
            result *= (i - 1)
    if n > 1:
        result *= (n - 1)
    return result
