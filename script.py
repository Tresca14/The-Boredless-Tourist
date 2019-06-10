destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "So Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ["Erin Wilkes", "Shanghai, China", ["historical site", "art"]]


def get_destination_index(destination):
  for city in destinations:
    if city == destination:
      destination_index = destinations.index(city) 
  return destination_index

#print(get_destination_index("Cairo, Egypt"))

def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler)
      
print(test_destination_index)
      
  