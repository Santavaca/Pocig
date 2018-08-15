class FlatFilePersister():
    def __init__(self, csv):
        self.csv = csv

    def persistfile(self):
        print('persistfile called with ' + self.csv)


if __name__ == '__main__':
    csv = 'value,value,value'
    flatfilepersister = FlatFilePersister(csv)
    flatfilepersister.persistfile()