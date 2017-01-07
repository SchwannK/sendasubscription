del db.sqlite3
del subscriptions_lib\migrations\*
del sendasubscription\migrations\*
del subscriptions_dir\migrations\*

python manage.py makemigrations subscriptions_lib
python manage.py makemigrations sendasubscription
python manage.py makemigrations subscriptions_dir
python manage.py makemigrations faq
python manage.py migrate

call subscriptions_lib\load_fix.bat

python manage.py loaddata sites
