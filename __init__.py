import os
import cytoplasm


class Page(object):
    "A file-like object that'll be created from each file in the source dir."
    def __init__(self, controller, path):
        # interpret this file
        cytoplasm.interpreters.interpret_to_filelike(path, self,
                controller.site)

    def close(self):
        # This is just here so that python doesn't throw up an error when
        # something else think this is a file.
        pass

    def write(self, s):
        "Instead of writing to disk, simply save to self.contents."
        # if s is a bytes object, decode it.
        if isinstance(s, bytes):
            s = s.decode("utf-8")
        # save to self.contents.
        self.contents = s


class PageController(cytoplasm.controllers.Controller):
    "A controller for putting pages inside templates."
    def __call__(self):
        template = self.template("page")
        for page in os.listdir(self.data_directory):
            # save to the destination directory with a filename minus the
            # last extension
            destination = os.path.join(self.destination_directory,
                    cytoplasm.interpreters.interpreted_filename(page, self.site))
            page_object = Page(self, os.path.join(self.data_directory, page))
            # interpret the template to the destination above;
            # give it the page object as an argument.
            cytoplasm.interpreters.interpret(template, destination,
                    self.site, page=page_object)


info = {"class": PageController}
