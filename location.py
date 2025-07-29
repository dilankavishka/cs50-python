import sys
def main():

    coordinates = (42.376, -71.115)
    coordinates_list = [42.376, -71.115]
    print(f"Latitude: {coordinates[0]}")
    print(f"Longitude: {coordinates[1]}")

print("----------------")

# we can also unpack the tuple like this
    #coordinates = (42.376, -71.115)
    #Latitude, Longitude = coordinates
    #print(f"Latitude: {Latitude}")
    #print(f"Longitude: {Longitude}")


# we can also use a list and let's check which takes the most space
    
    # check the size of the tuple and list
    print("Size of tuple:", sys.getsizeof(coordinates))
    print("Size of list:", sys.getsizeof(coordinates_list))

main()