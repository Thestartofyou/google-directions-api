import googlemaps

def calculate_fastest_route(api_key, origin, destination):
    # Create a client using the API key
    gmaps = googlemaps.Client(key=api_key)

    # Request directions
    directions_result = gmaps.directions(origin, destination, mode="driving")

    # Extract the duration of the fastest route
    fastest_route = directions_result[0]["legs"][0]
    duration = fastest_route["duration"]["text"]

    return duration

# Replace "YOUR_API_KEY" with your actual Google Maps API key
api_key = "YOUR_API_KEY"

# Enter the origin and destination addresses
origin = "Origin Address"
destination = "Destination Address"

# Calculate the fastest route duration
fastest_duration = calculate_fastest_route(api_key, origin, destination)
print("The fastest route duration is:", fastest_duration)
