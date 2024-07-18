class SingletonMeta(type):
    """
    Metaclass that implements the Singleton pattern.

    This metaclass ensures that only one instance of a class is created.

    Attributes:
        _instances (dict): Dictionary to store the single instances of the classes.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Controls the instantiation of classes using this metaclass, ensuring only one instance is created.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            object: The single instance of the class.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
