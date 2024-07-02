import os
import logging

from dotenv import load_dotenv


class Settings:
    """Class for reading setting from envieroment"""

    ADMIN = None
    TOKEN = None
    _TOKEN = "BOT_TOKEN"
    _ADMIN = "ADMIN_ID"
    _SQL_USER = "SQL_USER"
    _SQL_PASSWORD = "SQL_PASSWORD"
    _SQL_HOST = "SQL_HOSTNAME"
    _SQL_DB_NAME = "SQL_DATABASE_NAME"

    @classmethod
    def load_data_from_file(cls):
        """tries to read data from file into environment"""
        dotenv_path = os.path.join(os.getcwd(), ".env")
        if os.path.exists(dotenv_path):
            load_dotenv(dotenv_path)
            logging.info("Data from ebv has been uploaded to environment")
        else:
            logging.warning(
                "Script didn't find .env file to upload file to environment"
            )

    @classmethod
    def get_token(cls):
        return os.getenv(cls._TOKEN)

    @classmethod
    def get_admin_id(cls):
        return os.getenv(cls._ADMIN)

    @classmethod
    def init_variables(cls):
        cls.ADMIN = cls.get_admin_id()
        cls.TOKEN = cls.get_token()

    @classmethod
    def get_sql_user(cls):
        return os.getenv(cls._SQL_USER)

    @classmethod
    def get_sql_password(cls):
        return os.getenv(cls._SQL_PASSWORD)
    
    @classmethod
    def get_sql_host(cls):
        return os.getenv(cls._SQL_HOST)
    
    @classmethod
    def get_sql_db_name(cls):
        return os.getenv(cls._SQL_DB_NAME)
