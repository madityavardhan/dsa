import math

def solution(N, patients):
    total_waiting_time = 0
    current_time = 0
    
    for arrival, time in patients:
        if arrival >= current_time:
            current_time = arrival
        current_time += time
        total_waiting_time += current_time - arrival
    
    average_waiting_time = total_waiting_time // N
    return average_waiting_time


# Example usage:
N = 4
patients = [[5, 2], [5, 4], [10, 3], [20, 1]]
print(solution(N, patients))  # Output: 3
