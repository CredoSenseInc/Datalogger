# Datalogger

In this file we've created a mysql table and connected it to the django app. 
Created a table and Insert data from post man and esp.

# Process:

  1.  Create project
  2.  Create app
  3.  Change Settings
        $ localhost
        $ template
        $ static url
        $ installed apps
        $ timeZone(if needed)
  4.  models.py 
        $ define class & database data table
  5.  templates
  6.  makemigrations & migrate
  7.  create views
  8.  create app urls
  9.  connect app urls to project urls
  10. Test it
  11. Add rest_api to post, get, pull
  12. Add Serializer
  13. Edit Admin if needed
  
  
  
  
 # Error 
   Port eroor: The port is alredy in use
   Solve: sudo fuser -k 8000/tcp
   
   
# database will be created having appname_modelclass
# DateTimeField:- Y-M-D H-M-S
 
