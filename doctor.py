from data_structures.queue import Queue
from datetime import datetime
from patient_record import PatientRecord


class Doctor(object):
    def __init__(self, username, password):
        self.hospital = None
        self.username = username
        self.password = password
        self.consultation_queue = Queue()

    def start_serve(self, hospital):
        self.hospital = hospital
        self.show_menu()

    def show_menu(self):
        choice = input("What would you like to do?\n"
                       "1 - get a patient in the queue\n"
                       "2 - logout\n")
        if choice == "1":
            self.get_patient()
        elif choice == "2":
            return
        else:
            print("Invalid choice.")
        self.show_menu()

    def get_patient(self):
        patient = self.consultation_queue.remove()

        def patient_menu():
            if not patient:
                print("No patients in the queue.")
                return
            choice = input("Select the option you would like to\n1 - Get a patient details."
                           "\n2 - Add new recrord\n")
            if choice == "1":
                patient.show_summary()
                patient_menu()
            elif choice == "2":
                date = datetime.now().strftime("%d/%m/%Y")
                sickness_summary = input("Describe the sickness summary: ")
                prescription = input(
                    "Enter the prescription (if you have multiple please use commas instead of newlines): ")
                record = PatientRecord(patient.nic, date, sickness_summary, prescription)
                patient.add_record(record)
            else:
                print("Invalid choice")
                patient_menu()

        patient_menu()

    def add_patient_to_queue(self, patient):
        self.consultation_queue.insert(patient)
        print(f"patient with nic {patient.nic} has added to queue of doctor {self.username}")
