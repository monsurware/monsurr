# 
import calendar
from datetime import datetime


calendar_data = {
    "2025-07-07": "Presentation",
    "2025-12-25": "Christmas"
}

def display_month(year, month):
    """Display a simple calendar for a given month and year."""
    month_name = calendar.month_name[month]
    print(f"\n{month_name} {year}")
    print("Mo Tu We Th Fr Sa Su")

    first_weekday, num_days = calendar.monthrange(year, month)

    current_weekday = first_weekday


    print("   " * current_weekday, end="")

    for day in range(1, num_days + 1):
        date_str = f"{year}-{month:02d}-{day:02d}"

        if date_str in calendar_data and calendar_data[date_str]:
            print(f"*{day:2d}", end=" ")
        else:
            print(f" {day:2d}", end=" ")

        current_weekday += 1
        if current_weekday % 7 == 0:
            print()

    if current_weekday % 7 != 0:
        print()

def display_year(year):
    """Display all 12 months for the given year."""
    for month in range(1, 13):
        display_month(year, month)

def main():
    display_year(2025)

if __name__ == "__main__":
    main()
