import os, pgeocode

country = pgeocode.Nominatim('GB')

with open('postcodes.txt') as file_object:
  postcodes = file_object.readlines()

with open('final.txt', 'w+') as file_object:
  content = file_object.readlines()
  first_line_text = 'WKT,name,description'

  # Check if file contains first line
  if len(content) > 0 and content[0] != first_line_text:
    content[0] = f'{first_line_text}\n'

  if len(content) == 0 or content[0] != first_line_text:
    file_object.write(f'{first_line_text}\n')

  # Write to the file line by line
  for postcode in postcodes:
    latitude = country.query_postal_code(postcode).latitude
    longitude = country.query_postal_code(postcode).longitude

    file_object.write(f'"POINT ({longitude} {latitude})",{postcode}')

