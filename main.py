from hospital import Hospital
from doctor import Doctor
from reception import Reception

hospital = Hospital('city hospital')
d1 = Doctor('malith', '1234')
d2 = Doctor('kamal', '123')

r1 = Reception('rec1', '1234')
r2 = Reception('rec2', '123')

hospital.add_doctor(d1)
hospital.add_doctor(d2)

hospital.add_receptionist(r1)
hospital.add_receptionist(r2)


hospital.login()
