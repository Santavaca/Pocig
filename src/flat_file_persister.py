class FlatFilePersister():
    def __init__(self, csv):
        self.csv = csv

    def persistfile(self):
        print('persistfile called with ' + self.csv)
        # TODO: connect to google drive and save file


if __name__ == '__main__':
    csv = 'value,value,value'
    persister = FlatFilePersister(csv)
    persister.persistfile()