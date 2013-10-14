"""
Reservation finder

Along with this file, you'll find two files named units.csv and reservations.csv 
with fields in the following format

location_id, unit_size
location_id, reservation_start_date, reservation_end_date

You will write a simple application that manages a reservation system. 
It will have two commands, 'available' and 'reserve' with the following behaviors:

available <date> <number of occupants> <length of stay>
This will print all available units that match the criteria. Any unit with capacity equal or greater to the number of occupants will be printed out.

Example:
SeaBnb> available 10/10/2013 2 4
Unit 10 (Size 3) is available
Unit 20 (Size 2) is available

reserve <unit number> <start date> <length of stay>
This creates a record in your reservations that indicates the unit has been reserved.
It will print a message indicating its success.

A reservation that ends on any given day may be rebooked for the same evening, ie:
    
    If a reservation ends on 10/10/2013, a different reservation may be made starting on 10/10/2013 as well.

Example:
SeaBnb> reserve 10 10/11/2013 3 
Successfully reserved unit 10 for 3 nights

Reserving a unit must make the unit available for later reservations. Here's a sample session:

SeaBnb> available 10/10/2013 2 4
Unit 10 (Size 3) is available
Unit 20 (Size 2) is available
SeaBnb> reserve 10 10/11/2013 3 
Successfully reserved unit 10 for 3 nights
SeaBnb> available 10/10/2013 2 4
Unit 20 (Size 2) is available
SeaBnb> reserve 10 10/11/2013 3 
Unit 10 is unavailable during those dates
SeaBnb> quit

Notes:
Start first by writing the functions to read in the csv file. 
These have been stubbed for you. Then write the availability function, then reservation. 
Test your program at each step (it may be beneficial to write tests in a separate file.) 
Use the 'reservations' variable as your database. Store all the reservations in there, including the ones from the new ones you will create.

The datetime and timedelta classes will be immensely helpful here, as will the strptime function.
"""

import sys
import datetime
import time

def parse_time(raw_date):
    struct = time.strptime(raw_date.strip(), "%m/%d/%Y")
    return datetime.date.fromtimestamp(time.mktime(struct))

def read_units():
    """Read in the file units.csv and returns a list of all known units."""
    units = open("units.csv")
    result = []
    for line in units.readlines():
        splitted = line.split(",")
        index = int(splitted[0])
        size = int(splitted[1])
        result.append((index, size))
    units.close()
    return result


def read_existing_reservations():
    """Reads in the file reservations.csv and returns a list of reservations."""
    csv = open("reservations.csv")
    result = {}
    for line in csv.readlines():
        parsed = line.split(",")
        index = int(parsed[0])
        start_date = parse_time(parsed[1])
        end_date = parse_time(parsed[2])
        if index in result:
            result[index].append((start_date, end_date))
        else:
            result[index] = [(start_date, end_date)]
    csv.close()
    return result

def is_not_reserved(reservations, start_date, end_date, unit_id):
    is_free = True
    if unit_id in reservations:
        for res_begin, res_end in reservations[unit_id]:
            if not (res_end <= start_date or end_date <= res_begin):
                is_free = False
    return is_free

def available(units, reservations, start_date, occupants, stay_length):
    occupants = int(occupants)
    start_date = parse_time(start_date)
    stay_length = int(stay_length)
    end_date = start_date + datetime.timedelta(days=stay_length)
    for unit_id, unit_size in units:
        if unit_size >= occupants:
            if is_not_reserved(reservations, start_date, end_date, unit_id):
                print "Unit %d (Size %d) is available" % (unit_id, unit_size)



def reserve(units, reservations, unit_id, start_date, stay_length):
    unit_id = int(unit_id)
    start_date = parse_time(start_date)
    stay_length = int(stay_length)
    end_date = start_date + datetime.timedelta(days=stay_length)
    if not is_not_reserved(reservations, start_date, end_date, unit_id):
        print "Unit already reserved. Reservation failed."
        return 
    if unit_id in reservations:
        reservations[unit_id].append((start_date, end_date))
    else:
        reservations[unit_id] = [(start_date, end_date)]

    print "Successfully reserved"




def main():
    units = read_units()
    reservations = read_existing_reservations()  

    while True:
        command = raw_input("SeaBnb> ")
        cmd = command.split()
        if cmd[0] == "available":
            # look up python variable arguments for explanation of the *
            available(units, reservations, *cmd[1:])
        elif cmd[0] == "reserve":
            reserve(units, reservations, *cmd[1:])
        elif cmd[0] == "quit":
            sys.exit(0)
        else:
            print "Unknown command"

if __name__ == "__main__":
    main()