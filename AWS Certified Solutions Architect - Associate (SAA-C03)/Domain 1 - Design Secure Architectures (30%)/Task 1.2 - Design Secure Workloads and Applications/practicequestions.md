# Task 1.2 - Design Secure Workloads and Applications - Practice Questions

> **Domain 1 - Design Secure Architectures (30%)**  
> Curated from 18 practice sets: duplicates removed, outdated items retired, ordered **highest-frequency exam topics first**.  
> **83 multiple-choice (single answer)** followed by **35 multiple-response (select 2+)**. Total **118**.


**Topic order in this file:** VPC Security Groups & NACLs → IAM Roles, Policies & Permissions → DynamoDB Design & Capacity → RDS Multi-AZ, Read Replicas & Aurora → S3 Security, Access & Durability → S3 Storage Classes & Lifecycle → VPC Connectivity: Endpoints, Peering, TGW → High Availability & Fault Tolerance → CloudFront & Edge Delivery → EC2 Instances, AMIs & Placement → Route 53 & DNS Routing → Hybrid Connectivity: Direct Connect & VPN → Monitoring: CloudWatch, CloudTrail & Config → AWS Organizations & Multi-Account → Cost Management & Optimization Tools → Secrets, Parameters & Credentials → General Design → Elastic Beanstalk & Deployment → Auto Scaling & Elastic Load Balancing → Encryption & AWS KMS → Lambda & Serverless Compute → Federation, SSO & Cognito → Threat Detection & Compliance


---


# Section A - Multiple Choice (one correct answer)


## VPC Security Groups & NACLs


**Q1.** You are a Solutions Architect at Digital Cloud Training. One of your clients has requested some advice on how to implement security measures in their VPC. The client has recently been the victim of some hacking attempts. Fortunately, no data has been exposed at this point but the client wants to implement measures to mitigate further threats. The client has explained that the attacks always come from the same small block of IP addresses. What would be a quick and easy measure to help prevent further attacks?

- **A.** Use a Network ACL rule that denies connections from the block of IP addresses
- **B.** Create a Bastion Host restrict all connections to the Bastion Host only
- **C.** Use CloudFront’s DDoS prevention features
- **D.** Use a Security Group rule that denies connections from the block of IP addresses


**Q2.** What aspect of an Amazon VPC is stateful?

- **A.** Network ACLs
- **B.** Amazon S3
- **C.** Security groups
- **D.** Amazon DynamoDB


**Q3.** You are tasked with setting up a Linux bastion host for access to Amazon EC2 instances running in your VPC. Only clients connecting from the corporate external public IP address 72.34.51.100 should have SSH access to the host. Which option will meet the customer requirement?

- **A.** Security Group Inbound Rule: Protocol - TCP. Port Range - 22, Source 72.34.51.100/32
- **B.** Security Group Inbound Rule: Protocol - UDP, Port Range - 22, Source 72.34.51.100/32
- **C.** Network ACL Inbound Rule: Protocol - UDP, Port Range - 22, Source 72.34.51.100/32
- **D.** Network ACL Inbound Rule: Protocol - TCP, Port Range-22, Source 72.34.51.100/0


**Q4.** You are working for a large financial firm and you are instructed to set up a Linux bastion host. It will allow access to the Amazon EC2 instances running in their VPC. For security purposes, only the clients connecting from the corporate external public IP address 175.45.116.100 should have SSH access to the host. Which is the best option that can meet the customer's requirement?

- **A.** Security Group Inbound Rule: Protocol – UDP, Port Range – 22, Source 175.45.116.100/32
- **B.** Security Group Inbound Rule: Protocol – TCP. Port Range – 22, Source 175.45.116.100/32
- **C.** Network ACL Inbound Rule: Protocol – UDP, Port Range – 22, Source 175.45.116.100/32
- **D.** Network ACL Inbound Rule: Protocol – TCP, Port Range-22, Source 175.45.116.100/0


**Q5.** An instance is launched into a VPC subnet with the network ACL configured to allow all inbound traffic and deny all outbound traffic. The instance's security group is configured to allow SSH from any IP address and deny all outbound traffic. What changes need to be made to allow SSH access to the instance?

- **A.** Nothing, it can be accessed from any IP address using SSH.
- **B.** The outbound security group needs to be modified to allow outbound traffic.
- **C.** The outbound network ACL needs to be modified to allow outbound traffic.
- **D.** Both the outbound security group and outbound network ACL need to be modified to


**Q6.** Which of the following Amazon Virtual Private Cloud (Amazon VPC) elements acts as a stateless firewall?

- **A.** An Amazon VPC endpoint
- **B.** Network Access Control List (ACL)
- **C.** Security group
- **D.** Network Address Translation (NAT) instance


**Q7.** You are unable to connect to your newly deployed EC2 instance via SSH from your home computer. However, you were able to successfully access other existing instances in your VPC without any issues. Which of the following should you check and possibly correct to restore connectivity?

- **A.** Use Amazon Data Lifecycle Manager.
- **B.** Configure the Security Group of the EC2 instance to permit ingress traffic over port 22 from your IP.
- **C.** Configure the Network Access Control List of your VPC to permit ingress traffic over port 22 from your IP.
- **D.** Configure the Security Group of the EC2 instance to permit ingress traffic over port 3389 from your IP.


**Q8.** You are trying to SSH into an EC2 instance running Linux but cannot connect. The EC2 instance has been launched in a public subnet with an Internet Gateway. Upon investigation you have verified that the instance has a public IP address and that the route table does reference the Internet Gateway correctly. What else needs to be checked to enable connectivity?

- **A.** Check that the Security Groups and Network ACLs have the correct rules configured
- **B.** Check that the VPN is configured correctly
- **C.** Check that the subnet CIDR block is referenced properly in the route table
- **D.** Check that there is a Bastion Host in the subnet and connect to it first


**Q9.** For security reasons, you need to ensure that an On-Demand EC2 instance can only be accessed from a specific public IP address (100.156.52.12) using the SSH protocol. You are configuring the Security Group of the EC2 instance, and need to configure an Inbound rule. Which of the rules below will achieve the requirement?

- **A.** Protocol - TCP, Port Range - 22, Source 100.156.52.12/0
- **B.** Protocol - UDP, Port Range - 22, Source 100.156.52.12/0
- **C.** Protocol - UDP, Port Range - 22, Source 100.156.52.12/32
- **D.** Protocol - TCP, Port Range - 22, Source 100.156.52.12/32


**Q10.** A colleague from your company’s IT Security team has notified you of an Internet-based threat that affects a certain port and protocol combination. You have conducted an audit of your VPC and found that this port and protocol combination is allowed on an Inbound Rule with a source of 0.0.0.0/0. You have verified that this rule only exists for maintenance purposes and need to make an urgent change to block the access. What is the fastest way to block access from the Internet to the specific ports and protocols?

- **A.** Delete the security group
- **B.** Add a deny rule to the security group with a higher priority
- **C.** Update the security group by removing the rule
- **D.** You don’t need to do anything; this rule will only allow access to VPC based resources


**Q11.** You have an On-Demand EC2 instance located in a subnet in AWS which hosts a web application. The security group attached to this EC2 instance has the following Inbound Rules: The Route table attached to the VPC is shown below. You can establish an SSH connection into the EC2 instance from the internet. However, you are not able to connect to the web server using your Chrome browser. Which of the below steps would resolve the issue?

- **A.** In the Security Group, add an Inbound HTTP rule.
- **B.** In the Route table, add this new route entry: 0.0.0.0 -> igw-b51618cc
- **C.** In the Security Group, remove the SSH rule.
- **D.** In the Route table, add this new route entry: 10.0.0.0/27 -> local


**Q12.** Which of the following is an optional security control that can be applied at the subnet layer of a VPC?

- **A.** Firewall
- **B.** Web application firewall
- **C.** Security Group
- **D.** Network ACL


**Q13.** You are responsible for your company’s AWS resources, and you notice a significant amount of traffic from an IP address in a foreign country in which your company does not have customers. Further investigation of the traffic indicates the source of the traffic is scanning for open ports on your EC2-VPC instances. Which one of the following resources can deny the traffic from reaching the instances?

- **A.** Network ACL
- **B.** Security group
- **C.** An Amazon VPC endpoint
- **D.** NAT instance


**Q14.** You can use _____ and _____ to help secure the instances in your VPC.

- **A.** security groups and biometric authentication
- **B.** security groups and 2-Factor authentication
- **C.** security groups and multi-factor authentication
- **D.** security groups and network ACLs


**Q15.** Security groups act like a firewall at the instance level, whereas ____________ are an additional layer of security that act at the subnet level.

- **A.** DB Security Groups
- **B.** VPC Security Groups
- **C.** Network ACLs


**Q16.** What is the purpose of the native VPC router?

- **A.** Route packets across VPN
- **B.** Route packets across the internet
- **C.** Route packets from instances to S3 storage volumes
- **D.** Route packets between private cloud instances
- **E.** Route packets between subnets


**Q17.** What AWS best practice is recommended for creating fault tolerant systems?

- **A.** RedShift
- **B.** Vertical scaling
- **C.** Security groups
- **D.** Horizontal scaling
- **E.** Elastic IP (EIP)


**Q18.** If you're unable to connect via SSH to your EC2 instance, which of the following should you check and possibly correct to restore connectivity?

- **A.** Adjust the instance's Security Group to permit ingress traffic over port 22 from your IP.
- **B.** Configure the IAM role to permit changes to security group settings.
- **C.** Apply the most recently released Operating System security patches.
- **D.** Adjust Security Group to permit egress traffic over TCP port 443 from your IP.
- **E.** Modify the instance security group to allow ingress of ICMP packets from your IP.


**Q19.** A company is using a custom shell script to automate the deployment and management of their EC2 instances. The script is using various AWS CLI commands such as revoke-security-group-ingress, revoke-security-group-egress, run-scheduled-instances and many others. In the shell script, what does the revoke-security-group-ingress command do?

- **A.** Removes one or more egress rules from a security group.
- **B.** Removes one or more security groups from a rule.
- **C.** Removes one or more ingress rules from a security group.
- **D.** Removes one or more security groups from an Amazon EC2 instance.


**Q20.** In your VPC you have several EC2 instances that have been running for some time. You have logged into an instance and need to determine a few pieces of information including what IAM role is assigned, the instance ID and the names of the security groups that are assigned to the instance. From the options below, what would be a source of this information?

- **A.** Parameters
- **B.** Tags
- **C.** Metadata
- **D.** User data


**Q21.** Which of the following describes how Amazon Elastic MapReduce (Amazon EMR) protects access to the cluster?

- **A.** The master node is launched into a security group that allows Secure Shell (SSH) and service access, while the slave nodes are launched into a separate security group that only permits communication with the master node.
- **B.** The master node and the slave nodes are launched into an Amazon Virtual Private Cloud (Amazon VPC).
- **C.** The master node supports a Virtual Private Network (VPN) connection from the key specified at cluster launch.
- **D.** The master node and slave nodes are launched into a security group that allows SSH and service access.


**Q22.** Your team has a tomcat-based Java application you need to deploy into development, test and production environments. After some research, you opt to use Elastic Beanstalk due to its tight integration with your developer tools and RDS due to its ease of management. Your QA team lead points out that you need to roll a sanitized set of production data into your environment on a nightly basis. Similarly, other software teams in your org want access to that same restored data via their EC2 instances in your VPC. Which of the following optimal setup for persistence and security meets the above requirements?

- **A.** Create your RDS instance as part of your Elastic Beanstalk definition and alter its security group to allow access to it from hosts in your application subnets.
- **B.** Create your RDS instance separately and add its IP address to your application's DB connection strings in your code Alter its security group to allow access to it from hosts within your VPC's IP address block.
- **C.** Create your RDS instance separately and pass its DNS name to your's DB connection string as an environment variable Alter its security group to allow access to It from hosts In your application subnets.
- **D.** Create your RDS instance separately and pass its DNS name to your app's DB connection string as an environment variable. Create a security group for client machines and add it as a valid source for DB traffic to the security group of the RDS instance itself.


