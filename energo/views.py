from django.shortcuts import render
from functools import lru_cache
import for_energo


@lru_cache(maxsize=None)
def energo(request):
    return render(request, 'energo.html')
