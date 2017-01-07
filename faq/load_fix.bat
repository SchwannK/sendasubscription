REM Windows only!

REM populate database
python manage.py loaddata faq\fixtures\faqcategory_db.json
python manage.py loaddata faq\fixtures\faqentry_db.json
