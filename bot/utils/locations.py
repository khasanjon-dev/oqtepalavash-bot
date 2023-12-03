from geopy.geocoders import Nominatim


def get_address(latitude: float, longitude: float) -> str:
    geolocator = Nominatim(user_agent="oqtepa")
    location = geolocator.reverse(f"{latitude}, {longitude}")
    address = location.raw['address']
    house_number = address.get('house_number', None)
    road = address.get('road', None)
    residential = address.get('residential', None)
    city = address['city']
    text = f"{city}, {residential}, {road}, {house_number}"
    return text
