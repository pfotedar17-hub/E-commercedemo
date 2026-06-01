from configparser import ConfigParser
import os

config = ConfigParser()
config.read("Configurations/config.ini")

env = os.getenv("ENV","PROD")

class ReadConfig:

    @staticmethod
    def get_application_url():

        return config.get(
            env,
            "baseURL"
        )


    @staticmethod
    def get_username():

        return config.get(
            env,
            "username"
        )


    @staticmethod
    def get_password():

        return config.get(
            env,
            "password"
        )


    @staticmethod
    def get_file_path():

        return config.get(
            env,
            "File_Path"
        )