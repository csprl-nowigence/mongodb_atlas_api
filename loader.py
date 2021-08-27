import os

from dotenv import load_dotenv

load_dotenv()

ATLAS_API_PUBLIC_KEY = os.getenv("ATLAS_API_PUBLIC_KEY")
ATLAS_API_PRIVATE_KEY = os.getenv("ATLAS_API_PRIVATE_KEY")
ATLAS_GROUP_ID = os.getenv("ATLAS_GROUP_ID")
ATLAS_ORG_ID = os.getenv("ATLAS_ORG_ID")
ATLAS_CLUSTER_NAME = os.getenv("ATLAS_CLUSTER_NAME")

from atlas_search import AtlasSearchClient
asc = AtlasSearchClient(ATLAS_API_PUBLIC_KEY, ATLAS_API_PRIVATE_KEY, ATLAS_GROUP_ID, ATLAS_CLUSTER_NAME)

from access_list import AccessListClient
alc = AccessListClient(ATLAS_API_PUBLIC_KEY, ATLAS_API_PRIVATE_KEY, ATLAS_GROUP_ID)

from alerts import AlertsClient
ac = AlertsClient(ATLAS_API_PUBLIC_KEY, ATLAS_API_PRIVATE_KEY, ATLAS_GROUP_ID)

from data_lake import DataLakeClient
dlc = DataLakeClient(ATLAS_API_PUBLIC_KEY, ATLAS_API_PRIVATE_KEY, ATLAS_GROUP_ID)

from invoices import InvoicesClient
ic = InvoicesClient(ATLAS_API_PUBLIC_KEY, ATLAS_API_PRIVATE_KEY, ATLAS_ORG_ID)

from root import RootClient
rc = RootClient(ATLAS_API_PUBLIC_KEY, ATLAS_API_PRIVATE_KEY)
