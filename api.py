from fastapi import FastAPI
from typing import Dict, List

# api init
app = FastAPI()

objects = [
            {"name": "Elevation of Privilege", "type": "Platform", "description": "Security Feature Bypass", "date": "2022-01-01"},
            {"name": "Password Bruteforce", "type": "Platform", "description": "Security Feature Bypass", "date": "2022-05-06"},
            {"name": "Executable File Upload", "type": "Platform", "description": "Security Feature Bypass", "date": "2022-07-02"},
            {"name": "Abnormal IP of Privileged User Login", "type": "Platform", "description": "Security Feature Bypass", "date": "2022-02-10"},
            {"name": "Abnormal Request Rate", "type": "Platform", "description": "Security Feature Bypass", "date": "2022-12-05"},
            {"name": "Elevation of Privilege", "type": "Platform", "description": "Security Feature Bypass", "date": "2022-11-20"},
            {"name": "Abnormal Request Rate", "type": "Platform", "description": "Security Feature Bypass", "date": "2022-05-29"},
            {"name": "Executable File Upload", "type": "Platform", "description": "Security Feature Bypass", "date": "2022-04-04"},
            {"name": "Password Bruteforce", "type": "Platform", "description": "Security Feature Bypass", "date": "2022-09-19"},
            {"name": "Abnormal IP of Privileged User Login", "type": "Platform", "description": "Security Feature Bypass", "date": "2022-08-20"},
            {"name": "Abnormal Request Rate", "type": "Platform", "description": "Security Feature Bypass", "date": "2022-10-12"}
        ]

def return_objects(object_dict: dict, objects_to_append: dict = {}):
    new_list = object_dict
    if objects_to_append:
        submitted_list = objects_to_append["submissions"]
        new_list.extend(submitted_list)
    
    return {"results": new_list}

@app.get("/")
def get_objects():
    return return_objects(object_dict=objects)


@app.post("/")
def post_objects(request: Dict[str,List]):
    return return_objects(object_dict=objects, objects_to_append=request)