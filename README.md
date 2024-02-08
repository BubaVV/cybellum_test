# cybellum_test

curl -X POST http://127.0.0.1:5000/post -d '{"title": "Post title", "content": "Post content"}'
curl -X POST http://127.0.0.1:5000/comment/1 -d '{"content": "Comment content"}'
curl -X POST http://127.0.0.1:5000/user -d '{"username": "user_1", "password": "pass123", "email":"user@example.com"}'

curl --cookie cookie.txt --cookie-jar cookie.txt <url>