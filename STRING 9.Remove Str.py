mainS=str(input("ENTER THE MAIN STRING : "))
removeS=str(input("ENTER THE REMOVE STRING : "))

if(removeS in mainS):
    newstring=mainS.replace(removeS,"")
    print("FINAL STRING is here:",newstring)
else:
    print("REMOVE STRING IS NOT FOUND IN MAIN STRING")
