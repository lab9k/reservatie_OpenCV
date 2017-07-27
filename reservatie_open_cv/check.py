def searchSpace(time):
    #lookup in database if there is a space left at that moment
    #when there is space left --
    freeroomname="zaal D01.24A"
    file = open("freeRoom.txt", "w")
    file.write(freeroomname)
    file.close()
    return True
