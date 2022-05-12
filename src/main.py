import csv, logging, locale

from datetime import datetime as dt

class Person:
    def __init__(self, id, first_name, last_name, street, zip, city, type, last_check_in, job, phone, company):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.street = self._is_valid_street(street)
        self.zip = self._is_valid_zip(zip)
        self.city = self._is_valid_city(city)
        self.type = type
        self.last_check_in = self._is_valid_last_check_in(last_check_in)
        self.job = job
        self.phone = phone
        self.company = self._is_valid_company(company)

        self._has_fields_data()

    def _is_valid_street(self, street):
        if not street:
            logging.warning(f"Row number {self.id} is missing a required field: Street")
        return street

    def _is_valid_zip(self, zip):
        if not zip:
            logging.warning(f"Row number {self.id} is missing a required field: Zip")
        return zip

    def _is_valid_city(self, city):
        if not city:
            logging.warning(f"Row number {self.id} is missing a required field: City")
        return city

    def _is_valid_last_check_in(self, last_check_in):
        if not last_check_in:
            logging.warning(f"Row number {self.id} is missing a required field: Last Check-In Date")
            return None
        return dt.strptime(last_check_in, "%d/%m/%Y")

    def _is_valid_company(self, company):
        if not company:
            logging.warning(f"Row number {self.id} is missing a required field: Company")
        return company

    def _has_fields_data(self):
        if len(self.first_name) + len(self.last_name) + len(self.street) + len(self.zip) + len(self.city) + \
            len(self.type) + len(str(self.last_check_in)) + len(self.job) + len(self.phone) + len(self.company) < 5:
                logging.warning(f"Row number {self.id} does not contain any data!")

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

def earliest_check_in(list_of_people):
    sorted_list = sorted(list_of_people, key=lambda person: person.last_check_in if (person.last_check_in) else dt.now())
    print(f"\nThe customer with the earliest check-in is: {sorted_list[0].first_name} {sorted_list[0].last_name}")

def latest_check_in(list_of_people):
    unix_dt = dt.strptime("01/01/1970", "%d/%m/%Y")
    sorted_list = sorted(list_of_people, key=lambda person: person.last_check_in if (person.last_check_in) else unix_dt, reverse=True)
    print(f"The customer with the latest check-in is: {sorted_list[0].first_name} {sorted_list[0].last_name}")    

def full_name_alphabetically(list_of_people):
    sorted_list = sorted(list_of_people, key=lambda person: (person.first_name, person.last_name))

    print("\nFull Names, in alphabetical order:")

    for item in sorted_list:
        print(item.first_name + " " + item.last_name)

def companies_users_jobs(list_of_people):
    print("")


def main():
    list_of_people = []

    read_file(list_of_people)
    earliest_check_in(list_of_people)
    latest_check_in(list_of_people)
    full_name_alphabetically(list_of_people)
    companies_users_jobs(list_of_people)

if __name__ == "__main__":
    main()
    locale.setlocale(locale.LC_ALL, "es_ES")