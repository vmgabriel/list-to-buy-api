"""Events Handlers Control"""

# Libraries
from typing import Dict, List, Type, Callable

# Modules
from src.domain import commands, events


EVENT_HANDLERS: Dict[Type[events.Event], List[Callable]] = {
}

COMMAND_HANDLERS: Dict[Type[commands.Command], Callable] = {
}
