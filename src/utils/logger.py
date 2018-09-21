class Logger:
    def __init__(self, spark_context):
        self.sc = spark_context
        self.logger = self._logger_factory(self, self.sc)

    @staticmethod
    def _logger_factory(self, sc):
        log4jLogger = sc._jvm.org.apache.log4j
        logger = log4jLogger.LogManager.getLogger(__name__)
        return logger

    def write(self, level, msg):
        """
        Writes log entry
        :param level: log level (INFO, WARNING, ERROR)
        :param msg: message to log
        :return:
        """
        if level == 'info':
            self.logger.info('-------------------------------------------------------------------------------------')
            self.logger.info(msg)
            self.logger.info('-------------------------------------------------------------------------------------')
        elif level == 'warning':
            self.logger.warning('-------------------------------------------------------------------------------------')
            self.logger.warning(msg)
            self.logger.warning('-------------------------------------------------------------------------------------')
        elif level == 'error':
            self.logger.error('-------------------------------------------------------------------------------------')
            self.logger.error(msg)
            self.logger.error('-------------------------------------------------------------------------------------')
        else:
            print('[!] Log level is not set properly: {}'.format(level))