import csv

class Person:
    def __init__(self, id, first_name, last_name, street, zip, city, type, last_check_in, job, phone, company):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.street = street
        self.zip = zip
        self.city = city
        self.type = type
        self.last_check_in = last_check_in
        self.job = job
        self.phone = phone
        self.company = company

def read_file(list_of_people):
    with open("data.csv", mode = "r", encoding = "utf8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        index = 0
        for row in csv_reader:
            append_data(index, row, list_of_people)
            index += 1

def append_data(index, row, list_of_people):
    person = Person((index + 1), row["First Name"], row["Last Name"], row["Street"], row["Zip"], row["City"], row["Type"], \
                     row["Last Check-In Date"], row["Job"], row["Phone"], row["Company"])
    
    list_of_people.append(person)

def main():
    list_of_people = []

    read_file(list_of_people)

if __name__ == "__main__":
    main()