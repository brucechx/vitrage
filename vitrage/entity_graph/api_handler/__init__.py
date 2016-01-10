# Copyright 2016 - Alcatel-Lucent
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

from oslo_log import log
from oslo_service import service as os_service


LOG = log.getLogger(__name__)


class VitrageApiHandlerService(os_service.Service):

    def __init__(self, e_graph):
        super(VitrageApiHandlerService, self).__init__()
        self.entity_graph = e_graph

    def start(self):
        LOG.info("Start VitrageApiHandlerService")

        super(VitrageApiHandlerService, self).start()

        LOG.info("Finish start VitrageApiHandlerService")

    def stop(self):
        LOG.info("Stop VitrageApiHandlerService")

        super(VitrageApiHandlerService, self).stop()

        LOG.info("Finish stop VitrageApiHandlerService")