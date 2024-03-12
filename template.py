import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO)

project_name='practice'
list_of_files=[
    "requirements.txt",
    'main.py',
    'Dockerfile',
    'setup.py',
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/utils.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_building.py",
    f"src/{project_name}/components/model_monitring.py",

    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipiline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
]

for file_path in list_of_files:
    file_path=Path(file_path)
    file_dir,file_name=os.path.split(file_path)
    print(f"dir=> {file_dir} => {file_name}")
    # creating the directory if not exits
    if(file_dir and not os.path.isdir(file_dir)):
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"Creating directory {file_dir} with file name {file_name}")

    # creating the file if not exits
    elif(not os.path.isfile(file_path) or (os.path.getsize(file_path))==0 ):
        logging.info(f"Creating the empty file {file_name}")
        with open(file_path,'w') as f:
            pass
        logging.info(f"crating {file_name} successfully")
    else:
        logging.info(f"{file_name} already exists")
