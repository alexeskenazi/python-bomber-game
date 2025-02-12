class Logger:
    '''
    Utility class to print output to the console is debug mode is enabled.
    '''
    logger = None
    is_debug = True

    def __init__(self) -> None:
        # Singleton
        if Logger.logger is None:
            return
        Logger.logger = self

    def log(text: str) -> None:
        '''
        Prints input string into the console.
        text: (str) text to print on the console
        '''
        if Logger.is_debug:
            print(text)
