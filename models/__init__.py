#!/usr/bin/python3

"""Initialize models file. """

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()