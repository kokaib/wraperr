"""wrap_error
=============
"""


import functools
from typing import Any, Callable, Type


def wrap_error(
    error_handler: Callable[[BaseException], Any],
    exception_type: Type[BaseException] = Exception
):
    """Parameterizes a function that can wrap another function.
    The wrapee function might raise an exception, and when it does,
    the wrapped function will call the specified error handler
    if the specified exception type was raised.

    :param error_handler: The specified error handler.
    :type error_handler: Callable[[BaseException], Any]
    :param exception_type: The specified exception type,
                           defaults to Exception.
    :type exception_type: Type[BaseException]

    :returns: A function that takes a function as input then
              decorates it, so that the specified error handler
              will handle the specified exception, in case it was
              raised during the execution of the input function.
    :rtype: Callable[[Callable], Callable]
    """

    def f(wrappee: Callable):
        @functools.wraps(wrappee)
        def g(*args, **kwargs):
            try:
                return wrappee(*args, **kwargs)
            except exception_type as e:
                return error_handler(e)
        return g
    return f
