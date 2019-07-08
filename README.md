Cross Country Road Trip Plot
==========================

## Description
In the past, I have done a few road trips through various parts of the country. This visualization is used to plot the actual routes I took in a [Google Maps](https://www.google.com/maps) view.

Google Maps has a [timeline](https://www.google.com/maps/timeline) feature which allows you to see your location history by year, month, and day. You can use [Google Takeout](https://takeout.google.com/settings/takeout) to download this data in a JSON format. It doesn't seem like you can plot a route across days or weeks in the Timeline view, so I wanted to do it myself.

## Build
This project requires [Python 2.7](https://www.python.org/download/releases/2.7/), as well as the following packages:

* [`gmplot`](https://github.com/vgm64/gmplot)

This project also requires the Google Takeout JSON file of location history. This can be done creating an archive of your Google data and only selecting your location history as the archive contents. This [link](https://takeout.google.com/settings/takeout/custom/location_history?hl=en&gl=US&expflags) should directly allow you to do this. Place the JSON file at `data/location_history.json` in the project folder.

## Usage

### Data Sanitization

To sanitize the JSON location data, simply run the sanitization script:

```
python .\sanitize_data.py -i <raw file from Google Takeout> -o .\data\<sanitized JSON file> -s <Start Epoch Unix timestamp of data> -e <End Epoch Unix timestamp of data>
```

This will produce a sanitized JSON file for just the minimum data required to plot the map.

For example:

```
python .\sanitize_data.py -i .\data\boston_sandiego_location_history_raw.json -o .\data\boston_sandiego_location_history.json -s 1495425600000 -e 1496030340000
```

produces the provided file [boston_sandiego_location_history.json](data/boston_sandiego_location_history.json).

### Map Plot

To plot the map, simply run the road trip plot script:

```
python .\road_trip_plot.py -i .\data\<sanitized JSON file> -o .\maps\<map HTML file> -s <Start Epoch Unix timestamp of data> -e <End Epoch Unix timestamp of data>
```

### Output

An example of each of my road trip maps can be found below. There are more map images in the corresponding `img/` directories.

#### Boston to San Diego

![1920x1080](img/boston-sandiego/boston-sandiego-1920x1080.png)

#### Seattle to Yellowstone National Park (and Back)

![1920x1080](img/seattle-yellowstone/seattle-yellowstone-1920x1080.png)

![1920x1080](img/seattle-yellowstone/seattle-yellowstone-reverse-1920x1080.png)