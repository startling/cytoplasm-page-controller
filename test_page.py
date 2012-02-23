import os
import unittest
import cytoplasm
from cytoplasm.interpreters import interpreted_filename
from cytoplasm.test_build import Base


test_site = os.path.join(os.path.dirname(__file__), "test")


class TestPageController(Base):
    def setUp(self):
        Base.setUp(self, test_site)

    def test_page_controller(self):
        """Test that the template is correctly applied to each of the files
        in the source directory.
        """
        # a list of all the page controllers.
        controllers = [c for c in self.site.config.controllers if
                c[0] == "page"]
        # for each of them...
        for controller, [source, build, templates] in controllers:
            # read the template.
            # assume the template in question is a mako template, too.
            with open(os.path.join(self.directory, templates,
                "page.mako")) as f:
                template = f.read()
            # for the purposes of this test, assume there is no actual logic
            # going on, just interpolation. Get everything before and after
            # ${page.contents}.
            template_before, template_after = template.split(
                    "${page.contents}")
            # figure out the beginning and ending parts of
            # for each of the source files:
            for file in os.listdir(os.path.join(self.directory, source)):
                # get the contents of the file.
                with open(os.path.join(self.directory, source, file)) as f:
                    source_contents = f.read()
                # get the contents of the built file
                shortened_filename = interpreted_filename(file, self.site)
                with open(os.path.join(self.directory, build,
                    shortened_filename)) as f:
                    build_contents = f.read()
                # make sure it starts with the first part of the template:
                assert build_contents.startswith(template_before)
                # make sure it contains the contents of the source file:
                assert source_contents.strip() in build_contents
                # make sure it ends with the last part of the template
                assert build_contents.endswith(template_after)


if __name__ == '__main__':
    unittest.main()
