from enum import Enum
from collections import defaultdict, deque


class DoctorType(Enum):
    CARDIOLOGIST = 1
    DERMATOLOGIST = 2
    SURGEON = 3


class Doctor:
    def __init__(self, id, name, doctorType) -> None:
        self.id = id
        self.name = name
        self.doctorType = doctorType
        self.slot = set()
        self.booked_slot = []


class Patient:
    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name
        self.booked_slot = []


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
        self.patient = patient
        self.doctor = doctor
        self.start = start
        self.end = end


if __name__ == "__main__":
    doctorList = []
    patientList = []
    booking = {}
    waiting = defaultdict(deque)

    def addFreeSlot(doctor, start, end):
        if start > end:
            raise Exception("start can't be more than end")
        if end - start != 0.5:
            raise Exception("time slot can only be 30 minutes")

        for doc in doctorList:
            if doc == doctor:
                doctor.slot.add((start, end))

    def showAvailBySpeciality(doctorType):
        for doc in doctorList:
            if doc.doctorType == doctorType:
                for slot in doc.slot:
                    print(doc.name, slot[0], slot[1])

    def bookAppointment(patient, doctor, start):
        for doc in doctorList:
            if doc == doctor:
                for slot in doc.slot:
                    if slot[0] == start:
                        doc.slot.discard((start, start + 0.5))
                        booking[len(booking)] = Booking(id=len(booking), patient=patient, doctor=doctor, start=start, end=start + 0.5)
                        patient.booked_slot.append(booking[len(booking) - 1])
                        doctor.booked_slot.append(booking[len(booking) - 1])
                        print("Booking done")
                        return
                waiting[doctor.id].append(Waiting(id=len(waiting[doctor.id]), patient=patient, doctor=doctor, start=start, end=start + 0.5))
                print("Added to waiting list")
                return
        print("Doctor not found")

    def cancelBookingById(bookingId):
        if bookingId in booking:
            booking_info = booking[bookingId]
            doctor = booking_info.doctor
            start = booking_info.start
            end = booking_info.end
            booking.pop(bookingId)
            doctor.slot.add((start, end))
            if len(waiting[doctor.id]) > 0:
                patient_waiting = waiting[doctor.id].popleft()
                new_booking = Booking(id=len(booking), patient=patient_waiting.patient, doctor=patient_waiting.doctor, start=patient_waiting.start, end=patient_waiting.end)
                booking[len(booking)] = new_booking
                patient_waiting.patient.booked_slot.append(new_booking)
                doctor.booked_slot.append(new_booking)
                print("Booking moved from waiting list")
        else:
            print("Booking not found")

    def showPatientBookedSlot(patient):
        for _patient in patientList:
            if _patient == patient:
                for book in patient.booked_slot:
                    print(book.id, book.doctor.name, book.start, book.end)

    def showDoctorBookedSlot(doctor):
        for _doctor in doctorList:
            if _doctor == doctor:
                for book in doctor.booked_slot:
                    print(book.id, book.patient.name, book.start, book.end)

    # Sample Data and Usage

    doctor1 = Doctor(id=1, name="Curious", doctorType=DoctorType.CARDIOLOGIST)
    doctorList.append(doctor1)

    patient1 = Patient(id=1, name="PatientA")
    patientList.append(patient1)

    addFreeSlot(doctor1, start=9, end=9.5)
    addFreeSlot(doctor1, start=9.5, end=10)
    addFreeSlot(doctor1, start=12.5, end=13)
    addFreeSlot(doctor1, start=16, end=16.5)

    bookAppointment(patient1, doctor1, start=9)
    bookAppointment(patient1, doctor1, start=9.5)

    showAvailBySpeciality(DoctorType.CARDIOLOGIST)
    showPatientBookedSlot(patient1)
    showDoctorBookedSlot(doctor1)

    cancelBookingById(0)
    showDoctorBookedSlot(doctor1)
