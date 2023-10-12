import datetime
from datetime import timezone
import json
import numpy as np

from constants import *
from file_util import *

def sanitize_location_data(start_time, end_time, input_file, output_file):
    """
    Sanitizes the provided input file by removing extra location data and
    minimizing the data time frame.

    Arguments:
        start_time: Start timestamp in milliseconds from Unix Epoch to capture data.
        end_time: End timestamp in milliseconds from Unix Epoch to capture data.
        input_file: Input JSON file to read raw location data.
        output_file: Output JSON file to write sanitized location data.
    """

    start_time_s = float(start_time) / MS_TO_SECONDS
    end_time_s = float(end_time) / MS_TO_SECONDS

    start_date = datetime.datetime.fromtimestamp(start_time_s, timezone.utc)
    end_date = datetime.datetime.fromtimestamp(end_time_s, timezone.utc)

    loc_list = []

    with open(input_file) as json_file:
        locs = json.load(json_file)
        
        # Read locations object in file
        all_locs = locs[LOCATIONS_KEY]

        for loc in all_locs:
            # Convert location time to datetime instance
            loc_date = datetime.datetime.fromisoformat(loc[TIMESTAMP_MS_KEY])

            if loc_date >= start_date and loc_date <= end_date:
                # Remove extra information
                loc.pop(ACCURACY_KEY, None)
                loc.pop(ACTIVE_WIFI_SCAN_KEY, None)
                loc.pop(ACTIVITY_KEY, None)
                loc.pop(ALTITUDE_KEY, None)
                loc.pop(BATTERY_CHARGING_KEY, None)
                loc.pop(DEVICE_TAG_KEY, None)
                loc.pop(DEVICE_TIMESTAMP_KEY, None)
                loc.pop(FORM_FACTOR_KEY, None)
                loc.pop(HEADING_KEY, None)
                loc.pop(INFERRED_LOCATION, None)
                loc.pop(LOCATION_METADATA_KEY, None)
                loc.pop(OS_LEVEL_KEY, None)
                loc.pop(PLACE_ID_KEY, None)
                loc.pop(PLATFORM_TYPE_KEY, None)
                loc.pop(SERVER_TIMESTAMP_KEY, None)
                loc.pop(SOURCE_KEY, None)
                loc.pop(VELOCITY_KEY, None)
                loc.pop(VERTICAL_ACCURACY_KEY, None)
            
                loc_list.append(loc)

    json_obj = {
        LOCATIONS_KEY: loc_list
    }

    with open(output_file, 'w') as output_file:
        json.dump(json_obj, output_file)

    print('Finished sanitizing raw location data.')


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser(description='Sanitizes the Location History JSON file from Google Takeout to remove extra data and minimize the data time frame.')
    parser.add_argument('-i', '--input', type=file, help='Input JSON file to read raw location data.')
    parser.add_argument('-o', '--output', type=file, help='Output JSON file to write sanitized location data.')
    parser.add_argument('-s', '--starttime', type=int, help='Start timestamp in milliseconds from Unix Epoch to capture data.')
    parser.add_argument('-e', '--endtime', type=int, help='End timestamp in milliseconds from Unix Epoch to capture data.')
    args = parser.parse_args()

    sanitize_location_data(args.starttime, args.endtime, args.input, args.output)
