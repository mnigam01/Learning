
# doctor
# doctorType
# patient
# slot  (maybe don't need this one)
# booking
# waiting

from enum import Enum


class DoctorType(Enum):
    CARDIOLOGIST = 1
    DERMATOLOGIST = 2
    SURGEON = 3

class Doctor:
    def __init__(self, id, name, type) -> None:
        self.id = id
        self.name = name
        self.type = type
        self.slot = set()
        self.booked_slot = set()
        
class Patient:
    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name
        self.booked_slot = set()

class Booking:
    def __init__(self, id, patient, doctor, start, end) -> None:
        self.id = id
        self.patient = patient
        self.doctor = doctor
        self.start = start
        self.end = end

class Waiting:
    def __init__(self, id, patient, doctor, start, end) -> None:
        self.id = id
        self.pateint = patient
        self.doctor = doctor
        self.start = start
        self.end = end



from collections import defaultdict, deque


if __name__=="__main__":
    doctorList = []
    doctor = Doctor(id = 1, name = "Curious", type=DoctorType.CARDIOLOGIST)
    doctorList.append(doctor)

    def addFreeSlot(doctor, start, end):
        if (start>end):
            raise Exception("start can't be more than end")
        if (end-start!=0.5):
            raise Exception("time can't be anything by 30 minutes")

        for doc in doctorList:
            if doc==doctor:
                # doctor.slot.append([start, end])  # treating slot as list
                doctor.slot.add((start, end))  # treating slot as dict

    def showAvailBySpeciality(type):
        for doc in doctorList:
            if doc.type==type:
                for slot in doc.slot:
                    print(doc.name, slot[0], slot[1])  # maybe this line can be changed


    booking = dict()
    waiting = defaultdict(deque)
    def bookAppointment(patient, doctor, start):
        for doc in doctorList:
            if doc==doctor:
                
                for slot in doc.slot:
                    print(slot, start)
                    if slot[0]==start:
                        doc.slot.discard((start,start+0.5))
                        booking[len(booking)] = Booking(id=len(booking), patient = patient, doctor=doctor, start = start, end = start+0.5)
                        doctor.booked_slot.add(booking[len(booking)-1])
                        patient.booked_slot.add(booking[len(booking)-1])
                        print("booking done")
                        return 
                waiting[doctor.id].append(Waiting(id=1234, patient = patient, doctor = doctor, start = start, end = start+ 0.5))
                
            
    def cancelBookingId(booking):
        Booking.discard(booking.id)
        booking.patient.booked_slot.discard(booking)
        booking.doctor.booked_slot.discard(booking)
        if len(waiting[booking.doctor.id])>0:
            patient_waiting = waiting[booking.doctor.id].popleft()
            booking[len(booking)] = Booking(id=len(booking), patient = patient_waiting.patient, doctor=patient_waiting.doctor, start = patient_waiting.start, end = patient_waiting.end)
            doctor.booked_slot.add(booking[len(booking)-1])
            patient.booked_slot.add(booking[len(booking)-1])

        print("booking cancelled")

    


    # addFreeSlot(doctor, start = 9, end=10)
    addFreeSlot(doctor, start = 9.5, end=10)
    addFreeSlot(doctor, start = 12.5, end=13)
    addFreeSlot(doctor, start = 16, end=16.5)

    patientList = []
    patient = Patient(id = 1, name="PatientA")
    patientList.append(patient)

    def showPatientBookedSlot(patient):
        for _pateint in patientList:
            if _pateint==patient:
                for booking in patient.booked_slot:
                    print(booking.id, booking.doctor.name, booking.start, booking.end)
                
    def showDoctorBookedSlot(doctor):
        for _doctor in doctorList:
            if _doctor==doctor:
                for booking in doctor.booked_slot:
                    print(booking.id, booking.patient.name, booking.start, booking.end)

    
    # showAvailBySpeciality(DoctorType.CARDIOLOGIST)
    bookAppointment(patient, doctor, 9.5)
    # print(booking)
    # print(doctor.booked_slot)
    showDoctorBookedSlot(doctor)
    print(doctor.slot)





