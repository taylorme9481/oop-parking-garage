from ParkingGarage import ParkingGarage
import time
test = ParkingGarage()

while True:
    time.sleep(0.5)
    command = input(""" Welcome to the Rangers Lot. Would you like to park, pay, or leave?: 
  """).lower()

    if command == 'park':
        if not test.parkingSpaces:
            print("sorry no more spots available")
        else:
            print(f"The rate is $10/hr, these are the available spaces: {test.parkingSpaces}")
            picked = int(input("Which space number would you like?: "))
            if picked not in test.parkingSpaces:
                print("Sorry that spot is unavailable")

            else:
                test.takeTicket(picked)
                continue
    elif command == 'pay':
        spotNum = int(input("What is your spot number?: "))
        if spotNum in test.parkingSpaces:
            print("invalid entry")

        else:
            test.payForParking(spotNum)

    elif command == 'leave':
        spotNum = int(input("What is your spot number?: "))
        test.leaveGarage(spotNum)

    else:
        print("Sorry, I don't understand")


