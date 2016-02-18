#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright (c) 2016 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import ovirtsdk4 as sdk
import ovirtsdk4.types as types

# This example will connect to the server and create a new data center:

# Create the connection to the server:
connection = sdk.Connection(
    url='https://engine40.example.com/ovirt-engine/api',
    username='admin@internal',
    password='redhat123',
    ca_file='ca.pem',
    debug=True,
)

# Get the reference to the data centers service:
dcs_service = connection.system_service().data_centers_service()

# Use the "add" method to create a new data center:
dc = dcs_service.add(
    types.DataCenter(
        name='mydc',
        description='My data center',
        local=False,
    ),
)

# Close the connection to the server:
connection.close()
