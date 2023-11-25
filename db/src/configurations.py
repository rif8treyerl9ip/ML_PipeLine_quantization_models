import os

import json

file_path = r'C:\Users\thyt\confidential_files\Postgresql\config.json'

# JSONファイルの読み込み
with open(file_path, 'r', encoding='utf-8') as file:
    config = json.load(file)

class DBConfigurations:
    postgres_username =config['POSTGRES_USER']
    postgres_password =config['POSTGRES_PASSWORD']
    postgres_port = int(config['POSTGRES_PORT'])
    postgres_db =config['POSTGRES_DB']
    postgres_server =config['POSTGRES_SERVER']
    sql_alchemy_database_url = (
        f"postgresql://{postgres_username}:{postgres_password}@{postgres_server}:{postgres_port}/{postgres_db}"
    )


class APIConfigurations:
    title = os.getenv("API_TITLE", "Model_DB_Service")
    description = os.getenv("API_DESCRIPTION", "machine learning system training patterns")
    version = os.getenv("API_VERSION", "0.1")


