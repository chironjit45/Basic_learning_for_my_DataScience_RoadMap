from pydantic import BaseModel, EmailStr
from typing import List, Dict, Optional


class patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool = False
    allergies:Optional[list[str]] = None
    phone_num: Dict[str, str]

def insert_patient_data(patient: patient):
    print("Patient Information")
    print(f"Name: ", patient.name)
    print(f"Age:", patient.age)
    print(f"Weight: ", patient.weight)
    print(f"Phone: ", patient.contact_details)
    print('inserted')

def update_patient_data(patient: patient):
    print("Patient Information")
    print(f"Name: ",patient.name)
    print(f"Age:",patient.age)
    print(f"Weight: ",patient.weight)
    print(f"Patient Email: ",patient.email)
    print(f"Contact Details: ", patient.phone_num)
    print("update")

patient_info = {'name':'Hiro','email':'abcd@gmail.com','age':30 ,'weight': 74.2,
                'phone_num':{'phone':'19388494'}}
patient1 = patient(**patient_info)
update_patient_data(patient1)