#!/usr/bin/python3

import time
from multiprocessing import Process


class Worker(Process):

    def run(self):
        # overwrite run method
        print(f'In {self.name}')
        time.sleep(2)


def main():

    worker = Worker()
    worker.start()

    worker2 = Worker()
    worker2.start()

    worker.join()
    worker2.join()


if __name__ == '__main__':
    main()
