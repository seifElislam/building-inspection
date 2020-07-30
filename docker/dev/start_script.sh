if [ $1 -eq 1 ]
then
    sleep 20
fi
echo " >> installing dev requirements.."
pip install -r requirements/dev.txt
echo " >> starting app.."
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
