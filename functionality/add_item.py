from .display_item import display_specific_items
import time

def add_item(item, chores:list):
  """
  Add a single item to the to-do list.

  Args:
    Name(str): The name of the item (required).

  Returns:
    None.
  """
  new_item = {"name": item, "status": "pending"}
  chores.append(new_item)

def request_to_add_item(chores:list):
  """
  Manages the interaction with the user for adding an item.

  Args:
    chores(list): the list of chores, each chore as a dictionary (required).
  
  Returns:
    None
  """
  while True:
    try:
      user_input_1 = input(">> Would you like to add a chore to the list ? [y/n]: ")
      user_input_1.lower()
      if user_input_1 not in ['y', 'n']:
        raise ValueError("ERROR: Please enter a required letter.")
      elif user_input_1 == 'y':
        user_input_2 = input(">> And what do you plan to do ?\n==> ")
        add_item(user_input_2, chores=chores)
        print(">> Activity added successfully ! \n")
        time.sleep(2)
        display_specific_items(chores=chores, status="all")
        time.sleep(2)
        return
      else:
        print(">> Okay ! Let's go back to the menu...")
        time.sleep(2)
        return
    except ValueError as e:
      print(e)

if __name__ == "__main__":
  request_to_add_item()