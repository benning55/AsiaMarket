# AsiaMarket

# Start The Project
``` bash run-local.sh ```

# Run Frontend
``` docker-compose exec frontend sh -c "npm run serve" ```

# Run Backend
``` docker-compose exec app sh -c "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000" ```

# Create Database
``` docker-compose exec app sh -c "python manage.py makemigrations && python manage.py migrate" ```
