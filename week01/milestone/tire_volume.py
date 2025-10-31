import math
from datetime import datetime

tire_width = int(input("Enter the width of the tire in mm (ex 205): "))
tire_aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60) "))
tire_diameter = int(input("Enter the diameter of the wheel in inches (ex 15) "))

volume = ((math.pi * (tire_width ** 2) * tire_aspect_ratio) * ((tire_width * tire_aspect_ratio) + (2540 * tire_diameter) )) / 10000000000

current_date_and_time = datetime.now()

with open("volumes.txt", "at") as volumes:
    print(f"{current_date_and_time:%Y-%m-%d}, {tire_width}, {tire_aspect_ratio}, {tire_diameter}, {volume:.2f}", file=volumes)

print(f"The approximate volume is {volume:.2f} liters")