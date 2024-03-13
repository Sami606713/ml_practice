import logging
import os,sys
from datetime import datetime

# make the log folder
log_folder=os.path.join(os.getcwd(),'log')
os.makedirs(log_folder,exist_ok=True)

log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}"


final_path=os.path.join(log_folder,log_file)+".log"

logging.basicConfig(
    level=logging.INFO,
    format="[ %(asctime)s] %(lineno)s - %(levelname)s - %(message)s",
    filename=final_path,
    filemode="w"  # Set file mode to write
)