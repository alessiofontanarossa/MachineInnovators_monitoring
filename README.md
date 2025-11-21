# MachineInnovators_monitoring

This repository contains the elements of the final project of the course *MLOps e Machine Learning in Produzione*. 

We want to automatically monitor the online reputation of an agency. To do so, we use an [HuggingFace model](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest) which classify the reviews as negative, neutral or positive. The project is structured as follows:

- **.gitignore**: to ignore the virtual environment 'new_env' created with venv;
- **requirements.txt**: obtained (and later manually modified) with 'pip freeze > requirements.txt'. Note: The file was manually optimized to use the CPU-only version of PyTorch, significantly reducing the Docker image size;
- **src**: this folder contains the model logic (model.py), the API logic (main.py) and a file to make POST requests (inference.py). The API contains: 
    - a POST method, to simulate the arrival of new reviews on the agency website. Contemporarily, a CSV file is updated, containing all the old and new reviews. This CSV, named 'sentiment.csv', is then exposed;
    - a GET method, to expose the CSV. In this way, Grafan can automatically read the CSV content using the Infinity plugin (see later).
- **data**: this folder contains the csv file 'sentiment.csv';
- **tests**: this folder contains tests (to be run with pytest) for the important logic contained in the 'src' folder. In particular, 'patch' has been used. Otherwise, each test would have modified the 'sentiment.csv';
- **Dockerfile**, contains the instructions to build the container image, set up the environment, and serve the application with Uvicorn;
- **.github/workflows**: here there is the .yml used to define the github actions. In particular, since we worked on a single branch (main branch), we required that for each push on the main the CI and the CD part are triggered. The CI part run all the relevant tests. If and only if the tests are succesful, the container is pushed on the hub;
- **docker_compose.yml** this file contains the instruction to link the app (downloaded from the HUB) and Grafana. On Grafana, for which the Infinity plugin is installed, we can use the link ' http://backend_api:8080/obtain_csv' to import the CSV data (once the default JSON has been changed to CSV, of course). The Grafana visualization, as a pie chart for example, is updated automatically when a new POST request is done to the app.