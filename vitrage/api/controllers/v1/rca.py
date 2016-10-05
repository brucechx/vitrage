# Copyright 2016 - Nokia Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import json

import pecan

from oslo_log import log
from pecan.core import abort
from vitrage.api.controllers.rest import RootRestController
from vitrage.api.policy import enforce

# noinspection PyProtectedMember
from vitrage.i18n import _LI


LOG = log.getLogger(__name__)


class RCAController(RootRestController):
    @pecan.expose('json')
    def index(self, alarm_id):
        enforce('get rca', pecan.request.headers,
                pecan.request.enforcer, {})

        LOG.info(_LI('received show rca with alarm id %s') % alarm_id)
        if pecan.request.cfg.api.use_mock_file:
            return self.get_mock_data('rca.sample.json')
        else:
            return self.get_rca(alarm_id)

    @staticmethod
    def get_rca(alarm_id):
        try:
            graph_data = pecan.request.client.call(pecan.request.context,
                                                   'get_rca',
                                                   root=alarm_id)
            LOG.info(graph_data)
            graph = json.loads(graph_data)
            return graph

        except Exception as e:
            LOG.exception('failed to get rca %s ', e)
            abort(404, str(e))
