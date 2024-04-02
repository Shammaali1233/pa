class PatientRecord:
    patient_record_id = 0

    def __init__(self, patient_id, date, sickness_summary, prescription):
        self.patient_record_id += 1
        self.record_id = PatientRecord.patient_record_id
        self.patient_id = patient_id
        self.date = date
        self.sickness_summary = sickness_summary
        self.prescription = prescription

    def __str__(self):
        return (f"Record ID: {self.record_id}\nDate: {self.date}\nSickness Summary: {self.sickness_summary}\n"
                f"Prescription: {self.prescription}")
