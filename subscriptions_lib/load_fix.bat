REM Windows only!

REM populate database
python manage.py loaddata subscriptions_lib\fixtures\category_db.json
python manage.py loaddata subscriptions_lib\fixtures\company_db.json
python manage.py loaddata subscriptions_lib\fixtures\subscriptions_db.json
