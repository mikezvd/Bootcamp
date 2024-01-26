'''
This code is part of the fourth task. (practical task 1)

Pseudo code:

- ask the participant to enter the time they took to run the 3 diferent events
- calculate and store in a variable the total time taken of a person in the triathlon
- display the total time taken
- display which if they won any ward and display which one

The times inserted by the user will be saved as integers numbers since it is calculated in minutes
If a float is inserted, it will round the number to the nearest integer for example,
5.75 will round to 6, but 5.25 will be rounded to 5

(NOTE: 5.50 is rounded to 5, but 5.51 get rounded to 6)

'''


# ask participant to enter the time they took on the swimming event
swimming = round(float(input("Enter the time (in minutes) of your Swimming Event: ")))
print(swimming)
# ask participant to enter the time they took on the cycling event
cycling = round(float(input("Enter the time (in minutes) of your Cycling Event: ")))

# ask participant to enter the time they took on the running event
running = round(float(input("Enter the time (in minutes) of your Running Event: ")))

# calculate the total time taken in the three events
time_taken = swimming + cycling + running

# show the participant their total time taken
print(f"Your time taken in the Triathlon was: {time_taken} minutes.")

# based on the time taken, shows the participant which award they won , if they won one
if (time_taken >= 111) :
    # if they took 111 minutes or more it displays that they didn't win any award
    print("Sorry, you didn't win any award. Good luck next time.")

elif (time_taken >= 106) and (time_taken <= 110) :
    # if their time is between 106 minutes or up to 111 minutes they won the Provincial scroll award
    print("Congratulations! You won the Provincial Scroll award!")
    
elif (time_taken >= 101) and (time_taken <= 105) :
    # if their time is between 101 minutes or up to 105 minutes they won the provincial half colours award
    print("Congratulations! You won the Provincial Half Colours award!")
    
elif time_taken <= 100 :
    # if their time is below 101 minutes they won the provincial colours award
    print("Congratulations! You won the Provincial Colours award!")
