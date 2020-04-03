/*
 * Licensed under the Apache License, Version 2.0 (the 'License');
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an 'AS IS' BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
(function () {
    'use strict';

    /**
     * @ngdoc overview
     * @name horizon.dashboard.identity.policy
     * @description
     * A sample top level module.
     */

    angular
        .module('horizon.dashboard.identity.policy', [
            'ngRoute',
            'horizon.dashboard.identity.policy.policies.details'
        ])
        .config(config);
        // this is the right place to add .constant() declarations for
        // the module

    config.$inject = [
        '$provide',
        '$windowProvider',
        '$routeProvider'
    ];

    function config($provide, $windowProvider, $routeProvider) {
        var basePath = $windowProvider.$get().STATIC_URL + 'dashboard/identity/policy/';
        $provide.constant('horizon.dashboard.identity.policy.basePath', basePath);

        var policies = '/identity/policies/details';

        $routeProvider.when(policies, {
            templateUrl: basePath + 'details/details.html'
        });
    }

}());
