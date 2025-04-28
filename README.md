# Image-Scraping

Python Web Scraping Module. based  

* BeautifulSoup4
* img2pdf

![](./docs/thumbnail.png)

## Quick Start

```bash
# Launch server
$ docker compose up

# Get Image List
$ curl -X POST -H "Content-Type: application/json" -d '{"url":"https://example.com"}' http://localhost:9999/listup

# Generate PDF from selected images
$ curl -X POST -H "Content-Type: application/json" -d '{"uuid": "11213421-21632-4132", "indexes": ["1", "4", "6"]}'
```

On `Generate PDF from selected images`  
`uuid` is returned from response of  `Get Image List API`.

# Use with Web Application

This Repository is only Python backend program.  

If you want to use web application.
Please pull [Imgae-Scraping-Web](https://github.com/sasayabaku/Image-Scraping-Web) Repository in here.

## Step1. Put Web Application Repository

Directory Architechture

```
Image-Scraping/
┝ Image-Scraping-Web/
┝ ・・・
┝ src/
┝ ・・・
┗ README.md
```

## Step2. Launch both application

Uncomment `web` in `docker-compose.yml` 

```yml
web:
    build:
        context: ./Image-Scraping-Web
        dockerfile: Dockerfile
    image: scraping-web
    container_name: scraping-web

    ports:
        - "3000:3000"

    tty: true
```

and Launch 

```bash
$ docker compose up
```