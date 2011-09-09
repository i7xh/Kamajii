"""myapp.py

Usage:

   (window1)$ python myapp.py -l info

   (window2)$ python
   >>> from myapp import add
   >>> add.delay(16, 16).get()
   32


You can also specify the app to use with celeryd::

    $ celeryd -l info --app=myapp.celery

"""
import sys
sys.path.insert(0,'lib')
sys.path.insert(0, 'lib/celery')
sys.path.insert(0, 'lib/kombu')


from celery import Celery


celery = Celery("myapp")
celery.conf.update(BROKER_URL="amqp://guest:guest@localhost:5672//")


@celery.task
def add(x, y):
    return x + y

if __name__ == "__main__":
    import celery.bin.celeryd
    celery.bin.celeryd.main()
