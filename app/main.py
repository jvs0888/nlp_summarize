import os
import sys
import json
import uvicorn
from pathlib import Path
from loguru import logger
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

sys.path.append(str(Path(__file__).parent.parent))
fn = sys.argv[0]

try:
    from app.static import static_files
except ImportError as ie:
    exit(f'failed to import static files:: {fn} :: {ie}')

try:
    from app.templates import templates
except ImportError as ie:
    exit(f'failed to import templates:: {fn} :: {ie}')

try:
    from logger import init_logger
except ImportError as ie:
    exit(f'failed to import logger:: {fn} :: {ie}')

try:
    from app.routers import route
except ImportError as ie:
    exit(f'failed to import route:: {fn} :: {ie}')


@logger.catch
def init_app() -> FastAPI:
    init_logger()
    app = FastAPI()

    cors_dir = Path(__file__).parent
    cors_path = os.path.join(cors_dir, 'cors.json')

    with open(file=cors_path, mode='r', encoding='utf-8') as file:
        cors = json.loads(file.read())

    app.add_middleware(CORSMiddleware, **cors)
    app.mount(**static_files)
    app.include_router(route)

    return app


if __name__ == '__main__':
    uvicorn.run(app=init_app, host='0.0.0.0', port=8000)
