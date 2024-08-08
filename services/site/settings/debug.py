if DEBUG:  # type: ignore # noqa: F821
    INSTALLED_APPS.extend(['django_browser_reload'])  # type: ignore # noqa: F821
    MIDDLEWARE.insert(-1, 'django_browser_reload.middleware.BrowserReloadMiddleware')  # type: ignore # noqa: F821
