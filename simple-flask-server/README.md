## Simple flask server


#### Prepare Python virtual env

```
# git clone <this repo>
# cd Py-scripts/simple-flask-server
---
# python3 -m venv venv
# . venv/bin/activate
# python3 -m pip install --upgrade pip
# pip install flask gunicorn
```


#### Local docker build & run

```
docker build --build-arg APP_NAME=FOO -t foo:v1 .
docker build --build-arg APP_NAME=BAR -t bar:v1 .
docker run -p 3001:8001 -d foo:v1
docker run -p 3002:8001 -d bar:v1
```

and open in browser (host system): http://localhost:3002/


#### how to build image & push it to public repo
```
docker login -u hostick

# 1. Build the Image with final tag
docker build --build-arg APP_NAME=FOO -t hostick/foo:v1 .
docker build --build-arg APP_NAME=BAR -t hostick/bar:v1 .

# 2. OR rename the existing Tag to publish
docker tag foo:v1 hostick/foo:v1
docker tag bar:v1 hostick/bar:v1

# Push the Image
docker push hostick/foo:v1
docker push hostick/bar:v1

```


