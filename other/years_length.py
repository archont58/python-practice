from math import pi


def years_length(r, v):
    r = r*1000000
    year = 2*pi*r/v
    year = year/(60*60*24)
    return round(year)


while True:
    radius = input("Enter the radius of the planet’s orbit (million kilometers): ")
    try:
        radius = float(radius)
    except ValueError:
        print("Enter the number!")
        continue

    speed = input("Enter the orbital speed (km/s): ")
    try:
        speed = float(speed)
    except ValueError:
        print("Enter the number!")
        continue

    print("The length of year (years):", years_length(radius, speed))
    yes = ('yes', 'Yes', 'y', 'Y')
    no = ('no', 'No', 'n', 'N')

    while True:
        a = str(input("Would you like to continue (yes/no; y/n): "))
        if a not in yes and a not in no:
            continue
        else:
            break

    if a in yes:
        continue
    elif a in no:
        break
