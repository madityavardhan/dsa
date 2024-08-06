from collections import defaultdict

def get_prefix_frequencies(s):
    n = len(s)
    prefix_freq = [defaultdict(int) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        prefix_freq[i] = prefix_freq[i - 1].copy()
        prefix_freq[i][s[i - 1]] += 1
    
    return prefix_freq

def min_operations(a_freq, b_freq, l, r):
    operations = 0
    for char in set(a_freq[r].keys()).union(set(b_freq[r].keys())):
        count_a = a_freq[r].get(char, 0) - a_freq[l - 1].get(char, 0)
        count_b = b_freq[r].get(char, 0) - b_freq[l - 1].get(char, 0)
        if count_b > count_a:
            operations += count_b - count_a
    return operations

for _ in range(int(input())):
    n, q = map(int, input().strip().split())
    a = input().strip()
    b = input().strip()
    
    a_freq = get_prefix_frequencies(a)
    b_freq = get_prefix_frequencies(b)
    
    for _ in range(q):
        l, r = map(int, input().strip().split())
        print(min_operations(a_freq, b_freq, l, r))
