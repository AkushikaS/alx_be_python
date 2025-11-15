task1 =input ("Enter your task:")
priority = input("Enter the priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: Your task '{task1}' is a high priority that requires immediate attention.")
        else:
            print(f"Reminder: Your task '{task1}' with high priority is pending. Please attend to it when possible.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: Your task '{task1}' is of medium priority and should be completed soon.")
        else:
            print(f"Reminder: Your task '{task1}' is of medium priority. Please remember to complete it.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: Your task '{task1}' is low priority but time-bound. Please schedule it accordingly.")
        else:
            print(f"Reminder: Your task '{task1}' is low priority. You can complete it at your convenience.")
    