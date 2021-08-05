import logging
import multiprocessing as mp
import requests
import os


logging.basicConfig(level=logging.INFO)

mc = mp.current_process()


def cpu_waster():
    while True:
        logging.info(f'Process: {mp.current_process().name}')


def current_process_func(url):
    name = os.path.basename(url)
    file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'files', name)
    logging.info(f'Process {mp.current_process().name}: Url {url} downloads to file {file}.')

    with requests.get(url, stream=True) as s:
        s.raise_for_status()
        with open(rf'{file}', 'wb') as f:
            for chunk in s.iter_content(chunk_size=8192):
                f.write(chunk)

    logging.info(f'File {file} has been downloaded.')


def pool_functions():
    urls = [
        'https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-mp4-file.mp4',
        'https://coliseum.cloud.cdnland.in/movies/d4eb1dcd8160c9830db1d99540d91213ccdc4a90'
        '/3cca34b8f6e04eb7ccbe5ca8caecd399:2021080602/720.mp4',
    ]
    with mp.Pool(mp.cpu_count()*2) as pool:
        # in this case we don't need pool.close() and pool.join()
        pool.map(current_process_func, urls)
        pool.starmap(cpu_waster, [() for _ in range(mp.cpu_count())])

        # in async case we have to use pool.close() and pool.join()
        # pool.map_async(current_process_func, urls)
        # pool.starmap_async(cpu_waster, [() for _ in range(mp.cpu_count())])
        # pool.close()
        # pool.join()


if __name__ == '__main__':
    logging.info('It started...')
    pool_functions()
