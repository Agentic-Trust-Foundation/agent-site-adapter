from dataclasses import dataclass
from typing import FrozenSet


@dataclass(frozen=True)
class ServiceManifest:
    service_id: str
    origin: str
    protocol_versions: FrozenSet[str]
    profiles: FrozenSet[str]
    capabilities: FrozenSet[str]
    auth_requirements: FrozenSet[str]

    def supports(self, protocol_version: str, profile: str, capability: str) -> bool:
        return (
            protocol_version in self.protocol_versions
            and profile in self.profiles
            and capability in self.capabilities
        )
