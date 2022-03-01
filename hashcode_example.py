
# importing os module
import os

#Please write own your project's file path below.
path = "C:/Users/Username/..."

#input and output file names
file_names = ['a_an_example.in.txt','b_basic.in.txt', 'c_coarse.in.txt', 'd_difficult.in.txt', 'e_elaborate.in.txt']
output_files = ['Output_A.txt', 'Output_B.txt', 'Output_C.txt', 'Output_D.txt', 'Output_E.txt']

def read_file(input_filename):
    #Join the main path with input file name
    with open (os.path.join(path, input_filename), "r") as textFile:
        for line in textFile:
            pizza_order = [item.strip() for item in line.split(" ")]
            pizza_orders.append(pizza_order)
    textFile.close()

def write_file(output_filename):
    #Join the main path with input file name
    with open(os.path.join(path, output_filename), 'w+') as f:
        f.write('\n'.join([' '.join([str(item) for item in ingredients])]))
        print("File were successfully written.")
    f.close()

def get_orders():
    for i in range(len(pizza_orders)):
        for j in range(len(pizza_orders[i])):
            if (i>0):
                check_ingredient = int(pizza_orders[i][0])
                if (check_ingredient != 0) & ((i % 2) != 0):
                    if(j>0):
                        preferred_ingredients.append(pizza_orders[i][j])
                elif (check_ingredient != 0) & ((i % 2) == 0):
                    if(j>0):
                        notpreferred_ingredients.append(pizza_orders[i][j])
#
for file in range(len(file_names)):

    pizza_orders = [] #define 2D array
    preferred_ingredients = []
    notpreferred_ingredients =[]

    read_file(file_names[file])
    get_orders()

    ingredients = list(set(preferred_ingredients)-set(notpreferred_ingredients))
    ingredients.sort()
    ingredients.insert(0, len(ingredients))
    
    write_file(output_files[file])  
