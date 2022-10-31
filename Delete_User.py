def Delete_User():
    userID = int(input("Please enter your user ID: "))
    # list to store file lines
    lines = []
    # read file
    with open(r"accountfiles.txt", 'r') as fp:
        # read and store all lines into list
        lines = fp.readlines()
        if userID > len(lines) or userID < 1:
            print("Error: That User ID does not exist")
            return
        lines[userID-1] = " \n"
    # Write file
    with open(r"accountfiles.txt", 'w') as fp:
        # iterate each line
        for number, line in enumerate(lines):
            fp.write(line)