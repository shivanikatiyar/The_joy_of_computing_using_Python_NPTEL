def swap_case(s):
    t=""    # empty string taken
    for l in s:
        if(l.isupper()):
           t+=l.lower()
        else :
           t+=l.upper()
    return t;

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)