string = input("Input Of The Word:")
character = input("character:")
count = sum(1 for char in string if char in character)
print("Number of ", character," in ",string,"is",count)