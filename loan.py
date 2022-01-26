

def calculate_loan(account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected):
    eligible_loan_amount=0
    bank_emi_expected=0
    list=[]
    for i in str(account_number):
        list.append(i)
    if list[0]=='1' and len(list)==4:
        if account_balance>=100000:
            if salary>25000 and salary<=50000:
                bank_emi_expected=36
                eligible_loan_amount=500000
                if loan_type=="Car" and customer_emi_expected<=bank_emi_expected and eligible_loan_amount>=loan_amount_expected:
                    if loan_type=="Car":    
                        print("Account number:", account_number)
                        print("The customer can avail the amount of Rs.", eligible_loan_amount)
                        print("Eligible EMIs :", bank_emi_expected)
                        print("Requested loan amount:", loan_amount_expected)
                        print("Requested EMI's:",customer_emi_expected)
                    else:
                        print("Invalid loan type or salary")
                elif loan_type !="Car":
                    print("Invalid loan type or salary")
                else:
                    print("The customer is not eligible for the loan")
            elif salary>50000 and salary<=75000:
                bank_emi_expected=60
                eligible_loan_amount=6000000
                if loan_type=="House" and customer_emi_expected<=bank_emi_expected and eligible_loan_amount>=loan_amount_expected:
                    print("Account number:", account_number)
                    print("The customer can avail the amount of Rs.", eligible_loan_amount)
                    print("Eligible EMIs :", bank_emi_expected)
                    print("Requested loan amount:", loan_amount_expected)
                    print("Requested EMI's:",customer_emi_expected)
                elif loan_type!="House":
                     print("Invalid loan type or salary")
                else:
                    print("The customer is not eligible for the loan")
            elif salary>75000:
                bank_emi_expected=84
                eligible_loan_amount=7500000
                if loan_type=="Business" and customer_emi_expected<=bank_emi_expected and eligible_loan_amount>=loan_amount_expected:
                    print("Account number:", account_number)
                    print("The customer can avail the amount of Rs.", eligible_loan_amount)
                    print("Eligible EMIs :", bank_emi_expected)
                    print("Requested loan amount:", loan_amount_expected)
                    print("Requested EMI's:",customer_emi_expected)
                elif loan_type!="Business":
                     print("Invalid loan type or salary")
                else:
                    print("The customer is not eligible for the loan")
            else:
                print("Invalid loan type or salary")
        else:
            print("Insufficient account balance")
    else:
        if list[0]!=1 or len(list)!=4:
            print("Invalid account number")
account_no=int(input("Enter your account number: "))
Salary=int(input("Enter your salary: "))
account_bal=int(input("Enter your account balance: "))
type=input("Enter your loan type(Car,House,Business): ")
amount=int(input("Enter the loan amount expected: "))
emi=int(input("Enter the number of emi you want to repay: "))
calculate_loan(account_no,Salary,account_bal,type,amount,emi)