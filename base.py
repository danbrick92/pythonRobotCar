# This is the base file for the robot car

def main():
    print "Running Remote Control Car program..."
    keepRunning = True
    count = 1
    while keepRunning == True:
        keepRunning = update()
        count+= 1
        if count > 10:
            keepRunning = False
    print "Ending Remote Control Car program..."

def update():
    keepRunning = True
    command = raw_input("Type instructions. Type h for list of commands. Type q to exit.")
    if command.lower() == 'q':
        keepRunning = False
    return keepRunning

# Calls main
if __name__ == "__main__":
    main()