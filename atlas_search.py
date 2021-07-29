
from typing import List, Union

import requests

from base import BaseAtlasClient


class AtlasSearchClient(BaseAtlasClient):
    _endpoints = {
        "get_all_indexes": "/groups/{}/clusters/{}/fts/indexes/{}/{}",
        "get_index": "/groups/{}/clusters/{}/fts/indexes/{}",
        "get_analyzers": "/groups/{}/clusters/{}/fts/analyzers",
        "create_index": "/groups/{}/clusters/{}/fts/indexes/",
        "update_index": "/groups/{}/clusters/{}/fts/indexes/{}",
        "update_analyzers": "/groups/{}/clusters/{}/fts/analyzers",
        "delete_index": "/groups/{}/clusters/{}/fts/indexes/{}",
    }

    def __init__(self, public_key: str, private_key: str, group_id: str, cluster_name: str):
        super().__init__(public_key, private_key, group_id)
        self.cluster_name = cluster_name

    def get_all_indexes(self, database_name: str, collection_name: str, query_params: dict = None):
        """Get all Atlas Search indexes for a specified collection."""
        if query_params is None:
            query_params = {}
        url = self._base_url.format(
            self._endpoints.get("get_all_indexes").format(
                self.group_id, self.cluster_name, database_name, collection_name
            )
        )
        return self._request(requests.Request("GET", url, params=query_params), expect_list=True)

    def get_index(self, index_id: str, query_params: dict = None):
        """Get one Atlas Search index by its `indexId`."""
        if query_params is None:
            query_params = {}
        url = self._base_url.format(
            self._endpoints.get("get_index").format(
                self.group_id, self.cluster_name, index_id
            )
        )
        return self._request(requests.Request("GET", url, params=query_params))

    def get_analyzers(self, query_params: dict = None):
        """Get all Atlas Search user-defined analyzers for a specified cluster."""
        if query_params is None:
            query_params = {}
        url = self._base_url.format(
            self._endpoints.get("get_analyzers").format(
                self.group_id, self.cluster_name
            )
        )
        return self._request(requests.Request("GET", url, params=query_params), expect_list=True)

    def create_index(self, body_params: dict, query_params: dict = None):
        """Create an Atlas Search index."""
        if query_params is None:
            query_params = {}
        url = self._base_url.format(
            self._endpoints.get("create_index").format(
                self.group_id, self.cluster_name
            )
        )
        return self._request(requests.Request("POST", url, params=query_params, json=body_params))

    def update_index(self, index_id: str, body_params: dict, query_params: dict = None):
        """Update an Atlas Search index by its `indexId`."""
        if query_params is None:
            query_params = {}
        url = self._base_url.format(
            self._endpoints.get("update_index").format(
                self.group_id, self.cluster_name, index_id
            )
        )
        return self._request(requests.Request("PATCH", url, params=query_params, json=body_params))

    def update_analyzers(self, body_params: Union[List[dict], dict], query_params: dict = None):
        """Update the Atlas Search user-defined analyzers for a specified cluster."""
        if query_params is None:
            query_params = {}
        url = self._base_url.format(
            self._endpoints.get("update_analyzers").format(
                self.group_id, self.cluster_name
            )
        )
        return self._request(requests.Request("PUT", url, params=query_params, json=body_params))

    def delete_index(self, index_id: str, query_params: dict = None):
        """Delete one Atlas Search index by its `indexId`."""
        if query_params is None:
            query_params = {}
        url = self._base_url.format(
            self._endpoints.get("delete_index").format(
                self.group_id, self.cluster_name, index_id
            )
        )
        return self._request(requests.Request("DELETE", url, params=query_params))
