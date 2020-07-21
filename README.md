### About
My (Lukas van den Berk) portfolio website. Currently hosted at lukashisprojects.rocks/
### Installation 
Make sure you add a .env file with the following content.
```env
MYSQL_DATABASE=db_name
MYSQL_ROOT_PASSWORD=password
MYSQL_USER=user
MYSQL_PASSWORD=password
IS_LIVE=false
```
To run this project make sure docker and docker-compose is installed.
Simple then run
```bash
docker-compose up --build
```
The build flag is for building and is only needed the first time.
