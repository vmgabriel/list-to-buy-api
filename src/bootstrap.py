"""Bootstrap"""

# Libraries
import inspect
from typing import Callable

# Modules
from .domain import unit_of_work
from src.services import handlers, messagebus
from .adapters.unit_of_work import unit_of_work as unit_of_work_specific


def bootstrap(
    uow: unit_of_work.AbstractUnitOfWork = unit_of_work_specific(),
) -> messagebus.MessageBus:
    dependencies = {"uow": uow}
    injected_event_handlers = {
        event_type: [
            inject_dependencies(handler, dependencies)
            for handler in event_handlers
        ]
        for event_type, event_handlers in handlers.EVENT_HANDLERS.items()
    }
    injected_command_handlers = {
        command_type: inject_dependencies(handler, dependencies)
        for command_type, handler in handlers.COMMAND_HANDLERS.items()
    }

    return messagebus.MessageBus(
        uow=uow,
        event_handlers=injected_event_handlers,
        command_handlers=injected_command_handlers,
    )


def inject_dependencies(handler, dependencies):
    params = inspect.signature(handler).parameters
    deps = {
        name: dependency
        for name, dependency in dependencies.items()
        if name in params
    }
    return lambda message: handler(message, **deps)
