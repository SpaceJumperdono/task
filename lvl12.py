def parse(s):
    result = 0
    if s == chr(48):
        result = 0
    if s == chr(49):
        result = 1
    if s == chr(50):
        result = 2
    if s == chr(51):
        result = 3
    if s == chr(52):
        result = 4
    if s == chr(53):
        result = 5
    if s == chr(54):
        result = 6
    if s == chr(55):
        result = 7
    if s == chr(56):
        result = 8
    if s == chr(57):
        result = 9
    return result
    
def BigMinus(s1, s2):
    a = s1[::-1]
    b = s2[::-1]
    t = 0
    shift = 0
    result = ""
    for i in range(len(a)):
        if(i < len(b)):
            t = parse(a[i]) - parse(b[i]) - shift
            shift = 0
        else:
            t = parse(a[i]) - shift
            shift = 0
        if(t < 0):
            t += 10
            shift = 1
        if(i == len(a) - 1 and t == 0):
            break
        else:
            result += str(t)
    return result[::-1]
