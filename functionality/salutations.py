import time

def show_menu():
  print("\n===Menu===")
  print("1. Display to-do list")
  print("2. Add an activity")
  print("3. Mark an activity as completed")
  print("4. Remove an activity")
  print("5. Exit", end="\n\n")

def first_welcome_user():
  while True:
    print("Our functionnalities :")
    show_menu()
    try:
      user_input = int(input(">>Tell us what you want to do:\n==> "))
      if user_input in list(range(1, 6)):
        return str(user_input)
      else:
        raise ValueError("ERROR: The entered number should be an integer between 1 and 5!")
    except ValueError as e:
      print(e)
      time.sleep(2)
    except Exception as e:
      print(f"ERROR: {e}")
      time.sleep(2)

def goodbye_message():
  print("\n\n=======================================================================================\nIt has been a pleasure to interact with you, see you for your next day-to-day tasks!\n=======================================================================================\n")
  time.sleep(5)