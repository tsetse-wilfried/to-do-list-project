import time
from data.chores_data import chore_data as chores
from functionality import add_item as ai, display_item as di, remove_item as ri, salutations as slt, mark_item_completed as mc

def main():
  """
  Main function for welcoming the user and linking to functionalities of the app.
  """
  while True:
    user_choice = slt.first_welcome_user()
    if user_choice == '1':
      print("\nDISPLAY CHORE\n=============")
      time.sleep(2)
      di.request_to_display_items(chores=chores)
    elif user_choice == '2':
      print("\nADD CHORE\n==========")
      time.sleep(2)
      ai.request_to_add_item(chores=chores)
    elif user_choice == "3":
      print("\nMARK A CHORE AS COMPLETED\n========================")
      time.sleep(2)
      mc.mark_item_as_completed(chores=chores)
    elif user_choice == '4':
      ri.request_to_remove_item(chores=chores)
    else:
      slt.goodbye_message()
      break

if __name__ == "__main__":
  print("\n=======================================================================================\n         Welcome to your to-do list app, your ally for your day-to-day tasks!\n=======================================================================================\n")
  main()