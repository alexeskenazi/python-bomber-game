import shelve


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
        store = shelve.open(self.file_name)
        store[name] = value
        store.close()

    def load(self, name: str):
        '''
        Loads a name/value pair from the file.
        name: (str) name of the data to store
        return: (Any) value retrieved from the file
        '''

        # First time we read we fail because the file is not there. Create it to get things going.
        error = False
        value = 0
        store = shelve.open(self.file_name)
        try:
            value = store[name]
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            error = True
        store.close()
        if error:
            self.save(name, value)
        return value
