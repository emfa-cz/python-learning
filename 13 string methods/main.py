name = input("Enter your name: ")

#result = len(name) # lengs in chars
#result = name.find("a") # kolikaty char je jaky prvni specifikovany char (prvni char je 0)
#result = name.rfind("a") # kolikaty char je jaky posledni specifikovany char (prvni char je 0)
#result = name.upper() # prevede chars na capslock
#result = name.lower() # opak
#result = name.isdigit() # true/false jestli je pouze cislo
#result = name.isalpha() # jestli je pouze pismena
#result = name.count("a") # kolik char ve string
result = name.replace("a", "X") #replace dany char za jiny char

print(result)