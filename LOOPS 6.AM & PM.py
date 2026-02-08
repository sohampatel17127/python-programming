for hour in range(24):
    if hour == 0:
        print("00:00 midnight")
    elif hour == 12:
        print("12:00 noon")
    elif hour < 12:
        print(f"{hour:02d}:00 am")
    else:
        print(f"{hour:02d}:00 pm")