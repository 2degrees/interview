# 2degrees interview project

## Tasks
### 1. Implement a way to get each Buyer's total CO<sub>2</sub> emission

The value is equivalent of the buyer's own emission plus all of its suppliers emission applicable to a given buyer

For example:

- Buyer's emission is 1 tCO<sub>2</sub>e
- Buyer has two suppliers
  - Supplier 1 has 0.2 tCO<sub>2</sub>e; 50% of its production goes to Buyer
  - Supplier 2 has 2 tCO<sub>2</sub>e; 10% of its production goes to Buyer
    
1 tCO<sub>2</sub>e + (0.2 tCO<sub>2</sub>e * 0.5) + (2 tCO<sub>2</sub>e * 0.1) = 1.3 tCO<sub>2</sub>e

### 2. Code review

Imagine that the app `authn` has just been sent to you for review. What points would you raise?

## How to run:

Prerequisites: 
* [Docker](https://docs.docker.com/install/)
* [docker-compose](https://docs.docker.com/compose/install/)

1. Clone this repo & `docker-compose build`
2. `docker-compose up web` starts the web application on (the host's) port 8080
3. `docker-compose run console` allows you to run commands within the container: `docker-compose run console python manage.py test`

## Structure

* `src` contains your django application. It also has a `bin` folder for
scripts you might want to run (even in prod)
* `web` contains a sample `nginx.conf` file, and a `static` folder where you can put
your js/css/whatever files.

For static files defined in the Django app, the path will be `server/static/resource.ext` (`/static` is defined in `settings.py`).
For all other assets, it'll be the subfolder names only in `web/static`. 
Example: js files will be `server/js/hello.js` not `server/static/hello.js` nor `sever/static/js/hello.js`
