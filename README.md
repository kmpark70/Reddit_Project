# Reddit ETL Pipe Line Project

This project provides a comprehensive data pipeline solution to ETL Reddit data into a AWS Redshift data warehouse. The pipeline leverages a combination of tools and services including Apache Airflow, Celery, PostgreSQL, Amazon S3, AWS Glue, Amazon Athena, and Amazon Redshift.

## Prerequisites
- AWS Account with appropriate permissions for S3, Glue, Athena, and Redshift.
- Reddit API Credentials, you need to get the own reddit_secret_key and reddit_client_id.
- Docker Installation
- Python 3.9, It might not work if the version is lower or higher.
- Apache Airflow Fernet Key (specific secret key)
- PostGreSQL

## How to get Apache Airflow Fernet Key
Open the Python and print the below code.
- Referecned by https://cryptography.io/en/latest/fernet/
- Once you run this code, you will get the fernet key and keep it in secured place!
```bash
from cryptography.fernet import Fernet

fernet_key = Fernet.generate_key()
print(fernet_key.decode())
```

## How to get Reddit API
https://www.geeksforgeeks.org/how-to-get-client_id-and-client_secret-for-python-reddit-api-registration/![image](https://github.com/kmpark70/Reddit_Project/assets/72221217/1f6d8697-d575-43e4-b266-9ff9e8b94871)

## How to change username and password in Apache Airflow
1. Go to Docker.compose.yml and find the below lines.
```bash
  airflow-init:
    <<: *airflow-common
    command: >
      bash -c "pip install -r /opt/airflow/requirements.txt && airflow db init && airflow db upgrade && airflow users create --username admin --firstname admin --lastname admin --role Admin --email airflow@airflow.com --password admin"
    restart: "no"
```
2. You can change the username and password. Initially, we set id and password are admin.

## System Setup
1. Clone the repository.
```bash
https://github.com/kmpark70/Reddit_Project.git
```
2. Create a virtual environment.
```bash
python-3 -m venv venv
```
3. Activate the virtual environment.
```bash
On windows:
myenv\Scripts\activate
```
```bash
On MacOS/Linux:
source venv/bin/activate
```
4. Install the dependencies.
```bash
pip install -r requirements.txt
```
5. Create a folder named config and place the config.conf.example file inside that folder.
- If Broken.DAG issue occurs
```bash
.../config/config.conf.example
```
6. Starting the containers
```bash
docker-compose up -d --build
```
7. Launch the Airflow web UI.
```bash
open http://localhost:8080
```

## Data Preparation and Setup
1. Specify the database system(s) and version(s) used, along with installation instructions (a link to official documentation will be enough).
- PostGreSQL, makesure the portnumber: 5432
- AWS S3, Redshift, referenced by https://pypi.org/project/s3fs/
2. Describe how to acquire project data. Include a small dataset sample (< 5 MB) or provide scripts to download/scrape/process the data.
3. How do we load this data into the database system?
- When you open the data folder, you'll find input and output as sub-folders. The input folder contains the raw log files, while the output folder contains the result of the ETL process, which is a CSV file.
- You can download those files.
4. Do you have some scripts to do that? If so, how do we execute them?
- Please follow the installation guide above.
5. Did you use some tools for loading? If so, provide appropriate details and links.
- We don't use any tools for loading, but when it comes to parquet file in AWS, you can download in AWS ecosystem.
If you are benchmarking different database systems, detail any configuration modifications made.
- You have to follow the port number and PostgreSQL due to our initial configuration.
If generating your own data, include a sample of the synthetic dataset/database.
- We don't use any our own data, The data is from the Real-time Reddit API.
