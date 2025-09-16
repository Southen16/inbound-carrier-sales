# Inbound Carrier Sales - Local Development Setup


## 2. Install dependencies

Activate your virtual environment (recommended):
```
. .venv/Scripts/Activate.ps1  # PowerShell
```
Or use your Python executable directly:
```
C:/learning-space/inbound-carrier-sales/.venv/Scripts/python.exe -m pip install -r requirements.txt
```
Or simply:
```
pip install -r requirements.txt
```

## 3. Run the app locally with Flask

Set environment variable for Flask app:
```
$env:FLASK_APP="app.py"
```
Then start the app:
```
flask run
```
This will start the app at `http://localhost:5000`.


## 4. Access the app

Open your browser and go to:
```
http://localhost:5000/carriers
```

---
