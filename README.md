# single-api
## init
```sh
pip install -r requirements.txt
```
## run api (fastapi) using uvicorn
```sh
uvicorn api:app --reload
```
## run command-line tool
```sh
python3 cmd-app.py --help
```
### command-line tool example:
##### GET request:
```sh
python3 cmd-app.py --type GET --url http://localhost:8000
```
##### POST request:
```sh
python3 cmd-app.py --type POST --url http://localhost:8000 --filename example.json
```

### JSON file example:
Check out the "example.json" in the directory for accepted JSON format.
```json
{
    "submissions":[
        {
            "name": "Elevation of Privilege",
            "type": "Platform",
            "description": "Security Feature Bypass",
            "date": "2022-11-21"
        },
        {
            "name": "Abnormal Request Rate",
            "type": "Platform",
            "description": "Security Feature Bypass",
            "date": "2022-03-31"
        }
    ]
}
```