**Q23.** You manually launch a NAT AMI in a public subnet. The network is properly configured. Security groups and network access control lists are property configured. Instances in a private subnet can access the NAT. The NAT can access the Internet. However, private instances cannot access the Internet. What additional step is required to allow access from the private instances?

- **A.** Enable Source/Destination Check on the private Instances.
- **B.** Disable Source/Destination Check on the private instances.
- **C.** Disable Source/Destination Check on the NAT instance.
- **D.** Enable Source/Destination Check on the NAT instance.


**Q24.** After an Amazon VPC instance is launched, can I change the VPC security groups it belongs to?

- **A.** Only if the tag "VPC_Change_Group" is true
- **B.** No. You cannot.
- **C.** Only if you are the root user
- **D.** Yes. You can.


**Q25.** You have an environment that consists of a public subnet using Amazon VPC and 3 instances that are running in this subnet. These three instances can successfully communicate with other hosts on the Internet. You launch a fourth instance in the same subnet, using the same AMI and security group configuration you used for the others, but find that this instance cannot be accessed from the internet. What should you do to enable Internet access?

- **A.** Assign an Elastic IP address to the fourth instance.
- **B.** Configure a publically routable IP Address in the host OS of the fourth instance.
- **C.** Deploy a NAT instance into the public subnet.
- **D.** Modify the routing table for the public subnet.


**Q26.** A Database security group controls network access to a database instance that is inside a Virtual Private Cloud (VPC) and by default allows access from?

- **A.** Access for the database connection string is provided by default in the DB security group.
- **B.** No access is provided by default, and any access must be explicitly added with a rule to the DB security group.
- **C.** Access from any IP address for any port is provided by default in the DB security group.
- **D.** Access from any IP address for the standard ports that the database uses is provided by default.


**Q27.** Who is responsible for the configuration of security groups in an AWS environment?

- **A.** Neither AWS nor the customer is responsible for the configuration of security groups; security groups are intelligently and automatically configured using traffic heuristics.
- **B.** The customer and AWS are both jointly responsible for ensuring that security groups are correctly and securely configured.
- **C.** AWS is responsible for ensuring that all security groups are correctly and securely configured. Customers do not need to worry about security group configuration.
- **D.** AWS provides the security group functionality as a service, but the customer is responsible for correctly and securely configuring their own security groups.


**Q28.** Which Amazon VPC feature allows you to create a dual-homed instance?

- **A.** EIP address
- **B.** Security groups
- **C.** CGW
- **D.** ENI


**Q29.** Your instance is associated with two security groups. The first allows Remote Desktop Protocol (RDP) access over port 3389 from Classless Inter-Domain Routing (CIDR) block 72.14.0.0/16. The second allows HTTP access over port 80 from CIDR block 0.0.0.0/0. What traffic can reach your instance?

- **A.** No traffic is allowed.
- **B.** RDP and HTTP access from CIDR block 0.0.0.0/0
- **C.** RDP traffic over port 3389 from 72.14.0.0/16 and HTTP traffic over port 80 from 0.0.00/0
- **D.** RDP and HTTP traffic from 72.14.0.0/16


**Q30.** A customer is running a multi-tier web application farm in a virtual private cloud (VPC) that is not connected to their corporate network. They are connecting to the VPC over the Internet to manage all of their Amazon EC2 instances running in both the public and private subnets. They have only authorized the bastion-security-group with Microsoft Remote Desktop Protocol (RDP) access to the application instance security groups, but the company wants to further limit administrative access to all of the instances in the VPC. Which of the following Bastion deployment scenarios will meet this requirement?

- **A.** Deploy a Windows Bastion host with an Elastic IP address in the private subnet, and restrict RDP access to the bastion from only the corporate public IP addresses.
- **B.** Deploy a Windows Bastion host on the corporate network that has RDP access to all instances in the VPC.
- **C.** Deploy a Windows Bastion host with an Elastic IP address in the public subnet and allow SSH access to the bastion from anywhere.
- **D.** Deploy a Windows Bastion host with an auto-assigned Public IP address in the public subnet, and allow RDP access to the bastion from only the corporate public IP addresses.


**Q31.** You have an EC2 Security Group with several running EC2 instances. You change the Security Group rules to allow inbound traffic on a new port and protocol, and launch several new instances in the same Security Group. The new rules apply _________________.

- **A.** Immediately to the new instances, but old instances must be stopped and restarted before the new rules apply.
- **B.** Immediately to all instances in the security group.
- **C.** To all instances, but it may take several minutes for old instances to see the changes.
- **D.** Immediately to the new instances only.


**Q32.** What does the following command do with respect to the Amazon EC2 security groups? ec2-revoke RevokeSecurityGroupIngress

- **A.** Removes one or more rules from a security group.
- **B.** Removes one or more security groups from an Amazon EC2 instance.
- **C.** Removes a security group from our account.
- **D.** Removes one or more security groups from a rule.


## IAM Roles, Policies & Permissions


**Q33.** What route is used in a VPC routing table for packet forwarding to a Gateway?

- **A.** static route
- **B.** 0.0.0.0/16
- **C.** 10.0.0.0/16
- **D.** 0.0.0.0/0
- **E.** tenant configured


**Q34.** What statement is true of Network Access Control Lists (ACL) operation within an Amazon VPC?

- **A.** outbound only
- **B.** Inbound only
- **C.** Subnet level packet filtering
- **D.** Instance and subnet level packet filtering
- **E.** Only one ACLallowed per VPC


## DynamoDB Design & Capacity


**Q35.** As Per the AWS Acceptable Use Policy, penetration testing of EC2 instances ________________.

- **A.** May be performed by AWS, and will be performed by AWS upon customer request.
- **B.** Are expressly prohibited under all circumstances.
- **C.** May be performed by the customer on their own instances, only if performed from EC2 instances
- **D.** May be performed by AWS, and is periodically performed by AWS.
- **E.** May be performed by the customer on their own instances with prior authorization from AWS.


## RDS Multi-AZ, Read Replicas & Aurora


**Q36.** Amazon RDS supports SOAP only through __________.

- **A.** TCP/IP
- **B.** HTTP
- **C.** HTTP or HTTPS
- **D.** HTTPS


## S3 Security, Access & Durability


**Q37.** What is required for remote management access to your Linux-based instance?

- **A.** ACL
- **B.** Telnet
- **C.** SSH
- **D.** RDP


## S3 Storage Classes & Lifecycle


**Q38.** Your company previously configured a heavily used, dynamically routed VPN connection between your on-premises data center and AWS. You recently provisioned a DirectConnect connection and would like to start using the new connection. After configuring DirectConnect settings in the AWS Console, which of the following options win provide the most seamless transition for your users?

- **A.** Update your VPC route tables to point to the DirectConnect connection configure your DirectConnect router with the appropriate settings verify network traffic is leveraging DirectConnect and then delete the VPN connection.
- **B.** Configure your DireclConnect router, update your VPC route tables to point to the DirectConnect connection, configure your VPN connection with a higher BGP pointy. And verify network traffic is leveraging the DirectConnect connection.
- **C.** Configure your DireclConnect router with a higher 8GP priority man your VPN router, verify network traffic is leveraging Directconnect and then delete your existing VPN connection.
- **D.** Delete your existing VPN connection to avoid routing loops configure your DirectConnect router with the appropriate settings and verity network traffic is leveraging DirectConnect.


## VPC Connectivity: Endpoints, Peering, TGW


**Q39.** A Solutions Architect is determining the best method for provisioning Internet connectivity for a data-processing application that will pull large amounts of data from an object storage system via the Internet. The solution must be redundant and have no constraints on bandwidth. Which option satisfies these requirements?

- **A.** Create a VPC endpoint
- **B.** Attach an Internet Gateway
- **C.** Deploy NAT Instances in a public subnet
- **D.** Use a NAT Gateway


**Q40.** What feature requires tenants to disable source/destination check?

- **A.** Internet gateway
- **B.** Elastic IP (EIP)
- **C.** Data replication
- **D.** VPC peering
- **E.** NAT


**Q41.** You are asked to deploy a web application comprised of multiple public web servers with only private addressing assigned. What Amazon AWS solutions enables multiple servers on a private subnet with only a single EIP required and Availability Zone redundancy?

- **A.** Virtual private gateway
- **B.** NAT gateway
- **C.** NAT instance
- **D.** Internet gateway
- **E.** Elastic Network Interface (ENI)


**Q42.** What problem is caused by the fact that VPC peering does not permit transitive routing?

- **A.** Internet gateway is required for each VPC
- **B.** Virtual private gateway is required
- **C.** Increased number of peer links required
- **D.** Routing between connected spokes through hub VPC is complex
- **E.** Additional VPC route tables to manage


**Q43.** How are packets forwarded between public and private subnets within VPC?

- **A.** VPN
- **B.** EIP
- **C.** main route table
- **D.** NAT


**Q44.** You have launched an Amazon Elastic Compute Cloud (EC2) instance into a public subnet with a primary private IP address assigned, an internet gateway is attached to the VPC, and the public route table is configured to send all Internet-based traffic to the Internet gateway. The instance security group is set to allow all outbound traffic but cannot access the internet. Why is the Internet unreachable from this instance?

- **A.** The instance "Source/Destination check" property must be enabled.
- **B.** The internet gateway security group must allow all outbound traffic.
- **C.** The instance does not have a public IP address.
- **D.** The instance security group must allow all inbound traffic.


**Q45.** After launching an instance that you intend to serve as a NAT (Network Address Translation) device in a public subnet you modify your route tables to have the NAT device be the target of internet bound traffic of your private subnet. When you try and make an outbound connection to the internet from an instance in the private subnet, you are not successful. Which of the following steps could resolve the issue?

- **A.** Disabling the Source/Destination Check attribute on the NAT instance
- **B.** Attaching a second Elastic Network Interface (ENI) to the NAT instance, and placing it in the private subnet
- **C.** Attaching a second Elastic Network Interface (ENI) to the instance in the private subnet, and placing it in the public subnet
- **D.** Attaching an Elastic IP address to the instance in the private subnet


**Q46.** You have created a custom Amazon VPC with both private and public subnets. You have created a NAT instance and deployed this instance to a public subnet. You have attached an EIP address and added your NAT to the route table. Unfortunately, instances in your private subnet still cannot access the Internet. What may be the cause of this?

- **A.** Your NAT should be behind an Elastic Load Balancer.
- **B.** Your NAT is in a public subnet, but it needs to be in a private subnet.
- **C.** You should disable source/destination checks on the NAT.
- **D.** Your NAT has been deployed on a Windows instance, but your other instances are Linux. You should redeploy the NAT onto a Linux instance.


**Q47.** You've been brought in as solutions architect to assist an enterprise customer with their migration of an e-commerce platform to Amazon Virtual Private Cloud (VPC) The previous architect has already deployed a 3-tier VPC. The configuration is as follows: VPC vpc-2f8t>C447 IGVV ig-2d8bc445 NACL acl-2080c448 Subnets and Route Tables: Web server’s subnet-258Dc44d Application server’s suDnet-248bc44c Database server’s subnet-9189c6f9 Route Tables: rrb-218DC449rtb-238bc44b Associations: subnet-258bc44d: rtb-2i8bc449 Subnet-248DC44C rtb-238tX44b subnet-9189c6f9 rtb-238Dc 44b You are now ready to begin deploying EC2 instances into the VPC Web servers must have direct access to the internet Application and database servers cannot have direct access to the internet. Which configuration below will allow you the ability to remotely administer your application and database servers, as well as allow these servers to retrieve updates from the Internet?

- **A.** Create a bastion and NAT Instance in subnet-248bc44c and add a route from rtb238bc44b to subnet-258bc44d
- **B.** Create a bastion and MAT Instance In subnet-258bc44d. Add a route from rtb-238bc44b to igw-2d8bc445. And a new NACL that allows access between subnet-258bc44d and subnet-248bc44c.
- **C.** Add a route from rtD-238bc44D to igw-2d8bc445 and add a bastion and NAT instance within suonet-248bc44c
- **D.** Create a bastion and mat instance in suDnet-258Dc44d and add a route from rtD238Dc44D to the mat instance.


