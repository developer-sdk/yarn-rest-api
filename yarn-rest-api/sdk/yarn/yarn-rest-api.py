#!/usr/bin/env python
# -*- coding: utf-8 -*-
from httputil import HttpRequest, HttpResponse
import json

class Yarn():
    
    def __init__(self, yarn_url, response_type = "json"):
        self.yarn_url = yarn_url    # http://localhost:8088
        self.response_type = response_type
        self.http = HttpRequest()

        if response_type == "json":
            self.headers = {"Content-Type": "application/json" }
        elif response_type == "xml":
            self.headers = {"Accept": "application/xml" }
        
    def cluster_information(self):
        request_url = "{0}/ws/v1/cluster/info".format(self.yarn_url)
        response = self.http.request(request_url, headers=self.headers)
        return response.body

if __name__ == '__main__':
    yarn = Yarn("http://localhost:8088", 'json')
    result = yarn.cluster_information()