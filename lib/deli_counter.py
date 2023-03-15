katz_deli = []

def line(list):

    if len(list) == 0:
        print("The line is currently empty.")
    else:
        printed_line = []
        for index, name  in enumerate(list, start = 1):
            printed_line.append(f"{index}. {name}")
        print(f"The line is currently: {' '.join(printed_line)}")
            
    

def take_a_number(list, new_name):

    list.append(new_name)
    # called_list = []
    for index, name in enumerate(list, start = 1):
        if new_name == name:
            print(f"Welcome, {name}. You are number {index} in line.")

def now_serving(list):
    
    if len(list) > 0:
        print(f"Currently serving {list[0]}.")
        list.pop(0)
    else:
        print("There is nobody waiting to be served!")


