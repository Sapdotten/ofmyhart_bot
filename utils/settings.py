import os
import logging

from dotenv import load_dotenv

class Settings:
    """Class for reading setting from envieroment
    """
    TOKEN = "BOT_TOKEN"
    ADMIN = 'ADMIN_ID'
    @classmethod
    def load_data_from_file(cls):
        """tries to read data from file into environment
        """
        dotenv_path = os.path.join(os.getcwd(), '.env')
        if os.path.exists(dotenv_path):
            load_dotenv(dotenv_path)
            logging.info("Data from ebv has been uploaded to environment")
        else:
            logging.warning("Script didn't find .env file to upload file to environment")
            
    @classmethod
    def get_token(cls):
        return os.getenv(cls.TOKEN)
    @classmethod
    def get_admin_id(cls):
        return os.getenv(cls.ADMIN)
            
            