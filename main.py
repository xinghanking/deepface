import logging
from fastapi import FastAPI
from api.analyze import router as analyze_router

app = FastAPI(client_max_size=1024 * 1024 * 100)
logging.basicConfig(filename="log/run.log", level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

app.include_router(analyze_router)
