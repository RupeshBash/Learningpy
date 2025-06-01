i = 0
while i < 7:
    print("ello World")
    if i == 5:
        i += 1  # increment before continue to avoid infinite loop
        continue
    if i == 6:
        break
    
    i += 1
