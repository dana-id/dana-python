import importlib
import pkgutil
import os
from typing import List

PACKAGE_NAME = 'dana_python'

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
