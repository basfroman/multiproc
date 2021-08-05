from multiprocessing import Process
import os
import multiprocessing as mp


def fun():

    print('--------------------------')

    print('Calling fun')
    print('\tParent process id:', os.getppid(), 'from OS module')
    print('\tCurrent process id:', os.getpid(), 'from OS module\n')
    print('\tParent process ID:', mp.parent_process().pid, 'from Multiprocessing module')
    print('\tCurrent process ID:', mp.current_process().pid, 'from Multiprocessing module')


def main():

    print('main fun')
    print('process id:', os.getpid())

    p1 = Process(target=fun)
    p1.start()
    p1.join()

    p2 = Process(target=fun)
    p2.start()
    p2.join()


if __name__ == '__main__':
    main()
