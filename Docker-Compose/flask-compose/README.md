### App.py

- A python file to describe my flask application.

- For the `get_hits_counts` function :

- Configurable Retries:

    The `retries` parameter allows you to specify how many times the function should retry the operation before giving up.

- Configurable Sleep Time:

    The `initial_delay parameter` lets you set the initial wait time between retries.
    The `backoff_factor` parameter allows for exponential backoff, meaning the wait time increases exponentially after each failed attempt (e.g., 0.5s, 1s, 2s, etc.).

- Logging:

    Added logging to monitor retries and failures. The `logger` provides information about each retry attempt, including which attempt it is and how long it will wait before trying again.
    If all retries fail, an error message is logged before the exception is raised.


### Docker compose commands

```
docker compose up
docker compose down
docker compose ps
docker compose web env
```

- We use  `gunicorn` since it is capable of handling real users, higher traffic, and security concerns.

### Nginx configuration
- Create a new file via nano: `sudo nano /etc/nginx/sites-available/flask_app`
- inside the the file paste the following while adjusting the paths and domain names as necessary:

```
server {
    listen 80;
    server_name your_domain.com;  # Replace with your domain or IP

    location / {
        proxy_pass http://127.0.0.1:8000;  # Forward requests to Gunicorn
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static/ {
        alias /path/to/static/files;  # Replace with the actual path to your static files
    }
}

```

- To save Press `Ctrl+o` and `Enter`
- To exit `CTRL+X`

- Enable configuration `sudo ln -s /etc/nginx/sites-available/flask_app /etc/nginx/sites-enabled/`

- Test the nginx configuration to ensure no errors: `sudo nginx -t`
- To restart and apply change : `sudo systemctl restart nginx`

### Secure your application 

- Install certbot for HTTPS:
```
sudo apt-get install certbot python3-certbot-nginx
sudo certbot --nginx -d your_domain.com
```
- follow the installation 

- `docker-compose up --build`
