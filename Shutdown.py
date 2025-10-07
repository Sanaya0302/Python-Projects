def shutdown():
    question=input("Do you want to shutdown,say yes or no: ")
    if question=="yes":
        print("shuting down")
    elif question=="no":
        print("Abort shutdown")
    else:
        print("Sorry, invalid answer")
shutdown()
