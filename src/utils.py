import os

def get_project_root():
    """Returns the absolute path to the ecommerce-image-intelligence folder."""
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def ensure_dir(directory_path):
    """Ensures a directory exists, cleaning up if a file exists with the same name."""
    if os.path.exists(directory_path) and not os.path.isdir(directory_path):
        os.remove(directory_path)
    os.makedirs(directory_path, exist_ok=True)