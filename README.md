# AsiaMarket
``` docker-compose exec app sh -c "python manage.py loaddata products" ```

# Start The Project
``` bash run-local.sh ```

# Check container run
``` docker ps```

# Run Frontend
``` docker-compose exec frontend sh -c "npm run serve" ```

# Run Backend
``` docker-compose exec app sh -c "python manage.py makemigrations && python manage.py migrate && python manage.py initdb && python manage.py runserver 0.0.0.0:8000" ```

# Database Connection
``` 
port: 5433
database_name: asiamarket
user: adminmarket
password: postgres15
```
