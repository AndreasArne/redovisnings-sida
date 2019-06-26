sudo mysql -uroot -p < infrastructure-as-code/scripts/resources/setup.sql > /dev/null

. venv/bin/activate
flask db upgrade