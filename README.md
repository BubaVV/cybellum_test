# cybellum_test

curl -X POST http://127.0.0.1:5000/user -d '{"username": "admin", "password": "admin", "email":"admin@example.com"}'

curl -X POST http://127.0.0.1:5000/post --cookie cookie.txt --cookie-jar cookie.txt -d '{"title": "Post title", "content": "Post content"}'
curl -X POST http://127.0.0.1:5000/comment/1 --cookie cookie.txt --cookie-jar cookie.txt -d '{"content": "Comment content"}'
curl -X POST http://127.0.0.1:5000/user -d '{"username": "user_1", "password": "pass123", "email":"user@example.com"}'

curl -X POST --cookie cookie.txt --cookie-jar cookie.txt http://127.0.0.1:5000/login -d '{"username": "admin", "password": "admin"}'

curl -X DELETE --cookie cookie.txt --cookie-jar cookie.txt http://127.0.0.1:5000/login