def add_patient(patients):
    id = input("Enter patient ID: ")
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    bp_sys = int(input("Systolic BP: "))
    bp_dia = int(input("Diastolic BP: "))
    sugar = float(input("Fasting blood sugar: "))
    bmi = float(input("BMI: "))
    patient = {
        'id': id,
        'name': name,
        'age': age,
        'bp_sys': bp_sys,
        'bp_dia': bp_dia,
        'sugar': sugar,
        'bmi': bmi
    }
    patients.append(patient)
    print("Patient added!")

def update_vitals(patients):
    id = input("Enter patient ID to update: ")
    for p in patients:
        if p['id'] == id:
            print(f"Updating {p['name']}...")
            p['bp_sys'] = int(input("New Systolic BP: "))
            p['bp_dia'] = int(input("New Diastolic BP: "))
            p['sugar'] = float(input("New Fasting sugar: "))
            p['bmi'] = float(input("New BMI: "))
            print("Vitals updated!")
            return
    print("Patient not found.")
