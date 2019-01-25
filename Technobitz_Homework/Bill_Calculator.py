def gst_add(total_bill):  # Function to include gst in the bill
    return total_bill + (total_bill * 0.18)


def tip_add(total_bill):  # Function to add tip
    return total_bill + (total_bill * 0.2)


bill = float(input("Enter the total bill :"))  # Taking user input for bill
bill = gst_add(bill)  # Adding gst(Function call)
print("Total Bill :", bill)
tip_flag = input("To give tip press Y else press N").upper()  # To check if user wants to give tip
if tip_flag == "Y":
    bill = tip_add(bill)
print("Total Bill :", bill)
