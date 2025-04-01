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

import importlib
import pkgutil
import os
from typing import List

PACKAGE_NAME = 'dana'

def import_all_models(base_path: str) -> None:
    """
    Imports all model modules from subdirectories of the specified base path.
    
    This allows serialization and deserialization of models within api_client.py.
    
    :param base_path: The file path to the top-level package directory.
    """
    
    # Find domain packages within the base path
    domains = [
        domain for domain in pkgutil.iter_modules([base_path])
        if domain.ispkg and domain.name != 'base'
    ]
    
    # Construct domain paths
    domain_paths = [os.path.join(base_path, domain.name) for domain in domains]
    
    # Find subdomain packages within domain paths
    subdomains = [
        subdomain for subdomain in pkgutil.iter_modules(domain_paths)
        if subdomain.ispkg
    ]

    # Import model modules from each subdomain
    for subdomain in subdomains:
        path_to_domain: List[str] = getattr(subdomain.module_finder, 'path', '')
        domain = os.path.basename(path_to_domain)

        # Construct the full module path and import
        module_name = f"{PACKAGE_NAME}.{domain}.{subdomain.name}.models"
        importlib.import_module(module_name)
