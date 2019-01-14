from collections import OrderedDict


class Well(OrderedDict):
    def __init__(self):
        super(Well, self).__init__()
    
    
    
    
class ManyOfWell(OrderedDict):
    def __init__(self):
        super(ManyOfWell, self).__init__()

    def add_well(self, well: Well):
        self.__setitem__('Well', Well())

    def remove_well(self, well: Well):
        new_self = OrderedDict()
        for i in self.items():
            if i != well:
                new_self.__setitem__('Well', well)
            else:
                continue
        self.clear()
        super(ManyOfWell, self).__init__(new_self)