class Customer():
    def __init__(self,login,password,id,balance,delete=False):
        self.login = login
        self.password = password
        self.id = id
        self.bal = balance
        self.dele = delete

    def __del__(self):
        if self.dele == False:
            replace_text = str(self.login) + ":" + str(self.password) + ":" + str(self.id) + ":" + str(self.bal) + "\n"
            replace_line("data.txt", int(self.id)-1, replace_text)
        else:
            replace_text_del = "DELETED:DELETED:" + str(self.id) + ":0.0\n"
            replace_line("data.txt", int(self.id)-1, replace_text_del)

    def deposit(customer,amount):
        customer.bal += amount

    def withdraw(customer, amount):
        if not customer.bal < amount:
            customer.bal -= amount
            return True
        else:
            return False
    
    def balance(customer):
        return float(round(customer.bal,2))
    
    def to_delete(customer):
        customer.dele = True

def new_id_creator():
    with open("data.txt", encoding="utf-8", mode="r") as file:
        data = file.readlines()
        return len(data)+1

def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    try:
        lines[line_num] = text
    except IndexError:
        lines.append(text)
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

                

