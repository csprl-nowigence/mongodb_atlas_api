
import requests

from base import BaseAtlasClient


class AccessListEntry():
    def __init__(self):
        self.ip_address = None
        self.cidr_block = None
        self.aws_security_group = None
        self.comment = None
        self.delete_after_date = None


class AccessListClient(BaseAtlasClient):
    _endpoints = {
        "get_all_entries": "/groups/{}/accessList",
        "get_entry": "/groups/{}/accessList/{}",
        "add_entries": "/groups/{}/accessList",
        "delete_entry": "/groups/{}/accessList/{}",
    }

    def __init__(self, public_key: str, private_key: str, group_id: str):
        super().__init__(public_key, private_key, group_id)

    def get_all_entries(self, query_params: dict = None):
        """Get all access list entries in the project."""
        if query_params is None:
            query_params = {}
        url = self._base_url.format(
            self._endpoints.get("get_all_entries").format(
                self.group_id
            )
        )
        return self._request(requests.Request("GET", url, params=query_params), expect_list=True)

    def get_entry(self, entry_id: str, query_params: dict = None):
        """Get the specified access list entry from the project."""
        if query_params is None:
            query_params = {}
        url = self._base_url.format(
            self._endpoints.get("get_entry").format(
                self.group_id, entry_id.replace("/", "%2F")
            )
        )
        return self._request(requests.Request("GET", url, params=query_params))

    def add_entries(self, body_params: dict, query_params: dict = None):
        """Add one or more access list entries to the project."""
        if query_params is None:
            query_params = {}
        url = self._base_url.format(
            self._endpoints.get("add_entries").format(
                self.group_id
            )
        )
        return self._request(requests.Request("POST", url, params=query_params, json=body_params), expect_list=True)

    def delete_entry(self, entry_id: str, query_params: dict = None):
        """."""
        if query_params is None:
            query_params = {}
        url = self._base_url.format(
            self._endpoints.get("delete_entry").format(
                self.group_id, entry_id.replace("/", "%2F")
            )
        )
        return self._request(requests.Request("DELETE", url, params=query_params))
