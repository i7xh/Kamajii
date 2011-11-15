BROKER_BACKEND = 'redis'
BROKER_HOST = '127.0.0.1'
BROKER_PORT = 6379
BROKER_VHOST = '12'


CELERY_RESULT_BACKEND = "redis"
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_DB = '100'
REDIS_CONNECT_RETRY = True

#CELERY_IMPORTS = ("web_config","core.middlewares.analytic","core.workers.sina_tasks")

CELERY_DEFAULT_RATE_LIMIT='500/s'

# Enables error e-mails.
CELERY_SEND_TASK_ERROR_EMAILS = False

# Name and e-mail addresses of recipients
ADMINS = (
    ("xi heng", "h@zhihu.com"),
)

