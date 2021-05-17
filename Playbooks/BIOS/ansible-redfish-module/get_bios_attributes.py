import requests, json, sys, re, time, warnings, argparse

from datetime import datetime

warnings.filterwarnings("ignore")

# parser=argparse.ArgumentParser(description="Python script using Redfish API with OEM extension to change one or multiple BIOS attributes")
# parser.add_argument('-ip',help='iDRAC IP address', required=True)
# parser.add_argument('-u', help='iDRAC username', required=True)
# parser.add_argument('-p', help='iDRAC password', required=True)
# parser.add_argument('script_examples',action="store_true",help='BiosSetAttributeREDFISH.py -ip 192.168.0.120 -u root -p calvin -a MemTest -v Disabled, this example will set one BIOS attribute. BiosSetAttributeREDFISH.py -ip 192.168.0.120 -u root -p calvin -an LogicalProc,EmbSata -av Disabled,AhciMode, this example is setting multiple BIOS attributes')
# parser.add_argument('-an', help='Pass in the attribute name you want to change current value, Note: make sure to type the attribute name exactly due to case senstive. Example: MemTest will work but memtest will fail. If you want to configure multiple attribute names, make sure to use a comma separator between each attribute name.', required=True)
# parser.add_argument('-av', help='Pass in the attribute value you want to change to. Note: make sure to type the attribute value exactly due to case senstive. Example: Disabled will work but disabled will fail. If you want to configure multiple attribute values, make sure to use a comma separator between each attribute value.', required=True)

# args=vars(parser.parse_args())

# idrac_ip=args["ip"]
# idrac_username=args["u"]
# idrac_password=args["p"]

idrac_ip = '10.53.212.10'
idrac_username = 'ADMIN'
idrac_password = 'Commscope123!'

def get_bios_attributes(idrac_ip,idrac_username,idrac_password):
    f=open("bios_attributes.txt","a")
    response = requests.get('http://%s/redfish/v1/Systems' % idrac_ip,verify=False,auth=(idrac_username,idrac_password))
    import pdb; pdb.set_trace();
    data = response.json()
    d=datetime.now()
    current_date_time="- Data collection timestamp: %s-%s-%s  %s:%s:%s\n" % (d.year,d.month,d.day, d.hour,d.minute,d.second)
    f.writelines(current_date_time)
    a="\n--- BIOS Attributes ---\n"
    print(a)
    f.writelines(a)
    for i in data[u'Attributes'].items():
        attribute_name = "Attribute Name: %s\t" % (i[0])
        f.writelines(attribute_name)
        attribute_value = "Attribute Value: %s\n" % (i[1])
        f.writelines(attribute_value)
        print("Attribute Name: %s\t Attribute Value: %s" % (i[0],i[1]))
        
    print("\n- Attributes are also captured in \"bios_attributes.txt\" file")
    f.close()