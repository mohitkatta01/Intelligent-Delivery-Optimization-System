# delivery-optimization
Freelancing project involving optimizing the delivery process for a Shipping /Software company based on project VROOM.


### Installation
This project is based on [Project VROOM](https://github.com/VROOM-Project/vroom) and [OSRM](https://github.com/Project-OSRM). Project VROOM uses [OSRM](http://project-osrm.org/) or [Valhalla](https://github.com/valhalla/valhalla) to run the shortest path algorithm. You can install either of them before you can run VROOM.

API References are available from their respective GitHubs.

1. Install [VROOM](https://github.com/VROOM-Project/vroom/wiki/Building) and [OSRM](https://github.com/VROOM-Project/vroom/wiki/Building).

2. If you do not want to read the entire OSRM Documentation and just want to get started, Check out out the [next section](#Setting-up-OSRM-Service-with-Docker) for all the commands. Make sure Docker is installed and running.

# Setting up OSRM Service with Docker

docker run -t -v "${PWD}:/data" ghcr.io/project-osrm/osrm-backend osrm-extract -p /opt/car.lua /data/southern-zone-latest.osm.pbf || echo "osrm-extract failed"

docker run -t -v "${PWD}:/data" ghcr.io/project-osrm/osrm-backend osrm-partition /data/southern-zone-latest.osrm || echo "osrm-partition failed"

docker run -t -v "${PWD}:/data" ghcr.io/project-osrm/osrm-backend osrm-customize /data/southern-zone-latest.osrm || echo "osrm-customize failed"

**Finally, You have the run the following everytime to start the OSRM Server** 

docker run -t -i -p 5000:5000 -v "${PWD}:/data" ghcr.io/project-osrm/osrm-backend osrm-routed --algorithm mld /data/southern-zone-latest.osrm

Note: `southern-zone-latest.osrm` is the South Asian region of India, you can select any country or region based on your computer's processing powers. Bigger the region, slower the server builds!

### Running the project
1. When running the project for the first time, It is imperative to run the first 3 commands from [the above section](#(#Setting-up-OSRM-Service-with-Docker). The 4th Step must be run to start the server.
2. Once the server is open (`Default Port : 5000`), you can use the VROOM interface (Make sure you install it globally).
3. Vroom works with JSON. A JSON File will be used as an input. Vehicles, Shipments and locations for pickup and delivery can be modified in the JSON file. A simple frontend has been created to generate a JSON file (Explained in the next section).
4. Example syntax to use VROOM: `vroom -i generatedJSON.json`. This will generate an output file (Example in `Frontend/output.json`)
5. 

VROOM API is available [here](https://github.com/VROOM-Project/vroom/blob/master/docs/API.md).

### Frontend

I created a basic frontend with Streamlit to generate a JSON code, which can be used to call VROOM. All you have to do is add vehicles and Jobs. An example is shown below, but please get creative and see how the system works. VROOM works with a help of an API call with a JSON.

Make sure you have `streamlit`, `folium`, `streamlit-folium` installed.

1. `cd Frontend`
2. `streamlit run JSONGenerator.py`
3. A new tab should open which shows the JSON generator and a map which shows the generated route for each vehicle.


### Example Coordinates

| Vehicles    |                      |                            |        |                     |                      |                   |
|-------------|----------------------|----------------------------|--------|---------------------|----------------------|-------------------|
| Vehicle 1   | Start Longitude:     | 77.70228200000001          |        | End Longitude:      | 77.70228200000001    |                   |
|             | Start Latitude:      | 12.7831358                 |        | End Latitude:       | 12.7831358           |                   |
|             | Capacity:            | 400                        |        | Start Time Window:  | 1600416000           |                   |
|             |                      |                            |        | End Time Window:    | 1600426800           |                   |
| Vehicle 2   | Start Longitude:     | 77.70228200000001          |        | End Longitude:      | 77.70228200000001    |                   |
|             | Start Latitude:      | 12.7831358                 |        | End Latitude:       | 12.7831358           |                   |
|             | Capacity:            | 4                          |        | Start Time Window:  | 1600416000           |                   |
|             |                      |                            |        | End Time Window:    | 1600426800           |                   |
|-------------|----------------------|----------------------------|--------|---------------------|----------------------|-------------------|
| Jobs        |                      |                            |        |                     |                      |                   |
| Job 1       | Delivery:            | 2                          |        | Service:            | 300                  |                   |
|             | Longitude:           | 77.7537243                 |        | Latitude:           | 13.0452482           |                   |
| Job 2       | Delivery:            | 2                          |        | Service:            | 300                  |                   |
|             | Longitude:           | 77.656476                  |        | Latitude:           | 13.0521424           |                   |
| Job 3       | Delivery:            | 1                          |        | Service:            | 300                  |                   |
|             | Longitude:           | 77.4538699                 |        | Latitude:           | 13.068898            |                   |
|             | Time Window Start:   | 1600416000                 |        | Time Window End:    | 1600423200           |                   |
| Job 4       | Delivery:            | 1                          |        | Service:            | 300                  |                   |
|             | Longitude:           | 77.4971795                 |        | Latitude:           | 12.9234009           |                   |
|             | Time Window Start:   | 1600416000                 |        | Time Window End:    | 1600423200           |                   |
| Job 5       | Delivery:            | 3                          |        | Service:            | 300                  |                   |
|             | Longitude:           | 77.47897809999999          |        | Latitude:           | 12.9097719           |                   |



### References:

Source: https://medium.com/@fbaierl1/setting-up-vroom-osrm-with-docker-compose-c8dc48d0cb2a </br>
OSRM Running API: https://github.com/Project-OSRM/osrm-backend

If you managed to follow my instructions until here, you must be really interested in my work; Please create pull requests and raise issues which will help me in perfecting my code! ✨