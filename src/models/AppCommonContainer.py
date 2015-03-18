class AppCommonContainer:
    settings = None
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(AppCommonContainer, cls).__new__(cls, *args, **kwargs)
        return cls._instance