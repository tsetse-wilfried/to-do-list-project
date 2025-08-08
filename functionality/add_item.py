from .display_item import display_specific_items
import time

def add_item(item, chores:list):
  """
  Manages the process of adding a single item to the to-do list.
  
  Args:
    Name(str): The name of the item (required).
  
  Returns:
    None.
  """
  new_item = {"name": item, "status":"pending"}
  chores.append(new_item)

def request_to_add_item(chores:list):
  """
  This function manages the interaction with the user for adding an item.

  Args:
    chores(list): the list of chores, each chore as a dictionnary (required).
  
  Returns:
    None
  """
  while True:
    user_input_1 = input(">> Would you like to add a chore to the list ? [y/n] :")
    if user_input_1.lower() == 'y':
      user_input_2 = input(">> And which chore would you like to complete today ?\n==> ")
      add_item(user_input_2, chores=chores)
      print(">> Chore added successfully !\n")
      display_specific_items(chores=chores, status="All")
      time.sleep(2)
      return
    elif user_input_1.lower() == 'n': 
      print(">> Okay ! Let's go back to the menu...")
      time.sleep(3)
      return
    else:
      print("ERROR : Please write a required letter.")

if __name__ == "__main__":
  request_to_add_item()