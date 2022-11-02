# Stores Rest API using flask-smorest

![](stores_rest_api.gif)

### Use docker to start application
<pre>
docker build -t flask-smorest-api .
docker run --name flask-api-2022 -dp 5005:5000 -w /app -v "$(pwd):/app" flask-smorest-api sh -c "flask run --host 0.0.0.0"
</pre>

### To use Flask-Migrate and create migrations
`Delete or drop any tables or database created earlier`
<pre>
flask db init
flask db migrate
flask db upgrade
</pre>

### Create a .env file with postgres access
`All databases are created with render.com`<br>
`Email service using mailgun.com`
<pre>
DATABASE_URL = postgresql://user:passwd@host:port/db
MAILGUN_API_KEY = hash-part1-part2
MAILGUN_DOMAIN = sandbox-hash.mailgun.org
REDIS_URL = rediss://user:passwd@host:6379
</pre>