from BaseGameEntity import BaseGameEntity
from Locations import Location
from MinerStates import GoHomeAndSleepTilRested

class Miner(BaseGameEntity):
    comfortLevel = 5
    maxNuggets = 3
    thirstLevel = 5
    tirednessThreshold = 5

    def __init__(self):
        super().__init__(BaseGameEntity.nextId)
        self.currentState = GoHomeAndSleepTilRested()
        self.location = Location.shack
        self.goldCarried = 0
        self.moneyInBank = 0

        # the higher the value, the thirstier the miner
        self.thirst = 0

        # the higher the value, the more tired the miner
        self.fatigue = 0

    def update(self):
        self.thirst += 1
        if self.currentState != None:
            self.currentState.execute(self)

    def changeLocation(self, location):
        self.location = location

    def changeState(self, newState):
        # call the exit method of the existing state
        self.currentState.exit(self)

        # change
        self.currentState = newState

        # call
        self.currentState.enter(self)

    def addToGoldCarried(self, amount):
        self.goldCarried += amount

        if self.goldCarried < 0:
            self.goldCarried = 0

    def arePocketsFull(self):
        return self.goldCarried >= Miner.maxNuggets;

    def addToWealth(self, amount):
        self.moneyInBank += amount
        if self.moneyInBank < 0:
            self.moneyInBank = 0

    def decreaseFatigue(self):
        self.fatigue -=1

    def increaseFatigue(self):
        self.fatigue += 1

    def isFatigued(self):
        return self.fatigue > Miner.tirednessThreshold

    def isThirsty(self):
        return self.thirst > Miner.thirstLevel

    def setGoldCarried(self, amount):
        self.goldCarried = amount

    def buyAndDrinkAWhiskey(self):
        self.thirst = 0
        self.addToWealth(-2)
