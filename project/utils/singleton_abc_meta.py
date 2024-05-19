from abc import ABCMeta


class SingletonABCMeta(ABCMeta, type):
    """
    Metaclass that combines Singleton and ABC (Abstract Base Class) patterns.

    This metaclass ensures that only one instance of a class is created (Singleton pattern)
    while also supporting abstract base classes.

    Attributes:
        _instances (dict): Dictionary to store the single instances of the classes.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Controls the instantiation of classes using this metaclass, ensuring only one instance is created.

        Args:
            cls: The class being instantiated.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            object: The single instance of the class.
        """
        if cls not in cls._instances:
            instance = super(SingletonABCMeta, cls).__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
