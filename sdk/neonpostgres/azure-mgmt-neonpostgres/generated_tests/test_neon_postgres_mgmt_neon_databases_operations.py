# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.neonpostgres import NeonPostgresMgmtClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestNeonPostgresMgmtNeonDatabasesOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(NeonPostgresMgmtClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_neon_databases_get(self, resource_group):
        response = self.client.neon_databases.get(
            resource_group_name=resource_group.name,
            organization_name="str",
            project_name="str",
            branch_name="str",
            neon_database_name="str",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_neon_databases_begin_create_or_update(self, resource_group):
        response = self.client.neon_databases.begin_create_or_update(
            resource_group_name=resource_group.name,
            organization_name="str",
            project_name="str",
            branch_name="str",
            neon_database_name="str",
            resource={
                "id": "str",
                "name": "str",
                "properties": {
                    "attributes": [{"name": "str", "value": "str"}],
                    "branchId": "str",
                    "createdAt": "str",
                    "entityId": "str",
                    "entityName": "str",
                    "ownerName": "str",
                    "provisioningState": "str",
                },
                "systemData": {
                    "createdAt": "2020-02-20 00:00:00",
                    "createdBy": "str",
                    "createdByType": "str",
                    "lastModifiedAt": "2020-02-20 00:00:00",
                    "lastModifiedBy": "str",
                    "lastModifiedByType": "str",
                },
                "type": "str",
            },
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_neon_databases_begin_update(self, resource_group):
        response = self.client.neon_databases.begin_update(
            resource_group_name=resource_group.name,
            organization_name="str",
            project_name="str",
            branch_name="str",
            neon_database_name="str",
            properties={
                "id": "str",
                "name": "str",
                "properties": {
                    "attributes": [{"name": "str", "value": "str"}],
                    "branchId": "str",
                    "createdAt": "str",
                    "entityId": "str",
                    "entityName": "str",
                    "ownerName": "str",
                    "provisioningState": "str",
                },
                "systemData": {
                    "createdAt": "2020-02-20 00:00:00",
                    "createdBy": "str",
                    "createdByType": "str",
                    "lastModifiedAt": "2020-02-20 00:00:00",
                    "lastModifiedBy": "str",
                    "lastModifiedByType": "str",
                },
                "type": "str",
            },
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_neon_databases_delete(self, resource_group):
        response = self.client.neon_databases.delete(
            resource_group_name=resource_group.name,
            organization_name="str",
            project_name="str",
            branch_name="str",
            neon_database_name="str",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_neon_databases_list(self, resource_group):
        response = self.client.neon_databases.list(
            resource_group_name=resource_group.name,
            organization_name="str",
            project_name="str",
            branch_name="str",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...
