
# compute coordinates of the corners with the high-level API
# returning an Astropy Skycoord object
print(w.pixel_to_world([0, 0, 999, 999], [0, 999, 999, 0]))

# using a method from the legacy API, which returns an array
print(w.calc_footprint())
