class Connector:
    def __init__(self, url=None):
        if url is not None:
            self.__url = url

    def print_url(self):
        print(self.__url)

    __url = "localhost"
