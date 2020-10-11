from aiohttp import web

app = web.Application()

async def index(request):
    return web.FileResponse('./site/index.html')

app.router.add_get('/', index)

web.run_app(app)