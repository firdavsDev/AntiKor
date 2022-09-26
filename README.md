## AntiKor


This project has the following prerequisites

- python 3.9.8
- docker 19.03.12
- docker-compose 1.25.0


- Installing docker-compose

```
- sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
- sudo chmod +x /usr/local/bin/docker-compose
- docker-compose --version
```

- Run via Docker
```
- docker-compose up --build
- docker-compose down #stop background process
```

- Run manually
* `python3 -m venv venv`
* `source venv/bin/activate`
* `pip install -r requirements.txt`
* `cd app`
* `(venv) sh start.sh` #ubuntu
* `(venv) python __main__.py` # other OS

