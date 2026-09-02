import logging
from pathlib import Path
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "automation.log"

def get_logger():
    #set log level
    logger = logging.getLogger("automation")
    logger.setLevel(level=logging.INFO)

    #format log file, log console
    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s",
                                "%H:%M:%S")

    #set format cho log file, log console
    file = logging.FileHandler(filename=LOG_FILE, mode="w", encoding="utf-8")
    file.setFormatter(formatter)

    console = logging.StreamHandler()
    console.setFormatter(formatter)

    #dang ky logfile, log console
    logger.handlers.clear()
    logger.addHandler(file)
    logger.addHandler(console)
    return logger