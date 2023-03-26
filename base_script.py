import json
import os


class ConfigLoader:
    """
    The Base class for the api_tests test scripts to load config
    """

    def __init__(self):
        # Loading the config data
        self.config_data = self.load_json()

        # Loading Host config data
        self.host_config_data = self.config_data.get('host_config')
        self.web_protocol = self.host_config_data.get('web_protocol')
        self.web_host = self.host_config_data.get('web_host')
        self.api_ver = self.host_config_data.get('api_ver')

        # Loading Headers
        self.headers = self.config_data.get('headers')
        self.headers_type = self.headers.get("Content-Type")

        # Loading api_tests endpoints
        self.user = self.config_data.get('api_endpoints').get('user')
        self.create_single_user = self.user.get('create_single_user')
        self.create_multiple_users = self.user.get('create_multiple_users')
        self.get_user_details = self.user.get('get_user_details')
        self.update_user_details = self.user.get('update_user_details')
        self.delete_user_details = self.user.get('delete_user_details')

        # Custom Logger
        self.log_level = self.config_data.get('log_settings').get('log_level')
        self.log_dir_name = self.config_data.get('log_settings').get('log_dir_name')
        self.file_write_mode = self.config_data.get('log_settings').get('file_write_mode')

    @staticmethod
    def load_json():
        """
        Loads the JSON config file
        Returns: The config file data as dict
        """
        config_file_path = os.path.join(os.path.dirname(__file__), 'api_config.json')

        with open(file=config_file_path, mode='r', encoding='utf-8') as file:
            config_data = json.load(file)
        return config_data
