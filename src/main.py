import csv, logging, time

from datetime import datetime as dt
from unidecode import unidecode as ud

class Person:
    def __init__(self, id, first_name, last_name, street, zip, city, type, last_check_in, job, phone, company):
        self.id = id
        self.first_name = self._remove_first_name_accent(first_name)
        self.last_name = self._remove_last_name_accent(last_name)
        self.street = self._is_valid_street(street)
        self.zip = self._is_valid_zip(zip)
        self.city = self._is_valid_city(city)
        self.type = type
        self.last_check_in = self._is_valid_last_check_in(last_check_in)
        self.job = job
        self.phone = phone
        self.company = self._is_valid_company(company)

        self._has_fields_data()

    def _remove_first_name_accent(self, first_name):
        return ud(first_name, "utf-8")

    def _remove_last_name_accent(self, last_name):
        return ud(last_name, "utf-8")

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


def read_file(list_of_people: list[None]) -> None:
    """Receives a blank list and reads data from a csv file.

    Args:
        list_of_people: An empty list.

    Returns:
        None
    """

    with open("data.csv", mode = "r", encoding = "utf8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        index = 0
        for row in csv_reader:
            append_data(index, row, list_of_people)
            index += 1

def append_data(index: int, row: dict[str, str], list_of_people: list[Person]) -> None:
    """Receives a row, as well as a list of people and creates a Person object, which it
    then appends to the given list.

    Args:
        index: Current line count.
        row: A row (dict[str, str]) of data, containing the columns as well as their respective values from the row.
        list_of_people: An list of people.

    Returns:
        None
    """

    person = Person((index + 1), row["First Name"], row["Last Name"], row["Street"], row["Zip"], row["City"], row["Type"], \
                     row["Last Check-In Date"], row["Job"], row["Phone"], row["Company"])
    
    list_of_people.append(person)

def earliest_check_in(list_of_people: list[Person]) -> None:
    """Receives a list of person objects and prints out the earliest checked in person.

    Args:
        list_of_people: A list of people.

    Returns:
        None
    """

    sorted_list_of_people = sorted(list_of_people, key = lambda person: person.last_check_in if (person.last_check_in) else dt.now())
    print(f"\nThe customer with the earliest check-in is: {sorted_list_of_people[0].first_name} {sorted_list_of_people[0].last_name}")

def latest_check_in(list_of_people: list[Person]) -> None:
    """Receives a list of person objects and prints out the latest checked in person.

    Args:
        list_of_people: A list of people.

    Returns:
        None
    """
    
    unix_dt = dt.strptime("01/01/1970", "%d/%m/%Y")
    sorted_list_of_people = sorted(list_of_people, key = lambda person: person.last_check_in if (person.last_check_in) else unix_dt, reverse=True)

    print(f"The customer with the latest check-in is: {sorted_list_of_people[0].first_name} {sorted_list_of_people[0].last_name}")    

def full_name_alphabetically(list_of_people: list[Person]) -> None:
    """Receives a list of person objects and prints out all of the people, sorted in alphabetical order by their full name.

    Args:
        list_of_people: A list of people.

    Returns:
        None
    """

    sorted_list_of_people = sorted(list_of_people, key = lambda person: (person.first_name, person.last_name))

    print("\nFull Names, in alphabetical order:")

    for person in sorted_list_of_people:
        print(person.first_name + " " + person.last_name)

def companies_users_jobs(list_of_people: list[Person]) -> None:
    """Receives a list of person objects and prints out all of the people, sorted by companies user's jobs.

    Args:
        list_of_people: A list of people.

    Returns:
        None
    """

    sorted_list_of_people = sorted(list_of_people, key = lambda person: (person.company, person.job))

    print("\nCompanies user's jobs, in alphabetical order:")

    for person in sorted_list_of_people:
        print(person.company + " " + person.job)

def main():
    t_start = time.time()
    list_of_people: list[Person] = []

    read_file(list_of_people)
    earliest_check_in(list_of_people)
    latest_check_in(list_of_people)
    full_name_alphabetically(list_of_people)
    companies_users_jobs(list_of_people)

    t_end = time.time()
    print("\nThe total running time for main is: " + str(t_end - t_start))


if __name__ == "__main__":
    main()