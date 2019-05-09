sudo mysql -uroot -p < infrastructure-as-code/1scripts/setup.sql > /dev/null

. venv/bin/activate
flask db upgrade