import time
def show_menu():
  print("\n===Menu===")
  print("1. Display to-do list")
  print("2. Add a chore")
  print("3. Mark a chore as completed")
  print("4. Remove a chore")
  print("5. Exit", end="\n\n")

def first_welcome_user():
  while True:
    print(">>Our functionalities :")
    show_menu()
    try:
      user_input = int(input(">>Tell us do you want to do :\n===> "))
      if user_input in list(range(1, 6)):
        return str(user_input)
      else:
        raise ValueError("The number should be between 1 and 5!")
    except ValueError:
      print("ERROR : Please the entered number should be between 1 and 5")
      time.sleep(2)
    except Exception:
      print("ERROR : Please enter a number !")
      time.sleep(2)


def goodbye_message():
  print("\n\n=======================================================================================\nIt has been a pleasure to interact with you, see you for your next day-to-day tasks!\n=======================================================================================\n")