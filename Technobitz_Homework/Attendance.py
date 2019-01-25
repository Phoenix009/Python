def exam_eligible(attendance):  # Defining function to check eligibility
    if attendance >= 75:  # If Attendance greater than 75 then eligible
        print("Eligible")
    else:
        print("Not Eligible")  # Else not eligible


attendance = int(input("Enter the percent attendance :"))
exam_eligible(attendance)  # Function call
