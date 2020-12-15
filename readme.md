# Flask microservices template

Created in a learning process and for quick development using websockets in microservices with docker

Mean to be as simple as possible. (KISS)

## Services
- Nginx load balancer on top of everything
- Svelte-Routify-Nginx static frontend
- REST API
- Async server with celery
- Websocket API
- Postgress database
- Redis used for message queue

## How to use
Clone the repo `git clone https://github.com/sinedie/Flask-Svelte-Websockets-Nginx-Docker.git`

Go to frontend app `cd frontend` and run `npm install` and `npm run build`

On the same folder of `docker-compose.yml` file run `docker-compose up --build`

Go to `localhost` (without setting the port)

## TODO
- Mail sending with Flask-Mail
