def squirrel(N):
    string_number = str(N)
    lengh = len(string_number)
    number = 10 ** (lengh - 1)
    result = N // number
    return result