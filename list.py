
user_list = []


while True:
    user_input = input("Enter an item (or 'exit' to finish): ")
    

    if user_input.lower() == 'exit':
        break
    
  
    user_list.append(user_input)


print("List of items entered by the user:")
for item in user_list:
    print(item)
