
import urllib.parse
from typing import Any, Dict, List, Optional, Tuple, Union

import requests
import requests.auth


class BaseAtlasClient:
    _base_url = "https://cloud.mongodb.com/api/atlas/v1.0{}"

    def __init__(self, public_key: str, private_key: str, group_id: str):
        self._session = requests.Session()
        self._session.auth = requests.auth.HTTPDigestAuth(public_key, private_key)
        # self._session.params.update({"pretty": False, "envelope": False})
        self.group_id = group_id

    def __del__(self):
        self._session.close()

    @staticmethod
    def _handle_response(response: requests.Response) -> Optional[Union[List[dict], Dict[str, Any]]]:
        """Returns successful response JSON body or prints unsuccessful response HTTP result."""
        if 200 <= response.status_code < 300:
            return response.json()
        print(response.status_code, response.reason, response.url)

    @staticmethod
    def _parse_href(href: str) -> Tuple[str, Dict[str, List[Any]]]:
        """Breaks a full URL into separate base URL string and query parameters dictionary."""
        u = urllib.parse.urlparse(href)
        url = urllib.parse.urlunparse((u.scheme, u.netloc, u.path, u.params, '', u.fragment))
        query_params = urllib.parse.parse_qs(u.query)
        return url, query_params

    def _request(
            self, request: requests.Request, expect_list: bool = False, expect_download: bool = False
    ) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
        """Sends request, returns successful response body (None if unsuccessful). De-paginates lists if applicable."""
        if expect_list:
            request.params.update({
                "itemsPerPage": 500,
                "includeCount": True,
            })
        request = self._session.prepare_request(request)
        result = self._handle_response(self._session.send(request))
        if result is not None:
            if not expect_list or (expect_list and isinstance(result, list)):
                return result
            all_results = []
            all_results.extend(result.get("results", []))
            next_href_queue = [
                link.get("href")
                for link in result.get("links", [])
                if link["rel"] == "next"
            ]
            while len(next_href_queue) > 0:
                next_href = next_href_queue.pop(0)
                if not next_href:
                    continue
                url, query_params = self._parse_href(next_href)
                request = self._session.prepare_request(requests.Request(request.method, url, params=query_params))
                result = self._handle_response(self._session.send(request))
                if result is not None:
                    all_results.extend(result.get("results", []))
                    next_href_queue.extend([
                        link.get("href")
                        for link in result.get("links", [])
                        if link["rel"] == "next"
                    ])

            return all_results
