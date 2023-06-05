cat test_on_start/name.txt
echo -e "\n"
sleep 1
cat test_on_start/mem_ansi
echo -e "Test API version 0.0.0\n\n"
sleep 2
export a=`python3 test_on_start/check_venv.py`
sleep 1
if [[ "$a" == "1" ]]; then
    echo -e "\033[42m\033[30m venv is exist \033[0m"
    echo -e "\033[43m\033[30m check new-requirements... \033[0m \n"
    requirements=`pip install -r requirements.txt `
    echo -e "\033[42m\033[30m all requirements done \033[0m"
    echo -e "\033[43m\033[30m check .env \033[0m \n"
    python3 test_on_start/check_venv.py 
    echo -e "\033[45m All done. Start django-server... Wait tests \033[0m"
    source venv/bin/activate
else
    echo "\033[41m\033[30m venv not exist \033[0m"
    echo "\033[43m\033[30m Setting venv..."
    venv=`python3 -m venv venv`
    echo "\033[43m\033[30m installing requirements..."
    requirements=`pip install -r requirements.txt`
    echo "\033[43m\033[30m create .env"
    python3 test_on_start/check_venv.py 
    
    source venv/bin/activate
fi


python3 DRFapi/manage.py runserver 0.0.0.0:8000 & python3 test_on_start/route_test.py && fg

