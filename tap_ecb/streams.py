"""Stream type classes for tap-ecb."""

from __future__ import annotations

import typing as t

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_ecb.client import ECBStream


class EXRStream(ECBStream):
    """ Euro exchange rate historic stream """ ""

    name = "exchangerate_historic"
    path = "/stats/eurofxref/eurofxref-hist.xml"
    primary_keys: t.ClassVar[list[str]] = ["date", "currency"]
    replication_key = "date"
    schema = th.PropertiesList(
        th.Property("name", th.StringType),
        th.Property(
            "date",
            th.DateType,
            description="The date of the currency conversion",
        ),
        th.Property(
            "currency",
            th.StringType,
            description="The currency to convert from Euros to",
        ),
        th.Property(
            "rate",
            th.NumberType,
            description="The rate at which Euros are converted to the currency",
        ),
    ).to_dict()
