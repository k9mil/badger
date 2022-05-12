import csv, logging, time, locale

from datetime import datetime as dt
from unidecode import unidecode as ud

class Customer:
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
            len(self.type) + len(self.job) + len(self.phone) + len(self.company) < 1 and self.last_check_in == None:
                logging.warning(f"Row number {self.id} does not contain any data!")

    def full_name(self):
        return self.first_name + " " + self.last_name


def read_file(list_of_customers: list[None]) -> None:
    """Receives a blank list and reads data from a csv file.

    Args:
        list_of_customers: An empty list.

    Returns:
        None
    """

    with open("data.csv", mode = "r", encoding = "utf8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        index = 0
        for row in csv_reader:
            append_data(index, row, list_of_customers)
            index += 1

def append_data(index: int, row: dict[str, str], list_of_customers: list[Customer]) -> None:
    """Receives a row, as well as a list of people and creates a Customer object, which it
    then appends to the given list.

    Args:
        index: Current line count.
        row: A row (dict[str, str]) of data, containing the columns as well as their respective values from the row.
        list_of_customers: A list of customer.

    Returns:
        None
    """

    customer = Customer((index + 1), row["First Name"], row["Last Name"], row["Street"], row["Zip"], row["City"], row["Type"], \
                     row["Last Check-In Date"], row["Job"], row["Phone"], row["Company"])
    
    list_of_customers.append(customer)

def earliest_check_in(list_of_customers: list[Customer]) -> None:
    """Receives a list of customer objects and prints out the earliest checked in customer.

    Args:
        list_of_customers: A list of customers.

    Returns:
        None
    """

    sorted_list_of_customers = sorted(list_of_customers, key = lambda customer: customer.last_check_in if (customer.last_check_in) else dt.now())
    print(f"\nThe customer with the earliest check-in is: {sorted_list_of_customers[0].full_name()}")

def latest_check_in(list_of_customers: list[Customer]) -> None:
    """Receives a list of customer objects and prints out the latest checked in customer.

    Args:
        list_of_customers: A list of people.

    Returns:
        None
    """
    
    unix_dt = dt.strptime("01/01/1970", "%d/%m/%Y")
    sorted_list_of_customers = sorted(list_of_customers, key = lambda customer: customer.last_check_in if (customer.last_check_in) else unix_dt, reverse = True)

    print(f"The customer with the latest check-in is: {sorted_list_of_customers[0].full_name()}")    

def full_name_alphabetically(list_of_customers: list[Customer]) -> None:
    """Receives a list of customer objects and prints out all of the people, sorted in alphabetical order by their full name.

    Args:
        list_of_customers: A list of people.

    Returns:
        None
    """
    
    full_list = []
    locale.setlocale(locale.LC_ALL, "")

    for customer in list_of_customers:
        if customer.first_name and customer.last_name:
            full_list.append(customer.full_name())

    full_list.sort(key=locale.strxfrm)

    print("\nFull Names, in alphabetical order:")

    for customer in full_list:
        print(customer)

def companies_users_jobs(list_of_customers: list[Customer]) -> None:
    """Receives a list of customer objects and prints out all of the people, sorted by companies user's jobs.

    Args:
        list_of_customers: A list of people.

    Returns:
        None
    """

    sorted_list_of_customers = sorted(list_of_customers, key = lambda customer: (customer.company, customer.job))

    print("\nCompanies user's jobs, in alphabetical order:")

    for customer in sorted_list_of_customers:
        print(customer.company + " " + customer.job)

def main():
    t_start = time.time()
    list_of_customers: list[Customer] = []

    read_file(list_of_customers)
    earliest_check_in(list_of_customers)
    latest_check_in(list_of_customers)
    full_name_alphabetically(list_of_customers)
    companies_users_jobs(list_of_customers)

    t_end = time.time()
    print("\nThe total running time for main is: " + str(t_end - t_start))


if __name__ == "__main__":
    main()