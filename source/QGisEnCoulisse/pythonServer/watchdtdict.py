#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""
Du pdf initial vers des plans pdf finaux.

Script permettant d'enchainer la lecture du pdf initial
et la génération des plans pdf finaux.

"""


import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
            print "ok"
    except KeyboardInterrupt:
        observer.stop()
        
    observer.join()
