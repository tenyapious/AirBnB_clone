#!/usr/bin/python3
"""
Package Initialization for 'models'

This __init__.py file serves as the initialization file for the 'models' package.
It includes the instantiation of the 'FileStorage' class and a 'storage' instance
for handling persistent storage of model objects.

Usage:
    from models import storage

    # Accessing the 'FileStorage' instance
    storage_instance = storage

    # Reloading data from storage
    storage_instance.reload()
"""

from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()

from models.engine.file_storage import FileStorage

storage = FileStorage()

storage.reload()
