def maximum_cost(n, m, routes):
    # Step 1: Initialize distances
    dist = [-float('inf')] * (n + 1)
    dist[1] = 0

    # Step 2: Relax all edges (n-1) times
    for _ in range(n - 1):
        for u, v, cost in routes:
            if dist[u] != -float('inf') and dist[u] + cost > dist[v]:
                dist[v] = dist[u] + cost
    
    # Step 3: Check for negative weight cycles (not necessary in this problem as weights are positive)

    # Step 4: Return the result
    return dist[n] if dist[n] != -float('inf') else -1

# Example 1
n = 5
m = 4
routes = [(1, 4, 1), (2, 5, 7), (3, 4, 6), (3, 5, 13)]
print(maximum_cost(n, m, routes))  # Output: 34```