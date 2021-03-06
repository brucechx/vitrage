# Copyright 2016 - Nokia
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import abc
import six


@six.add_metaclass(abc.ABCMeta)
class NotifierBase(object):

    @abc.abstractmethod
    def process_event(self, data, event_type):
        pass

    @staticmethod
    @abc.abstractmethod
    def get_notifier_name():
        pass

    @staticmethod
    def use_private_topic():
        return False

    @staticmethod
    def info(self, ctxt, publisher_id, event_type, payload, metadata):
        """An endpoint for notifiers that use a private topic"""
        pass
