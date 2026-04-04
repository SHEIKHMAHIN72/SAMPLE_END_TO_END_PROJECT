''' this is also doing with cookiecutter template, but we are doing it manually to understand the structure of the project and how to create a package from scrath. this file is used to turn your project into an installable python package. this makes your machine learning pipeline modular reusable and production ready '''

import os
from pathlib import Path
import logging

print(os.getcwd())

logging.basicConfig(level=logging.INFO)

project_name = "mlops_project"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_tranier.py",
    f"src/{project_name}/components/model_monitering.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/traning_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creting directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open (filepath, "w") as f:
            pass
        logging.info(f"creating file: {filename}")


    else:
        logging.info(f"{filename} already exists")






