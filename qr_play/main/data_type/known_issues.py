from python_helpers.ph_constants import PhConstants
from python_helpers.ph_util import PhUtil

from qr_play.main.data_type.data_type_master import DataTypeMaster
from qr_play.main.helper.data import Data

bulk_data_test_data = PhConstants.TEST_DATA_MIX_LEN_75 * 196

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


class KnownIssues(DataTypeMaster):

    def __init__(self):
        super().__init__()

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

    def set_output_path(self):
        output_path = None
        super().set_output_path(output_path)

    def set_output_file_name_keyword(self):
        output_file_name_keyword = None
        super().set_output_file_name_keyword(output_file_name_keyword)

    def set_archive_output(self):
        archive_output = None
        super().set_archive_output(archive_output)

    def set_archive_output_format(self):
        archive_output_format = None
        super().set_archive_output_format(archive_output_format)

    def set_output_format(self):
        output_format = None
        super().set_output_format(output_format)

    def set_size(self):
        size = None
        super().set_size(size)

    def set_qr_code_version(self):
        qr_code_version = None
        super().set_qr_code_version(qr_code_version)

    def set_split_qrs(self):
        split_qrs = None
        super().set_split_qrs(split_qrs)

    def set_decorate_qr(self):
        decorate_qr = None
        super().set_decorate_qr(decorate_qr)

    def set_label(self):
        label = None
        super().set_label(label)

    def set_label_position(self):
        label_position = None
        super().set_label_position(label_position)

    def set_data_pool(self):
        data_pool_high_priority = [
            #
            Data(
                remarks='Bulk Data Opportunity Old Data',
                input_data=bulk_data_2,
                print_input=False,
                qr_code_version=40,
                decorate_qr=False,
                split_qrs=True,
                dev_remarks="""Something is Definitely Wrong with the Library
                    When the QR count is 6: Qr scan is successful
                    When the QR count is 5: Qr scan does not produce result
                    Experiments Done (Some characters removed to fit in size 5): 
                      - New Line Character added in last ('\n' / '\n\r'); 
                      - '\n', Replaced with '\n\r'
                """
            ),
            #
            Data(
                remarks='Bulk Data Opportunity Test Data',
                input_data=PhUtil.generate_test_data(14765),
                print_input=False,
                qr_code_version=40,
                decorate_qr=False,
                split_qrs=True,
            ),
            #
            Data(
                remarks='Bulk Data Opportunity Test Data 6',
                input_data=PhUtil.generate_test_data(14765 + 1),
                print_input=False,
                qr_code_version=40,
                decorate_qr=False,
                split_qrs=True,
            ),
            #
        ]

        data_pool_low_priority = [
            #
        ]
        super().set_data_pool(
            data_pool_high_priority
            + data_pool_low_priority
        )
