# Doc Management System
# List to store doctors
doctors = []

# Doctor Class to define the attributes of a doctor
class Doctor:
    def __init__(self, doctor_id, name, age, specialty):
        self.doctor_id = doctor_id
        self.name = name
        self.age = age
        self.specialty = specialty
    
    def __str__(self):
        return f"ID: {self.doctor_id}, Name: {self.name}, Age: {self.age}, Specialty: {self.specialty}"

# Generate a unique ID for each doctor
def generate_id():
    return len(doctors) + 1

# Create a new doctor record
def add_doctor(name, age, specialty):
    doctor_id = generate_id()
    new_doctor = Doctor(doctor_id, name, age, specialty)
    doctors.append(new_doctor)
    print(f"Doctor {name} added successfully!")

# Read and display all doctor records
def view_doctors():
    if not doctors:
        print("No Doctors Found!")
        return
    print("\nDoctor Records:")
    for doctor in doctors:
        print(doctor)

# Update a doctor's details based on doctor_id
def update_doctor(doctor_id, name, age, specialty):
    for doctor in doctors:
        if doctor.doctor_id == doctor_id:
            doctor.name = name
            doctor.age = age
            doctor.specialty = specialty
            print(f"Doctor ID {doctor_id} updated successfully!")
            return
    print("Doctor Not Found!")

# Delete a doctor record based on doctor_id
def delete_doctor(doctor_id):
    global doctors
    doctors = [doctor for doctor in doctors if doctor.doctor_id != doctor_id]
    print(f"Doctor ID {doctor_id} deleted successfully!")

# Main Menu for the D.M.S
def DoctorMenu():
    while True:
        print("\nDoctor Management System")
        print("1. Add Doctor")
        print("2. View Doctors")
        print("3. Update Doctor")
        print("4. Delete Doctor")
        print("5. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            name = input("Enter Doctor's Name: ")
            age = input("Enter Doctor's Age: ")
            specialty = input("Enter Doctor's Specialty (e.g., Cardiologist, Dentist, Neurologist): ")
            add_doctor(name, age, specialty)

        elif choice == "2":
            view_doctors()

        elif choice == "3":
            doctor_id = int(input("Enter Doctor ID to Update: "))
            name = input("Enter New Name: ")
            age = input("Enter New Age: ")
            specialty = input("Enter New Specialty: ")
            update_doctor(doctor_id, name, age, specialty)

        elif choice == "4":
            doctor_id = int(input("Enter Doctor ID to Delete: "))
            delete_doctor(doctor_id)

        elif choice == "5":
            print("Exiting... Thank you!")
            break

        else:
            print("Invalid choice, Please try again!")

# Run the Menu
DoctorMenu()
