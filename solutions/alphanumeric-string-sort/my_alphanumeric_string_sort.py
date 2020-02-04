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


# alphanumeric-string-sort.py has a very nice solution taking advantage
# the size of our alphanumeric alphabet. More readable, less generalizable


def alpha_num_sort_2(s):
    return "".join(sorted(s, key=compare_decorator))


def compare_decorator(c):
    if c.islower():
        return "0" + c
    if c.isupper():
        return "1" + c
    if c.isnumeric():
        d = int(c)
        return str((d % 2) + 2) + str(d)