**Q48.** You have enabled Amazon RDS database services in VPC1 for an application with public web servers in VPC2. How do you connect the web servers to the RDS database instance so they can communicate considering the VPC's are in different regions?

- **A.** path-based routing
- **B.** VPN gateway
- **C.** publicly accessible database
- **D.** VPC endpoints
- **E.** VPC peering


**Q49.** A company has an AWS account that contains three VPCs (Dev, Test, and Prod) in the same region. Test is peered to both Prod and Dev. All VPCs have non-overlapping CIDR blocks. The company wants to push minor code releases from Dev to Prod to speed up time to market. Which of the following options helps the company accomplish this?

- **A.** Create a new entry to Prod in the Dev route table using the peering connection as the target.
- **B.** Create a new peering connection Between Prod and Dev along with appropriate routes.
- **C.** The VPCs have non-overlapping CIDR blocks in the same account. The route tables contain local routes for all VPCs.
- **D.** Attach a second gateway to Dev. Add a new entry in the Prod route table identifying the gateway as the target.


**Q50.** What is the difference between VPC main route table and custom route table?

- **A.** VPC does not creates a main route table when started
- **B.** Custom route table is created for private subnets
- **C.** Custom route table is created for public subnets
- **D.** Custom route table is the default
- **E.** Main route table is created for public and private subnets


**Q51.** What is the purpose of a local route within a VPC route table?

- **A.** Only installed in the main route table
- **B.** Used to communicate between instances within the same subnet
- **C.** Local route is derived from the default VPC CIDR block 10.0.0.0/16
- **D.** Default route for communicating between private and public subnets
- **E.** Communicate between instances within the same subnet or different subnets


**Q52.** How is routing enabled by default within a VPC for an EC2 instance?

- **A.** Custom route table
- **B.** Main route table
- **C.** Add a default route
- **D.** Must be configured explicitly


**Q53.** You create a new subnet and then add a route to your route table that routes traffic out from that subnet to the Internet using an IGW. What type of subnet have you created?

- **A.** An internal subnet
- **B.** A private subnet
- **C.** An external subnet
- **D.** A public subnet


**Q54.** Which of the following AWS resources would you use in order for an EC2-VPC instance to resolve DNS names outside of AWS?

- **A.** A DHCP option set
- **B.** A VPC peering connection
- **C.** A routing rule
- **D.** An IGW


**Q55.** How many VPC Peering connections are required for four VPCs located within the same AWS region to be able to send traffic to each of the others?

- **A.** 3
- **B.** 5
- **C.** 4
- **D.** 6


## High Availability & Fault Tolerance


**Q56.** You are a solutions architect working for a large travel company that is migrating its existing server estate to AWS. You have recommended that they use a custom Amazon VPC, and they have agreed to proceed. They will need a public subnet for their web servers and a private subnet in which to place their databases. They also require that the web servers and database servers be highly available and that there be a minimum of two web servers and two database servers each. How many subnets should you have to maintain high availability?

- **A.** 4
- **B.** 1
- **C.** 3
- **D.** 2


**Q57.** A web company is looking to implement an external payment service into their highly available application deployed in a VPC Their application EC2 instances are behind a public lacing ELB Auto scaling is used to add additional instances as traffic increases under normal load the application runs 2 instances in the Auto Scaling group but at peak it can scale 3x in size. The application instances need to communicate with the payment service over the Internet which requires whitelisting of all public IP addresses used to communicate with it. A maximum of 4 whitelisting IP addresses are allowed at a time and can be added through an API. How should they architect their solution?

- **A.** Whitelist the VPC Internet Gateway Public IP and route payment requests through the Internet Gateway.
- **B.** Automatically assign public IP addresses to the application instances in the Auto Scaling group and run a script on boot that adds each instances public IP address to the payment validation whitelist API.
- **C.** Route payment requests through two NAT instances setup for High Availability and whitelist the Elastic IP addresses attached to the MAT instances.
- **D.** Whitelist the ELB IP addresses and route payment requests from the Application servers through the ELB.


**Q58.** What is a requirement for attaching EC2 instances to on-premises clients and applications?

- **A.** Amazon Internet Gateway
- **B.** Elastic Load Balancer (ELB)
- **C.** Amazon Virtual Private Gateway (VPN)
- **D.** NAT
- **E.** VPN Connection


**Q59.** What happens when you create a new Amazon VPC?

- **A.** Three subnets are created by default in one Availability Zone.
- **B.** A main route table is created by default.
- **C.** Three subnets are created by default—one for each Availability Zone.
- **D.** An IGW is created by default.


## CloudFront & Edge Delivery


**Q60.** You run an ad-supported photo sharing website using S3 to serve photos to visitors of your site. At some point you find out that other sites have been linking to the photos on your site, causing loss to your business. What is an effective method to mitigate this?

- **A.** Store photos on an EBS volume of the web server.
- **B.** Remove public read access and use signed URLs with expiry dates.
- **C.** Use CloudFront distributions for static content.
- **D.** Block the IPs of the offending websites in Security Groups.


## EC2 Instances, AMIs & Placement


**Q61.** In order to optimize performance for a compute cluster that requires low inter-node latency, which of the following feature should you use?

- **A.** VPC private subnets
- **B.** AWS Direct Connect
- **C.** Placement Groups
- **D.** Multiple Availability Zones
- **E.** EC2 Dedicated Instances


## Route 53 & DNS Routing


**Q62.** How are private DNS servers assigned to an Amazon VPC?

- **A.** Select default VPC
- **B.** Not supported
- **C.** Select nondefault VPC
- **D.** Select EC-2 classic


## Hybrid Connectivity: Direct Connect & VPN


**Q63.** You were recently promoted to a technical lead role in your DevOps team. Your company has an existing VPC which is quite unutilized for the past few months. The business manager instructed you to integrate your on-premises data center and your VPC. You explained the list of tasks that you'll be doing and mentioned about a Virtual Private Network (VPN) connection. The business manager is not tech-savvy but he is interested to know what a VPN is and its benefits. What is one of the major advantages of having a VPN in AWS?

- **A.** It allows you to connect your AWS cloud resources to your on-premises data center using secure and private sessions with IP Security (IPSec) or Transport Layer Security (TLS) tunnels.
- **B.** It provides a cost-effective, hybrid connection from your VPC to your on-premises data centers which bypasses the public Internet.
- **C.** It enables you to establish a private and dedicated network connection between your network and your VPC
- **D.** It provides a networking connection between two VPCs which enables you to route traffic between them using private IPv4 addresses or IPv6 addresses.


**Q64.** You are putting together an architecture for a new VPC on AWS. Your on-premise data center will be connected to the VPC by a hardware VPN and has public and VPN-only subnets. The security team has requested that all traffic that hits the public subnets on AWS must be directed over the VPN to the corporate firewall. How can this be achieved?

- **A.** In the VPN-only subnet route table, add a route that directs all Internet traffic to the virtual private gateway
- **B.** In the public subnet route table, add a route for your remote network and specify the virtual private gateway as the target
- **C.** Configure a NAT Gateway and configure all traffic to be directed via the virtual private gateway
- **D.** In the public subnet route table, add a route for your remote network and specify the customer gateway as the target


**Q65.** You are designing the network infrastructure for an application server in Amazon VPC Users will access all the application instances from the Internet as well as from an onpremises network The on-premises network is connected to your VPC over an AWS Direct Connect link. How would you design routing to meet the above requirements?

- **A.** Configure a single routing table with two default routes: one to the internet via an Internet gateway the other to the on-premises network via the VPN gateway use this routing table across all subnets in your VPC.
- **B.** Configure a single routing Table with a default route via the Internet gateway Propagate a default route via BGP on the AWS Direct Connect customer router Associate the routing table with all VPC subnets.
- **C.** Configure a single routing table with a default route via the internet gateway Propagate specific routes for the on-premises networks via BGP on the AWS Direct Connect customer router Associate the routing table with all VPC subnets.
- **D.** Configure two routing tables one that has a default route via the Internet gateway and another that has a default route via the VPN gateway Associate both routing tables with each VPC subnet.


**Q66.** Which of the following Amazon VPC resources would you use in order for EC2-VPC instances to send traffic directly to Amazon S3?

- **A.** CGW
- **B.** VPC endpoint
- **C.** Amazon S3 gateway
- **D.** IGW


**Q67.** What is the maximum access port speed available with Amazon Direct Connect service?

- **A.** 500 Mbps
- **B.** 100 Mbps
- **C.** 100 Gbps
- **D.** 1 Gbps
- **E.** 10 Gbps


**Q68.** Is there any way to own a direct connection to Amazon Web Services?

- **A.** Yes, it's called Direct Connect.
- **B.** Yes, it's called Amazon Dedicated Connection.
- **C.** No, AWS only allows access from the public Internet.
- **D.** You can create an encrypted tunnel to VPC, but you don't own the connection.


**Q69.** Which of the following is the Amazon side of an Amazon VPN connection?

- **A.** A CGW
- **B.** An EIP
- **C.** An IGW
- **D.** A VPG


## Monitoring: CloudWatch, CloudTrail & Config


**Q70.** What Amazon AWS service provides account transaction monitoring and security audit?

- **A.** CloudWatch
- **B.** CloudTrail
- **C.** CloudFront
- **D.** Security group


**Q71.** What statement correctly describes CloudWatch operation within AWS cloud?

- **A.** Log data is stored for 15 days
- **B.** ELB is not supported
- **C.** Log data is stored indefinitely
- **D.** Alarm history is never deleted


**Q72.** You are asked to select an AWS solution that will create a log entry anytime a snapshot of an RDS database instance and deletes the original instance. Select the AWS service that would provide that feature?

- **A.** CloudWatch
- **B.** VPC Flow Logs
- **C.** RDS Access Logs
- **D.** CloudTrail


**Q73.** What AWS service automatically publishes access logs every five minutes?

- **A.** CloudTrail
- **B.** Elastic Load Balancer
- **C.** VPC Flow Logs
- **D.** DNS Route 53


**Q74.** What is the purpose of VPC Flow Logs?

- **A.** Monitor network performance
- **B.** Monitor netflow data from subnets
- **C.** Capture VPC error messages
- **D.** Capture IP traffic on network interfaces
- **E.** Enable Syslog services for VPC


## AWS Organizations & Multi-Account


**Q75.** What CIDR block range is supported for IPv4 addressing and subnetting within a single VPC?

- **A.** /16 to /24
- **B.** /16 to /32
- **C.** /16 to /20
- **D.** /16 to /28


**Q76.** Which of the following is the name of the feature within Amazon Virtual Private Cloud (Amazon VPC) that allows you to launch Amazon Elastic Compute Cloud (Amazon EC2) instances on hardware dedicated to a single customer?

- **A.** Amazon VPC-based tenancy
- **B.** Default tenancy
- **C.** Dedicated tenancy
- **D.** Host-based tenancy


**Q77.** You create a new VPC in US-East-1 and provision three subnets inside this Amazon VPC. Which of the following statements is true?

- **A.** By default, these subnets will not be able to communicate with each other; you will need to create routes.
- **B.** All subnets will be able to communicate with each other by default.
- **C.** Each subnet will have identical CIDR blocks.
- **D.** All subnets are public by default.


**Q78.** How many IGWs can you attach to an Amazon VPC at any one time?

- **A.** 2
- **B.** 4
- **C.** 3
- **D.** 1


## Cost Management & Optimization Tools


**Q79.** What AWS service provides vulnerability assessment services to tenants within the cloud?

- **A.** Amazon Trusted Advisor
- **B.** Amazon Inspector
- **C.** Amazon Cloud Logic
- **D.** Amazon WAF


## Secrets, Parameters & Credentials


**Q80.** An application is hosted in AWS Fargate and uses RDS database in Multi-AZ Deployments configuration with several Read Replicas. A Solutions Architect was instructed to ensure that all of their database credentials, API keys, and other secrets are encrypted and rotated on a regular basis to improve data security. The application should also use the latest version of the encrypted credentials when connecting to the RDS database. Which of the following is the MOST appropriate solution to secure the credentials?

