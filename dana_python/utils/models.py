import os, sys
import re
from typing import Any
from dana_python.utils.script import import_all_models

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
import_all_models(parent_dir)

all_modules = sys.modules.keys()
regex_pascal_to_snake = re.compile(r"(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])")

def get_model_from_name(*, name: str) -> Any:
        """
        Retrieves a class from dynamically imported modules based on the class name.

        :param name: The name of the class to retrieve.
        :return: The class object if found, or None.
        """
        # Convert Pascal case class name to snake case
        model_name = regex_pascal_to_snake.sub('_', name).lower()

        # Find the module containing the class name
        module_name = next(
            (module for module in all_modules if module.split('.')[-1] == model_name),
            None
        )

        if module_name:
            # Get the class from the module
            return getattr(sys.modules[module_name], name, None)

        else:
            raise ValueError("Unregistered model")
