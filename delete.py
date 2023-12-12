def delete_middle_element(my_list):
    if len(my_list) % 2 == 0:
      
        middle1 = len(my_list) // 2
        middle2 = middle1 - 1
        my_list.pop(middle1)
        my_list.pop(middle2)
    else:

        middle = len(my_list) // 2
        my_list.pop(middle)
my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)
delete_middle_element(my_list)
print("List after deleting the middle element(s):", my_list)
