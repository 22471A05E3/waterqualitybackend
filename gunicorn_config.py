workers = 4
worker_class = 'sync'
worker_connections = 1000
timeout = 30
keepalive = 2

# Server socket
bind = '0.0.0.0:' + str(int('5000'))

# Logging
errorlog = '-'  # Log to stdout
loglevel = 'info'
accesslog = '-'  # Log to stdout
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
