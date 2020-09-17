kill -9 $(lsof -t -i:5000)
rm nohup.out
git pull https://github.com/SouravDatta1995/JuteCultivationApp.git
source /venv/bin/activate
nohup uvicorn main:app --reload --host 0.0.0.0 --port 5000 &
deactivate
