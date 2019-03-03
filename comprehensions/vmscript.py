from pprint import pprint
import libcloud
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver
import yaml
import io

with open('./vm.yaml', 'r') as f:
    try:
        creds = yaml.load(f)
    except yaml.YAMLError as exc:
        print(exc)




EC2Driver = get_driver(Provider.EC2)
conn = EC2Driver(creds['EC2_ACCESS_ID'], creds['EC2_SECRET_KEY'], region="us-west-1")

nodes = conn.list_nodes()
node = [n for n in nodes if 'testServer' in n.name][0]
print(node)

conn.ex_start_node(node=node)

print(conn.list_nodes())

conn.ex_stop_node(node=node)





