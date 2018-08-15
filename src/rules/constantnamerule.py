class ConstantNameRule():
    def __init__(self, address): # by convention, all rules will have an init method that accepts and address
        self.address = address

    def run(self): # by convention all rules will have a run method that returns an owner
        owner = Owner(first_name = 'constant', last_name = 'name')
        return owner