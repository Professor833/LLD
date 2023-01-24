from typing import Type, TypeVar, Any

T = TypeVar("T")

class Registry:
    def __init__(self) -> None:
        self._registry = {}

    def register(self, cls: Type[T]) -> T:
        self._registry[cls.__name__] = cls
        return cls

    def get(self, name: str) -> Type[T]:
        return self._registry[name]

registry = Registry()

@registry.register
class MyClass:
    pass

cls = registry.get("MyClass")
obj = cls()

print(obj)

