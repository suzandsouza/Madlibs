# adj=input("Ajectives:")
# verb1=input("Ajective: ")
# verb2=input("Verb:")
# famous_person=input("Famous person:")


# madlibs=f"Computer programming is so {adj}! It makes me so excited all the time because \n I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

# print(madlibs)
loop=1
while(loop<10):
    #All the questions that the program asks the user 
    noun = input("Choose a noun:")
    p_noun=input("Choose a plural noun:")
    noun2=input("Choose a noun: ")
    place=input("Name a place: ")
    adjective=input("Choose an adjective (Describing word): ")
    noun3=input("Choose a noun: ")
    #Displays the story based on the users input
    print("----------------------------------")
    print("Be kind to your",noun,"- footed",p_noun)
    print("For a duck may be somebody's ",noun2," ,")
    print("Be kind to this little thing called the",p_noun,"in",place)
    print("Where the weather is always",adjective,".")
    print()
    print("You may think that is this the ",noun3,",")
    print("Well it is.")
    print("---------------------------------------")
    #Loop back to loop=1
    loop=loop+1
