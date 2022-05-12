import csv

def read_file():
    with open("data.csv", mode = "r", encoding = "utf8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        index = 0
        for row in csv_reader:
            print(row)
            index += 1

def main():
    read_file()

if __name__ == '__main__':
    main()