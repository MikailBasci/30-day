import datetime

def new_year_greeting():
    now = datetime.datetime.now()
    current_year = now.year

    # Calculate the date of the upcoming New Year
    new_year = datetime.datetime(current_year + 1, 1, 1, 0, 0, 0)

    # Calculate the remaining time from the current moment
    remaining_time = new_year - now

    # Extract days, hours, minutes, and seconds
    days = remaining_time.days
    seconds = remaining_time.seconds
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

    # Create the greeting message
    greeting = "Happy New Year!\n"
    greeting += f"Time remaining until New Year: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds."

    return greeting

# Display the greeting
print(new_year_greeting())
