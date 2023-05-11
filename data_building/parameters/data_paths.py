# ATTENTION: If you want access to the data dirs listed here, ask julia.kaltenborn@mila.quebec for access
from pathlib import Path
from data_building.utils.helper_funcs import get_project_root

# where the raw data is downloaded, stored and deleted after preprocessing
RAW_DATA = Path("/network/scratch/j/julia.kaltenborn/data/raw/") # always deleted

# this data is stored and can be used for new user requests
PROCESSED_DATA = Path("/network/scratch/j/julia.kaltenborn/data/processed/") # never deleted

# this data can be used within the data loader
LOAD_DATA = Path("/network/scratch/j/julia.kaltenborn/data/load/") # deleted if necessary, can be recreated from processed_data

TEST_CASES = Path("/home/julia/Documents/Master/CausalSuperEmulator/data/test_cases/")

# root of the project directory
#ROOT = Path("/home/julia/Documents/Master/CausalSuperEmulator/causalpaca/")
ROOT = get_project_root()

