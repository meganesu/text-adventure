#! python3
# Text Adventure!

'''

set default room

while (not won):

  print prompt
  get user input

  switch(room)
  	case: 1
    do stuff for room one

'''

room = 0
playerHasWon = False

while not playerHasWon:

    if room == 0:
        # Print room description and get user input
        print("\nRoom 0 description")
        input = raw_input('> ').lower()

        # Do room action based on input
        if input == 's' or input == 'south' or input == 'open door':
            room = 1
            continue


    elif room == 1:
        # Print room description and get user input
        print("\nRoom 1 description")
        input = raw_input('> ').lower()

        # Do room action based on input
        if input == 'n' or input == 'north':
            room = 0
            continue
        elif input == 's' or input == 'south':
            room = 2
            continue

    elif room == 2:
        # Print room description and get user input
        print("\nRoom 2 description")
        input = raw_input('> ').lower()

        # Do room action based on input
        if input == 'n' or input == 'north':
            room = 1
            continue
        elif input == 's' or input == 'south':
            room = 5
            continue
        elif input == 'w' or input == 'west':
            room = 4
            continue
        elif input == 'e' or input == 'east':
            room = 3
            continue

    elif room == 3:
        # Print room description and get user input
        print("\nRoom 3 description")
        input = raw_input('> ').lower()

        # Do room action based on input
        if input == 'w' or input == 'west':
            room = 2
            continue

    elif room == 4:
        # Print room description and get user input
        print("\nRoom 4 description")
        input = raw_input('> ').lower()

        # Do room action based on input
        if input == 'e' or input == 'east':
            room = 2
            continue

    elif room == 5:
        # Print room description and get user input
        print("\nRoom 5 description")
        input = raw_input('> ').lower()

        # Do room action based on input
        if input == 'n' or input == 'north':
            room = 2
            continue
        elif input == 'take crystal':
            playerHasWon = True
            break

if playerHasWon:
    print("\nWin description")

