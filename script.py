destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "So Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ["Erin Wilkes", "Shanghai, China", ["historical site", "art"]]

attractions = [[] for destination in destinations]

#print(attractions)

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
      
#print(test_destination_index)

def add_attraction(destination, attraction):
  try:
    destination_index = get_destination_index(destination)
    attractions_for_list = attractions[destination_index]
    attractions_for_list.append(attraction)
  except ValueError:
    return 

  
  
add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])

add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("So Paulo, Brazil", ["So Paulo Zoo", ["zoo"]])
add_attraction("So Paulo, Brazil", ["Ptio do Colgio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

#print(attractions)

def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []
  possible_attractions = [attraction for attraction in attractions_in_city]
  for attraction in possible_attractions:
    attraction_tags = attraction[1]
    for interest in attraction_tags:
      if interests == interest:
        attractions_with_interest.append(attraction[0])
      else:
        continue
  return attractions_with_interest
  
la_arts = find_attractions("Los Angeles, USA", 'art')
  
#print(la_arts)
      
def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
  print(traveler_attractions)
  interests_string = "Hi " + traveler[0] + ", we think you'll like these places around " + traveler_destination
  for attraction in traveler_attractions:
    interests_string += ": the " + attraction
  return interests_string

smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', 'monument'])

print(smills_france)