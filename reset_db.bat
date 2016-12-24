REM Windows only!

REM delete database and migration files
del db.sqlite3
del subscriptions_lib\migrations\*
del sendasubscription\migrations\*
del subscriptions_dir\migrations\*

REM regenerate migration files and database based on current models
python manage.py makemigrations subscriptions_lib
python manage.py makemigrations sendasubscription
python manage.py makemigrations subscriptions_dir
python manage.py migrate

REM populate database
pushd subscriptions_lib
call load_fix.bat
popd

REM All done