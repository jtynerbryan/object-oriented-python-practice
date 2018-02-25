class Inventory:
    def __init__(self):
        self.slots = []

    def add(self, item):
        self.slots.append(item)

    def __len__(self):
        return len(self.slots)

    # check __contains__ with ## item in (class instance) ##
    def __contains__(self, item):
        return item in self.slots

    ## The yield keyword works a lot like return, but doesn't end the execution of the method ##
    ## yield let's us send values back out of the function while continuing to loop through the iterable object ##

    # use __iter__ with ## for item in (class instance) ##
    def __iter__(self):
        yield from self.slots
        # for item in self.slots:
        #     yield item
