def min_removals_to_2x_minus_1(A):
    def is_2x_minus_1(num):
        return num & (num + 1) == 0
    
    n = len(A)
    # Initial possible OR results
    possible_or_results = {0: 0}  # {current OR result: minimum removals to achieve this OR result}
    
    for num in A:
        new_or_results = possible_or_results.copy()
        
        for or_result in possible_or_results:
            new_or_result = or_result | num
            if new_or_result not in new_or_results:
                new_or_results[new_or_result] = possible_or_results[or_result] + 1
            else:
                new_or_results[new_or_result] = min(new_or_results[new_or_result], possible_or_results[or_result] + 1)
        
        possible_or_results = new_or_results
    
    min_removals_required = float('inf')
    for result in possible_or_results:
        if is_2x_minus_1(result):
            min_removals_required = min(min_removals_required, n - (possible_or_results[result]))
    
    return min_removals_required

# Sample inputs
print(min_removals_to_2x_minus_1([6, 16]))  # Output: 2
print(min_removals_to_2x_minus_1([1, 17, 18, 5, 6]))  # Output: 2


# # Sample inputs
# for _ in range(int(input())):
#     n = int(input())
#     A = list(map(int, input().split()))
#     print(min_removals_to_2x_minus_1(A))
