from os import curdir


class ParkingGarage():
    
    parkingSpaces = [1,2,3,4,5,6,7,8,9,10]
    tickets = [1,2,3,4,5,6,7,8,9,10]
    currentTicket = {   1: 'unpaid',
                        2: 'unpaid',
                        3: 'unpaid',
                        4: 'unpaid',
                        5: 'unpaid',
                        6: 'unpaid',
                        7: 'unpaid',
                        8: 'unpaid',
                        9: 'unpaid',
                        10: 'unpaid'
} 

    def takeTicket(self, picked):
        self.tickets.remove(picked)
        self.parkingSpaces.remove(picked)
        self.currentTicket[picked] = 'unpaid'
        

    def payForParking(self, picked):
        if self.currentTicket[picked] == 'unpaid':
            
            hours = int(input("How many hours did you park?: "))
            self.calc_parking_fee(hours)
            self.currentTicket[picked] = 'paid'

            if hours == 0:
                print("Enter a value that is bigger than 0")
                return
            else:
                self.parkingSpaces.insert((picked-1),picked)
                self.tickets.insert((picked-1),picked)
        else:
            print("Your ticket has been paid, you have 15 min to leave")
        

    def leaveGarage(self, picked):
        paid = input("Have you paid?: ")
        if paid == 'yes':
            if self.currentTicket[picked] == 'unpaid':
                print("Stop lying, go pay.")
                
            elif self.currentTicket[picked] == 'paid':
                print("Thank you, have a nice day. You have 15 min to leave.")
                self.currentTicket[picked] = 'paid'
                self.parkingSpaces.insert((picked-1),picked)
                self.tickets.insert((picked-1),picked)
            else:
                print("Sorry I didn't understand")
                return
        elif paid == 'no':
            print("Go Pay")
            spot = int(input("What's your spot number?: "))
            self.payForParking(spot)
        else:
            print("I don't understand, yes or no only")


    def calc_parking_fee(self, hours):
        if hours <= 1:
            print(f'${10*hours:.2f}')

        elif 1 <= hours < 12:
            print(f'${10*hours:.2f}')
            
        elif hours >= 10:
            print(f'${10*hours:.2f}')