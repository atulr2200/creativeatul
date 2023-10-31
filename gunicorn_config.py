workers = 4  # Number of worker processes
bind = "0.0.0.0:8000"  # Address and port to bind
worker_class = "sync"  # You can use "sync", "eventlet", or "gevent" depending on your requirements
