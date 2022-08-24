print("Welcome to Rakshith's Dealership!")
user_input = ''
started = False
while True:
    user_input = input("Enter your command:\n").lower()
    if user_input == "start":
       if started:
           print("Car is already started!")
       else:
            started = True
            print("Car started! ")
    elif user_input == "stop":
            if not started:
                print("Car is already stopped! ")
            else:
                started = False
                print("Car is stopped: ")
    elif user_input == "help":
        print("""
start-> start
stop-> stop
quit-> end
        """)
    elif user_input == "quit":
        break
    else:
        print("Enter a valid command! ")

#Letter F

numbers = [2, 2, 2, 2, 5]
for i in numbers:
    y = ''
    for count in range(i):
        y += 'x'
    print(y)


