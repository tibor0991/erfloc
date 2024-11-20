from erfloc.dependencies.geoloc import get_geolocator

loc = get_geolocator().get_eci_coords("Turin, Piedmont")

print(loc.model_dump_json())
