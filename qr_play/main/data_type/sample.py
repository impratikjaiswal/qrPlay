from collections import OrderedDict

from python_helpers.ph_util import PhUtil

from qr_play.main.data_type.data_type_master import DataTypeMaster
from qr_play.main.helper.data import Data
from qr_play.main.helper.formats import Formats

# Data has to be declared in global, so that it can be used by other classes
small_data = 'Welcome To QrPlay'

bulk_data_1 = """}**************************************************{ ToDO
}+++++++++++++++++++++++++{ Explore 
CLI
Cloudshell;  CLI Browser
SDK
ENI is available automatically?
Instance with Custom EBS volume only (EBS snapshot)
}----------------------------------------------------------------------------------------------------{ 
AWS Global Infrastructure
- AWS Regions (e.g. ap-southeast-2 => asia specific Sydney )
- AWS Availability Zones (e.g. ap-southeast-2a, ap-southeast-2b, ap-southeast-2c)
- AWS Data Centers
- AWS Edge Locations /Points of Presence
}----------------------------------------------------------------------------------------------------{ 
Many services are Region-scoped, but few are global (like IAM, Route53)
}----------------------------------------------------------------------------------------------------{ 
Each AZ: one ore more discreate Data centers with redundant power, networking , connectivity. isolated from disasters.
}**************************************************{ IAM: Global Service 
Least Privilege Principle
    Don't give more permission than a user need
One user can be part of multiple groups
Inline IAM Policy (Direct to individual)
    VS 
IAM Policy inheritance (inherit from group)
}**************************************************{ Access AWS
    AWS Management Console  (Access: Password & MFA)
    AWS CLI                 (Access: Access Keys (Access Key ID, Secret Access Key))
    AWS SDK                 (Access: Access Keys)
}**************************************************{     
IAM User    (Permission to user to perform action)
    Vs 
IAM Role    (Permission to service to perform action on your behalf)
}**************************************************{ IAM Security Tools
IAM Credential Report (Account Level)
IAM Access Advisor (User level)
    All service permissions granted and last accessed. helpful to revise policies
}----------------------------------------------------------------------------------------------------{ AWS Billing
Billing Information has to be enabled for IAM Access (if needed)
Bills page has option for "charges by Service"; region specific data is available.
Free tier usage balance
}**************************************************{ Budget
Email Triggers: Actual 85% & 100% or forecast is 100%
}----------------------------------------------------------------------------------------------------{ EC2
If a instance is stopped, AWS is not going to bill it. 
If a instance is stopped & Started, Public IP may changed. Private is fixed.
SSH is not allowed with Private IP unless VPN is not established.
}**************************************************{ SG: Security Group
allow rules; control how traffic is allowed in & out of EC2 instance
can be refence by IP of other SG
if application is not accessible (time out error), then its a SG issue.
if There's a connection refused; This means the instance is reachable, Not an SG issue; its application g"""

