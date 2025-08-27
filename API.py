from fastapi import FastAPI , Path, HTTPException
import json

app = FastAPI()

# Function to load patients.json
def load_data():
    with open("patients.json","r") as f:
        data = json.load(f)
        return data

@app.get("/")
def hello():
    return {"message": "Patient Management System API"}

@app.get("/about")
def about():
    return {"message": "A fully functional API to manage your patient records."}

@app.get("/see")
def view_patients():
    data = load_data()
    return data

@app.get('/patient/{pati'
         'ent_id}')
def view_patient(patient_id: str = Path(..., description='ID of the patient in the Database.',example='P001')):
    # load all the patients
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail='Patient not found.')
