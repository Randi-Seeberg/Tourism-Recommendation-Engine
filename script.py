destinations = [("Paris, France"), ("Shanghai, China"), ("Los Angeles, USA"), ("São Paolo, Brazil"), ("Cairo, Egypt")]
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

def get_destination_index(destination):
  destination_index = 0
  for i in destinations:
    if i == destination:
      destination_index = destinations.index(i)
  return destination_index
#print(get_destination_index("Los Angeles, USA"))
#print(get_destination_index("Paris, France"))
#print(get_destination_index("Hyperabad, India"))
def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination) 
  return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler)
#print(test_destination_index)
  
attractions = [[] for i in destinations]
#opretter liste af lister, én for hver destination
#print(attractions)

def add_attraction(destination, attraction):
  destination_index = get_destination_index(destination)
  try:
    destination = "Copenhagen, Denmark"
  except SyntaxError:
    return
  attractions_for_destination = attractions[destination_index]
  attractions_for_destination.append(attraction)
  return
add_attraction("Los Angeles, USA",["Venice Beach", ["beach"]])
#print(attractions)

add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []
  
  for a in attractions_in_city:
    possible_attraction = a
    attraction_tags = a[1]
    
    for i in interests:
      if i in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])
        
  return attractions_with_interest

la_arts = find_attractions("Los Angeles, USA", ['art'])
#print(la_arts)

def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
  interests_string = "Hi " + traveler[0] + ", we think you'll like these places around " + traveler_destination + ": "
  
  for i in range(len(traveler_attractions)):
    if traveler_attractions[i] == traveler_attractions[-1]:
      interests_string += the " + traveler_attractions[i] + "."
    else:
      interests_string += "the " + traveler_attractions[i] + ", "
  return interests_string

smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)
  
  
  
  
  
  
  
  
  
  
  
