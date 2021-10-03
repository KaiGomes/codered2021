import json
import mysql.connector

class DB:
    def __init__(self):
        # IP Adress must be added to Google Cloud Platform in order to access
        self.mydb = mysql.connector.connect(
            host="34.136.217.172", user="root", password="codered2021")
        self.mycursor = self.mydb.cursor(dictionary=True, buffered=True)
        self.mycursor.execute('USE codered;')

    def DropTable(self, table_name: str) -> None:
        self.mycursor.execute("DROP TABLE IF EXISTS " + str(table_name) + ";")
        self.mydb.commit()

    def CreateAccidentTable(self):
        command = "CREATE TABLE IF NOT EXISTS accidents (" \
                  "accident_id INT NOT NULL AUTO_INCREMENT, " \
                  "severity INT NOT NULL, " \
                  "start_time TIMESTAMP NOT NULL, " \
                  "start_lat FLOAT NOT NULL, " \
                  "start_long FLOAT NOT NULL, " \
                  "end_lat FLOAT NOT NULL, " \
                  "end_long FLOAT NOT NULL, " \
                  "distance FLOAT, " \
                  "description VARCHAR(255), " \
                  "number VARCHAR(255), " \
                  "street VARCHAR(255) NOT NULL, " \
                  "city VARCHAR(255) NOT NULL, " \
                  "state VARCHAR(255) NOT NULL, " \
                  "zipcode VARCHAR(255) NOT NULL, " \
                  "PRIMARY KEY (accident_id));"
        # print(command)
        self.mycursor.execute(command)
        self.mydb.commit()

    def InsertAccidents(self, values):
        command = "INSERT INTO accidents(severity, start_time, start_lat, start_long, end_lat, end_long, distance, "\
                  "description, number, street, city, state, zipcode) VALUES " + values + ";"
        self.mycursor.execute(command)
        self.mydb.commit()
    
    def QueryAccidents(self, route_coords, threshold):
        # lat_coords = [coords[0] for coords in route for route in route_coords]
        # lng_coords = [coords[1] for coords in route for route in route_coords]    
        coords = '(' + '),('.join([str(coord[0]) + ',' + str(coord[1]) for coord in route_coords]) + ')'
        self.mycursor.execute("drop table if exists tmp;")
        self.mydb.commit()
        self.mycursor.execute("create temporary table tmp (lat float not null, lng float not null);")
        self.mydb.commit()
        self.mycursor.execute("insert into tmp values" + coords + ";")
        command = "select severity from accidents where exists (select * from tmp where (accidents.start_lat between " \
                  "tmp.lat - " + str(threshold) + " and tmp.lat + " + str(threshold) + ") and (accidents.start_long between " \
                  "tmp.lng - " + str(threshold) + " and tmp.lng + " + str(threshold) + "));"
        self.mycursor.execute(command)
        return self.mycursor.fetchall()

    def AccidentsCount(self):
        self.mycursor.execute("Select COUNT(*) FROM accidents;")
        return self.mycursor.fetchall()