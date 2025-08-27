from pydantic import BaseModel
from typing import List, Dict, Optional


class patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool = False
    allergies:Optional[list[str]] = None
    contact_details: Dict[str, str]

def insert_patient_data(patient: patient):
    print("Patient Information")
    print(f"Name: ", patient.name)
    print(f"Age:", patient.age)
    print(f"Weight: ", patient.weight)
    print(f"Contact Details: ", patient.contact_details)
    print('inserted')

def update_patient_data(patient: patient):
    print("Patient Information")
    print(f"Name: ",patient.name)
    print(f"Age:",patient.age)
    print(f"Weight: ",patient.weight)
    print(f"Contact Details: ", patient.contact_details)
    print("update")

patient_info = {'name':'Hiro','age':30 ,'weight': 74.2,
                'contact_details':{'email':'abs@gmail.com','phone':'19388494'} }
patient1 = patient(**patient_info)
update_patient_data(patient1)