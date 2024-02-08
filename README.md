# Test for Cybellum

Application for Python senior developer position. Task was to generate backbone of blog application

## How to start

Tools dependends only on docker-compose. Configuration is passed via `.env` file. Example is provided, you can just copy it to `.env`. Then run `docker-compose up`. It will instantiate both server and database container. DB uses persistent volume, so data is saved between restarts until manual volume delete. Server starts at `127.0.0.1:5000` address, which is used in sample commands

## How to use

First of all, create at least one user:

`curl -X POST http://127.0.0.1:5000/user -d '{"username": "admin", "password": "admin", "email":"admin@example.com"}'`

Then login:

`curl -X POST --cookie cookie.txt --cookie-jar cookie.txt http://127.0.0.1:5000/login -d '{"username": "admin", "password": "admin"}'`

For now, you can create records:

`curl -X POST http://127.0.0.1:5000/post --cookie cookie.txt --cookie-jar cookie.txt -d '{"title": "Post title", "content": "Post content"}'`

`curl -X POST http://127.0.0.1:5000/comment/1 --cookie cookie.txt --cookie-jar cookie.txt -d '{"content": "Comment content"}'`

And read them:

`curl  http://127.0.0.1:5000/post --cookie cookie.txt --cookie-jar cookie.txt`

`curl http://127.0.0.1:5000/comment/1 --cookie cookie.txt --cookie-jar cookie.txt`

And check current user details:

`curl  --cookie cookie.txt --cookie-jar cookie.txt http://127.0.0.1:5000/user`

Some 404 are handled:
`curl  http://127.0.0.1:5000/post/1234 --cookie cookie.txt --cookie-jar cookie.txt`

`curl http://127.0.0.1:5000/comment/12345 --cookie cookie.txt --cookie-jar cookie.txt`

To logout, call:

`curl -X DELETE --cookie cookie.txt --cookie-jar cookie.txt http://127.0.0.1:5000/login`