- **A.** Store the database credentials, API keys, and other secrets to Systems Manager Parameter Store each with a SecureString data type. The credentials are automatically rotated by default.
- **B.** Store the database credentials, API keys, and other secrets to AWS ACM.
- **C.** Use AWS Secrets Manager to store and encrypt the database credentials, API keys, and other secrets. Enable automatic rotation for all of the credentials.
- **D.** Store the database credentials, API keys, and other secrets in AWS KMS.


## General Design


**Q81.** Which of the following is a storage device that moves data in sequences of bytes or bits (blocks)? Hint: These devices support random access and generally use buffered I/O.

- **A.** Mapping device
- **B.** Block device
- **C.** Block map
- **D.** Storage block


**Q82.** A group can contain many users. Can a user belong to multiple groups?

- **A.** Yes but only if they are using two factor authentication
- **B.** Yes always
- **C.** No
- **D.** Yes but only in VPC


## Elastic Beanstalk & Deployment


**Q83.** You are a Solutions Architect at Digital Cloud Training. A client from a large multinational corporation is working on a deployment of a significant amount of resources into AWS. The client would like to be able to deploy resources across multiple AWS accounts and regions using a single toolset and template. You have been asked to suggest a toolset that can provide this functionality?

- **A.** This cannot be done, use separate CloudFormation templates per AWS account and region
- **B.** Use a CloudFormation template that creates a stack and specify the logical IDs of each account and region
- **C.** Use a CloudFormation StackSet and specify the target accounts and regions in which the stacks will be created
- **D.** Use a third-party product such as Terraform that has support for multiple AWS accounts and regions


# Section B - Multiple Response (select all that apply)


## VPC Security Groups & NACLs


**Q84.** You have just created a new security group in your VPC. You have not yet created any rules. Which of the statements below are correct regarding the default state of the security group? **(Select 2.)**

- **A.** There are is an inbound rule that allows traffic from the Internet Gateway
- **B.** There are no inbound rules and traffic will be implicitly denied
- **C.** There is an outbound rule that allows all traffic to all IP addresses
- **D.** There is an outbound rule allowing traffic to the Internet Gateway


**Q85.** You have just created a new Network ACL in your VPC. You have not yet created any rules. Which of the statements below are correct regarding the default state of the Network ACL? **(Select 2.)**

- **A.** There is a default inbound rule denying all traffic
- **B.** There is a default inbound rule allowing traffic from the VPC CIDR block
- **C.** There is a default outbound rule allowing traffic to the Internet Gateway
- **D.** There is a default outbound rule denying all traffic


**Q86.** A company is deploying a new two-tier web application that uses EC2 web servers and a DynamoDB database backend. An Internet facing ELB distributes connections between the web servers.The Solutions Architect has created a security group for the web servers and needs to create a security group for the ELB. What rules should be added? **(Select 2.)**

- **A.** Add an Outbound rule that allows HTTP/HTTPS, and specify the destination as the web server security group
- **B.** Add an Outbound rule that allows ALL TCP, and specify the destination as the Internet Gateway
- **C.** Add an Inbound rule that allows HTTP/HTTPS, and specify the source as 0.0.0.0/0
- **D.** Add an Outbound rule that allows HTTP/HTTPS, and specify the destination as VPC CIDR


**Q87.** Your company has recently formed a partnership with another company. Both companies have resources running in the AWS cloud and you would like to be able to access each other’s resources using private IP addresses. The resources for each company are in different AWS regions and you need to ensure that fully redundant connectivity is established.You have established a VPC peering connection between the VPCs, what steps need to be taken next to establish connectivity and resource sharing between the VPCs across regions? **(Select 2.)**

- **A.** Update Security Group rules to allow resource sharing
- **B.** Establish an IPSec VPN between the VPCs
- **C.** Manually add routes to each VPCs routing tables as required to enable IP connectivity
- **D.** Establish redundant Direct Connect connections between the VPCs


**Q88.** You have two On-Demand EC2 instances inside your Virtual Private Cloud in the same Availability Zone but are deployed to different subnets. One EC2 instance is running a database and the other EC2 instance a web application that connects with the database. You want to ensure that these two instances can communicate with each other for your system to work properly. What are the things you have to check so that these EC2 instances can communicate inside the VPC? (Select TWO.) **(Select 2.)**

- **A.** Check if the default route is set to a NAT instance or Internet Gateway (IGW) for them to communicate.
- **B.** Check if both instances are the same instance class.
- **C.** Check if all security groups are set to allow the application host to communicate to the database on the right port and protocol.
- **D.** Ensure that the EC2 instances are in the same Placement Group.
- **E.** Check the Network ACL if it allows communication between the two subnets.


**Q89.** You have a load balancer configured for VPC, and all back-end Amazon EC2 instances are in service. However, your web browser times out when connecting to the load balancer's DNS name. Which options are probable causes of this behavior? **(Select 2.)**

- **A.** The Amazon EC2 instances do not have a dynamically allocated private IP address
- **B.** The VPC does not have a VGW configured.
- **C.** The load balancer is not configured in a private subnet with a NAT instance.
- **D.** The security groups or network ACLs are not property configured for web traffic.
- **E.** The load balancer was not configured to use a public subnet with an Internet gateway configured


**Q90.** You have an Elastic Load Balancer assigned to a VPC with public and private subnets. ELB is configured to load balance traffic to a group of EC2 instances assigned to an Auto-Scaling group. What three statements are correct? **(Select 3.)**

- **A.** Elastic Load Balancer is assigned to a public subnet
- **B.** Network ACLis assigned to Elastic Load Balancer
- **C.** Elastic Load Balancer forwards traffic to primary private IP address (eth0 interface) on each instance
- **D.** Cross-zone load balancing is not supported
- **E.** Security group is assigned to Elastic Load Balancer


**Q91.** You have implemented the AWS Elastic File System (EFS) to store data that will be accessed by a large number of EC2 instances. The data is sensitive and you are working on a design for implementing security measures to protect the data. You need to ensure that network traffic is restricted correctly based on firewall rules and access from hosts is restricted by user or group. How can this be achieved with EFS? **(Select 2.)**

- **A.** Use Network ACLs to control the traffic
- **B.** Use POSIX permissions to control access from hosts by user or group
- **C.** Use EFS Security Groups to control network traffic
- **D.** Use AWS Web Application Firewall (WAF) to protect EFS


**Q92.** What two features create security zones between EC2 instances within a VPC? **(Select 2.)**

- **A.** Security groups
- **B.** Virtual Security Gateway
- **C.** Network ACL
- **D.** WAF


**Q93.** What is the default behavior when adding a new subnet to your VPC? **(Select 2.)**

- **A.** New subnet is assigned from the VPC CIDR block
- **B.** New subnet is associated with the main route table
- **C.** New subnet is assigned to the default subnet
- **D.** New subnet is associated with the custom route table
- **E.** New subnet is associated with any selected route table


**Q94.** What are two characteristics of an Amazon security group? **(Select 2.)**

- **A.** Subnet level packet filtering
- **B.** Instance level packet filtering
- **C.** Permit rules only
- **D.** inbound only
- **E.** Deny rules only


**Q95.** What will cause AWS to terminate an EC2 instance on launch? **(Select 2.)**

- **A.** security group error
- **B.** multiple IP addresses assigned to instance
- **C.** EBS volume limits exceeded
- **D.** unsupported instance type assigned
- **E.** number of EC2 instances on AWS account exceeded


**Q96.** What rule must be added to the security group assigned to a mount target instance that enables EFS access from an EC2 instance? **(Select 2.)**

- **A.** Type = NFS, protocol = TCP, port = 2049, source = remote security group id
- **B.** Type = EC2, protocol = IP, port = 2049, source = remote security group id
- **C.** Type = EC2, protocol = EFS, port = 2049, source = 0.0.0.0/0
- **D.** Type = NFSv4, protocol = UDP, port = 2049, source = remote security group id


## Auto Scaling & Elastic Load Balancing


**Q97.** You have created a new VPC and setup an Auto Scaling Group to maintain a desired count of 2 EC2 instances. The security team has requested that the EC2 instances be located in a private subnet. To distribute load, you have to also setup an Internet-facing Application Load Balancer (ALB). With your security team’s wishes in mind what else needs to be done to get this configuration to work? **(Select 2.)**

- **A.** Associate the public subnets with the ALB
- **B.** Attach an Internet Gateway to the private subnets
- **C.** For each private subnet create a corresponding public subnet in the same AZ
- **D.** Add a NAT gateway to the private subnet


**Q98.** You are designing an intrusion detection prevention (IDS/IPS) solution for a customer web application in a single VPC. You are considering the options for implementing IOS IPS protection for traffic coming from the Internet. Which of the following options would you consider? **(Select 2.)**

- **A.** Configure an instance in each subnet to switch its network interface card to promiscuous mode and analyze network traffic.
- **B.** Implement IDS/IPS agents on each Instance running In VPC
- **C.** Implement Elastic Load Balancing with SSL listeners In front of the web applications
- **D.** Implement a reverse proxy layer in front of web servers and configure IDS/IPS agents on each reverse proxy server.


## IAM Roles, Policies & Permissions


**Q99.** For operational access to your AWS environment you are planning to setup a bastion host implementation. Which of the below are AWS best practices for setting up bastion hosts? **(Select 2.)**

- **A.** Access to the bastion hosts is configured to 0.0.0.0/0 for ingress in security groups
- **B.** Bastion hosts are deployed in the private subnets of the VPC
- **C.** Deploy in 2 AZs and use an Auto Scaling group to ensure that the number of bastion host instances always matches the desired capacity you specify during launch
- **D.** Elastic IP addresses are associated with the bastion instances to make it easier to remember and allow these IP addresses from on-premises firewalls


**Q100.** Select three requirements for configuring a Bastion host? **(Select 3.)**

- **A.** VPN
- **B.** EIP
- **C.** SSH inbound permission
- **D.** CloudWatch logs group
- **E.** Default route
- **F.** Auto-Scaling


## VPC Connectivity: Endpoints, Peering, TGW


**Q101.** You are troubleshooting a connectivity issue where you cannot connect to an EC2 instance in a public subnet in your VPC from the Internet. Which of the configuration items in the list below would you check first? **(Select 2.)**

- **A.** The security group attached to the EC2 instance has an inbound rule allowing the traffic
- **B.** The subnet has “Auto-assign public IPv4 address" set to “Yes"
- **C.** There is a NAT Gateway installed in the subnet
- **D.** The subnet route table has an attached NAT Gateway


**Q102.** What default configuration and components are added by AWS when Default VPC type is selected? **(Select 3.)**

- **A.** Virtual private gateway
- **B.** NAT instance
- **C.** DNS
- **D.** Security group
- **E.** Internet gateway


