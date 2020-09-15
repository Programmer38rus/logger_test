import logging

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s --- %(message)s")

logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)

class MyFilter:
    def filter(self, logRecord):
        return logRecord.levelno == logging.INFO


steam_handler = logging.StreamHandler()
# steam_handler = logging.FileHandler("aksjklsjf.gg")
steam_handler.setFormatter(formatter)
steam_handler.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("info.log", encoding="utf-8")
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.INFO)
file_handler.addFilter(MyFilter())

logger.addHandler(file_handler)
logger.addHandler(steam_handler)




logger.debug("Проверка того, что сообщения уровня DEBUG обрабатываются и логером и обработчиком")  
logger.info("Тестовое сообщение уровня INFO")  
logger.error("Ещё одно сообщение, но уже уровня ERROR")
logger.critical("вот еще одно")
