country_city{
Australia = ["Sydney","Melbourne","Brisbane","Perth"]
UAE = ["Dubai","Abu Dhabi","Sharjah","Ajman"]
India = ["Mumbai","Bangalore","Chennai","Delhi"]
}

## Function to find the country of a city
def find_city(city):
  for country,cityies in country_city.items():
   if city in cities:
     return country
     return none

# Task 1: Find the country of a city
city_name=input("Enter The City Name: ")
country_exist=find_city(city_name)

#print the city
if country:
    print(f"{city_name} is in {country}")
else:
    print(f"{city_name} is not found in the database")
