from configparser import ConfigParser


config = ConfigParser()
config.read("Configurations/config.ini")

class ReadConfig:

    @staticmethod
    def get_application_url():

        return config.get(
            "common info",
            "baseURL"
        )


    @staticmethod
    def get_username():

        return config.get(
            "common info",
            "username"
        )


    @staticmethod
    def get_password():

        return config.get(
            "common info",
            "password"
        )


    @staticmethod
    def get_file_path():

        return config.get(
            "common info",
            "File_Path"
        )