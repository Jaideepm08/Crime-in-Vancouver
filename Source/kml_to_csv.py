import utilities
import re

def homeless_kml_to_csv(kml_filename, use_headers=True, output_filename = 'doc.csv'):
    # we need to read it to string cause parser complains, so we need to clean it a bit first
    with open(kml_filename, 'r') as myfile:
        dataz=myfile.read().replace('\n', '')
    
    # we need to clean via regex 
    dataz = re.sub(r"<gx:labelVisibility>\d+</gx:labelVisibility>", "", dataz)

    #ok, just call magic function
    utilities.kml_to_csv(dataz, use_headers=True, output_filename='doc.csv')


def graffiti_kml_to_csv(kml_filename):
    #ok, just call magic function
    utilities.kml_to_csv(kml_filename, use_headers=True, output_filename='graffiti.csv')

def skytrain_station_kml_to_csv(kml_file):
    utilities.kml_to_csv(kml_file, use_headers=True, output_filename='rapid_transit_stations.csv')

def street_light_poles_kml_to_csv(kml_file):
    utilities.kml_to_csv(kml_file, use_headers=True, output_filename='street_lighting_poles.csv')
    
# homeless_kml_to_csv('../data/homeless_shelters/doc.kml')     
# graffiti_kml_to_csv('../data/graffiti/graffiti.kml')
#skytrain_station_kml_to_csv('../data/skytrain_stations/rapid_transit_stations.kml')
# street_light_poles_kml_to_csv('../data/street_lightings/street_lighting_poles.kml')