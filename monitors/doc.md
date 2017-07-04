# docker run -p 8083:8083 -p 8086:8086 influxdb
_GET  /monitors  		 => All available monitors

POST /monitors  		 => Add new monitors

GET, PUT, DELETE  /monitors/<id> => Get, Update, Delete a monitor

Base monitors :
availableMonitors
{
    id :          1
    name :        http_monitor
    description : monitoring du protocol HTTP, send HTTP GET request every x second | monitoring du ssl certificate every x second
    configuration : {
	url  : string ( url type )
	time : default 5 second
	email: [list of email]
	twitter:  twiter account
	phone :   phone number
    }
}

monitors
{
    id          : id in table
    name         : name of monitor
    type         : type of monitor example http_monitor
    user         : name of user
    status       : Up, Down, Ok , not Ok, expired ...
    date         : date of check
    wasNotified  : user was notified or not
    notifiedWith : mean of notification email, twitter ...
    extra        : extra information ( for ssl the date when certificate expire )
}


Users
{
    id:
    name:
    ...
    monitors : list of names or ids

}

GET /users/{userId}/monitors/{monitorId} all client's monitors
