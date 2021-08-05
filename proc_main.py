import logging
import multiprocessing as mp
import time

logging.basicConfig(level=logging.INFO)

mc = mp.current_process()


def cpu_waster():
    while True:
        logging.info(f'Process: {mp.current_process().name}')


def proc_functions():

    proc = mp.Process(target=cpu_waster, daemon=True)

    proc.start()
    time.sleep(1)
    # proc.join()


# https://zetcode.com/python/multiprocessing/
if __name__ == '__main__':
    logging.info('It started...')
    proc_functions()
