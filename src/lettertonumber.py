def getEncodedMessage():
    text = open("src\__sentence.txt", "r")
    s = text.readline()

    a = "asdf"
    print(ord(a[0]))

    e = []

    for char in s:
        if char == " ":
            e.append("53")
        
        else:
            ascii = ord(char)
            if ascii < 97:
                n = ascii - 38
                e.append(str(n))

            else:
                n = ascii - 96
                if n < 10: e.append("0" + str(n))
                else: e.append(str(n))

    encodedMessage = []
    temp = []
    for num in e:
        temp.append(num)
        if temp.__len__() == 2:
            encodedMessage.append(int(temp[0] + temp[1]))
            temp.clear()
    if temp.__len__() == 1: encodedMessage.append(int(temp[0]))

    return encodedMessage
        