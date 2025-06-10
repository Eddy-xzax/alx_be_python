from datetime import datetime, timedelta #date time module

def display_current_datetime():
    current_date = datetime.now().date()
    full_datetime = datetime.now()
    
    current_datetime = full_datetime.strftime("%Y-%m-%d %H:%M:%S")
    print("The date today is: ", current_date)
    print("Current date today is: ", current_datetime)
display_current_datetime()
Days = int(input("Enter number of days to add to the current date: "))
def calculate_future_date():
    date = datetime.now().date()
    future_date = date + timedelta(days=Days)
    Future_date = future_date.strftime("%Y-%m-%d")
    print("Future date: ", Future_date)
calculate_future_date()
