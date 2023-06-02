export a=`python3 test_on_start/check_venv.py`

echo -en "\033[10;5000;11;200]\7"

if [[ "$a" == "1" ]]; then
    echo "venv is exist"
    echo "\acheck new-requirements..."
    requirements=`pip install -r requirements.txt`
    echo "all requirements done"
    source venv/bin/activate
else
    echo "venv not exist"
    echo "Setting venv..."
    venv=`python3 -m venv venv`
    echo "installing requirements..."
    requirements=`pip install -r requirements.txt`
    source venv/bin/activate
fi


python3 DRFapi/manage.py runserver 0.0.0.0:8000 & python3 test_on_start/route_test.py && fg

