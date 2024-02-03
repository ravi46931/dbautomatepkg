import os
from pathlib import Path

package_name='dbautomate'

list_of_files = [
   ".github/workflows/ci.yaml",
   "src/__init__.py",
   f"src/{package_name}/__init__.py", 
   f"src/{package_name}/mongodboperator.py", 
   f"src/{package_name}/mysqloperator.py", 
   "tests/__init__.py",
   "tests/unit/__init__.py",
   "tests/unit/test_unit.py",
   "tests/integration/__init__.py",
   "tests/integration/test_int.py",
   "README.md",
   "init_setup.sh",
   "requirements.txt", 
   "requirements_dev.txt",
   "setup.py",
   "setup.cfg",
   "pyproject.toml",
   "tox.ini",
   "experiments/experiments.ipynb", 
]


for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir, file_name = os.path.split(file_path)
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path,"w") as f:
            pass

