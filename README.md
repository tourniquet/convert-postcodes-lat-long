# convert-postcodes-lat-long
Convert UK postcodes to latitude and longitude for using them as points on Google Maps

Will convert a list of UK postcodes to a list of latitudes and longitudes to a CSV file

Example: <br>
input file postcodes.txt

> SE18 3PG, <br>
> SE9 6SZ,

output file final.csv

> WKT,name,description <br>
> "POINT (0.0740666666666666 51.48716666666667)",SE18 3PG, <br>
> "POINT (0.0542799999999999 51.44698000000001)",SE9 6HZ, <br>

PS: For using this script you'll need to have Python installed. 
