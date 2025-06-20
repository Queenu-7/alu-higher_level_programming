#!/usr/bin/python3
import importlib.util

if __name__ == "__main__":
    # Path to the .pyc file
    file_path = "hidden_4.pyc"

    # Load the module spec from the pyc file
    spec = importlib.util.spec_from_file_location("hidden_4", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Get all names defined in the module
    names = dir(module)

    # Filter out names starting with __
    filtered_names = [name for name in names if not name.startswith("__")]

    # Sort and print
    for name in sorted(filtered_names):
        print(name)
