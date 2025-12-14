a = "SAV_E20"

for char in a:
    if not char.isalnum() and char != "_":
        break
else:
    print("Valid")
