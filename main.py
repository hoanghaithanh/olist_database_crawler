import datetime
import logging
import os
import sqlite3
from sqlite3 import Connection

import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi

FORMAT = '%(asctime)s %(levelname)s %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)


def download_olist_dataset(parent_folder, dataset):
    api = KaggleApi()
    # Authenticate using kaggle.json file in KAGGLE_CONFIG_DIR folder
    api.authenticate()

    # Download all files in dataset to parent_folder
    api.dataset_download_files(dataset=dataset, path=parent_folder, unzip=True)


def build_table(conn: Connection, filepath):

    logging.debug(f'File path: {filepath}')
    filename = os.path.basename(filepath)
    table_name = filename.split('.')[0]
    df = pd.read_csv(filepath)
    column_list = df.columns.values.tolist()

    query = f"""
    CREATE TABLE {table_name} ({','.join(column_list)});
    """
    logging.debug(f'Query: {query}')

    conn.execute(query)
    df.to_sql(filename, conn, if_exists='replace', index=False)


def build_database(filepath, dataset_folder):
    conn = sqlite3.connect(filepath)

    for file in os.listdir(dataset_folder):
        build_table(conn, os.path.join(dataset_folder, file))

    conn.close()


def main():
    TMP_DIR = 'tmp'
    DATABASE_FILE = 'database/olist.db'

    target_dir_name = datetime.datetime.now().strftime('%Y%m%d')
    target_dir_path = os.path.join(TMP_DIR, target_dir_name)

    if os.path.isdir(target_dir_path):
        logging.warning(f'Folder {target_dir_name} already existed in {TMP_DIR} folder, abort!')
        return

    os.mkdir(target_dir_path)
    download_olist_dataset(target_dir_path, 'olistbr/brazilian-ecommerce')

    build_database(DATABASE_FILE, target_dir_path)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
