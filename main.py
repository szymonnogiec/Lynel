from Connector import Connector

if __name__ == '__main__':
    print("Hello world")
    connector = Connector("192.168.0.1")
    empty_connector = Connector()

    connector.print_url()
    empty_connector.print_url()
