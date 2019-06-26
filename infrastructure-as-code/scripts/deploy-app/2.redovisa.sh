# cd ~ && git clone https://github.com/AndreasArne/redovisnings-sida.git
# cd redovisnings-sida 
git checkout v0.0.3
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt

echo "export FLASK_APP=me_page.py" >> ~/.profile 
cp infrastructure-as-code/scripts/resources/.env .
source ~/.profile
flask --help
