import pgeocode

country = pgeocode.Nominatim('GB')

with open('postcodes.txt') as file_object:
  postcodes = file_object.readlines()

with open('final.csv', 'w+') as file_object:
  content = file_object.readlines()
  first_line_text = 'WKT,name,description'

  # Check if file contains first line
  if len(content) == 0 or content[0] != first_line_text:
    file_object.write(f'{first_line_text}\n')

  # Write to the file line by line
  for item in postcodes:
    postcode = item.rstrip(',\n').upper()

    # check if there is space between outward and inward code, like in this case: SE18 3PG
    if postcode.find(' ') == -1:
      postcode = postcode[:-3] + ' ' + postcode[-3:].rstrip(",\\n")
    latitude = country.query_postal_code(postcode).latitude
    longitude = country.query_postal_code(postcode).longitude

    file_object.write(f'"POINT ({longitude} {latitude})",{postcode}\n')

