# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(E, L):
    # Implement your solution here
    entrance_fee = 2
    first_hour_cost = 3
    successive_hour_cost = 4

    entry_hour, entry_minute = map(int, E.split(':'))
    exit_hour, exit_minute = map(int, L.split(':'))

    # Calculate the duration of parking in minutes
    duration = (exit_hour - entry_hour) * 60 + (exit_minute - entry_minute)

    # Apply the billing rules
    total_cost = entrance_fee + first_hour_cost

    # Subtract the first hour as it's already accounted for
    duration -= 60

    if duration > 0:
        # Calculate the number of additional hours
        additional_hours = (duration + 59) // 60
        total_cost += additional_hours * successive_hour_cost

    return total_cost

print(solution('10:23', '12:30'))