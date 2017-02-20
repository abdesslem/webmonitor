from influxdb import InfluxDBClient


def write(host='localhost', port=8086 , data=[]):
    user = 'root'
    password = 'root'
    dbname = 'monitors'
    dbuser = 'admin'
    dbuser_password = 'admin_password'
    client = InfluxDBClient(host, port, user, password, dbname)
    client.create_database(dbname)
    client.write_points(data)
