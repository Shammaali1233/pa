from patient import Patient


class Reception:
    def __init__(self, username, password):
        self.hospital = None
        self.username = username
        self.password = password

    def start_serve(self, hospital):
        self.hospital = hospital
        self.show_menu()

    def show_menu(self):
        choice = input("Select your choice: \n"
                       "1 - Add patient\n"
                       "2 - Update patient\n"
                       "3 - Schedule an appointment\n"
                       "4 - logout\n")
        if choice == "1":
            self.add_patient()
        elif choice == "2":
            self.update_patient()
        elif choice == "3":
            self.book_appointment()
        elif choice == "4":
            print("Logging out.")
            return
        self.show_menu()

    def add_patient(self):
        nic = input("Enter NIC number: ")
        name = input("Enter patient name: ")
        age = input("Enter patient age: ")
        gender = input("Enter patient gender: (M/F)")
        patient = Patient(nic, name, age, gender)
        self.hospital.add_patient(patient)

    def update_patient(self):
        nic = input("Enter NIC number of  the patient you want to update: ")
        patient = self.hospital.get_patient(nic)
        if patient:
            print("Please insert new values for the fields you need. If no change please press enter")
            name = input(f"Enter new name (current: {patient.get_name()}): ")
            if name:
                patient.set_name(name)

            age = input(f"Enter new age (current: {patient.get_age()}): ")
            if age:
                patient.set_age(age)

            gender = input(f"Enter new gender (current: {patient.get_gender()}): ")
            if gender:
                patient.set_gender(gender)
        else:
            print("Patient does not exist with that NIC number.")

    def book_appointment(self):
        patient_nic = input("Enter patient NIC: ")
        patient = self.hospital.get_patient(patient_nic)
        if not patient:
            print("Patient does not exist.")
            return
        doctors = self.hospital.get_doctors()
        print("Please select the number of the doctor you want to need the appointment.")

        for i in range(len(doctors)):
            print(f"{i + 1} - {doctors[i].username}")
        doctor_number = int(input("Please enter the number of the doctor: "))
        selected_doctor = doctors[doctor_number - 1]
        selected_doctor.add_patient_to_queue(patient)
