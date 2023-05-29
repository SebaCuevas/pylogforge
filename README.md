[![PyPI Version](https://img.shields.io/pypi/v/pylogforge.svg)](https://pypi.org/project/pylogforge) [![Documentation Status](https://readthedocs.org/projects/pylogforge/badge/?version=latest)](https://pylogforge.readthedocs.io/en/latest/)

Custom Logger Module
--------------------

PyLogForge is a Python module that provides advanced logging functionality with color-coded log levels, customizable formatters, and flexible log output configuration.

Installation
------------

You can install pylogforge using pip:

```
pip install pylogforge
```

Usage
-----

To use pylogforge, follow these steps:

1. Import the module:
    ```
    from pylogforge import PyLogForge
    ```
2. Create an instance of the PyLogForge class, the name is optional.:
    ```python3
    logger = PyLogForge(name="my_logger").logger
    ```
3. Start logging messages:
    ```python3
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")
    ```
4. On the additional files you just need to include the import and call getLogger.
    ```
    import logging
    logger = logging.getLogger(name="my_logger")
    
   logger.critical("This is a critical message")
    ```

Configuration
-------------

pylogforge can be configured using environment variables:

- `LOG_CONSOLE_LEVEL`: Set the console log level (default: DEBUG)
- `LOG_FILE_LEVEL`: Set the file log level (default: INFO)
- `LOG_DIR`: Set the directory to store log files (default: no file logging)
- `LOG_SINGLE_FILE`: Set to "true" to log to a single file (default: separate files for each log level)

For example, you can set the environment variables before running your Python script:


```shell
export LOG_CONSOLE_LEVEL=INFO
export LOG_FILE_LEVEL=DEBUG
export LOG_DIR=/path/to/logs
export LOG_SINGLE_FILE=True
```
Contributing
------------

Contributions to pylogforge are welcome! If you encounter any issues, have feature requests, or want to contribute improvements, please submit an issue or pull request on the `GitHub repository <https://github.com/krash0n/pylogforge>`_.

License
-------

pylogforge is distributed under the MIT License. See the `LICENSE <https://github.com/krash0n/pylogforge/blob/main/LICENSE>`_ file for more details.

Links
-----

- `PyPI Package <https://pypi.org/project/pylogforge>`_
- `Documentation <https://pylogforge.readthedocs.io/en/latest>`_
- `GitHub Repository <https://github.com/krash0n/pylogforge>`_
