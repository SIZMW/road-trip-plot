import datetime
from datetime import timezone
import gmplot
import json
import numpy as np

from constants import *
from file_util import *

def generate_map(input_file, output_file, start_time, end_time):
    """
    Sanitizes the provided input file by removing extra location data and
    minimizing the data time frame.

    Arguments:
        input_file: Input JSON file to read sanitized location data.
        output_file: Output map HTML file to write the map.
        start_time: Start timestamp in milliseconds from Unix Epoch to capture data.
        end_time: End timestamp in milliseconds from Unix Epoch to capture data.
    """

    start_time_s = float(start_time) / MS_TO_SECONDS
    end_time_s = float(end_time) / MS_TO_SECONDS

    start_date = datetime.datetime.fromtimestamp(start_time_s, timezone.utc)
    end_date = datetime.datetime.fromtimestamp(end_time_s, timezone.utc)

    # List of all locations during trip
    loc_list = []

    with open(input_file) as json_file:
        locs = json.load(json_file)
        
        # Read locations object in file
        all_locs = locs[LOCATIONS_KEY]
        
        for loc in all_locs:
            # Convert location time to datetime instance
            loc_date = datetime.datetime.fromisoformat(loc[TIMESTAMP_MS_KEY])
            
            if loc_date >= start_date and loc_date <= end_date:
                # Track each location with time
                loc_list.append({
                        TIME_KEY: loc_date,
                        LAT_KEY: loc[LATITUDE_KEY] / LOCATION_E7,
                        LON_KEY: loc[LONGITUDE_KEY] / LOCATION_E7
                    })

    # Sort locations by time to connect them in chronological order
    loc_list.sort(key=lambda x: x[TIME_KEY], reverse=True)

    # Lists of latitudes and longitudes
    lats = []
    lons = []

    # Divide latitudes and longitudes for plotting
    for loc in loc_list:
        lats.append(loc[LAT_KEY])
        lons.append(loc[LON_KEY])

    gmap = gmplot.GoogleMapPlotter(39.5, -98.35, 5) # Center map on center of United States
    gmap.plot(lats,lons,'red', edge_width=3) # Format route line
    gmap.draw(output_file) # Output map to webpage view

    print('Finished generating map for location data.')


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser(description='Generates a map file with route data using the specified input location data file.')
    parser.add_argument('-i', '--input', type=file, help='Input JSON file to read sanitized location data.')
    parser.add_argument('-o', '--output', type=file, help='Output map HTML file to write the map.')
    parser.add_argument('-s', '--starttime', type=int, help='Start timestamp in milliseconds from Unix Epoch to capture data.')
    parser.add_argument('-e', '--endtime', type=int, help='End timestamp in milliseconds from Unix Epoch to capture data.')
    args = parser.parse_args()

    generate_map(args.input, args.output, args.starttime, args.endtime)