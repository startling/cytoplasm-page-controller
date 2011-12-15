import cytoplasm, os

class Page(object):
    def __init__(self, path):
        # interpret this file
        cytoplasm.interpreters.interpret(path, self)

    def close(self):
        # This is just here so that python doesn't throw up an error when something else thinks
        # this is a file.
        pass

    def write(self, s):
        # instead of writing to disk, simply change the contents attribute.
        self.contents = s.decode()

class PageController(cytoplasm.controllers.Controller):
    "A controller for just pages written in, for example, markdown."
    def __call__(self):
        for page in os.listdir(self.data_directory): print page 

info= { "class": PageController }
