"""
Question 1
"""

seconds = 42
minutes = 42

total_in_seconds = minutes * 60 + seconds
print(f"Total seconds: {total_in_seconds}")

"""
Question 2
"""

kilometers = 10
KILOMETERS_PER_MILE = 1.61

total_miles = kilometers / KILOMETERS_PER_MILE
print(f"Total miles: {round(total_miles)}")

"""
Question 3
"""

avg_seconds_per_mile = total_in_seconds / total_miles
print(f"Average pace in seconds per mile: {round(avg_seconds_per_mile)} seconds")

"""
Question 4
"""

avg_min_per_mile = avg_seconds_per_mile // 60
avg_sec_per_mile = avg_seconds_per_mile % 60

print(f"Average pace in minutes and seconds per mile: {round(avg_min_per_mile)} minutes and {round(avg_sec_per_mile)} seconds")

"""
Question 5
"""

seconds_to_minutes = seconds / 60
total_minutes = minutes + seconds_to_minutes
total_minutes_to_hours = total_minutes / 60

avg_miles_per_hour = total_miles / total_minutes_to_hours

print(f"Average speed in miles per hour: {avg_miles_per_hour:.2f} miles")

