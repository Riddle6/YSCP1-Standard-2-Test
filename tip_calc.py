# tip_calculator.py
# A simple tip calculator to compute tip amount and total bill

"""

***** Original Pseudo-code *****

Note:
    Some changes were made in the pseudocode.txt before I decided to list the major changes at the bottom of the file.
    This is the first version of the initial pseudo-code process.
    
-----------------------------------------------------------------------------------
BEGIN
    PRINT Welcome Statement to the Program.

    Ask the user to input their bill amount.
    Ask the user to input their tip as a percent (%).

    Calculate the tip percentage to a Float (Tip Percent / 100)

    Calculate the Total Tip (Bill * Tip Percent)
    Calculate the Total Bill (Bill + Total Tip)

    PROMPT the calculator summary.
    PRINT their Bill amount.
    PRINT their Tip amount.
    PRINT their Total Bill amount.

    PRINT a Thank You/Goodbye message for using the program.
END


FUNCTION main():
    PRINT Welcome to the Tip Calculator


    --- Ask User for Bill Amount ---
    
    LOOP forever

        IF bill_amount > 0:
            RETURN bill_amount
        ELSE
            PROMPT Negative Value error message.

        IF an EXCEPTION ValueError is triggered:
            PROMPT Invalid Value error message.

    
    --- Ask User for Tip Amount ---

    LOOP forever

        IF tip_percent > 0:
            RETURN tip_percent
        ELSE
            PROMPT Negative Value error message.

        IF an EXCEPTION ValueError is triggered:
            PROMPT Invalid Value error message.

    --- Calculate Tip Amount and Total Bill: ---
    
    total_tip = tip_percent * bill_amount
    total_bill = total_tip + bill_amount


    PROMPT Tip Calculator Summary:

    PRINT Bill Amount: + formatted bill_amount
    PRINT Tip Amount: + formatted total_tip
    PRINT Total Bill: + formatted total_bill


    PRINT Thank You for using the Tip Calculator!

"""

def main(): # Welcoming the user to the Tip Calculator program.
    print("\n----- Welcome to the Tip Calculator! -----\n")


def get_bill_amount():
    while True: # Loops forever to keep asking the user the question if an error occurrs. If none are found, the loop stops.

        try:
            bill_amount = float(input("Enter the bill amount: $"))

            if bill_amount > 0: # Returns the bill amount if it is not a negative number.
                return bill_amount
            else:
                print("\nError! The bill amount cannot be a negative number! Please try again.\n")

        except ValueError: # If the user inputs letters or symbols or something else that is not a number.
            print("\nError! This is an invalid value! Please do not enter letters or symbols.\n")
            
    
def get_tip_percent():
    while True: # Loops forever in-case if an error occurrs, and the loop stops if there are no errors found.

        try: # Calculating the tip percent to a float after the input statement.
            tip_percent = float(input("Enter the tip percentage (e.g. 10 for 10%) ")) / 100 # **Converting to decimal**

            if tip_percent > 0: # Returns the tip amount if the number is not a negative number.
                return tip_percent
            else:
                print("\nError! The tip percent cannot be a negative number! Please try again.\n")

        except ValueError: # If user inputs an invalid value and not a number/float.
            print("\nError! This is an invalid value! Please do not enter letters or symbols.\n")


def get_summary(bill_amount, tip_percent, TOTAL_BILL):

    # Calculating the Total Tip and Total Bill Amount.
    total_tip = tip_percent * bill_amount
    TOTAL_BILL = total_tip + bill_amount # Total Bill will be a constant since the result value won't change.

    # Displaying the Tip Calc. summary to the user.
    print("\n-- Tip Calculator Summary ---")
    print(f"Bill Amount: ${bill_amount:.2f}")
    print(f"Tip Amount: ${total_tip:.2f}")
    print(f"Total Bill: ${TOTAL_BILL:.2f}")

    print("\nThank you for using Tip Calculator!\n") # Thanking the user for using the program.

# Calling the functions.
TOTAL_BILL = main()
bill_amount = get_bill_amount()
tip_percent = get_tip_percent()
get_summary(bill_amount, tip_percent, TOTAL_BILL)