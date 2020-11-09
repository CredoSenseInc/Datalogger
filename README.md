#Datalogger

In this file we've created a mysql table and connected it to the django app. Created a table and Insert data from post man and esp.
Process:

    Create project
    Create app
    Change Settings $ localhost $ template $ static url $ installed apps $ timeZone(if needed)
    models.py $ define class & database data table
    templates
    makemigrations & migrate
    create views
    create app urls
    connect app urls to project urls
    Test it
    Add rest_api to post, get, pull
    Add Serializer
    Edit Admin if needed

#Error

#Port eroor: The port is alredy in use Solve: sudo fuser -k 8000/tcp

#database will be created having appname_modelclass

#DateTimeField:- Y-M-D H-M-S
