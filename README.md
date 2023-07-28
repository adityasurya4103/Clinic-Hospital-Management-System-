# Clinic_Hospital_Management

IMPORTANT INSTRUCTIONS HOW TO RUN THE PROJECT :-


Run the main.py file 
In login page 
  user name: abc 
  password : pqr

Create a database for the students in mysql commandline using following Commands:

1.  CREATE DATABASE PATIENTS_DB;

2.   USE PATIENTS_DB;
   
3.  CREATE TABLE `patients` (
  `MOBILE` varchar(200) NOT NULL,
  `NAME` varchar(200) NOT NULL,
  `DOB` varchar(200) NOT NULL,
  `HISTORY` varchar(200) NOT NULL,
  `MEDICINES` varchar(200) NOT NULL,
   PRIMARY KEY (`MOBILE`)
);


Description of the project :
The project is build using Python and tkinter and uses mysql as a database
Welcome to the Clinic/Hospital Management System! Our system is designed to efficiently store and manage patient data, as well as handle appointment bookings and cancellations. Here are the key features:

1. Patient Database:
   - The system maintains a comprehensive patient database.
   - Each patient's record includes the following information:
     - Mobile number (primary key)
     - Name
     - Date of Birth
     - Medical History
     - Prescribed Medicines

2. Patient Management:
   - You can easily add new patients to the database, providing all the necessary details.
   - Select and view specific patient records when required.
   - Search for patients based on their mobile number, name, or other criteria.
   - Delete patient records if needed (e.g., upon request or when a patient is discharged).

3. Appointment Management:
   - Our system also handles appointment scheduling and cancellations.
   - Patients can book appointments at their preferred date and time.
   - In case of schedule changes or conflicts, patients can cancel their appointments.
   - You can search for upcoming or past appointments for any patient.

Our Clinic/Hospital Management System is designed to streamline administrative tasks, improve patient record-keeping, and enhance the overall appointment management process. It ensures that essential patient information and appointment details are readily accessible and efficiently managed. If you have any questions or need assistance, feel free to ask!
