#!/usr/bin/env python
# -*- coding: utf-8 -*-
from httputil import HttpRequest, HttpResponse
import json

class Yarn():
    
    def __init__(self, yarn_url, response_type = "json"):
        self.yarn_url = yarn_url    # http://10.11.96.221:8088
        self.response_type = response_type
        self.http = HttpRequest()

        if response_type == "json":
            self.headers = {'Content-Type': 'application/json' }
        elif response_type == "xml":
            self.headers = {'Accept': 'application/xml' }

    def request_yarn(self, uri, params=None):
        request_url = "{0}{1}".format(self.yarn_url, uri)

        if params:
            request_url = "{0}?{1}".format(request_url, self.http.param_encode(params))

        response = self.http.request(request_url, headers=self.headers)
        
        if self.response_type == "json":
            return json.loads(response.body)
        elif self.response_type == "xml":
            return xml.etree.ElementTree.fromstring(response.body)
        else:
            return response.body

    def cluster_information(self):
        uri = "/ws/v1/cluster/info"
        return self.request_yarn(uri)

    def cluster_metrics(self):
        uri = "/ws/v1/cluster/metrics"
        return self.request_yarn(uri)

    def cluster_scheduler(self):
        uri = "/ws/v1/cluster/scheduler"
        return self.request_yarn(uri)

    def cluster_applications(self):
        # Query Parameters Supported
        uri = "/ws/v1/cluster/apps"
        return self.request_yarn(uri)

    def cluster_appstatistics(self, params=None):
        # Query Parameters Supported
        uri = "/ws/v1/cluster/appstatistics"
        return self.request_yarn(uri, params)

if __name__ == '__main__':
    yarn = Yarn("http://127.0.0.1:8088", 'json')
    # json_obj = yarn.cluster_information()
    # json_obj = yarn.cluster_metrics()
    # json_obj = yarn.cluster_scheduler()
    # json_obj = yarn.cluster_applications()  # query
    # json_obj = yarn.cluster_appstatistics()
    json_obj = yarn.cluster_appstatistics({"states":"accepted,running,finished","applicationTypes":"mapreduce"})

    print(json.dumps(json_obj, indent=4, sort_keys=True))