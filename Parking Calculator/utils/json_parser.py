import json


class JsonParser:
    def __init__(self, file_path: str):
        self._file_path = file_path

    def load_json_data(self):
        """
        Loads data from a JSON file.

        :param file_path: Path to the JSON file.
        :return: List of test data dictionaries.
        """
        with open(self._file_path, 'r') as file:
            return json.load(file)
