#!/bin/bash

clear

echo "Restarting..."
wait
echo "Erasing eventSearch and EventDetails /migrations/"
wait
rm -rf eventSearch/migrations/ EventDetails/migrations/ userCreateEvents/migrations/
wait
echo "Deleting old database..."
wait
rm db.sqlite3
wait
echo "Creating new migrations and migrating models"
wait
python manage.py makemigrations eventSearch EventDetails userCreateEvents
wait
python manage.py migrate 
wait
echo "Starting up server..."
wait
python manage.py runserver 0:8000
wait
