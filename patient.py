from data_structures.stack import Stack
from data_structures.sorted_linkedlist import SortedLinkedList


class Patient(object):

    def __init__(self, nic, name, age, gender):
        self.nic = nic  # This is the  unique identifier for the patient.
        self.name = name
        self.age = age
        self.gender = gender
        self.prescriptions = Stack()
        self.records = SortedLinkedList()

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

    def get_prescription(self):
        self.prescriptions.remove()

    def add_prescription(self, prescription):
        self.prescriptions.insert(prescription)

    def set_name(self, new_name):
        self.name = new_name

    def set_age(self, new_age):
        self.age = new_age

    def set_gender(self, new_gender):
        self.gender = new_gender

    def add_record(self, record):
        self.records.insert(record)
        self.add_prescription(record.prescription)

    def show_summary(self):
        print(f"==Personal details==\nName: {self.name}, Age: {self.age}, Gender: {self.get_gender()}\nPrevious medical reports,")
        # Printing the medical reports.
        no_of_records = self.records.get_size()
        if no_of_records > 0:
            print(f"There are {no_of_records}")
            for i in range(no_of_records):
                print(self.records.get(i))
        else:
            print("No previous records")
