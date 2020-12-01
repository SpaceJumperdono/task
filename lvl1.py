def squirrel(N):
    factorial = 1
    for i in range(1, N+1):
        factorial *= i
        print(factorial)
    string_number = str(factorial)
    lengh = len(string_number)
    number = 10 ** (lengh - 1)
    result = factorial // number
    return result