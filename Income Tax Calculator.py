Total_Income = input("Enter your Total Annual income :  ")

print("your Total Annual income is : {}".format(Total_Income))

investment = input("user have investment then 'S' or 'N':  ")

if investment == "N":

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

elif investment == "S":

    Total_Income = int(Total_Income)

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

    # (LIC=input("Enter the amount you invest for LIC : ")
   # National_Saving_Certificate = input("Enter the amount you invest for National_Saving_Certificate : ")
    #Invetsment_In_PF = input("Enter the amount you invest for Invetsment_In_PF : ")
    #Tuition_Fee = input("Enter the amount you invest for Tuition_Fee : ")
    #Mutual_Fund = input("Enter the amount you invest for Mutual_Fund : ")
    #Bank_FD = input("Enter the amount you invest for Mutual_Fund : ")
    #House_Loan_Repayment = input("Enter the amount you invest for House_Loan_Repayment : ")
    #Employee_PF = input("Enter the amount you invest for Employee_PF : ")
    #Stamp_Duty = input("Enter the amount you invest for Stamp_Duty : ")
    #Residential_Housing_Loan = input("Enter the amount you invest for Residential_Housing_Loan : ")
    #Sukanya_Samrudhhi_Scheme = input("Enter the amount you invest for Sukanya_Samrudhhi_Scheme : ")










