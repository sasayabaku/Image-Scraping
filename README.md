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