from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.requests import Request

# Instanciar uma variável da classe FastAPI sem as opções
# para criar documentação API pois não será uma api
app = FastAPI(docs_url=None, redoc_url=None)

# A variável templates para apontar ao diretório templates
templates = Jinja2Templates(directory='templates')

app.mount('/static', StaticFiles(directory='static'), name='static')
app.mount('/media', StaticFiles(directory='media'), name='media')


@app.get('/', name='index')
async def index(request: Request):
    context = {
        'request': request
    }

    return templates.TemplateResponse('home/index.html', context=context)


@app.get('/about', name='about')
async def about(request: Request):
    context = {
        'request': request
    }

    return templates.TemplateResponse('home/about.html', context=context)


@app.get('/contact', name='contact')
async def contact(request: Request):
    context = {
        'request': request
    }

    return templates.TemplateResponse('home/contact.html', context=context)


@app.get('/pricing', name='pricing')
async def pricing(request: Request):
    context = {
        'request': request
    }

    return templates.TemplateResponse('home/pricing.html', context=context)


@app.get('/faq', name='faq')
async def faq(request: Request):
    context = {
        'request': request
    }

    return templates.TemplateResponse('home/faq.html', context=context)


@app.get('/blog_home', name='blog_home')
async def blog_home(request: Request):
    context = {
        'request': request
    }

    return templates.TemplateResponse('home/blog-home.html', context=context)
