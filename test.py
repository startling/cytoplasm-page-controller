import os
import cytoplasm
from cytoplasm.test import Base

class TestPageController(Base):
    def __init__(self):
        Base.__init__(self, "test")

    def page_controller_test(self):
        "Test that the template is correctly applied to each of the files in the source directory."
        # a list of all the page controllers.
        controllers = [c for c in self.configuration.controllers if c[0] == "page"]
        # for each of them...
        for controller, [source, build, templates] in controllers:
            # read the template.
            # assume the template in question is a mako template, too.
            f = open(os.path.join(self.directory, templates, "page.mako"))
            template = f.read()
            f.close()
            # for the purposes of this test, assume there is no actual logic going on,
            # just interpolation. Get everything before and after ${page.contents}.
            template_before, template_after = template.split("${page.contents}")
            # figure out the beginning and ending parts of 
            # for each of the source files:
            for file in os.listdir(os.path.join(self.directory, source)):
                # get the contents of the file.
                f = open(os.path.join(self.directory, source, file))
                source_contents = f.read()
                f.close()
                # get the contents of the built file
                shortened_filename = cytoplasm.interpreters.interpreted_filename(file)
                f = open(os.path.join(self.directory, build, shortened_filename))
                build_contents = f.read()
                f.close()
                # make sure it starts with the first part of the template:
                assert build_contents.startswith(template_before)
                # make sure it contains the contents of the source file:
                assert source_contents.strip() in build_contents
                # make sure it ends with the last part of the template
                assert build_contents.endswith(template_after)


