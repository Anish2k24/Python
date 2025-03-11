import re #regular exp mod
import json #json mod

class finance_sir:
    def __init__(self):
        self.payments = []
        self.bal=0
        self.process_data()
    def add_income(self, amnt, sourceofincome):
        try:
            amnt=float(amnt)
            self.payments.append({"mode":"income","amount":amnt,"source":sourceofincome})
            self.bal+=amnt
            print(f"Added income of {amnt} from {sourceofincome}")
        except ValueError:
            print("Please enter a right amnt")
    def add_expenses(self, amnt, sourceofexpenditure):
        try:
            amnt=float(amnt)
            if amnt>self.bal:
                print("not enough money")
                return
            self.payments.append({"mode":"expenditure","amount":amnt,"source":sourceofexpenditure})
            self.bal-=amnt
            print(f"expended {amnt} on {sourceofexpenditure}")
        except ValueError:
            print("Please enter a right amnt")
    def view_conclusion(self):
        income = sum(a["amount"] for a in self.payments if a["mode"]=="income")
        expenditure = sum(a["amount"] for a in self.payments if a["mode"]=="expenditure")
        print(f"\ncurrent bal. is: {self.bal}")
        print(f"\nTotal income: {income}")
        print(f"\nTotal expenditure: {expenditure}")
    def search_payments(self, keyterm):
      pattern = re.compile(keyterm, re.IGNORECASE)  
      matchs = [a for a in self.payments if pattern.search(str(a))]  
      print("\nsearch results:")  
      for match in matchs:  
          print(match)
    def save_the_data(self):
        with open("finance_data.json", "w") as f:
         json.dump({"payments": self.payments, "bal": self.bal}, f)
    def process_data(self):
        try:
            with open("finance_data.json", "r") as f:
                data = json.load(f)
                self.payments = data["payments"]
                self.bal = data["bal"]
                
        except FileNotFoundError:
            self.payments = []
            self.bal = 0
        except json.decoder.JSONDecodeError:
            print("Data is corrupted, starting new data")
            self.payments = []
            self.bal = 0
        except Exception as e:
            print(f"An error occured: {e}")
            self.payments = []
            self.bal = 0
            
    def exit_program(self):
        self.save_the_data()
        print("saved_the_data.exit...")
        exit()
       

sir = finance_sir()

while True:
    print("\n1. add income")
    print("2. add expenditure")
    print("3. view conclusion")
    print("4. search payments")
    print("5. exit")

    choice= int(input("Enter your choice: "))
    if choice == 1:
        amnt = input("Enter the price: ")
        sourceofincome = input("Enter the sourceofincome: ")
        sir.add_income(amnt, sourceofincome)
    elif choice == 2:
        amnt = input("Enter the price: ")
        sourceofexpenditure = input("Enter the source of expenditure: ")
        sir.add_expenses(amnt, sourceofexpenditure)
    elif choice == 3:
        sir.view_conclusion()
    elif choice == 4:
        keyterm = input("Enter the keyterm: ")
        sir.search_payments(keyterm)
    elif choice == 5:
        sir.exit_program()
    else:
        print("Please enter a right choice")
        continue
print("thanks for using")