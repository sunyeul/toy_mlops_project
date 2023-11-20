from dataclasses import dataclass, field
from typing import Any


@dataclass
class BaseConfig:
    hydra: Any = field(
        default_factory=lambda: {
            "run": {"dir": "logs/${hydra:job.name}/${now:%Y-%m-%d_%H-%M-%S}"}
        }
    )
