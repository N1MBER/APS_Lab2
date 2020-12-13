class Logger(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_logger'):
            print("I was borned")
            cls._logger = super(Logger, cls
                    ).__new__(cls, *args, **kwargs)
        return cls._logger

    def log(self):
        print("logs:", self)

def main():
    logger = Logger.__new__()
    logger.log()

if __name__ == "__main__":
    main()