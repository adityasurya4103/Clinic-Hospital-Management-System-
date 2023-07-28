# Clinic_Hospital_Management

IMPORTANT INSTRUCTIONS HOW TO RUN THE PROJECT :-


Run the main.py file 
In login page 
  user name: abc 
  password : pqr

Create a database for the students in mysql commandline using following Commands:

1.  CREATE DATABASE PATIENTS_DB;

2.   USE PATIENTS_DB;

3.   
CREATE TABLE `patients` (
  `MOBILE` varchar(200) NOT NULL,
  `NAME` varchar(200) NOT NULL,
  `DOB` varchar(200) NOT NULL,
  `HISTORY` varchar(200) NOT NULL,
  `MEDICINES` varchar(200) NOT NULL,
   PRIMARY KEY (`MOBILE`)
);


This a system for clinic/hospital management. It store patients database which includes mobile number as primary key, name , date of birth , medical history and prescribed medicines. You can add , select , search and delete patients from the database. It also includes appointment management system. One can book , cancel and search the appointments.
