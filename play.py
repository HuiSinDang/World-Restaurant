#start

money = int(input("Enter your money: "))

machine_criteria = { 
    "B": "Criteria - Cooking process speed up to 40s",
    "C": "Criteria - Cooking process speed up to 30s ",
    "D": "Criteria - Cooking process speed up to 20s", 
    "E": "Criteria - Cooking process speed up to 15s"}

def confirm_upgrade(machine_options):
    print("Criteria of the available upgrade options:")
    for machine in machine_options:
        print(f"Machine {machine}: {machine_criteria[machine]}")

    confirm = input("If sure, please type YES/NO: ").upper()
    if confirm == "YES":
        if len(machine_options) == 1:
            print(f"You have successfully upgraded your machine. Your current machine is {machine_options[0]}.")
        else:
            chosen_machine = input(f"Please type your choice ({'/'.join(machine_options)}): ").upper()
            if chosen_machine in machine_options:
                print(f"You have successfully upgraded your machine. Your current machine is {chosen_machine}.")
            else:
                print("Invalid answer!!!")
    elif confirm == "NO":
        print("Thank you! ^_^")
    else:
        print("Invalid answer!!!")

if 500 <= money <= 800:
    print("You can only upgrade to machine B. Do you want to upgrade your current machine to machine B?")
    confirm_upgrade(["B"])
elif 800 <= money <= 1500:
    print("You can choose to upgrade to machine B or C. Do you want to upgrade your current machine?")
    confirm_upgrade(["B", "C"])
elif 1500 <= money <= 2000:
    print("You can choose to upgrade to machine B, C, or D. Do you want to upgrade your current machine?")
    confirm_upgrade(["B", "C", "D"])
elif money > 2200:
    print("You can choose to upgrade to machine B, C, D, or E. Do you want to upgrade your current machine?")
    confirm_upgrade(["B", "C", "D", "E"])
else:
    print("Oops, you are unable to upgrade any machine since your money is not enough!")
