def main ():
    number = get_number() #created a function
    meow(number) #Passes 'number' to meow()

# This function asks the user for a number
def get_number ():
     while True:  # Keeps looping until a valid input is given
          n=int(input("whats n?")) # Asks user for input and converts it to an integer
          if n > 0:
               break
     return n #If valid, return the number and exit the loop
def meow(n):
     for _ in range(n): # Loops n times
          print("meow =^.^=") #printing output
main()