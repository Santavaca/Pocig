from os import listdir
from os.path import isfile, join


class RuleRunner():
    def __init__(self, address):
        self.address = address
        self.rules_path = '/rules'  # relative path to the rules

    def runrules(self):  # TODO: add datasourceId parameter
        address_helper = AddressHelper()
        enriched_address = EnrichedAddress(self.address)
        rules = self.getrules()
        for (file) in rules:
            rule = file(self.address) # TODO: make this instantiate a class from a string of the class name
            owner = rule.run() # by convention all rules will have a run method
            enriched_address = address_helper.append(owner, enriched_address)
        return enriched_address

    def getrules(self):
        files = []
        for (dirpath, dirnames, filenames) in walk(self.rules_path):
            files.extend(filenames)
            break  # search only the level of the rules_path
        return files


if __name__ == '__main__':
    address = sys.argv[1]
    rule_runner = RuleRunner(address)
    rule_runner.runrules()
