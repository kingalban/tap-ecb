"""ECB tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_ecb import streams


class TapECB(Tap):
    """ECB tap class."""

    name = "tap-ecb"

    config_jsonschema = th.PropertiesList().to_dict()

    def discover_streams(self) -> list[streams.ECBStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.EXRStream(self),
        ]


if __name__ == "__main__":
    TapECB.cli()
