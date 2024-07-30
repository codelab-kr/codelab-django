from django.urls import reverse_lazy

from common.settings.applied import *

INSTALLED_APPS += [   # type: ignore # noqa: F821
    'services.edu.apps.courses',
    'services.edu.apps.students',
    'services.edu.apps.chat',
]
ROOT_URLCONF = 'services.edu.edu.urls'
WSGI_APPLICATION = 'services.edu.edu.wsgi.application'
TEMPLATES[0]['DIRS'] += BASE_DIR / 'services' / 'edu' / 'templates',  # type: ignore # noqa: F821
STATICFILES_DIRS += BASE_DIR / 'services' / 'edu' / 'static',  # type: ignore # noqa: F821
LOGIN_REDIRECT_URL = reverse_lazy('student_course_list')  # type: ignore # noqa: F821
