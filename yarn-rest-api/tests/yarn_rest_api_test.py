'''
Created on May 14, 2019

@author: seo
'''
from hadoop.yarn import Yarn
import xml.etree.ElementTree as ET
import json
import xml.dom.minidom

def main():
    yarn = Yarn("http://localhost:8088", 'json')
    response_obj = yarn.cluster_information()
    # response_obj = yarn.cluster_metrics()
    # response_obj = yarn.cluster_scheduler()
    # response_obj = yarn.cluster_applications()
    # response_obj = yarn.cluster_applications({"limit":100})
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
    
if __name__ == '__main__':
    main()