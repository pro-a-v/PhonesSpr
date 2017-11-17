class Wrapper():
    def __init__(self, wrapped_class, input_type):
        self.wrapped_class = wrapped_class()

        if input_type == 'network':
            import socket
            s = socket.socket()
            conf = ('127.0.0.1', 9990)
            s.bind(conf)
            s.listen(5)
            print('Start listen')

            self.wrapped_class.print = self.print_network
            self.wrapped_class.input = self.input_network
            # а вот тут заврапить input и print
            self.c, self.a = s.accept()

    def input_network(self, text):
            self.c.sendall(text.encode("utf8"))
            return self.c.recv(1024).decode("utf8")

    def print_network(self, text):
            self.c.sendall(text.encode("utf8"))

    def __getattr__(self,attr):
            return self.wrapped_class.__getattribute__(attr)

