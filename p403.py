# Dictionary with countries and their cities
country_city = {
    "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth"],
    "UAE": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"],
    "India": ["Mumbai", "Bangalore", "Chennai", "Delhi"]
}

# Convert the structure to a city-to-country map for easier lookup
city_country = {}
for country, cities in country_city.items():
    for city in cities:
        city_country[city.lower()] = country

# Input from the user
city1 = input("Enter the first city: ").strip().lower()
city2 = input("Enter the second city: ").strip().lower()

# Check if both cities are in the map
if city1 in city_country and city2 in city_country:
    if city_country[city1] == city_country[city2]:
        print(f"Both cities are in {city_country[city1]}")
    else:
        print("They don't belong to the same country")
else:
    print("One or both cities are not in our database.")
