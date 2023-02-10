from aiohttp.web import Application, run_app


app = Application()
if __name__ == "__main__":
    run_app(app, host="127.0.0.1")
