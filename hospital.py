class Hospital(object):
    doctors = []
    receptionist = []
    patients = []
    patient_records = []

    def __init__(self, hospital_name):
        self.hospital_name = hospital_name

    def add_doctor(self, doctor):
        self.doctors.append(doctor)
        print("Doctor added")

    def add_receptionist(self, receptionist):
        self.receptionist.append(receptionist)
        print("Receptionist added")

    def add_patient(self, patient):
        self.patients.append(patient)
        print("Successfully added patient.")

    def add_patient_record(self, patient_record):
        self.patient_records.append(patient_record)
        print("Successfully added patient record.")

    def get_patient(self, nic):
        for patient in self.patients:
            if patient.nic == nic:
                return patient

    def remove_patient(self, nic):
        for patient in self.patients:
            if patient.nic == nic:
                self.patients.remove(patient)
                print(f"Patient with nic {nic} has removed.")
                return

    def get_doctors(self):
        return self.doctors

    def login(self):
        usertype = int(input("Select your user type:\n1 - Doctor\n2 - Receptionist\n"))
        username = input("Enter your username: ")
        user = self.__is_valid_username(username, usertype)
        if not user:
            print("Invalid username")
            return self.login()
        password = input("Enter your password: ")
        if user.password == password:
            print("Logged in successfully")
            user.start_serve(self)
            self.login()
        else:
            print("Invalid password")
            return self.login()

    def __is_valid_username(self, username, usertype):
        if usertype == 1:
            user_array = self.doctors
        else:
            user_array = self.receptionist
        for user in user_array:
            if user.username == username:
                return user
