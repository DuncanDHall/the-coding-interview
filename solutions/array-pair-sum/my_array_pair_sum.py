#  Given an integer array, output all pairs that sum up to a specific value k. Consider the fact that the same number can add up to `k` with its duplicates in the array.
#
#  > For example the array is [1, 1, 2, 3, 4] and the desired sum is 4. Should we output the pair (1, 3) twice or just once? Also do we output the reverse of a pair, meaning both (3, 1) and (1, 3)? Let’s keep the output as short as possible and print each pair only once. So, we will output only one copy of (1, 3). Also note that we shouldn’t output (2, 2) because it’s not a pair of two distinct elements.
# [EDIT] the above clarification invalidates the examples below
#
#  ## Example
#
#  ```
#  f(10, [3, 4, 5, 6, 7]) // [ [6, 4], [7, 3] ]
#  f(8, [3, 4, 5, 4, 4]) // [ [3, 5], [4, 4], [4, 4], [4, 4] ]
#  ```

from copy import deepcopy


# first solution is O(n^2)
def sol1(k, q):
    s = set()
    for i, n in enumerate(q):
        for j in range(i+1, len(q)):
            if q[i] + q[j] == k:
                s.add((q[i], q[j]))
    res = [list(li) for li in s]
    return res


# this is a better solution using sort then linear time pairing
def sol2(k, q):
    q = deepcopy(q)
    res = []

    q.sort()
    i = 0
    j = len(q) - 1
    while i < j:
        if q[i] + q[j] == k:
            res.append([q[i], q[j]])
        if q[i] + q[j] <= k:
            i += 1
        if q[i] + q[j] >= k:
            j -= 1

    return res
