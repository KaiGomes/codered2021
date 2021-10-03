coord_from_db = [[,],[,]] #list of coordinates
coord_from_dir = [[,],[,]] #list of coordinates

i = 0, j =0
hits = 0 # of incidents along path


TOLERANCE = 0.00045 #50 meters

for point in coord_from_db:
    for point2 in coord_from_dir:
        if (coord_from_db[i][0] - coord_from_dir[j][0] < TOLERANCE) and (coord_from_db[i][1] - coord_from_dir[j][1] < TOLERANCE):
            hits += 1
        j+=1
    i+=1

