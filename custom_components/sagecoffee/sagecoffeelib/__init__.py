"""Sage Coffee Control Library - Control Breville/Sage coffee machines via their cloud API."""

from .client import SageCoffeeClient, TokenManager
from .models import Appliance, DeviceState, StateReport, TokenSet

__version__ = "0.1.0"
__all__ = [
    "Appliance",
    "DeviceState",
    "StateReport",
    "TokenSet",
    "SageCoffeeClient",
    "TokenManager",
]
