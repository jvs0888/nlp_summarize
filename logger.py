import os
from pathlib import Path
from loguru import logger
from datetime import datetime


def init_logger() -> None:
    bind = logger.bind()
    path = Path(__file__).parent
    log_path = os.path.join(path, 'logs', f'{datetime.now().date()}.log')
    bind.add(sink=log_path,
             backtrace=True,
             diagnose=True,
             encoding='utf-8',
             rotation='1 MB')
