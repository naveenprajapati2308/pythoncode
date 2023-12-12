
user_dict = {}

while True:
    key = input("Enter a key (or 'exit' to finish): ")
    

    if key.lower() == 'exit':
        break
    
    value = input(f"Enter a value for the key '{key}': ")
    
  
    user_dict[key] = value


print("Dictionary created by the user:")
for key, value in user_dict.items():
    print(f"{key}: {value}")
