class State:
    def enter(self, object):
        raise NotImplementedError()
    def exit(self, object):
        raise NotImplementedError()
    def execute(self, object):
        raise NotImplementedError()