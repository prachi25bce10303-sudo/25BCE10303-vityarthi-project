import csv

CSV_FILE = 'patients.csv'

def load_patients():
    patients = []
    try:
        with open(CSV_FILE, mode='r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['age'] = int(row['age'])
                row['bp_sys'] = int(row['bp_sys'])
                row['bp_dia'] = int(row['bp_dia'])
                row['sugar'] = float(row['sugar'])
                row['bmi'] = float(row['bmi'])
                patients.append(row)
    except FileNotFoundError:
        pass
    return patients

def save_patients(patients):
    with open(CSV_FILE, mode='w', newline='') as f:
        fieldnames = ['id', 'name', 'age', 'bp_sys', 'bp_dia', 'sugar', 'bmi']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for patient in patients:
            writer.writerow(patient)
