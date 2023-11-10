from data import stock


'''

warehouse_dict_state = dict()
for i in stock:
     if i["state"] in warehouse_dict_state:
          warehouse_dict_state[i["state"]]+=1
     else:
        warehouse_dict_state[i["state"]] = 1
#print(warehouse_dict_state)

warehouse_dict_category = dict()
for i in stock:
    if i["category"] in warehouse_dict_category:
        warehouse_dict_category[i["category"]]+=1
    else:
        warehouse_dict_category[i["category"]]=1
#print(warehouse_dict_category)

warehouse_dict_werehouse = dict()
for i in stock:
    if i["warehouse"] in warehouse_dict_werehouse:
        warehouse_dict_werehouse[i["warehouse"]]+=1
    else:
        warehouse_dict_werehouse[i["warehouse"]]=1
#print(warehouse_dict_werehouse)
'''

state_list=[]
for i in stock:
     if i["state"] not in state_list:
         
          state_list.append(i["state"])
     else:
         pass
#print(state_list)

category_list=[]
for i in stock:
     if i["category"] not in category_list:
          category_list.append(i["category"])
     else:
          pass
#print(category_list)

for id,i in enumerate(category_list):
    #print(id+1, i)
    pass

warehouse_dict_state = dict()
for i in stock:
     if i["state"] in warehouse_dict_state:
          warehouse_dict_state[i["state"]]+=1
     else:
        warehouse_dict_state[i["state"]] = 1
#print(warehouse_dict_state)




#print(warehouse1_dict, warehouse2_dict)

name = input("whats your name? ")

print(f"Hallo and welcome {name}")



print(f"Menu:\n 1.List items by warehouse,\n 2.Search an item and place an order,\n 3.Browse by category,\n 4.Quit")

user_choice = int(input("select one option from the menu, enter just the number:"))
if user_choice != (1 or 2 or 3 or 4):
    print("Operation is invalid")
if user_choice == 1:


    items_warehouse1=[]
    items_warehouse2=[]
    itemfullname =[]


    for i in stock:    
         itemfullname.append(i["state"] + " " + i["category"])

         if i["warehouse"] == 1:
              items_warehouse1.append(itemfullname)
         else:
              items_warehouse2.append(itemfullname)

    for id, i in enumerate(itemfullname):
         print(id+1, i)
#print(itemfullname)
print("--o--"*30)

print(f"Total items in warehouse 1:{len(items_warehouse1)}\nTotal items in warehouse 2:{len(items_warehouse1)}")


'''
    category_list=[]
    category_list_enum=[]
    for i in stock:
        if i["category"] not in category_list:
            category_list.append(i["category"])
        else:
            pass
    
    
    for id,i in enumerate(category_list(i)):
        print(id+1,category_list(i))
        
        #print(f"The items in warehouse are:\n  and no of items in warehouse:{warehouse_dict_werehouse}")
    
    
 

         



if user_choice ==2:
    itemname=input("what you like to have from warehouse?").lower()
    num_item_name = []
    if itemname in warehouse_dict_category:
        num_item_name = warehouse_dict_category[itemname]

    print(f"Total no of items available in both warehouse is:{num_item_name}")
    if warehouse_dict_werehouse[1] > warehouse_dict_werehouse[2]:
         print(f"warehouse1 has more than warehouse2, No.of items: {warehouse_dict_werehouse[itemname]}")
    
         print(f"warehouse2 has more than warehouse1, No.of items:{warehouse_dict_werehouse[itemname]}")
    
    order_msg= input("if they want to place an order for this item? (yes/no)")

    if order_msg == "no":
        pass
    else:
         order_value = int(input("How many items do you want?"))

    if order_value<=num_item_name:
         print("the order has been placed")
         print(itemname, order_value)
    else:
         re_order= input("Error! do u want to order maximum available? (yes/no)")
         
    if re_order == "yes":
             print(f"order has been placed,{itemname}:{num_item_name}")
    else:
         pass
    
if user_choice == 3:
     pass

if user_choice == 4:
     pass



print(f"thanks for the visit {name} !")
     
'''