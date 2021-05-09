import geocoder

# initialize your variable to None
lat_lng_coords = None
print("First Line")

g = geocoder.google('{}, Toronto, Ontario'.format("M1C"), key="AIzaSyBC0oGHn-FRFKMV_9Z32rkWUfaBWD5X-rI")
# g = geocoder.google([45.15, -75.14], method='reverse', key='AIzaSyBC0oGHn-FRFKMV_9Z32rkWUfaBWD5X-rI')
print(g)
g.latlng
print(g.url)
# print("long: {}, Lat: {}".format(longitude, latitude))
