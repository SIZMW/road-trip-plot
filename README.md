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
The notebook [road-trip-plot.ipynb](road-trip-plot.ipynb) can be executed top to bottom to produce the file `map.html`. This map can be viewed in a web browser to explore the road trip route.

### Output

An example of each of my road trip maps can be found below. There are more map images in the corresponding `img/` directories.

#### Boston to San Diego

![1920x1080](img/boston-sandiego/boston-sandiego-1920x1080.png)

#### Seattle to Yellowstone National Park (and Back)

![1920x1080](img/seattle-yellowstone/seattle-yellowstone-1920x1080.png)

![1920x1080](img/seattle-yellowstone/seattle-yellowstone-reverse-1920x1080.png)