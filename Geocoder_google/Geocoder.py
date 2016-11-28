import googlemaps

def WriteMyLine(coords, new_file, line, counter):
	line = line[:-1]
	templine = line + '\t' + str(coords['lat']) + "\t" + str(coords['lng']) + "\n"
	print(str(counter) + ": " + templine[:-1])
	new_file.write(templine)
	return

def main():

	googlekey = input("Enter Key: ")
	gmaps = googlemaps.Client(key=googlekey)
	counter = 0
	for i in range(1, 6):
		pathSimple = "D:/Spatial/Data/CSV/Rental_Data/CSV/simple/b" + str(i) + "_condo_comp012816.txt"
		pathReworked = "D:/Spatial/Data/CSV/Rental_Data/CSV/reworked/b" + str(i) + "_reworked.txt"
		with open(pathSimple, 'r') as old_file:
			with open(pathReworked, 'w') as new_file:
				for line in old_file:
					response = gmaps.geocode(line.split("\t")[0] + ", New York")
					coords = response[0]['geometry']['location']
					WriteMyLine(coords, new_file, line, counter)
					counter = counter + 1
					if counter > 2450:
						googlekey = input("Enter Key: ")
						gmaps = googlemaps.Client(key=googlekey)
						counter = 0
				
	print("Finished")

if __name__ == '__main__':main()