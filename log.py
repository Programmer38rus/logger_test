import logging
from bottle import route, run, request
import sentry_sdk
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    "https://079e09b3c0684ca8a241681891dc7913@o448256.ingest.sentry.io/5429334",
    integrations=[BottleIntegration()],
    traces_sample_rate=1.0
)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s --- %(message)s")

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class MyFilter:
    def filter(self, logRecord):
        return logRecord.levelno == logging.INFO


steam_handler = logging.StreamHandler()
steam_handler.setFormatter(formatter)
steam_handler.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("info.log", encoding="utf-8")
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.INFO)
file_handler.addFilter(MyFilter())

logger.addHandler(file_handler)
logger.addHandler(steam_handler)


# logger.debug("Проверка того, что сообщения уровня DEBUG обрабатываются и логером и обработчиком")  
# logger.info("Тестовое сообщение уровня INFO")  
# logger.error("Ещё одно сообщение, но уже уровня ERROR")
# logger.critical("вот еще одно")

@route('/success')
def index():
    # logger.debug(request.headers.get("User-Agent"))
    # return (request.headers.get("User-Agent"))
    return

@route('/fail')
def fail():

    raise RuntimeError("This is bad")

    return
run(host='localhost', port=9999)