bulk_data_2 = """}**************************************************{ ToDO
}+++++++++++++++++++++++++{ Explore 
CLI
Cloudshell;  CLI Browser
SDK
ENI is available automatically?
Instance with Custom EBS volume only (EBS snapshot)
}----------------------------------------------------------------------------------------------------{ 
AWS Global Infrastructure
- AWS Regions (e.g. ap-southeast-2 => asia specific Sydney )
- AWS Availability Zones (e.g. ap-southeast-2a, ap-southeast-2b, ap-southeast-2c)
- AWS Data Centers
- AWS Edge Locations /Points of Presence
}----------------------------------------------------------------------------------------------------{ 
Many services are Region-scoped, but few are global (like IAM, Route53)
}----------------------------------------------------------------------------------------------------{ 
Each AZ: one ore more discreate Data centers with redundant power, networking , connectivity. isolated from disasters.
}**************************************************{ IAM: Global Service 
Least Privilege Principle
    Don't give more permission than a user need
One user can be part of multiple groups
Inline IAM Policy (Direct to individual)
    VS 
IAM Policy inheritance (inherit from group)
}**************************************************{ Access AWS
    AWS Management Console  (Access: Password & MFA)
    AWS CLI                 (Access: Access Keys (Access Key ID, Secret Access Key))
    AWS SDK                 (Access: Access Keys)
}**************************************************{     
IAM User    (Permission to user to perform action)
    Vs 
IAM Role    (Permission to service to perform action on your behalf)
}**************************************************{ IAM Security Tools
IAM Credential Report (Account Level)
IAM Access Advisor (User level)
    All service permissions granted and last accessed. helpful to revise policies
}----------------------------------------------------------------------------------------------------{ AWS Billing
Billing Information has to be enabled for IAM Access (if needed)
Bills page has option for "charges by Service"; region specific data is available.
Free tier usage balance
}**************************************************{ Budget
Email Triggers: Actual 85% & 100% or forecast is 100%
}----------------------------------------------------------------------------------------------------{ EC2
If a instance is stopped, AWS is not going to bill it. 
If a instance is stopped & Started, Public IP may changed. Private is fixed.
SSH is not allowed with Private IP unless VPN is not established.
}**************************************************{ SG: Security Group
allow rules; control how traffic is allowed in & out of EC2 instance
can be refence by IP of other SG
if application is not accessible (time out error), then its a SG issue.
if There's a connection refused; This means the instance is reachable, Not an SG issue; its application g}**************************************************{ ToDO
}+++++++++++++++++++++++++{ Explore 
CLI
Cloudshell;  CLI Browser
SDK
ENI is available automatically?
Instance with Custom EBS volume only (EBS snapshot)
}----------------------------------------------------------------------------------------------------{ 
AWS Global Infrastructure
- AWS Regions (e.g. ap-southeast-2 => asia specific Sydney )
- AWS Availability Zones (e.g. ap-southeast-2a, ap-southeast-2b, ap-southeast-2c)
- AWS Data Centers
- AWS Edge Locations /Points of Presence
}----------------------------------------------------------------------------------------------------{ 
Many services are Region-scoped, but few are global (like IAM, Route53)
}----------------------------------------------------------------------------------------------------{ 
Each AZ: one ore more discreate Data centers with redundant power, networking , connectivity. isolated from disasters.
}**************************************************{ IAM: Global Service 
Least Privilege Principle
    Don't give more permission than a user need
One user can be part of multiple groups
Inline IAM Policy (Direct to individual)
    VS 
IAM Policy inheritance (inherit from group)
}**************************************************{ Access AWS
    AWS Management Console  (Access: Password & MFA)
    AWS CLI                 (Access: Access Keys (Access Key ID, Secret Access Key))
    AWS SDK                 (Access: Access Keys)
}**************************************************{     
IAM User    (Permission to user to perform action)
    Vs 
IAM Role    (Permission to service to perform action on your behalf)
}**************************************************{ IAM Security Tools
IAM Credential Report (Account Level)
IAM Access Advisor (User level)
    All service permissions granted and last accessed. helpful to revise policies
}----------------------------------------------------------------------------------------------------{ AWS Billing
Billing Information has to be enabled for IAM Access (if needed)
Bills page has option for "charges by Service"; region specific data is available.
Free tier usage balance
}**************************************************{ Budget
Email Triggers: Actual 85% & 100% or forecast is 100%
}----------------------------------------------------------------------------------------------------{ EC2
If a instance is stopped, AWS is not going to bill it. 
If a instance is stopped & Started, Public IP may changed. Private is fixed.
SSH is not allowed with Private IP unless VPN is not established.
}**************************************************{ SG: Security Group
allow rules; control how traffic is allowed in & out of EC2 instance
can be refence by IP of other SG
if application is not accessible (time out error), then its a SG issue.
if There's a connection refused; This means the instance is reachable, Not an SG issue; its application issue in instance
}**************************************************{ 
IA: Infrequent Access
}+++++++++++++++++++++++++{ Explore 
CLI
Cloudshell;  CLI Browser
SDK
ENI is available automatically?
Instance with Custom EBS volume only (EBS snapshot)
}----------------------------------------------------------------------------------------------------{ 
AWS Global Infrastructure
- AWS Regions (e.g. ap-southeast-2 => asia specific Sydney )
- AWS Availability Zones (e.g. ap-southeast-2a, ap-southeast-2b, ap-southeast-2c)
- AWS Data Centers
- AWS Edge Locations /Points of Presence
}----------------------------------------------------------------------------------------------------{ 
Many services are Region-scoped, but few are global (like IAM, Route53)
}----------------------------------------------------------------------------------------------------{ 
Each AZ: one ore more discreate Data centers with redundant power, networking , connectivity. isolated from disasters.
}**************************************************{ IAM: Global Service 
Least Privilege Principle
    Don't give more permission than a user need
One user can be part of multiple groups
Inline IAM Policy (Direct to individual)
    VS 
IAM Policy inheritance (inherit from group)
}**************************************************{ Access AWS
    AWS Management Console  (Access: Password & MFA)
    AWS CLI                 (Access: Access Keys (Access Key ID, Secret Access Key))
    AWS SDK                 (Access: Access Keys)
}**************************************************{     
IAM User    (Permission to user to perform action)
    Vs 
IAM Role    (Permission to service to perform action on your behalf)
}**************************************************{ IAM Security Tools
IAM Credential Report (Account Level)
IAM Access Advisor (User level)
    All service permissions granted and last accessed. helpful to revise policies
}----------------------------------------------------------------------------------------------------{ AWS Billing
Billing Information has to be enabled for IAM Access (if needed)
Bills page has option for "charges by Service"; region specific data is available.
Free tier usage balance
}**************************************************{ Budget
Email Triggers: Actual 85% & 100% or forecast is 100%
}----------------------------------------------------------------------------------------------------{ EC2
If a instance is stopped, AWS is not going to bill it. 
If a instance is stopped & Started, Public IP may changed. Private is fixed.
SSH is not allowed with Private IP unless VPN is not established.
}**************************************************{ SG: Security Group
allow rules; control how traffic is allowed in & out of EC2 instance
can be refence by IP of other SG
if application is not accessible (time out error), then its a SG issue.
if There's a connection refused; This means the instance is reachable, Not an SG issue; its application g}**************************************************{ ToDO
}+++++++++++++++++++++++++{ Explore 
CLI
Cloudshell;  CLI Browser
SDK
ENI is available automatically?
Instance with Custom EBS volume only (EBS snapshot)
}----------------------------------------------------------------------------------------------------{ 
AWS Global Infrastructure
- AWS Regions (e.g. ap-southeast-2 => asia specific Sydney )
- AWS Availability Zones (e.g. ap-southeast-2a, ap-southeast-2b, ap-southeast-2c)
- AWS Data Centers
- AWS Edge Locations /Points of Presence
}----------------------------------------------------------------------------------------------------{ 
Many services are Region-scoped, but few are global (like IAM, Route53)
}----------------------------------------------------------------------------------------------------{ 
Each AZ: one ore more discreate Data centers with redundant power, networking , connectivity. isolated from disasters.
}**************************************************{ IAM: Global Service 
Least Privilege Principle
    Don't give more permission than a user need
One user can be part of multiple groups
Inline IAM Policy (Direct to individual)
    VS 
IAM Policy inheritance (inherit from group)
}**************************************************{ Access AWS
    AWS Management Console  (Access: Password & MFA)
    AWS CLI                 (Access: Access Keys (Access Key ID, Secret Access Key))
    AWS SDK                 (Access: Access Keys)
}**************************************************{     
IAM User    (Permission to user to perform action)
    Vs 
IAM Role    (Permission to service to perform action on your behalf)
}**************************************************{ IAM Security Tools
IAM Credential Report (Account Level)
IAM Access Advisor (User level)
    All service permissions granted and last accessed. helpful to revise policies
}----------------------------------------------------------------------------------------------------{ AWS Billing
Billing Information has to be enabled for IAM Access (if needed)
Bills page has option for "charges by Service"; region specific data is available.
Free tier usage balance
}**************************************************{ Budget
Email Triggers: Actual 85% & 100% or forecast is 100%
}----------------------------------------------------------------------------------------------------{ EC2
If a instance is stopped, AWS is not going to bill it. 
If a instance is stopped & Started, Public IP may changed. Private is fixed.
SSH is not allowed with Private IP unless VPN is not established.
}**************************************************{ SG: Security Group
allow rules; control how traffic is allowed in & out of EC2 instance
can be refence by IP of other SG
if application is not accessible (time out error), then its a SG issue.
if There's a connection refused; This means the instance is reachable, Not an SG issue; its application issue in instance
}**************************************************{ 
IA: Infrequent Access
}+++++++++++++++++++++++++{ Explore 
CLI
Cloudshell;  CLI Browser
SDK
ENI is available automatically?
Instance with Custom EBS volume only (EBS snapshot)
}----------------------------------------------------------------------------------------------------{ 
AWS Global Infrastructure
- AWS Regions (e.g. ap-southeast-2 => asia specific Sydney )
- AWS Availability Zones (e.g. ap-southeast-2a, ap-southeast-2b, ap-southeast-2c)
- AWS Data Centers
- AWS Edge Locations /Points of Presence
}----------------------------------------------------------------------------------------------------{ 
Many services are Region-scoped, but few are global (like IAM, Route53)
}----------------------------------------------------------------------------------------------------{ 
Each AZ: one ore more discreate Data centers with redundant power, networking , connectivity. isolated from disasters.
}**************************************************{ IAM: Global Service 
Least Privilege Principle
    Don't give more permission than a user need
One user can be part of multiple groups
Inline IAM Policy (Direct to individual)
    VS 
IAM Policy inheritance (inherit from group)
}**************************************************{ Access AWS
    AWS Management Console  (Access: Password & MFA)
    AWS CLI                 (Access: Access Keys (Access Key ID, Secret Access Key))
    AWS SDK                 (Access: Access Keys)
}**************************************************{     
IAM User    (Permission to user to perform action)
    Vs 
IAM Role    (Permission to service to perform action on your behalf)
}**************************************************{ IAM Security Tools
IAM Credential Report (Account Level)
IAM Access Advisor (User level)
    All service permissions granted and last accessed. helpful to revise policies
}----------------------------------------------------------------------------------------------------{ AWS Billing
Billing Information has to be enabled for IAM Access (if needed)
Bills page has option for "charges by Service"; region specific data is available.
Free tier usage balance
}**************************************************{ Budget
Email Triggers: Actual 85% & 100% or forecast is 100%
}----------------------------------------------------------------------------------------------------{ EC2
If a instance is stopped, AWS is not going to bill it. 
If a instance is stopped & Started, Public IP may changed. Private is fixed.
SSH is not allowed with Private IP unless VPN is not established.
}**************************************************{ SG: Security Group
allow rules; control how traffic is allowed in & out of EC2 instance
can be refence by IP of other SG
if application is not accessible (time out error), then its a SG issue.
if There's a connection refused; This means the instance is reachable, Nota"""


