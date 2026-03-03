# How old
from datetime import datetime, timedelta
millennium = datetime(1999, 12, 31)
day = int(input("Day:"))
month = int(input("Month:"))
year = int(input("Year:"))
date_birth = datetime(year, month, day)
if year > 1999:
    print("You weren't born yet on the eve of the new millennium.")
else:
    difference = millennium - date_birth
    print(f"You were {difference.days} days old on the eve of the new millennium.")

# Valid PIC?
from datetime import datetime, timedelta
def is_it_valid(pic: str):
    if len(pic) != 11:
        return False
    day = int(pic[0:2])
    month = int(pic[2:4])
    year_part = int(pic[4:6])
    century_marker = pic[6]
    identifier = pic[7:10]
    control_char = pic[10]
    if century_marker == "+":
        year = 1800 + year_part
    elif century_marker == "-":
        year = 1900 + year_part
    elif century_marker == "A":
        year = 2000 + year_part
    else:
        return False
    try:
        datetime(year, month, day)
    except ValueError:
        return False
    part_pic = int(pic[0:6] + identifier)
    control_string = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    control_number= part_pic % 31
    expected_control_char = control_string[ control_number]
 
    if control_char == expected_control_char:
        return True
    else:
        return False
if __name__ == "__main__":
    print(is_it_valid("230827-906F")) 
    print(is_it_valid("120488+246L")) 
    print(is_it_valid("310823A9877")) 
    print(is_it_valid("290200-1239"))

# Screen time
from datetime import datetime, timedelta
 
my_file = input("Filename: ")
starting_date = input("Starting date: ")
days_count = int(input("How many days: "))
 
start_obj = datetime.strptime(starting_date, "%d.%m.%Y")
end_date = start_obj + timedelta(days=days_count - 1)
 
print("Please type in screen time in minutes on each day (TV computer mobile):")
 
data_list = []
total_minutes = 0
current_day = start_obj
 
while current_day <= end_date:
    display_date = current_day.strftime("%d.%m.%Y")
    days_info = input(f"Screen time {display_date}: ")
    
    formatted_info = days_info.replace(" ", "/")
    data_list.append(f"{display_date}: {formatted_info}")
    
    minutes = days_info.split()
    for m in minutes:
        total_minutes += int(m)
        
    current_day += timedelta(days=1)
 
average_minutes = total_minutes / days_count
 
with open(my_file, "w") as f:
    f.write(f"Time period: {start_obj.strftime('%d.%m.%Y')}-{end_date.strftime('%d.%m.%Y')}\n")
    f.write(f"Total minutes: {total_minutes}\n")
    f.write(f"Average minutes: {average_minutes:.1f}\n")
    for line in data_list:
        f.write(line + "\n")
 
print(f"Data saved to {my_file}")
