
from typing import List, Union

import requests

from base import BaseAtlasClient


class AlertsClient(BaseAtlasClient):
    _endpoints = {
        "get_all_alerts": "/groups/{}/alerts",
        "get_alert": "/groups/{}/alerts/{}",
        "update_alert": "/groups/{}/alerts/{}",
    }

    def __init__(self, public_key: str, private_key: str, group_id: str):
        super().__init__(public_key, private_key, group_id)

    def get_all_alerts(self, query_params: dict = None):
        """Get all alerts for the project."""
        if query_params is None:
            query_params = {}
        url = self._base_url.format(
            self._endpoints.get("get_all_alerts").format(
                self.group_id
            )
        )
        return self._request(requests.Request("GET", url, params=query_params), expect_list=True)

    def get_alert(self, alert_id: str, query_params: dict = None):
        """Get the specified alert for the project."""
        if query_params is None:
            query_params = {}
        url = self._base_url.format(
            self._endpoints.get("get_alert").format(
                self.group_id, alert_id
            )
        )
        return self._request(requests.Request("GET", url, params=query_params))

    def update_alert(self, alert_id: str, body_params: dict, query_params: dict = None):
        """Acknowledge or un-acknowledge the alert specified in `alert_id` for the project."""
        if query_params is None:
            query_params = {}
        url = self._base_url.format(
            self._endpoints.get("get_analyzers").format(
                self.group_id, alert_id
            )
        )
        return self._request(requests.Request("PATCH", url, params=query_params, json=body_params), expect_list=True)
