import sys
import googlemaps

def getInput():
    return input("Please enter address: ") 

def main():
    if len(sys.argv) == 2:
        if sys.argv[1] == "-?" or sys.argv[1] == "-help":
            print("Start with google api key as Parameter, to end enter exit")
        else:
            gmaps = googlemaps.Client(key=sys.argv[1])
            address = getInput()
            while address != "exit":
                response = gmaps.geocode(address)
                print(response[0]['geometry']['location'])
                address = getInput()
    else:
        print("Wrong Parameters to start. Check -help or -?")



if __name__ == "__main__": main()