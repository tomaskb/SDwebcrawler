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

#Creates threads (max NUMBER_OF_THREADS
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


#Next job in line
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()

#Every link in the queue ia a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()


#If there still are links left in the queue 
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print("There still are"+ str(len(queued_links)) + ' links in the queue.')
        create_jobs()

create_workers()
crawl()
