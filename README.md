## AntiKor


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
* `pip install -r requirements.txt`
* `cd app`
* `python __main__.py`