**Q103.** You have deployed a three-tier web application in a VPC with a CIOR block of 10 0 0 0/28 You initially deploy two web servers, two application servers, two database servers and one NAT instance tor a total of seven EC2 instances The web. Application and database servers are deployed across two availability zones (AZs). You also deploy an ELB in front of the two web servers, and use Route53 for DNS Web (raffle gradually increases in the first few days following the deployment, so you attempt to double the number of instances in each tier of the application to handle the new load unfortunately some of these new instances fail to launch. Which of the following could De the root caused? **(Select 2.)**

- **A.** The ELB has scaled-up. Adding more instances to handle the traffic reducing the number of available private IP addresses for new instance launches.
- **B.** AWS reserves one IP address In each subnet's CIDR block for Route53 so you do not have enough addresses left to launch all of the new EC2 instances.
- **C.** AWS reserves the first tour and the last IP address in each subnet's CIDR block so you do not have enough addresses left to launch all of the new EC2 instances.
- **D.** AWS reserves the first and the last private IP address in each subnet's CIDR block so you do not have enough addresses left to launch all of the new EC2 instances.
- **E.** The Internet Gateway (IGW) of your VPC has scaled-up adding more instances to handle the traffic spike, reducing the number of available private IP addresses for new instance launches.


**Q104.** You are implementing a URL whitelisting system for a company that wants to restrict outbound HTTP'S connections to specific domains from their EC2-hosted applications you deploy a single EC2 instance running proxy software and configure It to accept traffic from all subnets and EC2 instances in the VPC. You configure the proxy to only pass through traffic to domains that you define in its whitelist configuration You have a nightly maintenance window or 10 minutes where ail instances fetch new software updates. Each update Is about 200MB In size and there are 500 instances In the VPC that routinely fetch updates After a few days you notice that some machines are failing to successfully download some, but not all of their updates within the maintenance window. The download URLs used for these updates are correctly listed in the proxy's whitelist configuration and you are able to access them manually using a web browser on the instances. What might be happening? **(Select 2.)**

- **A.** The route table for the subnets containing the affected EC2 instances is not configured to direct network traffic for the software update locations to the proxy.
- **B.** You have not allocated enough storage to the EC2 instance running me proxy so the network buffer is filling up. causing some requests to fall
- **C.** You are running the proxy on an undersized EC2 instance type so network throughput is not sufficient for all instances to download their updates in time.
- **D.** You are running the proxy on a affilelentiy-sized EC2 instance in a private subnet and its network throughput is being throttled by a NAT running on an undersized EO£ instance
- **E.** You are running the proxy in a public subnet but have not allocated enough EIPs lo support the needed network throughput through the Internet Gateway (IGW)


**Q105.** Your company has offices in several locations around the world. Each office utilizes resources deployed in the geographically closest AWS region. You would like to implement connectivity between all of the VPCs so that you can provide full access to each other’s resources. As you are security conscious you would like to ensure the traffic is encrypted and does not traverse the public Internet. The topology should be many-to-many to enable all VPCs to access the resources in all other VPCs. How can you successfully implement this connectivity using only AWS services? **(Select 2.)**

- **A.** Implement a hub and spoke architecture
- **B.** Use inter-region VPC peering
- **C.** Use software VPN appliances running on EC2 instances
- **D.** Implement a fully meshed architecture


## CloudFront & Edge Delivery


**Q106.** What features are required to prevent users from bypassing AWS CloudFront security? **(Select 3.)**

- **A.** Signed cookies
- **B.** Origin access identity (OAI)
- **C.** Bastion host
- **D.** Signed URL
- **E.** IP whitelist


## Encryption & AWS KMS


**Q107.** You are working for an investment bank as their IT Consultant. You are working with their IT team to handle the launch of their digital wallet system. The applications will run on multiple EBS-backed EC2 instances which will store the logs, transactions, and billing statements of the user in an S3 bucket. Due to tight security and compliance requirements, you are exploring options on how to safely store sensitive data on the EBS volumes and S3. Which of the below options should be carried out when storing sensitive data on AWS? (Select TWO.) **(Select 2.)**

- **A.** Enable EBS Encryption
- **B.** Use AWS Shield and WAF
- **C.** Migrate the EC2 instances from the public to private subnet.
- **D.** Enable Amazon S3 Server-Side or use Client-Side Encryption
- **E.** Create an EBS Snapshot


## High Availability & Fault Tolerance


**Q108.** Which of the following are characteristics of Amazon VPC subnets? **(Select 2.)**

- **A.** Each subnet maps to a single Availability Zone.
- **B.** Instances in a private subnet can communicate with the Internet only if they have an Elastic IP.
- **C.** Each subnet spans at least 2 Availability Zones to provide a high-availability environment.
- **D.** By default, all subnets can route between each other, whether they are private or public.
- **E.** CIDR block mask of/25 is the smallest range supported.


## Lambda & Serverless Compute


**Q109.** What three features are not supported with VPC peering? **(Select 3.)**

- **A.** IPv6 addressing
- **B.** Gateways
- **C.** Overlapping CIDR blocks
- **D.** ElastiCache
- **E.** RedShift
- **F.** Transitive routing


## Route 53 & DNS Routing


**Q110.** What services are primarily provided by DNS Route 53? **(Select 3.)**

- **A.** automated health checks to EC2 instances
- **B.** Load balancing data replication requests between ECS containers
- **C.** Load balancing web servers within a public subnet
- **D.** Resolve hostnames and IP addresses
- **E.** Resolve queries and route internet traffic to AWS resources
- **F.** Load balancing web servers within a private subnet


## Monitoring: CloudWatch, CloudTrail & Config


**Q111.** What two statements correctly describe AWS monitoring and audit operations? **(Select 2.)**

- **A.** CloudWatch alarm can send a message to a Lambda function
- **B.** VPC logs do not support events for security groups
- **C.** CloudWatch alarm can send a message to an SNS Topic that triggers an event for a Lambda Function
- **D.** CloudTrail captures all AWS events and stores them in a log file function
- **E.** CloudTrail captures API calls, stores them in an S3 bucket and generates a Cloudwatch event


**Q112.** What three services can invoke a Lambda function? **(Select 3.)**

- **A.** EC2 instance
- **B.** SNS topic
- **C.** security group
- **D.** CloudWatch event
- **E.** S3 bucket notification


**Q113.** Amazon CloudWatch supports which types of monitoring plans? **(Select 2.)**

- **A.** Basic monitoring, which is free
- **B.** Ad hoc monitoring, which is free
- **C.** Ad hoc monitoring, which has an additional cost
- **D.** Detailed monitoring, which is free
- **E.** Detailed monitoring, which has an additional cost
- **F.** Basic monitoring, which has an additional cost


## Hybrid Connectivity: Direct Connect & VPN


**Q114.** A company has configured and peered two VPCs: VPC-1 and VPC-2. VPC-1 contains only private subnets, and VPC-2 contains only public subnets. The company uses a single AWS Direct Connect connection and private virtual interface to connect their on-premises network with VPC-1. Which two methods increases the fault tolerance of the connection to VPC-1? **(Select 2.)**

- **A.** Establish a new AWS Direct Connect connection and private virtual interface in the same AWS region as VPC-1
- **B.** Establish a new AWS Direct Connect connection and private virtual interface in a different AWS region than VPC-1.
- **C.** Establish a hardware VPN over the internet between VPC-1 and the on-premises network.
- **D.** Establish a hardware VPN over the internet between VPC-2 ana the on-premises network.
- **E.** Establish a new AWS Direct Connect connection and private virtual interface in the same region as VPC-2.


**Q115.** What two statements correctly describe Amazon virtual private gateway? **(Select 2.)**

- **A.** Assign to public subnets only
- **B.** Multiple virtual private gateways per VPC
- **C.** Single virtual private gateway per VPC
- **D.** Assign to private subnets only
- **E.** Single virtual private gateway per region


## Federation, SSO & Cognito


**Q116.** What security authentication is required before configuring or modifying EC2 instances? **(Select 3.)**

- **A.** EC2 instance authentication with asymmetric keys
- **B.** Authentication at the operating system level
- **C.** Authentication at the application level
- **D.** SSH/RDP session connection
- **E.** Telnet username and password


## Threat Detection & Compliance


**Q117.** Which of the following is a valid report, certification, or third-party attestation for AWS? **(Select 3.)**

- **A.** SOC 1
- **B.** ISO 27001
- **C.** PCI DSS Level 1
- **D.** SOC 4


## Elastic Beanstalk & Deployment


**Q118.** What infrastructure services are provided to EC2 instances? **(Select 3.)**

- **A.** Compute
- **B.** Support
- **C.** Transport
- **D.** Storage
- **E.** VPN
- **F.** Security


---


# Answer Key & Explanations


**Q1. A**  
_VPC Security Groups & NACLs_  
With NACLs you can have permit and deny rules. Network ACLs contain a numbered list of rules that are evaluated in order from the lowest number until the explicit deny. Network ACLs have separate inbound and outbound rules and each rule can allow or deny traffic With Security Groups you can only assign permit rules, you cannot assign deny rules A bastion host is typically used for admin purposes, allowing access to a single endpoint in the AWS cloud for administration using SSH/RDP. From the bastion instance you then connect to other EC2 instances in your subnets. This is not used as a method of adding security to production systems and cannot stop traffic from hitting application ports CloudFront does have DDoS prevention features but we don't know that this is a DDoS style of attack and CloudFront can only help where the traffic is using the CloudFront service to access cached content References: https://digitalcloud.training/certification-training/aws-solutions-architect- associate/networking-and-content-delivery/amazon-vpc/

**Q2. C**  
_VPC Security Groups & NACLs_  
Security groups are stateful, whereas network ACLs are stateless

**Q3. A**  
_VPC Security Groups & NACLs_  
Security groups act as a firewall for associated instances, controlling both inbound and outbound traffic at the instance level. You must add rules to a security group that enable you to connect to your Linux instance from your IP address using SSH. To add a rule to a security group for inbound SSH traffic using the console In the navigation pane of the Amazon EC2 console, choose Instances. Select your instance and look at the Description tab; Security groups lists the security groups that are associated with the instance. Choose view rules to display a list of the rules that are in effect for the instance. In the navigation pane, choose Security Groups. Select one of the security groups associated with your instance. In the details pane, on the Inbound tab, choose Edit. In the dialog, choose Add Rule, and then choose SSH from the Type list. In the Source field, specify the public IP address of your computer, in CIDR notation. For example, if your IP address is 203.0.113.25, specify 203.0.113.25/32 to list this single IP address in CIDR notation. If your company allocates addresses from a range, specify the entire range, such as 203.0.113.0/24. For information about finding your IP address, see Before You Start. Choose Save.

**Q4. B**  
_VPC Security Groups & NACLs_  
A bastion host is a special purpose computer on a network specifically designed and configured to withstand attacks. The computer generally hosts a single application, for example a proxy server, and all other services are removed or limited to reduce the threat to the computer. When setting up a bastion host in AWS, you should only allow the individual IP of the client and not the entire network. Therefore, in the Source, the proper CIDR notation should be used. The /32 denotes one IP address and the /0 refers to the entire network.

**Q5. C**  
_VPC Security Groups & NACLs_  
Network ACLs are stateless, which means that responses to allowed inbound traffic are subject to the rules for outbound traffic (and vice versa). You can create a custom network ACL for your VPC. By default, a network ACL that you create blocks all inbound and outbound traffic until you add rules, and is not associated with a subnet until you explicitly associate it with one. Refer: https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network- acls.html

**Q6. B**  
_VPC Security Groups & NACLs_  
A network ACL is an optional layer of security for your Amazon VPC that acts as a firewall for controlling traffic in and out of one or more subnets. You might set up network ACLs with rules similar to your security groups in order to add an additional layer of security to your Amazon VPC.

**Q7. B**  
_VPC Security Groups & NACLs_  
When connecting to your EC2 instance via SSH, you need to ensure that port 22 is allowed on the security group of your EC2 instance. A security group acts as a virtual firewall that controls the traffic for one or more instances. When you launch an instance, you associate one or more security groups with the instance. You add rules to each security group that allow traffic to or from its associated instances. You can modify the rules for a security group at any time; the new rules are automatically applied to all instances that are associated with the security group.
- *Why not A:* This option is incorrect because this is primarily used to manage the lifecycle of your AWS resources and not to allow certain traffic to go through.
- *Why not C:* This option is incorrect because this is not necessary in this scenario as it was specified that you were able to connect to other EC2 instances. In addition, Network ACL is much suitable to control the traffic that goes in and out of your entire VPC and not just on one EC2 instance.
- *Why not D:* This option is incorrect because this is relevant to RDP and not SSH.

**Q8. A**  
_VPC Security Groups & NACLs_  
Security Groups and Network ACLs do need to be configured to enable connectivity. Check the there relevant rules exist to allow port 22 inbound to your EC2 instance Bastion Hosts are used as an admin tools so you can connect to a single, secured EC2 instance and then jump from there to other instances (typically in private subnets but not always) The subnet CIDR block is configured automatically as part of the creation of the VPC/subnet so should not be the issue here You do not need a VPN connection to connect to an instance in a public subnet. References: https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ec2/ https://digitalcloud.training/certification- training/aws-solutions-architect-associate/networking-and-content-delivery/amazon-vpc/

**Q9. D**  
_VPC Security Groups & NACLs_  
The SSH protocol uses TCP port 22 and to specify an individual IP address in a security group rule you use the format X.X.X.X/32. Therefore the rule should allow TCP port 22 from 100.156.52.12/32 Security groups act like a firewall at the instance level. Specifically, security groups operate at the network interface level and you can only assign permit rules in a security group, you cannot assign a deny rule References: https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-delivery/amazon-vpc/

**Q10. C**  
_VPC Security Groups & NACLs_  
Security group membership can be changed whilst instances are running Any changes to security groups will take effect immediately You can only assign permit rules in a security group, you cannot assign deny rules If you delete the security you will remove all rules and potentially cause other problems You do need to make the update, as it's the VPC based resources you're concerned about. References: https://digitalcloud.training/certification- training/aws-solutions-architect-associate/networking-and-content-delivery/amazon-vpc/

**Q11. A**  
_VPC Security Groups & NACLs_  
The scenario is that you can already connect to the EC2 instance via SSH. This means that there is no problem in the Route Table of your VPC. To fix this issue, you simply need to update your Security Group and add an Inbound rule to allow HTTP traffic.

**Q12. D**  
_VPC Security Groups & NACLs_  
Network ACLs are associated to a VPC subnet to control traffic flow.

**Q13. A**  
_VPC Security Groups & NACLs_  
Network ACL rules can deny traffic.

**Q14. D**  
_VPC Security Groups & NACLs_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q15. C**  
_VPC Security Groups & NACLs_  
A network access control list (ACL) is an optional layer of security for your VPC that acts as a firewall for controlling traffic in and out of one or more subnets. You might set up network ACLs with rules similar to your security groups in order to add an additional layer of security to your VPC. Refer: https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network- acls.html#:~:text=A%20network%20access%20control%20list,of%20security%20to%20your%20VPC.

**Q16. E**  
_VPC Security Groups & NACLs_  
Amazon Virtual Private Cloud (Amazon VPC) lets you provision a logically isolated section of the AWS Cloud where you can launch AWS resources in a virtual network that you define. You have complete control over your virtual networking environment, including selection of your own IP address range, creation of subnets, and configuration of route tables and network gateways. You can use both IPv4 and IPv6 in your VPC for secure and easy access to resources and applications. You can easily customize the network configuration of your Amazon VPC. For example, you can create a public-facing subnet for your web servers that have access to the internet. You can also place your backend systems, such as databases or application servers, in a private-facing subnet with no internet access. You can use multiple layers of security, including security groups and network access control lists, to help control access to Amazon EC2 instances in each subnet. Refer: https://aws.amazon.com/vpc/

**Q17. D**  
_VPC Security Groups & NACLs_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q18. A**  
_VPC Security Groups & NACLs_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q19. C**  
_VPC Security Groups & NACLs_  
The revoke-security-group-ingress command removes one or more ingress rules from a security group. Each rule consists of the protocol and the CIDR range or source security group. For the TCP and UDP protocols, you must also specify the destination port or range of ports. For the ICMP protocol, you must also specify the ICMP type and code. If the security group rule has a description, you do not have to specify the description to revoke the rule. Rule changes are propagated to instances within the security group as quickly as possible. However, a small delay might occur. This example removes TCP port 22 access for the 203.0.113.0/24 address range from the security group named MySecurityGroup. If the command succeeds, no output is returned. Command: aws ec2 revoke-security-group-ingress --group-name MySecurityGroup --protocol tcp --port 22 --cidr 203.0.113.0/24

**Q20. C**  
_VPC Security Groups & NACLs_  
Instance metadata is data about your instance that you can use to configure or manage the running instance and is available at http://169.254.169.254/latest/meta-data Tags are used to categorize and label resources Parameters are used in databases User data is used to configure the system at launch time and specify scripts. References: https://digitalcloud.training/certification-training/aws-solutions-architect- associate/compute/amazon-ec2/ https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html#instancedata-data-categories

**Q21. A**  
_VPC Security Groups & NACLs_  
Amazon EMR starts your instances in two Amazon Elastic Compute Cloud (Amazon EC2) security groups, one for the master and another for the slaves. The master security group has a port open for communication with the service. It also has the SSH port open to allow you to securely connect to the instances via SSH using the key specified at startup. The slaves start in a separate security group, which only allows interaction with the master instance.

**Q22. A**  
_VPC Security Groups & NACLs_  
Create your RDS instance separately and pass its DNS name to your app's DB connection string as an environment variable. Create a security group for client machines and add it as a valid source for DB traffic to the security group of the RDS instance itself. Refer: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.RDS.html

**Q23. C**  
_VPC Security Groups & NACLs_  
Disabling source/destination checks. In the navigation pane, choose Instances. Select the NAT instance, choose Actions, Networking, Change Source/Dest. For the NAT instance, verify that this attribute is disabled. Refer: https://docs.aws.amazon.com/vpc/latest/userguide/VPC_NAT_Instance.html

**Q24. C**  
_VPC Security Groups & NACLs_  
Security groups are associated with network interfaces. After you launch an instance, you can change the security groups associated with the instance, which changes the security groups associated with the primary network interface (eth0).

**Q25. A**  
_VPC Security Groups & NACLs_  
You first allocate an Elastic IP address for use in a VPC, and then associate it with an instance in your VPC (it can be assigned to only one instance at a time). Refer: https://docs.aws.amazon.com/vpc/latest/userguide/vpc-eips.html

**Q26. B**  
_VPC Security Groups & NACLs_  
By default, network access is turned off to a DB Instance. You can specify rules in a security group that allows access from an IP address range, port, or Amazon Elastic Compute Cloud (Amazon EC2) security group.

**Q27. D**  
_VPC Security Groups & NACLs_  
Customers are responsible for ensuring all of their security group configurations are appropriate for their own applications, therefore answer is correct.

**Q28. D**  
_VPC Security Groups & NACLs_  
Attaching an ENI associated with a different subnet to an instance can make the instance dual-homed.

**Q29. C**  
_VPC Security Groups & NACLs_  
When there are multiple security groups associated with an instance, all the rules are aggregated.

**Q30. D**  
_VPC Security Groups & NACLs_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q31. B**  
_VPC Security Groups & NACLs_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q32. A**  
_VPC Security Groups & NACLs_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q33. D**  
_IAM Roles, Policies & Permissions_  
0.0.0.0/0 represents all possible IP addresses. In the context of the way routing tables get set up by default on AWS, 0.0.0.0/0 is effectively "all non local addresses". This is because another route presumably exists in the routing table to route the VPC subnet to the local network on the VPC.

**Q34. C**  
_IAM Roles, Policies & Permissions_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q35. E**  
_DynamoDB Design & Capacity_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q36. D**  
_RDS Multi-AZ, Read Replicas & Aurora_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q37. C**  
_S3 Security, Access & Durability_  
Refer: https://aws.amazon.com/blogs/compute/new-using-amazon-ec2-instance-connect-for-ssh-access-to-your-ec2-instances/

**Q38. B**  
_S3 Storage Classes & Lifecycle_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q39. B**  
_VPC Connectivity: Endpoints, Peering, TGW_  
Both a NAT gateway and an Internet gateway offer redundancy however the NAT gateway is limited to 45 Gbps whereas the IGW does not impose any limits A VPC endpoint is used to access public services from a VPC without traversing the Internet NAT instances are EC2 instances that are used, in a similar way to NAT gateways, by instances in private subnets to access the Internet. However they are not redundant and are limited in bandwidth References: https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/

**Q40. D**  
_VPC Connectivity: Endpoints, Peering, TGW_  
Each EC2 instance performs source/destination checks by default. This means that the instance must be the source or destination of any traffic it sends or receives. However, a NAT instance must be able to send and receive traffic when the source or destination is not itself. Therefore, you must disable source/destination checks on the NAT instance. You can disable the SrcDestCheck attribute for a NAT instance that's either running or stopped using the console or the command line. To disable source/destination checking using the console Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/. In the navigation pane, choose Instances. Select the NAT instance, choose Actions, Networking, Change Source/Dest. Check. For the NAT instance, verify that this attribute is disabled. Otherwise, choose Yes, Disable. If the NAT instance has a secondary network interface, choose it from Network interfaces on the Description tab and choose the interface ID to go to the network interfaces page. Choose Actions, Change Source/Dest. Check, disable the setting, and choose Save. Refer: https://docs.aws.amazon.com/vpc/latest/userguide/VPC_NAT_Instance.html
- *Why not E:* An internet gateway is a horizontally scaled, redundant, and highly available VPC component that allows communication between your VPC and the internet. An internet gateway serves two purposes: to provide a target in your VPC route tables for internet-routable traffic, and to perform network address translation (NAT) for instances that have been assigned public IPv4 addresses. Refer: https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html

**Q41. B**  
_VPC Connectivity: Endpoints, Peering, TGW_  
_See the matching section of this task's `notes.md` for the underlying concept._
- *Why not A:* An elastic network interface is a logical networking component in a VPC that represents a virtual network card. It can include the following attributes: A primary private IPv4 address from the IPv4 address range of your VPC One or more secondary private IPv4 addresses from the IPv4 address range of your VPC One Elastic IP address (IPv4) per private IPv4 address One public IPv4 address One or more IPv6 addresses One or more security groups A MAC address A source/destination check flag A description Refer: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html

**Q42. C**  
_VPC Connectivity: Endpoints, Peering, TGW_  
Refer: https://docs.aws.amazon.com/vpc/latest/peering/invalid-peering-configurations.html

**Q43. D**  
_VPC Connectivity: Endpoints, Peering, TGW_  
The instances in the public subnet can send outbound traffic directly to the Internet, whereas the instances in the private subnet can't. Instead, the instances in the private subnet can access the Internet by using a network address translation (NAT) gateway that resides in the public subnet. The database servers can connect to the Internet for software updates using the NAT gateway, but the Internet cannot establish connections to the database servers. You can also use the VPC wizard to configure a VPC with a NAT instance; however, we recommend that you use a NAT gateway. For more information, see NAT gateways. Refer: https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Scenario2.html

**Q44. C**  
_VPC Connectivity: Endpoints, Peering, TGW_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q45. A**  
_VPC Connectivity: Endpoints, Peering, TGW_  
Refer: https://docs.aws.amazon.com/vpc/latest/userguide/VPC_NAT_Instance.html

**Q46. C**  
_VPC Connectivity: Endpoints, Peering, TGW_  
You should disable source/destination checks on the NAT.

**Q47. A**  
_VPC Connectivity: Endpoints, Peering, TGW_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q48. C**  
_VPC Connectivity: Endpoints, Peering, TGW_  
A VPC peering connection is a networking connection between two VPCs that enables you to route traffic between them using private IPv4 addresses or IPv6 addresses. Instances in either VPC can communicate with each other as if they are within the same network.

**Q49. B**  
_VPC Connectivity: Endpoints, Peering, TGW_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q50. C**  
_VPC Connectivity: Endpoints, Peering, TGW_  
The following are the key concepts for route tables. Main route table—The route table that automatically comes with your VPC. It controls the routing for all subnets that are not explicitly associated with any other route table. Custom route table—A route table that you create for your VPC. Refer: https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html

**Q51. B**  
_VPC Connectivity: Endpoints, Peering, TGW_  
Every route table contains a local route for communication within the VPC. This route is added by default to all route tables. If your VPC has more than one IPv4 CIDR block, your route tables contain a local route for each IPv4 CIDR block. Refer: https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html

**Q52. B**  
_VPC Connectivity: Endpoints, Peering, TGW_  
When you create a VPC, it automatically has a main route table. The main route table controls the routing for all subnets that are not explicitly associated with any other route table. On the Route Tables page in the Amazon VPC console, you can view the main route table for a VPC by looking for Yes in the Main column. Refer: https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html#RouteTableDetails

**Q53. D**  
_VPC Connectivity: Endpoints, Peering, TGW_  
By creating a route out to the Internet using an IGW, you have made this subnet public.

**Q54. A**  
_VPC Connectivity: Endpoints, Peering, TGW_  
A DHCP option set allows customers to define DNS servers for DNS name resolution, establish domain names for instances within an Amazon VPC, define NTP servers, and define the NetBIOS name servers

**Q55. D**  
_VPC Connectivity: Endpoints, Peering, TGW_  
Six VPC Peering connections are needed for each of the four VPCs to send traffic to the other.

**Q56. A**  
_High Availability & Fault Tolerance_  
You need two public subnets (one for each Availability Zone) and two private subnets (one for each Availability Zone). Therefore, you need four subnets.

**Q57. A**  
_High Availability & Fault Tolerance_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q58. A**  
_High Availability & Fault Tolerance_  
An internet gateway is a horizontally scaled, redundant, and highly available VPC component that allows communication between your VPC and the internet. Refer: https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html

**Q59. B**  
_High Availability & Fault Tolerance_  
When you create an Amazon VPC, a route table is created by default. You must manually create subnets and an IGW.

**Q60. B**  
_CloudFront & Edge Delivery_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q61. C**  
_EC2 Instances, AMIs & Placement_  
Cluster – packs instances close together inside an Availability Zone. This strategy enables workloads to achieve the low-latency network performance necessary for tightly-coupled node-to-node communication that is typical of HPC applications. Refer: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html

**Q62. C**  
_Route 53 & DNS Routing_  
Refer: https://aws.amazon.com/about-aws/whats-new/2014/11/05/amazon-route-53-now-supports-private-dns-with-amazon-vpc/

**Q63. A**  
_Hybrid Connectivity: Direct Connect & VPN_  
Amazon VPC offers you the flexibility to fully manage both sides of your Amazon VPC connectivity by creating a VPN connection between your remote network and a software VPN appliance running in your Amazon VPC network. This option is recommended if you must manage both ends of the VPN connection either for compliance purposes or for leveraging gateway devices that are not currently supported by Amazon VPC’s VPN solution. You can create an IPsec VPN connection between your VPC and your remote network. On the AWS side of the VPN connection, a virtual private gateway provides two VPN endpoints (tunnels) for automatic failover. You configure your customer gateway on the remote side of the VPN connection. If you have more than one remote network (for example, multiple branch offices), you can create multiple AWS managed VPN connections via your virtual private gateway to enable communication between these networks. With AWS Site-to-Site VPN, you can connect to an Amazon VPC in the cloud the same way you connect to your branches. AWS Site-to-Site VPN establishes secure and private sessions with IP Security (IPSec) and Transport Layer Security (TLS) tunnels.
- *Why not B:* This option is incorrect because although it is true that a VPN provides a cost-effective, hybrid connection from your VPC to your on- premises data centers, it certainly does not bypass the public Internet. A VPN connection actually goes through the public Internet, unlike the AWS Direct Connect connection which has a direct and dedicated connection to your on-premises network.
- *Why not C:* This option is incorrect because this is the advantage of an AWS Direct Connect connection and not a VPN.
- *Why not D:* This option is incorrect because this actually describes VPC Peering and not a VPN connection.

**Q64. B**  
_Hybrid Connectivity: Direct Connect & VPN_  
Route tables determine where network traffic is directed. In your route table, you must add a route for your remote network and specify the virtual private gateway as the target. This enables traffic from your VPC that's destined for your remote network to route via the virtual private gateway and over one of the VPN tunnels. You can enable route propagation for your route table to automatically propagate your network routes to the table for you You must select the virtual private gateway (AWS side of the VPN) not the customer gateway (customer side of the VPN) in the target in the route table NAT Gateways are used to enable Internet access for EC2 instances in private subnets, they cannot be used to direct traffic to VPG You must create the route table rule in the route table attached to the public subnet, not the VPN-only subnet References: https://docs.aws.amazon.com/vpc/latest/userguide/VPC_VPN.html

**Q65. B**  
_Hybrid Connectivity: Direct Connect & VPN_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q66. B**  
_Hybrid Connectivity: Direct Connect & VPN_  
An Amazon VPC endpoint enables you to create a private connection between your Amazon VPC and another AWS service without requiring access over the Internet or through a NAT device, VPN connection, or AWS Direct Connect.

**Q67. E**  
_Hybrid Connectivity: Direct Connect & VPN_  
AWS Direct Connect makes it easy to scale your connection to meet your needs. AWS Direct Connect provides 1 Gbps and 10 Gbps connections, and you can easily provision multiple connections if you need more capacity. Refer: https://aws.amazon.com/directconnect/#:~:text=AWS%20Direct%20Connect%20makes%20it,if%20you%20need%20more%20capacity.

**Q68. A**  
_Hybrid Connectivity: Direct Connect & VPN_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q69. D**  
_Hybrid Connectivity: Direct Connect & VPN_  
A CGW is the customer side of a VPN connection, and an IGW connects a network to the Internet. A VPG is the Amazon side of a VPN connection.

**Q70. B**  
_Monitoring: CloudWatch, CloudTrail & Config_  
AWS CloudTrail is a service that enables governance, compliance, operational auditing, and risk auditing of your AWS account. With CloudTrail, you can log, continuously monitor, and retain account activity related to actions across your AWS infrastructure. Refer: https://aws.amazon.com/cloudtrail/#:~:text=AWS%20CloudTrail%20is%20a%20service,actions%20across%20your%20AWS%20infrastructure.

**Q71. C**  
_Monitoring: CloudWatch, CloudTrail & Config_  
Amazon CloudWatch is a monitoring and management service that provides data and actionable insights for AWS, hybrid, and on-premises applications and infrastructure resources. With CloudWatch, you can collect and access all your performance and operational data in form of logs and metrics from a single platform. Refer: https://aws.amazon.com/cloudwatch/features/#:~:text=Amazon%20CloudWatch%20is%20a%20monitoring,metrics%20from%20a%20single%20platform.

**Q72. D**  
_Monitoring: CloudWatch, CloudTrail & Config_  
AWS CloudTrail is a service that enables governance, compliance, operational auditing, and risk auditing of your AWS account. ... CloudTrail provides event history of your AWS account activity, including actions taken through the AWS Management Console, AWS SDKs, command line tools, and other AWS services. Refer: https://aws.amazon.com/cloudtrail/

**Q73. B**  
_Monitoring: CloudWatch, CloudTrail & Config_  
Elastic Load Balancing publishes a log file for each load balancer node every 5 minutes. Log delivery is eventually consistent. The load balancer can deliver multiple logs for the same period. Refer: https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access- logs.html#:~:text=Elastic%20Load%20Balancing%20publishes%20a,logs%20for%20the%20same%20period.

**Q74. D**  
_Monitoring: CloudWatch, CloudTrail & Config_  
VPC Flow Logs is a feature that enables you to capture information about the IP traffic going to and from network interfaces in your VPC. Flow log data can be published to Amazon CloudWatch Logs or Amazon S3. After you've created a flow log, you can retrieve and view its data in the chosen destination. Refer: https://docs.aws.amazon.com/vpc/latest/userguide/flow- logs.html#:~:text=VPC%20Flow%20Logs%20is%20a,data%20in%20the%20chosen%20destination.

**Q75. D**  
_AWS Organizations & Multi-Account_  
The CIDR block of a subnet can be the same as the CIDR block for the VPC (for a single subnet in the VPC), or a subset of the CIDR block for the VPC (for multiple subnets). The allowed block size is between a /28 netmask and /16 netmask. If you create more than one subnet in a VPC, the CIDR blocks of the subnets cannot overlap. When you create a VPC, we recommend that you specify a CIDR block (of /16 or smaller) from the private IPv4 address ranges as specified in RFC 1918 : 10.0. 0.0 - 10.255. Refer: https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html#:~:text=When%20you%20create%20a%20VPC%2C%20we%20recommend%20that%20you%20specify,0.0%20%2D%2010.255.

**Q76. C**  
_AWS Organizations & Multi-Account_  
Dedicated instances are physically isolated at the host hardware level from your instances that aren’t dedicated instances and from instances that belong to other AWS accounts.

**Q77. B**  
_AWS Organizations & Multi-Account_  
When you provision an Amazon VPC, all subnets can communicate with each other by default.

**Q78. D**  
_AWS Organizations & Multi-Account_  
You may only have one IGW for each Amazon VPC.

**Q79. A**  
_Cost Management & Optimization Tools_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q80. C**  
_Secrets, Parameters & Credentials_  
AWS Secrets Manager is an AWS service that makes it easier for you to manage secrets. Secrets can be database credentials, passwords, third-party API keys, and even arbitrary text. You can store and control access to these secrets centrally by using the Secrets Manager console, the Secrets Manager command line interface (CLI), or the Secrets Manager API and SDKs. In the past, when you created a custom application that retrieves information from a database, you typically had to embed the credentials (the secret) for accessing the database directly in the application. When it came time to rotate the credentials, you had to do much more than just create new credentials. You had to invest time to update the application to use the new credentials. Then you had to distribute the updated application. If you had multiple applications that shared credentials and you missed updating one of them, the application would break. Because of this risk, many customers have chosen not to regularly rotate their credentials, which effectively substitutes one risk for another. Secrets Manager enables you to replace hardcoded credentials in your code (including passwords), with an API call to Secrets Manager to retrieve the secret programmatically. This helps ensure that the secret can't be compromised by someone examining your code, because the secret simply isn't there. Also, you can configure Secrets Manager to automatically rotate the secret for you according to a schedule that you specify. This enables you to replace long-term secrets with short-term ones, which helps to significantly reduce the risk of compromise.
- *Why not A:* This option is incorrect because Systems Manager Parameter Store doesn't rotate its parameters by default.
- *Why not B:* This option is incorrect because it is just a managed private CA service that helps you easily and securely manage the lifecycle of your private certificates to allow SSL communication to your application. This is not a suitable service to store database or any other confidential credentials.
- *Why not D:* This option is incorrect because this only makes it easy for you to create and manage encryption keys and control the use of encryption across a wide range of AWS services. This is primarily used for encryption and not for hosting your credentials.

**Q81. B**  
_General Design_  
A block device is a storage device that moves data in sequences of bytes or bits (blocks). These devices support random access and generally use buffered I/O. Refer: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html

**Q82. B**  
_General Design_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q83. C**  
_Elastic Beanstalk & Deployment_  
AWS CloudFormation StackSets extends the functionality of stacks by enabling you to create, update, or delete stacks across multiple accounts and regions with a single operation Using an administrator account, you define and manage an AWS CloudFormation template, and use the template as the basis for provisioning stacks into selected target accounts across specified regions. An administrator account is the AWS account in which you create stack sets A stack set is managed by signing in to the AWS administrator account in which it was created. A target account is the account into which you create, update, or delete one or more stacks in your stack set Before you can use a stack set to create stacks in a target account, you must set up a trust relationship between the administrator and target accounts A regular CloudFormation template cannot be used across regions and accounts. You would need to create copies of the template and then manage updates You do not need to use a third-party product such as Terraform as this functionality can be delivered through native AWS technology References: https://digitalcloud.training/certification-training/aws-solutions-architect- associate/management-tools/aws-cloudformation/ https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html

**Q84. B, C**  
_VPC Security Groups & NACLs_  
Custom security groups do not have inbound allow rules (all inbound traffic is denied by default) Default security groups do have inbound allow rules (allowing traffic from within the group) All outbound traffic is allowed by default in both custom and default security groups Security groups act like a stateful firewall at the instance level. Specifically security groups operate at the network interface level of an EC2 instance. You can only assign permit rules in a security group, you cannot assign deny rules and there is an implicit deny rule at the end of the security group. All rules are evaluated until a permit is encountered or continues until the implicit deny. You can create ingress and egress rules References: https://digitalcloud.training/certification- training/aws-solutions-architect-associate/networking-and-content-delivery/amazon-vpc/

**Q85. A, D**  
_VPC Security Groups & NACLs_  
A VPC automatically comes with a default network ACL which allows all inbound/outbound traffic A custom NACL denies all traffic both inbound and outbound by default Network ACL’s function at the subnet level and you can have permit and deny rules. Network ACLs have separate inbound and outbound rules and each rule can allow or deny traffic. Network ACLs are stateless so responses are subject to the rules for the direction of traffic. NACLs only apply to traffic that is ingress or egress to the subnet not to traffic within the subnet References: https://digitalcloud.training/certification- training/aws-solutions-architect-associate/networking-and-content-delivery/amazon-vpc/

**Q86. A, C**  
_VPC Security Groups & NACLs_  
An inbound rule should be created for the relevant protocols (HTTP/HTTPS) and the source should be set to any address (0.0.0.0/0) The address 0.0.0.0/32 is incorrect as the 32 mask means an exact match is required (0.0.0.0) The outbound rule should forward the relevant protocols (HTTP/HTTPS) and the destination should be set to the web server security group Using the VPC CIDR would not be secure and you cannot specify an Internet Gateway in a security group (not that you'd want to anyway) FYI on the web server security group you'd want to add an Inbound rule allowing HTTP/HTTPS from the ELB security group References: https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/elastic- load-balancing/

**Q87. A, C**  
_VPC Security Groups & NACLs_  
Peering connections can be created with VPCs in different regions (available in most regions now). Data sent between VPCs in different regions is encrypted (traffic charges apply). You must update route tables to configure routing. You must also update the inbound and outbound rules for VPC security group to reference security groups in the peered VPC When creating a VPC peering connection with another account you need to enter the account ID and VPC ID from the other account You do not use an IPSec VPN or Direct Connect to establish VPC peering, the connections are internal to AWS using the AWS network infrastructure BGP routing configuration is required for Direct Connect but not for VPC peering. References: https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content- delivery/amazon-vpc/

**Q88. C, E**  
_VPC Security Groups & NACLs_  
First, the Network ACL should be properly set to allow communication between the two subnets. The security group should also be properly configured so that your web server can communicate with the database server
- *Why not A:* This option is incorrect because an Internet gateway is primarily used to communicate to the Internet.
- *Why not B:* This option is incorrect because the EC2 instances do not need to be of the same class in order to communicate with each other.
- *Why not D:* This option is incorrect because Placement Group is mainly used to provide low-latency network performance necessary for tightly-coupled node-to-node communication.

**Q89. D, E**  
_VPC Security Groups & NACLs_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q90. A, C, E**  
_VPC Security Groups & NACLs_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q91. B, C**  
_VPC Security Groups & NACLs_  
You can control who can administer your file system using IAM. You can control access to files and directories with POSIX-compliant user and group-level permissions. POSIX permissions allows you to restrict access from hosts by user and group. EFS Security Groups act as a firewall, and the rules you add define the traffic flow You cannot use AWS WAF to protect EFS data using users and groups You do not use IAM to control access to files and directories by user and group, but you can use IAM to control who can administer the file system configuration You use EFS Security Groups to control network traffic to EFS, not Network ACLs References: https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon- efs/ https://aws.amazon.com/efs/features/

**Q92. A, D**  
_VPC Security Groups & NACLs_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q93. A, B**  
_VPC Security Groups & NACLs_  
You can use a default VPC as you would use any other VPC: Add additional nondefault subnets. Modify the main route table. Add additional route tables. Associate additional security groups. Update the rules of the default security group. Add AWS Site-to-Site VPN connections. Add more IPv4 CIDR blocks. Refer: https://docs.aws.amazon.com/vpc/latest/userguide/default-vpc.html#create-default-subnet

**Q94. B, C**  
_VPC Security Groups & NACLs_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q95. C, E**  
_VPC Security Groups & NACLs_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q96. B, D**  
_VPC Security Groups & NACLs_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q97. A, C**  
_Auto Scaling & Elastic Load Balancing_  
ELB nodes have public IPs and route traffic to the private IP addresses of the EC2 instances. You need one public subnet in each AZ where the ELB is defined and the private subnets are located Attaching an Internet gateway (which is done at the VPC level, not the subnet level) or a NAT gateway will not assist as these are both used for outbound communications which is not the goal here ELBs talk to the private IP addresses of the EC2 instances so adding an Elastic IP address to the instance won't help. Additionally Elastic IP addresses are used in public subnets to allow Internet access via an Internet Gateway References: https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/elastic-load-balancing/ https://aws.amazon.com/premiumsupport/knowledge-center/public-load-balancer-private-ec2/

**Q98. C, D**  
_Auto Scaling & Elastic Load Balancing_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q99. C, D**  
_IAM Roles, Policies & Permissions_  
You can configure EC2 instances as bastion hosts (aka jump boxes) in order to access your VPC instances for management. Bastion hosts are deployed in public (not private) subnets within your VPC. You can use the SSH or RDP protocols to connect to bastion hosts You need to configure a security group with the relevant permissions to allow the SSH or RDP protocols. You can also use security group rules to restrict the IP addresses/CIDRs that can access the bastion host. Bastion hosts can use auto-assigned public IPs or Elastic IPs It is a best practice is to deploy Linux bastion hosts in two AZs, use Auto Scaling (set to 1 to just replace)and Elastic IP addresses Setting the security rule to allow from the 0.0.0.0/0 source would allow any host on the Internet to access your bastion. It's a security best practice to restrict the sources to known (safe) IP addresses or CIDR blocks. You would not want to allow unrestricted access to ports on the bastion host. References: https://digitalcloud.training/certification-training/aws-solutions-architect- associate/compute/amazon-ec2/

**Q100. B, C, E**  
_IAM Roles, Policies & Permissions_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q101. A, B**  
_VPC Connectivity: Endpoints, Peering, TGW_  
Public subnets are subnets that have: “Auto-assign public IPv4 address?? set to “Yes?? which will assign a public IP The subnet route table has an attached Internet Gateway The instance will also need to a security group with an inbound rule allowing the traffic EC2 instances always have a private IP address assigned. When using a public subnet with an Internet Gateway the instance needs a public IP to be addressable from the Internet NAT gateways are used to enable outbound Internet access for instances in private subnets. References: https://digitalcloud.training/certification-training/aws- solutions-architect-associate/compute/aws-auto-scaling/

**Q102. C, D, E**  
_VPC Connectivity: Endpoints, Peering, TGW_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q103. A, C**  
_VPC Connectivity: Endpoints, Peering, TGW_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q104. B, E**  
_VPC Connectivity: Endpoints, Peering, TGW_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q105. B, D**  
_VPC Connectivity: Endpoints, Peering, TGW_  
Peering connections can be created with VPCs in different regions (available in most regions now) Data sent between VPCs in different regions is encrypted (traffic charges apply) You cannot do transitive peering so a hub and spoke architecture would not allow all VPCs to communicate directly with each other. For this you need to establish a mesh topology A VPC endpoint enables you to privately connect your VPC to supported AWS services and VPC endpoint services, it does not provide full VPC to VPC connectivity Using software VPN appliances to connect VPCs together is not the best solution as it is cumbersome, expensive and would introduce bandwidth and latency constraints (amongst other problems). References: https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-delivery/amazon- vpc/

**Q106. B, C, E**  
_CloudFront & Edge Delivery_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q107. A, D**  
_Encryption & AWS KMS_  
Enabling EBS Encryption and enabling Amazon S3 Server-Side or use Client-Side Encryption are correct. Amazon EBS encryption offers a simple encryption solution for your EBS volumes without the need to build, maintain, and secure your own key management infrastructure. In Amazon S3, data protection refers to protecting data while in-transit (as it travels to and from Amazon S3) and at rest (while it is stored on disks in Amazon S3 data centers). You can protect data in transit by using SSL or by using client-side encryption. You have the following options to protect data at rest in Amazon S3. Use Server-Side Encryption – You request Amazon S3 to encrypt your object before saving it on disks in its data centers and decrypt it when you download the objects. Use Client-Side Encryption – You can encrypt data client-side and upload the encrypted data to Amazon S3. In this case, you manage the encryption process, the encryption keys, and related tools.
- *Why not B:* This option is incorrect because these protect you from common security threats for your web applications. However, what you are trying to achieve is securing and encrypting your data inside EBS and S3.
- *Why not C:* This option is incorrect because the data you want to secure are those in EBS volumes and S3 buckets. Moving your EC2 instance to a private subnet involves a different matter of security practice, which does not achieve what you want in this scenario.
- *Why not E:* This option is incorrect because this is a backup solution of EBS. It does not provide security of data inside EBS volumes when executed.

**Q108. A, B**  
_High Availability & Fault Tolerance_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q109. B, C, F**  
_Lambda & Serverless Compute_  
VPC peering does not support transitive peering relationships. In a VPC peering connection, your VPC does not have access to any other VPCs with which the peer VPC may be peered. This includes VPC peering connections that are established entirely within your own AWS account. You can establish peering relationships between VPCs across different AWS Regions (also called InterRegion VPC Peering). This allows VPC resources including EC2 instances, Amazon RDS databases and Lambda functions that run in different AWS Regions to communicate with each other using private IP addresses, without requiring gateways, VPN connections, or separate network appliances. You cannot create a VPC peering connection between VPCs that have matching or overlapping IPv4 or IPv6 CIDR blocks. Amazon always assigns your VPC a unique IPv6 CIDR block. If your IPv6 CIDR blocks are unique but your IPv4 blocks are not, you cannot create the peering connection.
- *Why not A:* A VPC peering connection is a networking connection between two VPCs that enables you to route traffic between them using private IPv4 addresses or IPv6 addresses. Instances in either VPC can communicate with each other as if they are within the same network. Refer: https://docs.aws.amazon.com/vpc/latest/peering/vpc-pg.pdf

**Q110. A, D, E**  
_Route 53 & DNS Routing_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q111. C, E**  
_Monitoring: CloudWatch, CloudTrail & Config_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q112. B, D, E**  
_Monitoring: CloudWatch, CloudTrail & Config_  
List of services that invoke Lambda functions asynchronously: Amazon Simple Storage Service. 1. Amazon Simple Notification Service. 2. Amazon Simple Email Service. 3. AWS CloudFormation. 4. Amazon CloudWatch Logs. 5. Amazon CloudWatch Events. 6. AWS CodeCommit. 7. AWS Config. Refer: https://aws.amazon.com/blogs/architecture/understanding-the-different-ways-to-invoke-lambda-functions/

**Q113. A, E**  
_Monitoring: CloudWatch, CloudTrail & Config_  
Amazon CloudWatch has two plans: basic, which is free, and detailed, which has an additional cost. There is no ad hoc plan for Amazon CloudWatch.

**Q114. C, E**  
_Hybrid Connectivity: Direct Connect & VPN_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q115. C, D**  
_Hybrid Connectivity: Direct Connect & VPN_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q116. A, B, C**  
_Federation, SSO & Cognito_  
You can choose to generate your own Amazon EC2 key pairs using industry- standard tools like OpenSSL. You generate the key pair in a secure and trusted environment, and only the public key of the key pair is imported in AWS; you store the private key securely. We advise using a high- quality random number generator if you take this path. Refer: https://d1.awsstatic.com/whitepapers/Security/AWS_Security_Best_Practices.pdf To enable authentication to the EC2 instance, AWS provides asymmetric key pairs, known as Amazon EC2 key pairs. These are industry- standard RSA key pairs. Each user can have multiple Amazon EC2 key pairs, and can launch new instances using different key pairs. EC2 key pairs are not related to the AWS account or IAM user credentials discussed previously. Those credentials control access to other AWS services; EC2 key pairs control access only to your specific instance. Refer: https://d1.awsstatic.com/whitepapers/Security/AWS_Security_Best_Practices.pdf When you launch a new Amazon EC2 instance from a standard AMI, you can access that instance using secure remote system access protocols, such as Secure Shell (SSH), or Windows Remote Desktop Protocol (RDP). You must successfully authenticate at the operating-system level before you can access and configure the Amazon EC2 instance to your requirements. After you have authenticated and have remote access into the Amazon EC2 instance, you can set up the operating system authentication mechanisms you want, which might include X.509 certificate authentication, Microsoft Active Directory, or local operating system accounts. Refer: https://d1.awsstatic.com/whitepapers/Security/AWS_Security_Best_Practices.pdf

**Q117. A, B, C**  
_Threat Detection & Compliance_  
_See the matching section of this task's `notes.md` for the underlying concept._
- *Why not D:* There is no such thing as a SOC 4 report, therefore answer is incorrect.

**Q118. A, C, D**  
_Elastic Beanstalk & Deployment_  
Infrastructure as a Service, sometimes abbreviated as IaaS, contains the basic building blocks for cloud IT and typically provide access to networking features, computers (virtual or on dedicated hardware), and data storage space. Link - https://aws.amazon.com/types-of-cloud-computing/ When designing your Windows applications to run on Amazon EC2, you can plan for rapid deployment and rapid reduction of compute and storage resources, based on your changing needs. Refer: https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/EC2Win_Infrastructure.html
