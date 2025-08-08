import time
from .display_item import display_specific_items

def process_to_remove_item(chores:list,user_input):
  """
  Triggers the process of removing according to the input of the user.

  Args:
    user_input(int, str): the value enterd by the user
    chores(list): the list of chores, each chore as a dictionnary (required).
  
  Returns:
    success(bool): if the inner process of deleting was completed successfully or not.
  """
  if isinstance(user_input, int):
    chores.pop(user_input - 1)
    success = True
  else:
    try:
      item_to_remove = next((elm for elm in chores if elm["name"] == user_input), None)
      if item_to_remove:
        chores.remove(item_to_remove)
        success = True
      else:
        success = False

    except Exception as e:
      print(f">> ERROR: {e}")
      success = False
  return success

def remove_item(chores:list):
  """
  Manages the interaction with user of the way of removing a single item to the to-do list.
  
  Args:
    Name(str): The name of the item (required).
    chores(list): the list of chores, each chore as a dictionnary (required).
  
  Returns:
    success(bool): if the process of deleting was completed successfully or not.
  """
  user_input_2 = input(">> Which chore would you like to remove (select by typing the current index or its exact name)? ")
  try:
    user_input_as = int(user_input_2)
  except ValueError:
    user_input_as = user_input_2
  finally:
    removing_completed = process_to_remove_item(chores=chores,user_input=user_input_as)
    if removing_completed:
      success = True
    else:
      success = False
  return success

def request_to_remove_item(chores:list):
  """
  This manages the interaction with the user of removing an item.

  Args:
    chores(list): the list of chores, each chore as a dictionnary (required).

  Returns:
    None
  """
  while True:
    user_input_1 = input(">> Are you sure you would like to remove a chore ? [y/n] : ")
    if user_input_1.lower() == 'y':
      display_specific_items(chores=chores, status="All")
      item_removed = remove_item(chores=chores)
      if item_removed:
        print(">> Chore removed successfully !")
        display_specific_items(chores=chores, status="All")
        print(">> Okay ! Let's go back to the menu...")
        time.sleep(2)
      return
    elif user_input_1.lower() == 'n': 
      print(">> Okay ! Let's go back to the menu...")
      time.sleep(2)
      return
    else:
      print("ERROR : Please write a required letter.")

if __name__ == "__main__":
  request_to_remove_item()