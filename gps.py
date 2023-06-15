from machine import Pin, UART
from time import sleep

gps = UART(0, baudrate=9600, tx=Pin(12), rx=Pin(13))

while True:
    note = input('Note for this coordinate: ')
    while gps.any()<256:
        pass
    test_byte = gps.read()
    sleep(1)
    try:
        test = test_byte.decode("utf-8")
    except UnicodeError:
        print('Unicode')
    # Find the index of "$GPGGA" in the big string
    start_index = test.find("$GPGGA")

    if start_index != -1:
        # Extract the substring starting from "$GPGGA"
        substring = test[start_index:]

        # Split the substring using commas as the delimiter
        entries = substring.split(',')

        if len(entries) >= 8:
            # Extract the desired entries (3rd, 4th, 5th, and 6th)
            desired_entries = entries[2:8]

            # Print the extracted entries
            if 'N' in desired_entries[0]:
                pass
            else:
                #print(desired_entries)
                print(f"{note} {desired_entries[0]}{desired_entries[1]} {desired_entries[2]}{desired_entries[3]}")
        

