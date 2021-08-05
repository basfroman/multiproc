from multiprocessing import Process
import multiprocessing as mp
import time


def func():

    print('\tcalling func')
    print(f'\tProcess p is alive: {mp.current_process().is_alive()}')
    time.sleep(1)
    print('\texit func')


def main():

    print('main fun')

    p = Process(target=func)
    p.start()
    p.join()

    print(f'Process p is alive: {p.is_alive()}')


if __name__ == '__main__':
    main()
