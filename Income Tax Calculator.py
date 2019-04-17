def income_tax_calculaor():

    investment()


def investment():
    investment = input("user have investment then 'S' or 'N':  ")

    if investment == "N":
        tax_calculate_without_deduction()
    elif investment == "S":
        tax_calculate_with_deduction()


def tax_calculate_without_deduction():
    Total_Income = input("Enter your Total Annual income :  ")
    Total_Income = int(Total_Income)
    if Total_Income <= 250000:
        print("You don't pay any tax ")
    elif 250001 <= Total_Income <= 500000:
        A = Total_Income - 250000
        Tax1 = A * 0.05
        print("you have to pay Tax1 {}".format(Tax1))
    elif 500001 <= Total_Income <= 1000000:
        A = Total_Income - 250000
        B = A - 250000
        Tax2 = (B * 0.2) + 12500
        print("you have to pay Tax1 {}".format(Tax2))
    elif Total_Income >= 1000000:
        A = Total_Income - 250000
        B = A - 250000
        C = B - 500000
        Tax3 = (C * 0.3) + 100000 + 12500
        print("you have to pay Tax1 {}".format(Tax3))


def tax_calculate_with_deduction():

    deduction()




def deduction():
    addition = sum + NPS + medicalim
    print(addition)
    Deduction_Under_80C()
    Deduction_Under_80CCD()
    Deduction_for_medicalim()



def Deduction_Under_80C():
    print("YOur Deduction under 80C max 1,50,000")
    # Enter your dedection
    LIC = input("Enter the amount you invest for LIC : ")
    National_Saving_Certificate = input(
        "Enter the amount you invest for National_Saving_Certificate : ")
    Invetsment_In_PF = input(
        "Enter the amount you invest for Invetsment_In_PF : ")
    Tuition_Fee = input("Enter the amount you invest for Tuition_Fee : ")
    Mutual_Fund = input("Enter the amount you invest for Mutual_Fund : ")
    Bank_FD = input("Enter the amount you invest for Mutual_Fund : ")
    House_Loan_Repayment = input(
        "Enter the amount you invest for House_Loan_Repayment : ")
    Employee_PF = input("Enter the amount you invest for Employee_PF : ")
    Stamp_Duty = input("Enter the amount you invest for Stamp_Duty : ")
    Residential_Housing_Loan = input(
        "Enter the amount you invest for Residential_Housing_Loan : ")
    Sukanya_Samrudhhi_Scheme = input(
        "Enter the amount you invest for Sukanya_Samrudhhi_Scheme : ")

    list = [LIC, National_Saving_Certificate, Invetsment_In_PF, Bank_FD,
            House_Loan_Repayment, Employee_PF, Stamp_Duty,
            Residential_Housing_Loan, Sukanya_Samrudhhi_Scheme]

    print(list)

    sum = 0
    for num in list:
        sum = sum + int(num)
    print("Sum = ", sum)
    if sum <=150000:
        print(sum)
    else:
        sum=150000
        print(sum)

def Deduction_Under_80CCD():

    print("Additional deduction under 80CCD 50,000")

    NPS = int(input("Enter amount investment for NPS: "))

    if NPS <= 50000:
        print(NPS)
    else:
        NPS = 50000
        print(NPS)
def Deduction_for_medicalim():
    print("investment under section 80 D max 15,000")
    mediclaim = int(input("Enter your mediclaim amount: "))
    if mediclaim <= 15000:
        print(mediclaim)
    else:
        mediclaim = 15000
        print(mediclaim)



income_tax_calculaor()

"""
    if Total_Income <= 250000:
        print("You don't pay any tax ")

    elif 250001 <= Total_Income <= 500000:

        A = Total_Income - 250000

        A=int(A)

        if  A > 150000:

            Bank_FD = input("Enter the amount you invest for Mutual_Fund : ")

            Bank_FD = int(Bank_FD)


            B = A- Bank_FD

            Tax1 = B * 0.05

            print("you have to pay Tax1 {}".format(Tax1))

        else:

            Tax2 = A * 0.05

            print("you have to pay Tax2 {}".format(Tax2))

    elif Bank_FD < 150000:

        B = A - Bank_FD

        Tax2 = B * 0.05

        print("you have to pay Tax1 {}".format(Tax2))
"""
# (LIC=input("Enter the amount you invest for LIC : ")
# National_Saving_Certificate = input("Enter the amount you invest for National_Saving_Certificate : ")
# Invetsment_In_PF = input("Enter the amount you invest for Invetsment_In_PF : ")
# Tuition_Fee = input("Enter the amount you invest for Tuition_Fee : ")
# Mutual_Fund = input("Enter the amount you invest for Mutual_Fund : ")
# Bank_FD = input("Enter the amount you invest for Mutual_Fund : ")
# House_Loan_Repayment = input("Enter the amount you invest for House_Loan_Repayment : ")
# Employee_PF = input("Enter the amount you invest for Employee_PF : ")
# Stamp_Duty = input("Enter the amount you invest for Stamp_Duty : ")
# Residential_Housing_Loan = input("Enter the amount you invest for Residential_Housing_Loan : ")
# Sukanya_Samrudhhi_Scheme = input("Enter the amount you invest for Sukanya_Samrudhhi_Scheme : ")
