
def convert_time():
    from time import time

    now = time()

    # num of days
    num_days:int = int(now // 86400)     # 1 day = 86400 sec
    remaining:int = int(now % 86400)
    # hours
    hours = remaining // 3600
    remaining:int = int(hours % 3600)
    # minutes
    minutes:int = int(remaining // 60)
    # second
    seconds:int = int(remaining % 60)

    print("Days since Jan 1, 1970:", num_days)
    print("Current time: %02d:%02d:%02d" % (hours, minutes, seconds))

def is_triangle(stick1: int, stick2: int, stick3: int) -> str:
    if stick1 + stick2 <= stick3:
        return "No"
    elif stick1 + stick3 <= stick2:
        return "No"
    elif stick2 + stick3 <= stick1:
        return "No"
    else: 
        return "Yes"

def main():
    convert_time()
    print(is_triangle(10, 11, 10))

if __name__ == "__main__":
    main()