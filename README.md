# SEP-app-api
SEP app api source code

clone project ../sep-app-api && cd ../sep-app-api

docker-compose build

docker-compose run app sh -c "python manage.py createsuperuser"

#open new terminal
cd ../sep-app-api
docker-compose up

go to http://127.0.0.1:8000/admin/
http://127.0.0.1:8000/api/user
