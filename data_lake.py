
import requests

from base import BaseAtlasClient


class DataLakeClient(BaseAtlasClient):
    _endpoints = {
        "get_all_datalakes": "/groups/{}/dataLakes",
        "get_datalake": "/groups/{}/dataLakes/{}",
        "get_query_log": "/groups/{}/dataLakes/{}/queryLogs.gz",
        "create_datalake": "/groups/{}/dataLakes",
        "update_datalake": "/groups/{}/dataLakes/{}",
        "delete_datalake": "/groups/{}/dataLakes/{}",
    }

    def __init__(self, public_key: str, private_key: str, group_id: str, cluster_name: str):
        super().__init__(public_key, private_key, group_id)
        self.cluster_name = cluster_name

    def get_all_datalakes(self, query_params: dict = None):
        """Get all Atlas Data Lakes for the current project."""
        if query_params is None:
            query_params = {}
        url = self._base_url.format(
            self._endpoints.get("get_all_datalakes").format(
                self.group_id
            )
        )
        return self._request(requests.Request("GET", url, params=query_params), expect_list=True)

    def get_datalake(self, datalake_name: str, query_params: dict = None):
        """Get an Atlas Data Lake in the current project by name."""
        if query_params is None:
            query_params = {}
        url = self._base_url.format(
            self._endpoints.get("get_datalake").format(
                self.group_id, datalake_name
            )
        )
        return self._request(requests.Request("GET", url, params=query_params))

    def get_query_log(self, datalake_name: str, query_params: dict = None):
        """Download query log for the specified Atlas Data Lake."""
        if query_params is None:
            query_params = {}
        url = self._base_url.format(
            self._endpoints.get("get_query_log").format(
                self.group_id, datalake_name
            )
        )
        return self._request(requests.Request("GET", url, params=query_params), expect_download=True)

    def create_datalake(self, body_params: dict, query_params: dict = None):
        """Create an Atlas Data Lake in the current project."""
        if query_params is None:
            query_params = {}
        url = self._base_url.format(
            self._endpoints.get("create_datalake").format(
                self.group_id
            )
        )
        return self._request(requests.Request("POST", url, params=query_params, json=body_params))

    def update_datalake(self, datalake_name: str, body_params: dict, query_params: dict = None):
        """Update an Atlas Data Lake in the current project by name."""
        if query_params is None:
            query_params = {}
        url = self._base_url.format(
            self._endpoints.get("update_datalake").format(
                self.group_id, datalake_name
            )
        )
        return self._request(requests.Request("PATCH", url, params=query_params, json=body_params))

    def delete_datalake(self, datalake_name: str, query_params: dict = None):
        """Delete an Atlas Data Lake in the current project by name."""
        if query_params is None:
            query_params = {}
        url = self._base_url.format(
            self._endpoints.get("delete_datalake").format(
                self.group_id, datalake_name
            )
        )
        return self._request(requests.Request("DELETE", url, params=query_params))
