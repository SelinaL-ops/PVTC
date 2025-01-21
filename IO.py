import csv

# Class for reading in data from CSV
class CSVIO:
    # Constructor containing parameters for filepath and data
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = []

    # Reads the CSV file and stores the data
    def readFile(self):
        try:
            with open(self.filepath, mode='r', newline='', encoding='utf-8') as file:
                csvReader = csv.DictReader(file, fieldnames=['Owner', 'Name', 'Type', 'Partner', 'Status'])
                # Read the headers
                self.headers = next(csvReader, None)
                # Read the rest of the rows
                self.data = [row for row in csvReader]
                self.data = filter(lambda x: x['Owner'] != '', self.data)
        except FileNotFoundError:
            print(f"Error: The file '{self.filepath}' was not found.")
        except Exception as e:
            print(f"Error: {e}")

    # Returns the csv data
    def getData(self):
        return self.data

    # Displays the csv data
    def displayData(self):
        print(f"Headers: {self.headers}")
        for row in self.data:
            print(row)