class Sample(DataTypeMaster):

    def get_sample_data_pool_for_web(self):
        if not self.data_pool:
            self.set_data_pool()
        sample_data_dic = OrderedDict()
        for data in self.data_pool:
            remarks = data.remarks
            remarks = PhUtil.to_list(remarks, all_str=True, trim_data=True)
            if len(remarks) < 1:
                raise ValueError("Remarks should not be empty")
            key, data.data_group = PhUtil.generate_key_and_data_group(remarks)
            if key in sample_data_dic:
                raise ValueError(f'Duplicate Sample Remarks: {key}')
            sample_data_dic.update({key: super().to_dic(data)})
        return sample_data_dic

    def set_print_input(self):
        print_input = None
        super().set_print_input(print_input)

    def set_print_output(self):
        print_output = None
        super().set_print_output(print_output)

    def set_print_info(self):
        print_info = None
        super().set_print_info(print_info)

    def set_quiet_mode(self):
        quite_mode = None
        super().set_quiet_mode(quite_mode)

    def set_remarks(self):
        remarks = None
        super().set_remarks(remarks)

    def set_encoding(self):
        encoding = None
        super().set_encoding(encoding)

    def set_encoding_errors(self):
        encoding_errors = None
        super().set_encoding_errors(encoding_errors)

    def set_archive_output(self):
        archive_output = None
        super().set_archive_output(archive_output)

    def set_archive_output_format(self):
        archive_output_format = None
        super().set_archive_output_format(archive_output_format)

    def set_image_format(self):
        image_format = None
        super().set_image_format(image_format)

    def set_scale(self):
        scale = None
        super().set_scale(scale)

    def set_qr_code_version(self):
        qr_code_version = None
        super().set_qr_code_version(qr_code_version)

    def set_split_qrs(self):
        split_qrs = None
        super().set_split_qrs(split_qrs)

    def set_data_pool(self):
        data_pool = [
            #
            Data(
                remarks='Simple Qr (LPA)',
                input_data='LPA:1$SMDP.EXAMPLE.COM$04386-AGYFT-A74Y8-3F815',
            ),
            #
            Data(
                remarks='Simple Qr (Google Pay/GPay)',
                input_data='upi://pay?pa=impratikjaiswal@okicici&pn=Pratik%20Jaiswal&aid=uGICAgICw6tuJBw',
            ),
            #
            Data(
                remarks='Simple Qr; qr_code_version=20; scale=8',
                input_data=small_data,
                scale=10,
                qr_code_version=20,
            ),
            #
            Data(
                remarks='Simple Qr; png uri',
                input_data=small_data,
                image_format=Formats.PNG_URI,
            ),
            #
            Data(
                remarks='Simple Qr; svg',
                input_data=small_data,
                image_format=Formats.SVG,
            ),
            #
            Data(
                remarks='Simple Qr; svg uri',
                input_data=small_data,
                image_format=Formats.SVG_URI,
            ),
            #
            Data(
                remarks='Bulk Data Single Qr',
                input_data=bulk_data_1,
                qr_code_version=40,
                split_qrs=False,
            ),
            #
            Data(
                remarks='Bulk Data Split Qrs',
                input_data=bulk_data_2,
                qr_code_version=40,
                split_qrs=True,
            ),
            #
            Data(
                remarks='Bulk Data Single Qr; PNG URI',
                input_data=bulk_data_1,
                qr_code_version=40,
                split_qrs=False,
                image_format=Formats.PNG_URI,
            ),
            #
            Data(
                remarks='Bulk Data Split Qrs; PNG URI',
                input_data=bulk_data_2,
                qr_code_version=40,
                split_qrs=True,
                image_format=Formats.PNG_URI,
            ),
            #
        ]
        super().set_data_pool(data_pool)
