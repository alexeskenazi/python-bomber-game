import shelve
import dbm


class Storage:
    '''
    Simple file storage for saving and retrieving name value pairs
    '''

    def __init__(self, file_name: str) -> None:
        '''
        Used to store information on a file.
        file_name: (str) name of the file used to store information.
        constructor'''
        self.file_name = file_name

    def save(self, name: str, value):
        '''
        Saves a name/value pair on the file.
        name: (str) name of the data to store
        value: (Any) value to store
        '''
        with shelve.open(self.file_name, flag='c') as store:
            store[name] = value

    def load(self, name: str):
        '''
        Loads a name/value pair from the file.
        name: (str) name of the data to store
        return: (Any) value retrieved from the file
        '''
        try:
            with shelve.open(self.file_name, flag='r') as store:
                return store.get(name, 0)
        except dbm.error:
            # Handle the case where the dbm module is not available or the file cannot be opened in read mode
            with shelve.open(self.file_name, flag='c') as store:
                return store.get(name, 0)
