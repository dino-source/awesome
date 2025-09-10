from typing import Any


# to stop Pyright complaining about unused args variable
def maybe_unused(*args: Any) -> None:
    if args:
        pass
