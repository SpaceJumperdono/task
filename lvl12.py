def parse(s):
    number = []
    for i in s:
        if i == chr(48):
            number.append(0)
        if i == chr(49):
            number.append(1)
        if i == chr(50):
            number.append(2)
        if i == chr(51):
            number.append(3)
        if i == chr(52):
            number.append(4)
        if i == chr(53):
            number.append(5)
        if i == chr(54):
            number.append(6)
        if i == chr(55):
            number.append(7)
        if i == chr(56):
            number.append(8)
        if i == chr(57):
            number.append(9)
    result = 0
    for count, i in enumerate(reversed(number)):
        result += i*(10**count)
    return result
    
def BigMinus(s1, s2):
    s1 = s1
    s2 = s2
    number1 = parse(s1)
    number2 = parse(s2)
    number3 = abs(number1 - number2)
    return str(number3)

