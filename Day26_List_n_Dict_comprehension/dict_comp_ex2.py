"""
use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in degrees Celsius
 and converts it into degrees Fahrenheit.

To convert temp_c into temp_f: (temp_c * 9/5) + 32 = temp_f
"""

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:
weather_f = {day: (temp * 9 / 5) + 32 for (day, temp) in weather_c.items()}
weather_ovr_70 = {day: (temp * 9 / 5) + 32 for (day, temp) in weather_c.items() if temp >= 20}

print(weather_f)
print(f"Pleasant days: {weather_ovr_70}")
