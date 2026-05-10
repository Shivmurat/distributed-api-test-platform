import json
import os
from xml.etree.ElementTree import indent


class Filereader:

    @staticmethod
    def read_jason(file_path):

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"JSON file not found: {file_path}")

        with open(file_path, "r") as file:
            return json.load(file)
