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
        self.contents = s.decode("utf-8")

class PageController(cytoplasm.controllers.Controller):
    "A controller for putting pages inside templates."
    def __call__(self):
        template = self.template("page")
        for page in os.listdir(self.data_directory):
            # save to the destination directory with a filename minus the last extension
            destination = "%s/%s" %(self.destination_directory, ".".join(page.split(".")[:-1]))
            page_object = Page("%s/%s" %(self.data_directory, page))
            # interpret the template to the destination above;
            # give it the page object as an argument.
            cytoplasm.interpreters.interpret(template, destination, page=page_object)

info= { "class": PageController }
