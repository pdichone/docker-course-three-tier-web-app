# Run the mysql db
docker run id/name_of_image  # This should start a mysql connection

# While the connection is open, open a new terminal so we can interact with bash in the container
docker exec -it containername/id /bin/bash # or /bin/sh


# We should now be inside our container
ls # check the file structure, there should be all the files and folders

# CD into the 'docker-entrypoint-init.d' to verify the .sql file in there
cd docker-entrypoint-init.d  

# CD out of the folder, and acces mysql
cd ..
mysql -proot # attach the password, which is root

# Now we are using mysql database, so we can check the databaes, tables etc..
# Let's show all databases available
show databases;

# Pick our database
use quote;

# Show tables (shows quotes table)
show tables;

# Query the table (should see some data)
select * from quotes;



