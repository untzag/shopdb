# shopdb 

To prepare (starting with Ubuntu 20.04)
```
$ apt install docker.io
$ apt install docker compose
```

This machine needs the following ports to be open to the campus network:
- 80 (http)
- 443 (api)

To run locally (for development)
```
$ docker-compose up --build
```
You can ommit the build flag if you don't need to rebuild your node.js app.

To run on production, first make sure you edit the contents of the secrets directory.
Then:
```
$ docker-compose up -d --build
```
