import time
from functionality.display_item import display_specific_items

def modify_status(chores:list, index:int):
  """
  Kernel method of a task status change.

  Args:
    chores(list): the list of items, say dictionaries (required).
    index(int): the index of the item we want to remove (required).
  
  Returns:
    None.
  """
  if chores[index]['status'] == "pending":
    chores[index]['status'] = "completed"
  else:
    chores[index]['status'] = "pending"

def modify_status_trigger(chores:list, user_input):
  """
  2nd check input validity before triggering the process of modifying an item.
  No interaction with the user.

  Args:
    chores(list): the list of items, say dictionaries (required).
    user_input(str, int): the location of the item we want to remove.
  
  Returns:
    success(bool): process completed or not.
  """
  if not isinstance(user_input, (int, str)):
    success = False
  else:
    if isinstance(user_input, int):
      modify_status(chores=chores, index=user_input-1)
      success = True
    else:
      try:
        index = next(i for i, elm in enumerate(chores) if elm['name'] == user_input)
        modify_status(chores=chores, index=index)
        success = True
      except ValueError:
        success = False
  return success
  

def process_to_mark_item(chores:list):
  """
  1st check input validity before triggering the process of modifying an item.
  Include user interaction.

  Args:
    chores(list): the list of chores, say dictionaries(required).
  
  Returns:
    succes(bool): process completed or not
  """
  success = False
  display_specific_items(chores=chores, status='all')
  user_input = input("Which item status would you like to modify (select by its number or typing its exact name) ?")
  try:
    user_input_as = int(user_input)
    valid_number = 1 <= user_input_as <= len(chores)
    if not valid_number:
      print("ERROR: You've entered an invalid number.")
  except ValueError:
    user_input_as = user_input
  finally:
    success = modify_status_trigger(chores=chores, user_input=user_input_as)
  
  return success


def mark_item_as_completed(chores:list):
  """
  Manages the interaction with the user before triggering an item as completed.

  Args:
    chores(list): the list of chores (required).
  
  Returns:
    None.
  """
  while True:
    try:
      user_input = input(">> Would you like to a task as done ? [y/n]\n==> ")
      user_input.lower()
      if user_input not in ['y', 'n']:
        raise ValueError("ERROR: You should enter a required letter.")
      elif user_input == 'y':
        item_removed = process_to_mark_item(chores=chores)
        if item_removed:
          print(">> Item status modified successfully!")
          display_specific_items(chores=chores, status="all")
          time.sleep(3)
        else:
          raise Exception("ERROR: Impossible to find an item!")
        return
      else:
        print(">> Okay! Let's go back to the menu...")
        time.sleep(2)
        return
    except Exception as e:
      print(e)