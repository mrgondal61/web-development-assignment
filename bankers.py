# ==========================================================
#        BANKER'S ALGORITHM (CONTROLLED DEMO VERSION)
# ==========================================================

print("=" * 65)
print("              BANKER'S ALGORITHM PROGRAM")
print("=" * 65)

# ----------------------------------------------------------
# USER INPUT
# ----------------------------------------------------------

processes = int(input("\nEnter number of processes: "))
resources = 3  # Fixed to avoid complexity

print("\nNumber of resource types is fixed to 3 (A, B, C)")

print("\nEnter AVAILABLE Resources (Example: 3 3 2)")
available = list(map(int, input("Available: ").split()))

print("\nEnter ALLOCATION Matrix (space separated values)")
print("Example row format: 0 1 2\n")

allocation = []
for i in range(processes):
    row = list(map(int, input(f"P{i}: ").split()))
    allocation.append(row)

# ----------------------------------------------------------
# AUTO-GENERATE MAX MATRIX
# ----------------------------------------------------------

maximum = []
for i in range(processes):
    row = []
    for j in range(resources):
        row.append(allocation[i][j] + 2)   # Offset = 2
    maximum.append(row)

# ----------------------------------------------------------
# CALCULATE NEED MATRIX
# ----------------------------------------------------------

def calculate_need():
    need = []
    print("\nCalculating NEED Matrix (Need = Max - Allocation)\n")
    for i in range(processes):
        row = []
        for j in range(resources):
            value = maximum[i][j] - allocation[i][j]
            row.append(value)
        need.append(row)
        print(f"P{i} Need: {row}")
    return need


# ----------------------------------------------------------
# SAFETY ALGORITHM
# ----------------------------------------------------------

def bankers_algorithm():

    print("\n" + "=" * 65)
    print("                 INITIAL SYSTEM STATE")
    print("=" * 65)

    print("\nAvailable Resources:", available)

    print("\nALLOCATION MATRIX")
    for i in range(processes):
        print(f"P{i}: {allocation[i]}")

    print("\nAUTO-GENERATED MAXIMUM MATRIX")
    for i in range(processes):
        print(f"P{i}: {maximum[i]}")

    need = calculate_need()

    print("\n" + "=" * 65)
    print("              RUNNING SAFETY ALGORITHM")
    print("=" * 65)

    work = available.copy()
    finish = [False] * processes
    safe_sequence = []
    step = 1

    while len(safe_sequence) < processes:
        found = False

        for i in range(processes):
            if not finish[i]:
                if all(need[i][j] <= work[j] for j in range(resources)):

                    print(f"\nStep {step}:")
                    print(f"P{i} can execute (Need <= Available)")
                    print(f"Available Before Execution: {work}")

                    for j in range(resources):
                        work[j] += allocation[i][j]

                    print(f"Available After Execution:  {work}")

                    finish[i] = True
                    safe_sequence.append(i)
                    step += 1
                    found = True

        if not found:
            print("\n❌ SYSTEM IS NOT IN SAFE STATE")
            return

    print("\n" + "=" * 65)
    print("              FINAL RESULT")
    print("=" * 65)

    print("✅ SYSTEM IS IN SAFE STATE")
    print("Safe Sequence:", " -> ".join(f"P{i}" for i in safe_sequence))


# ----------------------------------------------------------
# RUN PROGRAM
# ----------------------------------------------------------

bankers_algorithm()

print("\n" + "=" * 65)
print("                PROGRAM EXECUTION COMPLETE")
print("=" * 65)