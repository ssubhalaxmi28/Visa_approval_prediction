import os
from pathlib import Path #this path will work on each operating system

project_name="us_visa" #root folder

list_of_files=[
    f"{project_name}/__init__.py", #inside this root folder i should have the constructer file 
    f"{project_name}/components/__init__.py", 
    f"{project_name}/components/data_integration.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipline/__init__.py",
    f"{project_name}/pipline/training_pipeline.py",
    f"{project_name}/pipline/prediction_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
     
     "app.py",
     "requirements.txt",
     "Dockerfile",
     ".dockerignore",
     "demo.py",
     "setup.py",
     "config/model.yaml",
     "config/schema.yaml"

     
]

for filepath in list_of_files:
    filepath=Path(filepath) #converting each file into paths
    filedir,filename=os.path.split(filepath) #to eparate the above folder and files, ex:separe component folder and data_integration.py file
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
    else:
        print(f"file is already preent at: {filepath}")
