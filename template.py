import os
import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s || %(levelname)s || %(message)s]'
)

while True:
    project_name = input("Enter Project name: ")
    if project_name !="":
        break

logging.info(f"Project folder created: {project_name}")

#List of folders and files required for the project
list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/dataingestion.py",
    f"{project_name}/components/datavalidation.py",
    f"{project_name}/components/datatransformation.py",
    f"{project_name}/components/modeltraining.py",
    f"{project_name}/components/modelevaluation.py",
    f"{project_name}/components/modelpusher.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entities/__init__.py",
    f"{project_name}/config.py",
    f"{project_name}/exception.py",
    f"{project_name}/logger.py",
    f"{project_name}/utils.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir , filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok= True)
        logging.info(f"New file directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"File created: {filename}")

    else:
        logging.info(f"File is already present: {filepath}")