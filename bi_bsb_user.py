from bsb_login import bisb_pl, bibsb_home


def bibs_login():
    while True:
        option = input("Choose Your Option: ")
        if option == "P":
            username = input("Enter Your Username: ")
            print(f"Hi, {username}")
            password = input("Enter Your Password: ")
            return password

        if option == "R":
            pl_info_reg()
            hit_type()
            abs()
            bisb_pl()


def pl_info_reg():
    username = input("\nCreate a Username: ")
    password = input("\nCreate Password: ")
    pl_first_name = input("\nEnter Your First Name: ")
    pl_mid_name = input("\nEnter Your Middle Initial: ")
    pl_last_name = input("\nEnter Your Last Name: ")
    pl_age = input("\nWhat is your age?: ")
    pl_school = input("\nWhat school do / did you attend: ")
    pl_graduation_yr = input("\nWhat year do you graduate?:\n")
    print(f"Name: {pl_first_name} {pl_mid_name}. {pl_last_name}")
    print(f"Username: {username} Password: {password}")
    print(f"Age: {pl_age}")
    print(f"School: {pl_school} Graduation Year: {pl_graduation_yr}")


def hit_type():
    small_ball = "Small Ball"
    line_drive = "Line Drive"
    power = "Power"
    while True:
        hit_type = input(
            "\nWhich hitting type best describes you?:\n1. small ball\n2. Line Drive\n3. Power\n")

        if hit_type == ("1"):
            print(f"Your hitting style is {small_ball}")

        elif hit_type == ("2"):
            print(f"Your hitting style is {line_drive}")

        elif hit_type == ("3"):
            print(f"Your hitting style is {power}")
        break


def abs():
    global at_bats
    global hits
    at_bats = input(f"\nHow may at bats have you had this season? ")
    hits = input(f"\nHow many hits did you have this season? ")
    avg = int(hits) / int(at_bats)
    print(f"\nYour batting avg is: {avg}")
    print(f"\nThank you for registering with Big Iron Baseball: ")


def new_ab():
    new_at_bats = input("\nHow many At Bats did you have last game?: ")
    print(new_at_bats)
    total_at_bats = new_at_bats + at_bats
    new_hits = input("\nHow many HITS did you have last game?: ")
    total_hits = new_hits + hits
    new_avg = int(total_hits) / int(total_at_bats)
    print(total_at_bats)
    print(total_hits)
    print(float(new_avg))


"""def coaches(balance):
    amount = input("Enter amount to deposit")
    new_balance = float(balance) + float(amount)
    return new_balance


def fanatics():

    # the argument balance is the user's balance at this exact moment
    while True:
        amount = input("\nEnter amount to withdraw: ")
        current_balance = float(balance) - float(amount)

        if float(amount) > float(balance):
            print(
                f"\nNot enough funds. Please try again.\n\nYour balance is {float(balance)}")
            return float(balance)

        else:
            print(f"\nYour current balance is {float(current_balance)}")
            return float(current_balance)
            break


def fanatics(name):
    print(f"Goodbye {name}!\n")

def apparel():
    
def sports_perf():

def events():

def bsb_news():"""
