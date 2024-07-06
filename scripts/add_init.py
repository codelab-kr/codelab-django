import os
from pathlib import Path

current_path = str(Path(__file__).resolve().parent)
root_path = str(Path(__file__).resolve().parent.parent)


def add_init_files(directory):
    for root, dirs, files in os.walk(directory):
        if str(root) == current_path or str(root) == root_path or str(
                root).endswith('__pycache__'):
            continue
        py_files = [
            f for f in files if f.endswith('.py') and f != '__init__.py'
        ]
        if len(py_files) > 0 and '__init__.py' not in files:
            with open(os.path.join(root, '__init__.py'),
                      'w') as f:  # type: ignore # noqa: F841
                pass
        for dir in dirs:  # type: ignore # noqa: A001
            add_init_files(os.path.join(root, dir))


if __name__ == '__main__':
    add_init_files(os.getcwd())
