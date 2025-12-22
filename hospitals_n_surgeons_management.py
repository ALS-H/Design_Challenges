"""
Docstring for hospitals_n_surgeons_management

Classes:
1. Surgeon (abstract/base class) [Types:SeniorSurgeon, JuniorSurgeon]
2. Hospital
3. Patient
4. Ward
5. Operation
6. SeniorSurgeon
7. JuniorSurgeon
"""


#Class Patient
class Patient:
    def __init__(self,patient_id,name):
        self.patient_id=patient_id
        self.name=name
    
#Class Ward
class Ward:
    def __init__(self,ward_no):
        self.ward_no=ward_no
        self.patients=[]
        
    def admit_patient(self,patient):
        self.patients.append(patient)
    
    #question 3: List all the patient admitted to a ward. 
    def get_admitted_patients(self):
        return self.patients
    
#Class Hospital
class Hospital:
    def __init__(self,hospital_name):
        self.hospital_name=hospital_name
        self.wards=[]
        self.surgeons=[]
        
    def add_ward(self,ward):
        self.wards.append(ward)
    
    def get_wards(self):
        return self.wards
    
    def add_surgeon(self,surgeon):
        self.surgeons.append(surgeon)
    
    #question 1:  Total number of patient being operated 
    def total_patients_operated(self,surgeons):
        count = 0
        for surgeon in self.surgeons:
            count += len(surgeon.operations)
        return count
        
#Abstract Class Surgeon
from abc import ABC, abstractmethod

class Surgeon(ABC):
    def __init__(self,surgeon_id,name):
        self.surgeon_id=surgeon_id
        self.name=name
        self.operations=[]
    
    def add_operation(self,operation):
        self.operations.append(operation)
    
    #question 2: List all the patient being operated by a surgeon 
    def get_operated_patients(self):
        return [op.patient for op in self.operations]
    
    @abstractmethod
    def get_type(self):
        pass

#Class SeniorSurgeon
class SeniorSurgeon(Surgeon):
    def get_type(self):
        return "Senior"
    
class JuniorSurgeon(Surgeon):
    def get_type(self):
        return "Junior"
    
    
#Class Operation
class Operation:
    def __init__(self,surgeon,patient):
        self.surgeon=surgeon
        self.patient=patient
        surgeon.add_operation(self)
    
    def get_patient(self):
        return self.patient
    
    def get_surgeon(self):
        return self.surgeon
    
    
if __name__=="__main__":
    # Patients
    p1 = Patient(1, "Alice")
    p2 = Patient(2, "Bob")
    p3 = Patient(3, "Charlie")

    # Ward
    ward1 = Ward(101)
    ward1.admit_patient(p1)
    ward1.admit_patient(p2)
    ward2= Ward(10)
    ward2.admit_patient(p3)

    # Hospital
    hospital = Hospital("City Hospital")
    hospital.add_ward(ward1)

    # Surgeons
    s1 = SeniorSurgeon(1, "Dr. Rao")
    s2 = JuniorSurgeon(2, "Dr. Mehta")

    hospital.add_surgeon(s1)
    hospital.add_surgeon(s2)

    # Operations
    Operation(s1, p1)
    Operation(s1, p2)
    Operation(s2, p3)

    # -------- OUTPUTS --------

    # 1. Total number of patients being operated
    print("Total patients operated:",
        hospital.total_patients_operated([s1, s2]))

    # 2. List patients operated by a surgeon
    print("\nPatients operated by Dr. Rao:")
    for p in s1.get_operated_patients():
        print(p.name)

    # 3. List patients admitted to a ward
    print("\nPatients admitted in Ward 10:")
    for p in ward2.get_admitted_patients():
        print(p.name)

