import contextlib
from collections.abc import Callable, Iterable


class MyIter:

    def __init__(self, _iter: Iterable, func: Callable = None, return_res_funk: bool = False) -> None:
        self._iter = iter(_iter)
        self.iter_obj = _iter
        self.func = func
        self.return_res_funk = return_res_funk
        self.history = []

    def __call__(
            self,
            _iter: Iterable = (),
            func: Callable = None,
            func_args: list | tuple = None,
            return_res_func: bool = False,
            upack: bool = False,
            **func_kwargs,
    ) -> any:
        """Returns an iterator object that iterates over the elements produced by calling the
        `self.__call__()` method until it returns a falsey value. Each element is appended to
        a list `a`, which is then converted to an iterator using `iter(a)` and returned.

        Returns
        -------
            iter: An iterator object that iterates over the elements produced by calling
                  `self.__call__()` until it returns a falsey value.
        """
        return_res_func = return_res_func or self.return_res_funk
        try:
            base_res = next(self._iter)
            args = []
            self.check_upack(args, base_res, upack)

            func = func or self.func

            if not isinstance(func, Callable):
                return base_res

            if isinstance(func_args, list | tuple):
                args.extend(func_args)

            with contextlib.suppress(OSError):
                res = func(*args, **func_kwargs)
                if return_res_func:
                    self.history.append(res)
                    return res

            self.history.append(base_res)

            return base_res

        except StopIteration:
            if not _iter:
                return False
            self._iter = iter(_iter)
            return self.__call__()

    def update_iter(self, *_iter) -> object:
        """Update the iterator of the object.

        Parameters
        ----------
            *_iter: The new iterator to be set.

        Returns
        -------
            self: The updated object itself.
        """
        self._iter = iter(_iter)
        return self

    def __iter__(self) -> Iterable:
        """Iterates over the object and returns an iterator.

        Returns
        -------
        An iterator object that yields the results of calling the object's __call__ method.
        """
        a = []
        while b := self.__call__():
            a.append(b)
        return iter(a)

    @staticmethod
    def check_upack(args: list | tuple, base_res: list | tuple, upack: bool) -> None:
        """Check if `upack` is truthy and `base_res` is an instance of `list` or `tuple`.
        If so, extend `args` with `base_res`. Otherwise, append `base_res` to `args`.

        Parameters
        ----------
            args (list): The list to which `base_res` will be appended or extended.
            base_res (any): The base result to be appended or extended.
            upack (bool): A flag indicating whether to extend `args` or append `base_res`.

        Returns
        -------
            None
        """
        if upack and isinstance(base_res, list | tuple):
            args.extend(base_res)
        else:
            args.append(base_res)

    def back_iter(self) -> None:
        """Reverses the order of iteration in the history list and sets the
            current iterator to iterate over the reversed
        history list.

        Parameters
        ----------
            self (object): The instance of the class.

        Returns
        -------
            None
        """
        self._iter = iter((self.history.pop(-1), *list(self._iter)))

    def back_and_call(self) -> any:
        """Execute the `back_iter` method and then call the `__call__` method.

        Returns
        -------
            The return value of the `__call__` method.
        """
        self.back_iter()
        return self.__call__()

    def __str__(self) -> str:
        return str(self._iter)
