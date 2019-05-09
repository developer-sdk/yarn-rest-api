#!/usr/bin/env python
# -*- coding: utf-8 -*-
from httputil import HttpRequest
import xml.etree.ElementTree as ET
import json
import xml.dom.minidom

class Yarn():
    
    def __init__(self, yarn_url, response_type = "json"):
        self.yarn_url = yarn_url                # http://192.168.10.1:8088
        self.response_type = response_type
        self.http = HttpRequest()

        if response_type == "json":
            self.headers = {'Content-Type': 'application/json' }
        elif response_type == "xml":
            self.headers = {'Accept': 'application/xml' }

    def __request_yarn__(self, uri, params=None):
        request_url = "{0}{1}".format(self.yarn_url, uri)

        if params:
            request_url = "{0}?{1}".format(request_url, self.http.param_encode(params))

        response = self.http.request(request_url, headers=self.headers)
        
        if self.response_type == "json":
            return json.loads(response.body)
        elif self.response_type == "xml":
            return ET.fromstring(response.body)
        else:
            return response.body

    def cluster_information(self):
        uri = "/ws/v1/cluster/info"
        return self.__request_yarn__(uri)

    def cluster_metrics(self):
        uri = "/ws/v1/cluster/metrics"
        return self.__request_yarn__(uri)

    def cluster_scheduler(self):
        uri = "/ws/v1/cluster/scheduler"
        return self.__request_yarn__(uri)

    def cluster_applications(self, params=None):
        # Query Parameters Supported
        uri = "/ws/v1/cluster/apps"
        return self.__request_yarn__(uri, params)

    def cluster_appstatistics(self, params=None):
        # Query Parameters Supported
        uri = "/ws/v1/cluster/appstatistics"
        return self.__request_yarn__(uri, params)

    def cluster_application(self, app_id):
        uri = "/ws/v1/cluster/apps/" + app_id
        return self.__request_yarn__(uri)

    def cluster_application_attempts(self, app_id):
        uri = "/ws/v1/cluster/apps/" + app_id + "/appattempts"
        return self.__request_yarn__(uri)

    def cluster_nodes(self, params=None):
        uri = "/ws/v1/cluster/nodes"
        return self.__request_yarn__(uri, params)

    def cluster_node(self, node_id):
        uri = "/ws/v1/cluster/nodes/" + node_id
        return self.__request_yarn__(uri)

    # Cluster Writeable APIs
    
if __name__ == '__main__':
    # https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/ResourceManagerRest.html
    yarn = Yarn("http://192.168.10.1:8088", 'xml')
    # response_obj = yarn.cluster_information()
    # response_obj = yarn.cluster_metrics()
    # response_obj = yarn.cluster_scheduler()
    # response_obj = yarn.cluster_applications()
    response_obj = yarn.cluster_applications({"limit":100})
    # response_obj = yarn.cluster_appstatistics()
    # response_obj = yarn.cluster_appstatistics({"states":"accepted,running,finished","applicationTypes":"mapreduce"})
    # response_obj = yarn.cluster_application("job_id")
    # response_obj = yarn.cluster_application_attempts("job_id")
    # response_obj = yarn.cluster_nodes()
    # response_obj = yarn.cluster_nodes({"states":"RUNNING"})  # NEW, RUNNING, UNHEALTHY, DECOMMISSIONING, DECOMMISSIONED, LOST, REBOOTED, SHUTDOWN
    # response_obj = yarn.cluster_node("node_id")

    if yarn.response_type == 'json':
        print(json.dumps(response_obj, indent=4, sort_keys=True))
    elif yarn.response_type == 'xml':
        print(xml.dom.minidom.parseString(ET.tostring(response_obj)).toprettyxml())
    else:
        print(response_obj)