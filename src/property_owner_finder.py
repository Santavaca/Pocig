import sys

class PropertOwnerFinder():
    def __init__(self, address):
        self.address = address
        print('PropertyOwnerFinder instantiated')

    def findowner(self):
        rule_runner = RuleRunner(self.address)
        enriched_address = rule_runner.runrules()

        consolidator = OwnerConsolidator(enriched_address)
        consolidated_address = consolidator.mergeowners()

        file_formater = FileFormater()
        csv = file_formater.createcsv(consolidated_address)

        persister = FlatFilePersister(csv)
        persister.persistfile()


if __name__ == '__main__':
    address1 = sys.argv[1]
    property_owner_finder = PropertOwnerFinder(address1)
    property_owner_finder.findowner()