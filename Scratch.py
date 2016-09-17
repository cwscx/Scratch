import os
import re

import ScratchUtil

if __name__ == '__main__':

    for file in os.listdir(os.getcwd() + "/pics"):
        filenames = re.match("(.*)\.(.*)", file)
        filename = filenames.group(1)
        fileext = filenames.group(2)

        if filename != "" and filename is not None:
            ScratchUtil.simpleImplementation("pics/" + file, 15, filename)

