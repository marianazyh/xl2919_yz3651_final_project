# xl2919_yz3651_final_project
## Project Description
In this web application, the user can import the [2018 Central Park Squirrel Census data](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw) and view the squirrel data on it. In addition, the user can add a new squirrel sighting or update an existing squirrel sighting. The modified dataset can be exported as a CSV file to keep a local record. Below is a detailed list for commands and features of our project and web application:

1. Import command:
```
$ python manage.py import_squirrel_data /path/to/file.csv
```
2. Export command:
```
$ python manage.py export_squirrel_data /path/to/file.csv
```
3. View the location of squirrel sightings on a map:
   - Locate at: ```/map```
4. View the list of all squirrel sightings:
   - Locate at: ```/sightings```
5. Update a particular squirrel sighting:
   - Locate at: ```/sightings/<unique-squirrel-id>```
6. Add a new squirrel sighting:
   - Locate at: ```/sightings/add```
7. View the general sightings statistics:
   - Locate at: ```/sightings/stats```



## Group Information
- Project Group 57, Section 2
- UNIs: [xl2919, yz3651]



## Link to directly view squirrel sightings
- [Link1](https://skilled-axis-255500.appspot.com/sightings)
- [Link2](https://final-project-261303.appspot.com/sightings)
