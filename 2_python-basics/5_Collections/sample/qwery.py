from data import stock

{"state": "Almost new", 
 "category": "Keyboard", 
  "warehouse": 1,  
    "date_of_stock": "2020-05-06 08:28:12"},
warehouse_dict_state = dict()
for i in stock:
     if i["state"] in warehouse_dict_state:
          warehouse_dict_state[i["state"]]+=1
     else:
        warehouse_dict_state[i["state"]] = 1
#print(list(warehouse_dict_state))

warehouse_dict_category = dict()
for i in stock:
    if i["category"] in warehouse_dict_category:
        warehouse_dict_category[i["category"]]+=1
    else:
        warehouse_dict_category[i["category"]]=1
print(warehouse_dict_category)
#dont till here

#print(warehouse1_dict, warehouse2_dict)

name = input("whats your name? ")

print(f"Hallo and welcome {name}")



print(f"Menu:\n 1.List items by warehouse,\n 2.Search an item and place an order,\n 3.Quit")

user_choice = int(input("select one option from the menu, enter just the number:"))
if user_choice != 1 or 2 or 3:
     print("Operation is invalid")
if user_choice == 1:
    print(f"The items in warehouse1 are:\n {warehouse1(enumerate)}\n--------\n The items in warehouse2 {warehouse2}")
if user_choice ==2:
    itemname=input("what you like to have from warehouse?")
    num_item_name = []
    if itemname in warehouse1_dict:
        num_item_name = warehouse1_dict[itemname]
    if itemname in warehouse2_dict:
        num_item_name += warehouse2_dict[itemname]
    print(f"Total no of items available in both warehouse is:{num_item_name}")
    if warehouse1_dict[itemname] > warehouse2_dict[itemname]:
         print(f"warehouse1 has more than warehouse2, No.of items: {warehouse1_dict[itemname]}")
    
         print(f"warehouse2 has more than warehouse1, No.of items:{warehouse2_dict[itemname]}")
    
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



print(f"thanks for the visit {name}")
     
