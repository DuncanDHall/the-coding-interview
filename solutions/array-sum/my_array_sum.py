#  Calculate the sum of an array which contains integers and other arrays with integers.
#  For example:
#
#  ```
#  array_sum([1,2,[3,4,[5]]])
#  ```
#
#  would return 15.


# recursive solution uses O(n+d) space in memory where n is term count and d is
# max depth
def recursive_sol(q):
    if type(q) == int:
        return q
    elif type(q) == list:
        if q:
            return recursive_sol(q[0]) + recursive_sol(q[1:])
        else:
            return 0  # for the [] case
    else:
        raise TypeError(
            "array_sum supports inputs of nested arrays and integers only"
        )


# this solution is pretty hacky
def str_hack(q):
    acc = 0
    for c in str(q).replace('[', '').replace(']', '').split(', '):
        acc += int(c)
    return acc


# this solution is a less hacky as-you-go than str_hack
def as_you_go(q):
    return sum(flat(q))


def flat(q):
    qq = []
    non_flats = [q]
    while non_flats:
        nf = non_flats.pop()
        for item in nf:
            if type(item) == int:
                qq.append(item)
            elif type(item) == list:
                non_flats.append(item)
            else:
                raise TypeError("array_sum supports inputs of nested arrays " /
                        "and integers only")
    return qq
