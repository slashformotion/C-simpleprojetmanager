import logging




class Logger(logging.Logger):
    def __init__(self, level = "INFO", name = "Basic Logger : "):
        super().__init__(name)

        self.handler = logging.StreamHandler()
        self.formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
        self.handler.setFormatter(self.formatter)
        self.addHandler(self.handler)
       
 
    def set_level(self, level):
        assert isinstance(level, str)
        assert level in ["DEBUG", "INFO", "WARNING", "ERROR","CRITICAL"]

        if level == "INFO":
            self.setLevel(logging.INFO)
        elif level == "DEBUG":
            self.setLevel(logging.DEBUG)
        elif level == "WARNING":
            self.setLevel(logging.WARNING)  
        elif level == "ERROR":
            self.setLevel(logging.ERROR)  
        elif level == "CRITICAL":
            self.setLevel(logging.CRITICAL)
       


if __name__ == "__main__":
    class test():
        def __init__(self):
            self.logger = Logger()
    logger = Logger("DEBUG")
    logger.debug("test")
