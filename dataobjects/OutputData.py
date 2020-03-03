class OutputData:

    def __init__(self, libraries):
        self.libraries = libraries

    def __str__(self):
        return "libraries={}".format([str(lib) for lib in self.libraries])