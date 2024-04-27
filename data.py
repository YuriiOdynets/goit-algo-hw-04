#Function for user data input. Removes extra spaces and changes input to lower register
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args
