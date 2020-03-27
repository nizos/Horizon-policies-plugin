# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
import itertools

from django.views import generic
from openstack_dashboard.api.rest import urls
from openstack_dashboard.api.rest import utils as rest_utils
from policies_plugin.api.rest.policy_test_api import get_text
LOG = logging.getLogger(__name__)


@urls.register
class PolicyClient(generic.View):
    url_regex = r'policy-client/policies/$'

    @rest_utils.ajax()
    def get(self, request):
        list_of_policies = []
        list_of_policies = get_text()
        test_list = list_of_policies.items()
        another_test_list = []
        for items in test_list:
          another_test_list.append(items[1])
        LOG.warning("##############################################")
        LOG.warning("!HERE client!")
        for i in list(itertools.chain.from_iterable(another_test_list)):
          LOG.warning(i)
        LOG.warning("##############################################")
        #test_list = list_of_policies.items()
        greeting = {
          'id': 'Test',
          'name': test_list[3]
        }
        #greeting = {
        #  'id': 'Hello',
        #  'name': 'Hello world!'
        #}
        policies = {'items': greeting}
        return policies
