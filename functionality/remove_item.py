import time
from .display_item import display_specific_items

def process_to_remove_item(chores:list, user_input):
  """
  Remove an item according to the user input.

  Args:
    user_input(int, str): the value intered by the user
    chores(list): the list of chores, say dictionaries (required).
  
  Returns:
    success(bool): removing completed or not.
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
      print(f"ERROR: {e}")
      success = False
  return success

def remove_item(chores:list):
  """
  Continue interacting with the user to retrieve necessary informations before triggereing the removing

  Args:
    chores(list): the list of chores, say dictionaries (required).
  
  Returns:
    success(bool): interaction and process completed or not.
  """
  user_input_2 = input(">>Which activity would you like to remove (select by typing its exact name or current index) ?")
  msg = f"ERROR: The entered number should be a valid one between 1 and {len(chores)}"
  try:
    user_input_as = int(user_input_2)
    valid_integer_input = 1 <= user_input_as <= len(chores)
    if not valid_integer_input:
      raise ValueError(msg)
  except ValueError as e:
    if str(e) == msg: 
      success = False
      return success
    else:
      user_input_as = user_input_2
  finally:
    removing_completed = process_to_remove_item(chores=chores, user_input=user_input_as)
    if removing_completed:
      success = True
    else:
      success = False
    return success

def request_to_remove_item(chores:list):
  """
  Start the interaction with the user to remove an item.

  Args:
    chores(list): list of chores, say dictionaries (required).
  
  Returns:
    None
  """
  while True:
    try:
      user_input_1 = input(">> Are you sure you would like to remove an activity ? [y/n]: ")
      user_input_1.lower()
      if user_input_1 not in ['y', 'n']:
        raise ValueError("ERROR: You should enter a required number !")
      elif user_input_1 == 'y':
        display_specific_items(chores=chores, status="all")
        item_removed = remove_item(chores=chores)
        if item_removed:
          print(">> Activity removed successfully !")
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
  request_to_remove_item()