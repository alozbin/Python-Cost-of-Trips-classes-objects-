#Anthony Lozbin
#This program allows the user to state the number of trips they will take in the next year, and the destination, length, and cost of each, and then
#organizes the information as the output, as well as calculates and displays the total cost of all the trips.

class BucketList:
    def __init__(self, dest, days, cost):
        self.__destination = dest
        self.__days_at_location = days
        self.__est_cost = cost

    def get_cost(self):
        return self.__est_cost

    def __str__(self):
        return f'Destination: {self.__destination}\nLength of trip: {self.__days_at_location} days\nEstimated cost: ${self.__est_cost}\n\n'

def main():
    num_trips = int(input('How many trips will you take in the next year? '))
    print()
    trips = triplist(num_trips)

    print('\nHere are the trips you indicated:\n')
    displaytrips(trips)

    total_cost = calc_total_cost(trips)
    print(f'The total estimated cost of all the trips would be ${total_cost:,.2f}')

def triplist(n):
    triplist = []

    for i in range(n):
        location = input('Where are you headed? ')
        numdays = input('How many days will you stay? ')
        tripcost = float(input('What is the cost of this specific trip? $'))
        print()

        tripobj = BucketList(location, numdays, tripcost)

        triplist.append(tripobj)

    return triplist

def calc_total_cost(trips):
    totalcost = 0
    for c in trips:
        totalcost += c.get_cost()

    return totalcost

def displaytrips(trip1):
    for t in trip1:
        print(t)

main()
