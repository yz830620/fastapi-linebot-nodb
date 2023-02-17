# fastapi-linebot-nodb

This project focus on creating a fastapi for the web framework and user able to use linebot as frontend client
there are few more constrains adding to this project

1. no db: I will try to use a file-base storage system to record my result. And save the data locally.
2. cache all the data in ram. only read from file if the system is crashed
3. test driven
4. add docker to manage env
5. since my cloud dev env is not ready. (cloudcone has connection issue) I'm going to develop by mac
