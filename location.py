def main():

    coordinates = (42.376, -71.115)
    print(f"Latitude: {coordinates[0]}")
    print(f"Longitude: {coordinates[1]}")

print("----------------")

# we can also unpack the tuple like this
    coordinates = (42.376, -71.115)
    Latitude, Longitude = coordinates
    print(f"Latitude: {Latitude}")
    print(f"Longitude: {Longitude}")

main()