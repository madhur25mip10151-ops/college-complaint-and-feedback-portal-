

complaints = []
feedbacks = []

while True:
    print("\n===== College Complaint & Feedback Portal =====")
    print("1. Submit Complaint")
    print("2. Submit Feedback")
    print("3. View All Complaints")
    print("4. View All Feedback")
    print("5. Exit")

    choice = input("Enter your choice: ")

    
    if choice == "1":
        print("\n--- Submit Complaint ---")
        name = input("Enter your name (or leave blank for anonymous): ")
        department = input("Enter your department: ")
        complaint = input("Enter your complaint: ")

        complaints.append({
            "name": name if name else "Anonymous",
            "department": department,
            "complaint": complaint
        })

        print("Complaint submitted successfully!")

    elif choice == "2":
        print("\n--- Submit Feedback ---")
        name = input("Enter your name (optional): ")
        rating = input("Enter rating (1 to 5): ")
        feedback = input("Enter your feedback: ")

        feedbacks.append({
            "name": name if name else "Anonymous",
            "rating": rating,
            "feedback": feedback
        })

        print("Feedback submitted successfully!")

    
    elif choice == "3":
        print("\n--- All Complaints ---")
        if len(complaints) == 0:
            print("No complaints submitted yet.")
        else:
            for i, c in enumerate(complaints, 1):
                print(f"\nComplaint #{i}")
                print("Name:", c["name"])
                print("Department:", c["department"])
                print("Complaint:", c["complaint"])

    
    elif choice == "4":
        print("\n--- All Feedback ---")
        if len(feedbacks) == 0:
            print("No feedback submitted yet.")
        else:
            for i, f in enumerate(feedbacks, 1):
                print(f"\nFeedback #{i}")
                print("Name:", f["name"])
                print("Rating:", f["rating"])
                print("Feedback:", f["feedback"])

    
    elif choice == "5":
        print("Thank you for using the portal!")
        break

    else:
        print("Invalid choice. Please try again.")
