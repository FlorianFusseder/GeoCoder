import googlemaps


def getInput():
    return input("Please enter address: ")

def getAllKeys():
    L = []
    with open("./key.txt", "r") as keylist:
        for line in keylist:
            currentLine = line.split("\t")[0]
            try:
                gmaps = googlemaps.Client(key=currentLine)
                gmaps.geocode("Regensburg, Germany")
                L.append(currentLine)
            except:
                print("key " + currentLine + " not working... skipping")
                continue

    if len(L) > 0:
        print(str(len(L)) + " keys Working")
    else:
        exit()
    return L


def main():
    counter = 0
    L = getAllKeys()
    gmaps = googlemaps.Client(key=L[counter])
    while True:
        try:
            address = getInput()
            if address == "exit":
                exit()
            response = gmaps.geocode(address)
            print(response[0]['geometry']['location'])
            address = getInput()
        except:
            counter +=1
            gmaps = googlemaps.Client(key=L[counter])


if __name__ == "__main__":
    main()
