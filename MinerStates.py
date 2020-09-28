from State import State
from Locations import Location
from colorama import Fore, Back, Style

class EnterMineAndDigForNugget(State):

    def enter(self, object):
        if object.location != Location.goldmine:
            output = str(object.id) + ": " + "Walking to the gold mine"
            print(Fore.RED + output)
            object.changeLocation(Location.goldmine);

    def execute(self, object):
        object.addToGoldCarried(1)

        object.increaseFatigue()

        output = str(object.id) + ": " + "Pickin' up a nugget"
        print(Fore.RED + output)

        # if enough gold mined, go and put it in the bank
        if object.arePocketsFull():
            object.changeState(VisitBankAndDepositGold())

        if object.isThirsty():
            object.changeState(QuenchThirst())

    def exit(self, object):
        output = str(object.id) + ": " + "I'm leaving the mine!"
        print(Fore.RED + output)


class VisitBankAndDepositGold(State):

    def enter(self, object):
        if object.location != Location.bank:
            output = str(object.id) + ": " + "Goin' to the bank. Yes siree"
            print(Fore.RED + output)

            object.changeLocation(Location.bank);


    def execute(self, object):
        # deposit the gold
        object.addToWealth(object.goldCarried)
        object.setGoldCarried(0);
        output = str(object.id) + ": " + "Depositing gold. Total savings now: " + str(object.moneyInBank)
        print(Fore.RED + output)

        # wealthy enough to rest?
        if object.moneyInBank >= 5:
            output = str(object.id) + ": " + "WooHoo! Rich enough for now. Back home to mah li'lle lady"
            print(Fore.RED + output)
            object.changeState(GoHomeAndSleepTilRested())
        else:
            object.changeState(EnterMineAndDigForNugget())

    def exit(self, object):
        output = str(object.id) + ": " + "Leavin' the bank"
        print(Fore.RED + output)


class GoHomeAndSleepTilRested(State):

    def enter(self, object):
        if object.location != Location.shack:
            output = str(object.id) + ": " + "Walkin' home"
            print(Fore.RED + output)
            object.changeLocation(Location.shack);

    def execute(self, object):
        if not object.isFatigued():
            output = str(object.id) + ": " + "What a God darn fantastic nap! Time to find more gold"
            print(Fore.RED + output)
            object.changeState(EnterMineAndDigForNugget())
        else:
            output = str(object.id) + ": " + "ZZZZ... "
            print(Fore.RED + output)
            object.decreaseFatigue()

    def exit(self, object):
        output = str(object.id) + ": " + "Leaving the house"
        print(Fore.RED + output)


class QuenchThirst(State):

    def enter(self, object):
        if object.location != Location.saloon:
            object.changeLocation(Location.saloon)
            output = str(object.id) + ": " + "Boy, ah sure is thusty! Walking to the saloon"
            print(Fore.RED + output)

    def execute(self, object):
        if object.isThirsty():
            object.buyAndDrinkAWhiskey();
            output = str(object.id) + ": " + "That's mighty fine sippin liquer"
            print(Fore.RED + output)
            object.changeState(EnterMineAndDigForNugget())
        else:
            output = str(object.id) + ": " + "ERROR! ERROR! ERROR!"
            print(Fore.RED + output)

    def exit(self, object):
        output = str(object.id) + ": " + "LEaving the saloon, feeling good!"
        print(Fore.RED + output)