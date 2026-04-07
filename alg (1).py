# Activity Selection Scheduler using Greedy Algorithm

def activity_selection(activities):
    # Sort activities based on finish time
    activities.sort(key=lambda x: x[1])

    selected = []
    
    # Select the first activity
    selected.append(activities[0])
    last_end = activities[0][1]

    # Go through remaining activities
    for i in range(1, len(activities)):
        if activities[i][0] >= last_end:
            selected.append(activities[i])
            last_end = activities[i][1]

    return selected


# ----------- MAIN PROGRAM -----------

# Take number of activities as input
n = int(input("Enter number of activities: "))

activities = []

# Input start and end times
for i in range(n):
    start = int(input(f"Enter start time of activity {i+1}: "))
    end = int(input(f"Enter end time of activity {i+1}: "))
    activities.append((start, end))

# Get selected activities
result = activity_selection(activities)

# Display results
print("\nSelected Activities (start, end):")
for act in result:
    print(act)

print(f"\nMaximum number of non-overlapping activities: {len(result)}")