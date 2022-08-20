from database_creation import DbInitialser
class User:
    
    def __init__(self, firstName, lastName, cardNumber) -> None:
        self.firstName = firstName
        self.lastName = lastName
        self.cardNumber = cardNumber
        self.db = DbInitialser()
        self.ridesLeft, self.lasRideDate, self.lastRechargeID = self.getRidesAndLastRideFor()
        self.lastRechargeDate = self.getLastRechargeDate()
    
    def getRidesAndLastRideFor(self):
        result = self.db.getRidesAndLastRideFor(self.cardNumber)
        print(result)
        if result == False:
            return (0,'-','-')
        else:
            (rides, lastRide, lastRechargeID) = result[0]
            print((rides, lastRide, lastRechargeID))
            return (rides, lastRide, lastRechargeID)
    
    def getLastRechargeDate(self):
        result = self.db.getLastRideDateFor(self.lastRechargeID)
        if result == False:
            return '-'
        else:
            (date, ) = result[0]
            print(date)
            return (date)