import os
import sys
from pathlib import Path
from fastapi import Request, APIRouter, Form
from fastapi.responses import HTMLResponse

sys.path.append(str(Path(__file__).parent.parent))
fn = sys.argv[0]

try:
    from app.templates import templates
except ImportError as ie:
    exit(f'failed to import templates:: {fn} :: {ie}')

try:
    from nlp_model import summarize_text
except ImportError as ie:
    exit(f'failed to import templates:: {fn} :: {ie}')


text_dir = Path(__file__).parent.parent
text_path = os.path.join(text_dir, 'input_text.txt')

with open(file=text_path, mode='r', encoding='utf-8') as file:
    input_text = file.read()


route = APIRouter()


@route.get(path='/', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@route.get(path='/summarization', response_class=HTMLResponse)
async def summarization(request: Request):
    return templates.TemplateResponse('summarization.html', {'request': request, 'input_text': input_text})


@route.post(path='/process_text', response_class=HTMLResponse)
async def process_text(request: Request, sentences_count: int = Form(5), text: str = Form(None)):
    output_text = summarize_text(input_text=text, sentences_count=sentences_count)
    return templates.TemplateResponse('output_text.html', {'request': request, 'output_text': output_text})
