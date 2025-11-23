from data_manager import load_patients, save_patients
from patient_manager import add_patient, update_vitals
from report_generator import show_report, list_high_risk

def main():
    patients = load_patients()
    while True:
        print("\nMENU:")
        print("1. Add patient")
        print("2. Update vitals")
        print("3. Show patient report")
        print("4. List high-risk patients")
        print("5. Save and Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_patient(patients)
        elif choice == '2':
            update_vitals(patients)
        elif choice == '3':
            show_report(patients)
        elif choice == '4':
            list_high_risk(patients)
        elif choice == '5':
            save_patients(patients)
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
