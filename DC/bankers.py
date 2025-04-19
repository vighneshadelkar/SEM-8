def is_safe(n, m, available, max_demand, allocation):
    need = [[max_demand[i][j] - allocation[i][j] for j in range(m)] for i in range(n)]
    finish = [False] * n
    safe_sequence = []
    work = available.copy()

    print("Need Matrix:")
    for row in need:
        print(row)

    while len(safe_sequence) < n:
        found = False
        for i in range(n):
            if not finish[i]:
                if all(need[i][j] <= work[j] for j in range(m)):
                    for j in range(m):
                        work[j] += allocation[i][j]
                    safe_sequence.append(i)
                    finish[i] = True
                    found = True
                    break
        if not found:
            print("System is in an **unsafe state** (deadlock possible).")
            return False

    print("\nSystem is in a **safe state**.")
    print("Safe sequence:", ' -> '.join(f"P{p}" for p in safe_sequence))
    return True

n = 5  # number of processes
m = 3  # number of resource types

# Available resources
available = [3, 3, 2]

# Maximum demand of each process
max_demand = [
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [2, 2, 2],
    [4, 3, 3]
]

# Resources currently allocated to each process
allocation = [
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2]
]

is_safe(n, m, available, max_demand, allocation)
