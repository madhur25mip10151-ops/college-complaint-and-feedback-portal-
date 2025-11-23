# college-complaint-and-feedback-portal-
📘 College Complaint & Feedback Portal

A simple Python-based terminal application that allows college students to submit complaints and feedback, and lets the admin view all submissions.
This project is beginner-friendly and perfect for assignments or small mini-projects.

🚀 Features

Submit complaints with optional name

Submit feedback with rating (1–5)

View all submitted complaints

View all submitted feedback

Anonymous submissions supported

Very easy to understand (no database, no files)

🛠 Technologies Used

Python 3

Basic loops, lists, and dictionaries

📂 Project Structure
project/
│
├── portal.py       # Main Python Program
└── README.md       # Documentation

▶ How to Run

Install Python 3

Save the program in a file named portal.py

Open Terminal / CMD

Run:

python portal.py

📜 Program Flow

Once the program runs, the user will see this menu:

===== College Complaint & Feedback Portal =====
1. Submit Complaint
2. Submit Feedback
3. View All Complaints
4. View All Feedback
5. Exit


Users can choose options by entering numbers 1–5.

🧩 How the Code Works
1. Storing Data

All complaints and feedback are stored in lists:

complaints = []
feedbacks = []


Each entry is stored as a dictionary:

{
  "name": "Anonymous",
  "department": "CSE",
  "complaint": "Classroom projector not working"
}

📝 Example Complaint Entry
Name: Anonymous  
Department: CSE  
Complaint: Need more lab PCs  

⭐ Sample Output
--- Submit Complaint ---
Enter your name (or leave blank for anonymous): 
Enter your department: CSE
Enter your complaint: Need more lab PCs
Complaint submitted successfully!

📌 Notes

Data is not saved permanently. It resets when the program is closed.

You can request a version that saves data to a file or database.
