# requires API key created by org owner

import requests

from base import BaseAtlasClient


class RootClient(BaseAtlasClient):
    """Starting point for the Atlas API."""
    _endpoints = {
        "get": "/",
    }

    def __init__(self, public_key: str, private_key: str):
        super().__init__(public_key, private_key, None)

    def get(self, query_params: dict = None):
        """Get links to API resources and API keys information."""
        if query_params is None:
            query_params = {}
        url = self._base_url.format(
            self._endpoints.get("get").format(

            )
        )
        return self._request(requests.Request("GET", url, params=query_params), expect_list=True)
