from risk_evaluator import calculate_risk

def show_report(patients):
    id = input("Enter patient ID to view report: ")
    for p in patients:
        if p['id'] == id:
            print("\n--- Patient Report ---")
            for key in p:
                print(f"{key.capitalize()}: {p[key]}")
            print("Risk status:", calculate_risk(p))
            return
    print("Patient not found.")

def list_high_risk(patients):
    print("\n--- High Risk Patients ---")
    found = False
    for p in patients:
        if "HIGH RISK" in calculate_risk(p):
            print(f"{p['name']} (ID: {p['id']}) - {calculate_risk(p)}")
            found = True
    if not found:
        print("No high-risk patients found.")
