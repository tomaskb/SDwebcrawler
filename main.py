import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

PROJECT_NAME = input("Crawl Name: ")
HOMEPAGE = input("Insert URL to crawl: ")

DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 50
queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

#Cria as threads (maximo NUMBER_OF_THREADS
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


#Proximo Job da fila
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()

#Cada link na fila é um novo Job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()


#Se existe itens na fila, é pesquisado
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print("Ainda existem "+ str(len(queued_links)) + ' links na fila')
        create_jobs()

create_workers()
crawl()
