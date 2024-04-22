"""REST client handling, including ECBStream base class."""

from __future__ import annotations

from typing import TYPE_CHECKING, Iterable

from defusedxml import ElementTree
from singer_sdk.pagination import BaseAPIPaginator, SinglePagePaginator
from singer_sdk.streams import RESTStream

if TYPE_CHECKING:
    import requests


class ECBStream(RESTStream):
    """ECB stream class."""

    @property
    def url_base(self) -> str:
        """Return the API URL root, configurable via tap settings."""
        return "https://www.ecb.europa.eu/"

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed.

        Returns:
            A dictionary of HTTP headers.
        """
        headers = {}
        if "user_agent" in self.config:
            headers["User-Agent"] = self.config.get("user_agent")
        return headers

    def get_new_paginator(self) -> BaseAPIPaginator:
        """Create a new pagination helper instance.

        If the source API can make use of the `next_page_token_jsonpath`
        attribute, or it contains a `X-Next-Page` header in the response
        then you can remove this method.

        If you need custom pagination that uses page numbers, "next" links, or
        other approaches, please read the guide: https://sdk.meltano.com/en/v0.25.0/guides/pagination-classes.html.

        Returns:
            A pagination helper instance.
        """
        return SinglePagePaginator()

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        """Parse the response and return an iterator of result records.

        Args:
            response: The HTTP ``requests.Response`` object.

        Yields:
            Each record from the source.
        """
        root = ElementTree.fromstring(response.text)
        for dates in root[2]:
            for observation in dates:
                obs = dict(observation.items())
                date = dict(dates.items())["time"]
                yield {
                    "date": date,
                    "currency": obs["currency"],
                    "rate": float(obs["rate"]),
                }
