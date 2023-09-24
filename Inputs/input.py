def SVInput(text = ""):
    return input(text)

def MVInput(text = "", values = []):
    length = len(values)

    if(len(text) != 0):
        print(text)
    
    if(length > 0):
        for i in range(length):
            print("{}. {}".format(i + 1, values[i]))
        
    inp = int(input())

    while(inp <= 0 or inp > length):
        inp = int(input())
    
    return values[inp - 1]

print(MVInput("Choose a weapon:", ["Sword", "Bow", "Wand"]))