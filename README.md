### About
My (Lukas van den Berk) portfolio website. Currently hosted at https://lukashisprojects.rocks/

Technology used for this project

- Django as a rest api for the backend
- Svelte with sapper for the front-end
- Docker with docker-compose to easily host and develop the site
- Cloudflare for routing
- Google analytics
- Ubuntu for the VM that runs this website (on my home server)

You may ask is docker and a seperate backend a bit overkill? Yes but I wanted this site to be easily maintainable and a little demo of what kinds of technologies I can use and how I would use them.

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
