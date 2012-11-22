import os
from django.contrib.gis.gdal import DataSource
from cities.models import PostalCode

def main(argv, argc):
    shapes = get_shapes(argv[1])
    for plz, shape in shapes:
        write_shape_to_model(plz, shape)

def write_shape_to_model(plz, shape, model= PostalCode):
    return
    obj = model.objects.get(code= plz)
    obj.shape = shape
    obj.save()

def get_shapes(filename):
    try:
        shp_filename = os.path.abspath(filename)
    except:
        print "File not found."

    layer = DataSource(shp_filename)[0]
    data = {}
    for feature in layer:
        plz = feature.get('PLZ99')
        geom = feature.geom
        data[plz] = geom

    return data

if __name__ == '__main__':
    import sys
    main(sys.argv, len(sys.argv))