
import requests

from base import BaseAtlasClient


class InvoicesClient(BaseAtlasClient):
    """View invoices for an Atlas organization."""
    _endpoints = {
        "get_all_invoices": "/orgs/{}/invoices",
        "get_invoice": "/orgs/{}/invoices/{}",
        "get_pending_invoice": "/orgs/{}/invoices/pending",
    }

    def __init__(self, public_key: str, private_key: str, org_id: str):
        super().__init__(public_key, private_key, None)
        self.org_id = org_id

    def get_all_invoices(self, query_params: dict = None):
        """Get all invoices for the current organization ."""
        if query_params is None:
            query_params = {}
        url = self._base_url.format(
            self._endpoints.get("get_all_invoices").format(
                self.org_id
            )
        )
        return self._request(requests.Request("GET", url, params=query_params), expect_list=True)

    def get_invoice(self, invoice_id: str, query_params: dict = None):
        """Get one invoice for the current organization."""
        if query_params is None:
            query_params = {}
        url = self._base_url.format(
            self._endpoints.get("get_invoice").format(
                self.org_id, invoice_id
            )
        )
        return self._request(requests.Request("GET", url, params=query_params))

    def get_pending_invoice(self, query_params: dict = None):
        """Get one pending invoice for the current organization."""
        if query_params is None:
            query_params = {}
        url = self._base_url.format(
            self._endpoints.get("get_pending_invoice").format(
                self.org_id
            )
        )
        return self._request(requests.Request("GET", url, params=query_params))
