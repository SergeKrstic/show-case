class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


# For more detail see:
# - http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html
# - http://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
