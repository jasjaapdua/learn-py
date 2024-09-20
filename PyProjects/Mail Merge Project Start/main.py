'''
    This script creates a list of invitations, given a standard message and 
    a list of invitees
'''

LETTER = "./Input/Letters/starting_letter.txt"
INVITEES = "./Input/Names/invited_names.txt"
PLACE_HOLDER = "[name]"

def generate_message(message, name) -> None:
    '''Creates a new file with the invitation for person named name.

    Args:
        message (str): Standard template for message to send out
        name (str): Name of the person who's receiving the message
    '''
    new_file_contents = message.replace(PLACE_HOLDER, f"{name.rstrip('\n')}")
    new_file_name = f"./Output/ReadyToSend/invite_for_{name}.txt"
    with open(new_file_name, 'w') as new_file:
        new_file.write(new_file_contents)

with open(LETTER, 'r') as letter, open(INVITEES, 'r') as invitee:
    try:
        letter_contents = letter.read()
    except EOFError:
        print('Read failed')

    names = [line.rstrip('\n') for line in invitee]
    for n in names:
        generate_message(letter_contents, n)
