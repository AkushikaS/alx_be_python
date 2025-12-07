import datetime

def display_current_datetime():
    #"""Display the current date and time in a readable format."""
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("YYYY-MM-DD HH:MM:SS")
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(days_to_add):
    #"""Calculate and display the future date after adding specified days."""
    current_date = datetime.datetime.now()
    future_date = current_date + datetime.timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")
    return future_date

# Main execution
if __name__ == "__main__":
    # Part 1: Display current date and time
    display_current_datetime()
    
    # Part 2: Calculate future date
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days)
    except ValueError:
        print("Error: Please enter a valid integer.")