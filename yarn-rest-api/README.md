# Hadoop YARN REST API

This is Python Library for Hadoop YARN REST api.

This project follows the [Resource Manager Rest](https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/ResourceManagerRest.html) document.

## Usage

### install
```python
pip install hadoop-yarn-rest-api
```

### Example

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from hadoop.yarn import Yarn


if __name__ == '__main__':
	yarn_url = "http://localhost:8088"
	response_type = "json"
	
    yarn = Yarn(yarn_url, response_type)
    
    response_obj = yarn.cluster_information()
    response_obj = yarn.cluster_metrics()
    response_obj = yarn.cluster_scheduler()
    response_obj = yarn.cluster_applications()
    response_obj = yarn.cluster_applications({"limit":100})
    response_obj = yarn.cluster_appstatistics()
    response_obj = yarn.cluster_appstatistics({"states":"accepted,running,finished","applicationTypes":"mapreduce"})
    response_obj = yarn.cluster_application("job_id")
    response_obj = yarn.cluster_application_attempts("job_id")
    response_obj = yarn.cluster_nodes()
    response_obj = yarn.cluster_nodes({"states":"RUNNING"})  # NEW, RUNNING, UNHEALTHY, DECOMMISSIONING, DECOMMISSIONED, LOST, REBOOTED, SHUTDOWN
    response_obj = yarn.cluster_node("node_id")

    if yarn.response_type == 'json':
        print(json.dumps(response_obj, indent=4, sort_keys=True))
    elif yarn.response_type == 'xml':
        print(xml.dom.minidom.parseString(ET.tostring(response_obj)).toprettyxml())
    else:
        print(response_obj)
```
