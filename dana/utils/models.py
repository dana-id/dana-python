# Copyright 2025 PT Espay Debit Indonesia Koe
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os, sys
import re
from typing import Any
from dana.utils.script import import_all_models

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