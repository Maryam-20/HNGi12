# """
# WSGI config for stage0_API project.

# It exposes the WSGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
# """

# import os
# import sys

# from django.core.wsgi import get_wsgi_application

# path = "C:\HNG Internship 12\stage0Task\stage0_API\stage0_API"
# if path not in sys.path:
#     sys.path.append(path)



# # then:



# os.environ.setdefault('DJANGO_SETTINGS_MODULE', ' stage0_API.stage0_API.settings') #stage0_API.

# application = get_wsgi_application()

"""
WSGI config for stage0_API project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

# Set the correct settings module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
os.environ.setdefault('DJANGO_SETTINGS_MODULE','stage0_API.settings')

application = get_wsgi_application()

