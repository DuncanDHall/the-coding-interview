def alpha_num_sort(s):
    lowers = [c for c in s if c.islower()]
    lowers.sort()
    uppers = [c for c in s if c.isupper()]
    uppers.sort()
    digits = [int(c) for c in s if c.isnumeric()]
    evens = [str(n) for n in digits if n % 2 == 0]
    evens.sort()
    odds = [str(n) for n in digits if n % 2 == 1]
    odds.sort()
    return "".join(lowers + uppers + evens + odds)
