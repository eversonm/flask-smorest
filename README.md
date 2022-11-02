# Flask-smorest

### Use docker to start application
<pre>
docker build -t flask-smorest-api .
docker run --name flask-api-2022 -dp 5005:5000 -w /app -v "$(pwd):/app" flask-smorest-api
</pre>

### To use Flask-Migrate and create migrations
`Delete or drop any tables or database created earlier`
<pre>
flask db init
flask db migrate
flask db upgrade
</pre>