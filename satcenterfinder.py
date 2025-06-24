import requests

def find_available_test_centers(date, zip_code, country, state):
    url = f"https://aru-test-center-search.collegeboard.org/prod/test-centers?date={date}&zip={zip_code}&country={country}"
    response = requests.get(url)

    if response.status_code == 200:
        test_centers = response.json()
        available_centers = [(center["name"], center["address1"], center["state"], center["distance"]) for center in test_centers if center["seatAvailability"] and center["state"] == state]
        available_centers.sort(key=lambda x: x[3])  # Sort by distance
        return available_centers
    else:
        print(f"Error: {response.status_code}")
        return []

# Inputs
date = "2024-08-24"
zip_code = "98006"
country = "US"
state = "WA"

available_centers = find_available_test_centers(date, zip_code, country, state)

if available_centers:
    print(f"Test centers with available seats for the SAT test on {date} in {state} (sorted by distance from {zip_code}):")
    for name, address, state, distance in available_centers:
        print(f"Name: {name}, Address: {address}, State: {state}, Distance: {distance} miles")
else:
    print("No test centers with available seats found.")
