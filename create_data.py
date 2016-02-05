# -*- coding: utf-8 -*-

import random
import os


class CreateData(object):

    """
    create data to analyze.
    """

    def create_number_data(self,
                           file_path,
                           count,
                           max_int=10000):

        with open(file_path, "w") as f:
            for n in range(count):
                f.write(str(n) + "\t" + str(random.randint(0, max_int)) + "\n")


if __name__ == '__main__':

    create_data = CreateData()
    create_data.create_number_data(
        os.path.dirname(os.path.abspath(__file__))
         + "/number_data.txt",
        10000,
        10000
    )
