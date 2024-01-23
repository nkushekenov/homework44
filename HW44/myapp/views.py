from django.core.cache import cache
from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

def my_view(request):
    data = cache.get('my_key')

    if data is None:
        data = expensive_database_query()
        cache.set('my_key', data, timeout=3600)
        logger.info("Data fetched from the database and cached.")
    else:
        logger.info("Data fetched from the cache.")
    return render(request, 'home.html', {'data': data})