import time

def display_specific_items(chores:list, status:str):
  """
  Responsible of displaying items given a specific status.
  
  Args:
    chores(list): the list of dictionnaries, say chores (required).
    status(str): The status of the items we want to display (required).

  Returns:
    None
  """
  status = status.lower()
  index = 0
  if status in "all":
    print("\n=======================\n=======ALL CHORES=======\n")
    for elm in chores:
      print(f"{index+1}. {elm['name']} || status : {elm['status']}")
      index+=1
    print("\n=======================")
  else:
    print(f"\n=======================\n======={status.upper()} CHORES=======\n")
    for elm in chores:
      if elm["status"] == status:
        print(f"{index+1}. {elm['name']} || status : {elm['status']}")
        index+=1
    print("\n=======================")
  time.sleep(3)

def request_to_display_items(chores:list):
  """
  The functions manages the interaction with the user before trigerring the process of displaying items to the user.

  Args:
    chores(list): the list of dictionnaries, say chores (required).
  
  Returns:
    None
  """
  while True:
    user_input_1 = input(">> Which items do you want to display :\n1. All\n2.Completed\n3.Pending\n===>")
    if user_input_1 not in ['1', '2', '3']:
      print("ERROR : Please enter a valide input!")
    elif user_input_1 == '1':
      display_specific_items(chores=chores, status="All")
      return
    elif user_input_1 == '2':
      display_specific_items(chores=chores, status="completed")
      return
    else:
      display_specific_items(chores=chores, status="pending")
      return

if __name__ == "__main__":
  request_to_display_items()