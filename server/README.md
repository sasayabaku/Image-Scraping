# Scraping Script Server

server for Scraping and Convert image to pdf.

# Usage

First Set arguments in `docker-compose.yml`
```yaml
environment:
    - URL=<Target url>
    - KEYWORD=<Filter word(alt or class tag)>
```

Running Script  
After Running pdf file is generated in `src` directory.

```bash
$ docker compose run scraping-server
```