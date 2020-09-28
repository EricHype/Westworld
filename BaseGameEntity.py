class BaseGameEntity:
    nextId = 1

    def __init__(self, id):
        self.setId(id);

    def setId(self, val):
        self.id = val;
        BaseGameEntity.nextId = self.id + 1

    def update(self):
        raise NotImplementedError()


