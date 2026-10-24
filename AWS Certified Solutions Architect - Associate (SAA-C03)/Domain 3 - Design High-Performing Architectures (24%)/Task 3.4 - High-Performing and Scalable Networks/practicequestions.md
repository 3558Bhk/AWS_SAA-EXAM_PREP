# Task 3.4 - High-Performing and Scalable Networks - Practice Questions

> **Domain 3 - Design High-Performing Architectures (24%)**  
> Curated from 18 practice sets: duplicates removed, outdated items retired, ordered **highest-frequency exam topics first**.  
> **31 multiple-choice (single answer)** followed by **24 multiple-response (select 2+)**. Total **55**.


**Topic order in this file:** RDS Multi-AZ, Read Replicas & Aurora → VPC Security Groups & NACLs → Auto Scaling & Elastic Load Balancing → DynamoDB Design & Capacity → Route 53 & DNS Routing → CloudFront & Edge Delivery → EBS Volumes & Snapshots → EC2 Instances, AMIs & Placement → High Availability & Fault Tolerance → VPC Connectivity: Endpoints, Peering, TGW → AWS Organizations & Multi-Account → Hybrid Connectivity: Direct Connect & VPN → General Design → SQS, SNS & Decoupling → Lambda & Serverless Compute → Monitoring: CloudWatch, CloudTrail & Config


---


# Section A - Multiple Choice (one correct answer)


## RDS Multi-AZ, Read Replicas & Aurora


**Q1.** You are migrating a legacy client-server application to AWS The application responds to a specific DNS domain (e g www example com) and has a 2-tier architecture, with multiple application servers and a database server Remote clients use TCP to connect to the application servers. The application servers need to know the IP address of the clients in order to function properly and are currently taking that information from the TCP socket A Multi-AZ RDS MySQL instance will be used for the database. During the migration you can change the application code but you have to file a change request. How would you implement the architecture on AWS In order to maximize scalability and high ability?

- **A.** File a change request to implement Latency Based Routing support in the application Use Route 53 with Latency Based Routing enabled to distribute load on two application servers in different AZs.
- **B.** File a change request to implement Alias Resource support in the application Use Route 53 Alias Resource Record to distribute load on two application servers in different AZs.
- **C.** File a change request to implement Proxy Protocol support In the application Use an EL8 with a TCP Listener and Proxy Protocol enabled to distribute load on two application servers in different AZs.
- **D.** File a change request to Implement Cross-Zone support in the application Use an EL8 with a TCP Listener and Cross-Zone Load Balancing enabled, two application servers in different AZs.


**Q2.** Which Amazon service can I use to define a virtual network that closely resembles a traditional data center?

- **A.** Amazon RDS
- **B.** Amazon EMR
- **C.** Amazon VPC
- **D.** Amazon ServiceBus


## VPC Security Groups & NACLs


**Q3.** You are a new Solutions Architect in your company. Upon checking the existing Inbound Rules of your Network ACL, you saw this configuration: If a computer with an IP address of 110.238.109.37 sends a request to your VPC, what will happen?

- **A.** It will be allowed.
- **B.** It will be denied.
- **C.** Initially, it will be allowed and then after a while, the connection will be denied.
- **D.** Initially, it will be denied and then after a while, the connection will be allowed.


**Q4.** Using the correctly decrypted Administrator password and RDP, you cannot log in to a Windows instance you just launched. Which of the following is a possible reason?

- **A.** The instance is not using enhanced networking.
- **B.** The instance is a Reserved Instance.
- **C.** There is no security group rule that allows RDP access over port 3389 from your IP address.
- **D.** The instance is not an Amazon EBS-optimized instance.


## Auto Scaling & Elastic Load Balancing


**Q5.** You have enabled Amazon RDS database services in VPC1 for an application that has public webservers in VPC2. How do you connect the web servers to the RDS database instance so they can communicate considering the VPC's are in the same region?

- **A.** AWS Network Load Balancer
- **B.** VPC endpoints
- **C.** VPN gateway
- **D.** VPC peering
- **E.** Path-based routing


## DynamoDB Design & Capacity


**Q6.** What read consistency method provides lower latency for GetItem requests?

- **A.** Strongly persistent
- **B.** Write consistent
- **C.** Strongly consistent
- **D.** Eventually consistent


## Route 53 & DNS Routing


**Q7.** You host a web application across multiple AWS regions in the world, and you need to configure your DNS so that your end users will get the fastest network performance possible. Which routing policy should you apply?

- **A.** Simple routing
- **B.** Geolocation routing
- **C.** Weighted routing
- **D.** Latency-based routing


**Q8.** Does Route 53 support MX Records?

- **A.** It supports CNAME records, but not MX records.
- **B.** Only Primary MX records. Secondary MX records are not supported.
- **C.** No
- **D.** Yes.


**Q9.** A customer is hosting their company website on a cluster of web servers that are behind a public-facing load balancer. The customer also uses Amazon Route 53 to manage their public DNS. How should the customer configure the DNS zone apex record to point to the load balancer?

- **A.** Create an A record pointing to the IP address of the load balancer
- **B.** Create a CNAME record pointing to the load balancer DNS name.
- **C.** Create an A record aliased to the load balancer DNS name
- **D.** Create a CNAME record aliased to the load balancer DNS name.


**Q10.** Which type of DNS record should you use to resolve a domain name to another domain name?

- **A.** A CNAME record
- **B.** An A record
- **C.** An SPF record
- **D.** A PTR record


**Q11.** Which resource record set would not be allowed for the hosted zone example.com ?

- **A.** www.example.com
- **B.** www.example.ca
- **C.** www.aws.example.com
- **D.** www.beta.example.com


**Q12.** Which type of record is commonly used to route traffic to an IPv6 address?

- **A.** A CNAME
- **B.** An A record
- **C.** An MX record
- **D.** An AAAA record


**Q13.** Which type of DNS record should you use to resolve an IP address to a domain name?

- **A.** A C Name
- **B.** An SPF record
- **C.** A PTR record
- **D.** An A record


**Q14.** Which DNS record must all zones have by default?

- **A.** TXT
- **B.** SPF
- **C.** MX
- **D.** SOA


**Q15.** Which DNS record can be used to store human-readable information about a server, network, and other accounting data with a host?

- **A.** A PTR record
- **B.** An SPF record
- **C.** A TXT record
- **D.** An MX record


## CloudFront & Edge Delivery


**Q16.** Your company provides an online photo sharing service. The development team is looking for ways to deliver image files with the lowest latency to end users so the website content is delivered with the best possible performance. What service can help speed up distribution of these image files to end users around the world?

- **A.** AWS Storage Gateway
- **B.** Amazon Elastic Compute Cloud (Amazon EC2)
- **C.** Amazon Route 53
- **D.** Amazon CloudFront


**Q17.** Where are HTMLfiles sourced from when they are not cached at a CloudFront edge location?

- **A.** Nearest edge location
- **B.** origin HTTP server
- **C.** S3 object
- **D.** Failover edge location
- **E.** S3 bucket
- **F.** RTMP server


**Q18.** A travel company has a suite of web applications hosted in an Auto Scaling group of On-Demand EC2 instances behind an Application Load Balancer that handles traffic from various web domains such as i-love-manila.com, i-love-boracay.com, i-love- cebu.com and many others. To improve security and lessen the overall cost, you are instructed to secure the system by allowing multiple domains to serve SSL traffic without the need to reauthenticate and reprovision your certificate everytime you add a new domain. This migration from HTTP to HTTPS will help improve their SEO and Google search ranking. Which of the following is the most cost-effective solution to meet the above requirement?

- **A.** Upload all SSL certificates of the domains in the ALB using the console and bind multiple certificates to the same secure listener on your load balancer. ALB will automatically choose the optimal TLS certificate for each client using Server Name Indication (SNI).
- **B.** Create a new CloudFront web distribution and configure it to serve HTTPS requests using dedicated IP addresses in order to associate your alternate domain names with a dedicated IP address in each CloudFront edge location.
- **C.** Use a wildcard certificate to handle multiple sub-domains and different domains.
- **D.** Add a Subject Alternative Name (SAN) for each additional domain to your certificate.


**Q19.** Your company provides media content via the Internet to customers through a paid subscription model. You leverage Amazon CloudFront to distribute content to your customers with low latency. What approach can you use to serve this private content securely to your paid subscribers?

- **A.** Use the Amazon CloudFront geo restriction feature to restrict access to all of the paid subscription media at the country level.
- **B.** Use HTTPS requests to ensure that your objects are encrypted when Amazon CloudFront serves them to viewers.
- **C.** Configure Amazon CloudFront to compress the media files automatically for paid subscribers.
- **D.** Provide signed Amazon CloudFront URLs to authenticated users to access the paid content.


**Q20.** Where does Amazon retrieve web content when it is not in the nearest CloudFront edge location?

- **A.** File server
- **B.** Secondary location
- **C.** S3 bucket
- **D.** EBS


**Q21.** What feature permits tenants to use a private domain name instead of the domain name that CloudFront assigns to a distribution?

- **A.** Route 53
- **B.** MX record
- **C.** Signed URL
- **D.** CNAME record
- **E.** RTMP


**Q22.** Your company is deploying a web site with dynamic content to customers in US, EU and APAC regions of the world. Content will include live streaming videos to customers. SSLcertificates are required for security purposes. Select the AWS service delivers all requirements and provides the lowest latency?

- **A.** Redis
- **B.** DynamoDB
- **C.** S3
- **D.** CloudFront


**Q23.** What AWS service is used to monitor tenant remote access and various security errors including authentication retries?

- **A.** Telnet
- **B.** CloudFront
- **C.** SSH
- **D.** CloudWatch


## EBS Volumes & Snapshots


**Q24.** You have an application running on an Amazon Elastic Compute Cloud instance, that uploads 5 GB video objects to Amazon Simple Storage Service (S3). Video uploads are taking longer than expected, resulting in poor application performance. Which method will help improve performance of your application?

- **A.** Enable enhanced networking
- **B.** Use Amazon S3 multipart upload
- **C.** Leveraging Amazon CloudFront, use the HTTP POST method to reduce latency.
- **D.** Use Amazon Elastic Block Store Provisioned IOPs and use an Amazon EBS-optimized instance


## EC2 Instances, AMIs & Placement


**Q25.** An EC2 instance you manage is generating very high packets-per-second and performance of the application stack is being impacted. You have been asked for a resolution to the issue that results in improved performance from the EC2 instance. What would you suggest?

- **A.** Create a placement group and put the EC2 instance in it
- **B.** Add multiple Elastic IP addresses to the instance
- **C.** Use enhanced networking
- **D.** Configure a RAID 1 array from multiple EBS volumes


## High Availability & Fault Tolerance


**Q26.** Which of the following features ensures even distribution of traffic to Amazon EC2 instances in multiple Availability Zones registered with a load balancer?

- **A.** An Amazon Route 53 weighted routing policy
- **B.** Elastic Load Balancing request routing
- **C.** Elastic Load Balancing cross-zone load balancing
- **D.** An Amazon Route 53 latency routing policy


## VPC Connectivity: Endpoints, Peering, TGW


**Q27.** You have created an application in a VPC that uses a Network Load Balancer (NLB). The application will be offered in a service provider model for AWS principals in other accounts within the region to consume. Based on this model, what AWS service will be used to offer the service for consumption?

- **A.** VPC Endpoint Services using AWS PrivateLink
- **B.** API Gateway
- **C.** IAM Role Based Access Control
- **D.** Route 53


## AWS Organizations & Multi-Account


**Q28.** What is the IP addressing schema assigned to a default VPC?

- **A.** 10.0.0.0/16 CIDR block subnetted with 10.0.0.0/24
- **B.** 172.16.0.0/16 CIDR block subnetted with 172.16.0.0/24
- **C.** 172.31.0.0/16 CIDR block subnetted with 172.31.0.0/20
- **D.** 172.16.0.0/24 CIDR block subnetted with 172.31.0.0/18


**Q29.** Can I detach the primary (eth0) network interface when the instance is running or stopped?

- **A.** Depends on the state of the interface at the time
- **B.** Yes, You can.
- **C.** No. You cannot


## Hybrid Connectivity: Direct Connect & VPN


**Q30.** You are building a solution for a customer to extend their on-premises data center to AWS. The customer requires a 50-Mbps dedicated and private connection to their VPC. Which AWS product or feature satisfies this requirement?

- **A.** Elastic IP Addresses
- **B.** Amazon VPC virtual private gateway
- **C.** Amazon VPC peering
- **D.** AWS Direct Connect


## General Design


**Q31.** Regarding the attaching of ENI to an instance, what does 'warm attach' refer to?

- **A.** Attaching an ENI to an instance when it is running
- **B.** Attaching an ENI to an instance during the launch process
- **C.** Attaching an ENI to an instance when it is stopped.
- **D.** This question doesn't make sense.


# Section B - Multiple Response (select all that apply)


## DynamoDB Design & Capacity


**Q32.** What AWS services are globally managed? **(Select 4.)**

- **A.** IAM
- **B.** S3
- **C.** Route 53
- **D.** WAF
- **E.** DynamoDB
- **F.** CloudFront


## SQS, SNS & Decoupling


**Q33.** When building a Distributed Denial of Service (DDoS)-resilient architecture, how does Amazon Virtual Private Cloud (Amazon VPC) help minimize the attack surface area? **(Select 3.)**

- **A.** Reduces the number of necessary Internet entry points
- **B.** Combines end user traffic with management traffic
- **C.** Adds non-critical Internet entry points to the architecture
- **D.** Obfuscates necessary Internet entry points to the level that untrusted end users
- **E.** Scales the network to absorb DDoS attacks


## CloudFront & Edge Delivery


**Q34.** Your customer has clients all across the globe that access product files stored in several S3 buckets, which are behind each of their own CloudFront web distributions. They currently want to deliver their content to a specific client, and they need to make sure that only that client can access the data. Currently, all of their clients can access their S3 buckets directly using an S3 URL or through their CloudFront distribution. The Solutions Architect must serve the private content via CloudFront only, to secure the distribution of files. Which combination of actions should you implement to meet the above requirements? (Select TWO.) **(Select 2.)**

- **A.** Use AWS Cloud Map to ensure that only their client can access the files.
- **B.** Require the users to access the private content by using special CloudFront signed URLs or signed cookies.
- **C.** Use S3 pre-signed URLs to ensure that only their client can access the files. Remove permission to use Amazon S3 URLs to read the files for anyone else.
- **D.** Use AWS App Mesh to ensure that only their client can access the files.
- **E.** Restrict access to files in the origin by creating an origin access identity (OAI) and give it permission to read the files in the bucket.


**Q35.** What two attributes are only associated with CloudFront private content? **(Select 2.)**

- **A.** Signed URL
- **B.** Object
- **C.** Signed cookies
- **D.** Web distribution
- **E.** Amazon S3 URL


**Q36.** A company uses CloudFront to provide low-latency access to cached files. An Architect is considering the implications of using CloudFront Regional Edge Caches. Which statements are correct in relation to this service? **(Select 2.)**

- **A.** Regional Edge Caches have larger cache-width than any individual edge location, so your objects remain in cache longer at these locations
- **B.** Regional Edge Caches are read-only
- **C.** Regional Edge Caches are enabled by default for CloudFront Distributions
- **D.** There are additional charges for using Regional Edge Caches


**Q37.** What DNS records can be used for pointing a zone apex to an Elastic Load Balancer or CloudFront distribution? **(Select 2.)**

- **A.** Name Server
- **B.** MX
- **C.** A
- **D.** Alias
- **E.** CNAME


**Q38.** Which of the following notification endpoints or clients are supported by Amazon Simple Notification Service? **(Select 2.)**

- **A.** Email
- **B.** CloudFront distribution
- **C.** Simple Network Management Protocol
- **D.** File Transfer Protocol
- **E.** Short Message Service


**Q39.** How are origin servers located within CloudFront? **(Select 2.)**

- **A.** Web distribution
- **B.** RTMP protocol
- **C.** Source mapping
- **D.** DNS request
- **E.** Distribution list


**Q40.** You have developed a web-based application for file sharing that will allow customers to access files. There are a variety of sizes that include larger .pdf and video files. What two solution stacks could tenants use for an online file sharing service? **(Select 2.)**

- **A.** EC2, ELB, Auto-Scaling, S3
- **B.** Route 53, Auto-Scaling, DynamoDB
- **C.** EC2, Auto-Scaling, RDS
- **D.** AWS CloudFront


**Q41.** Which of the following are good use cases for Amazon CloudFront? **(Select 2.)**

- **A.** A corporate website that serves training videos to employees. Most employees are located in two corporate campuses in the same city.
- **B.** A corporate HR website that supports a global workforce. Because the site contains sensitive data, all users must connect through a corporate Virtual Private Network (VPN).
- **C.** A popular software download site that supports users around the world, with dynamic content that changes rapidly
- **D.** A heavily used video and music streaming service that requires content to be delivered only to paid subscribers


## EC2 Instances, AMIs & Placement


**Q42.** You are creating a High-Performance Computing (HPC) cluster and need very low latency and high bandwidth between instances. What combination of the following will allow this? **(Select 3.)**

- **A.** Put the instances in a placement group.
- **B.** Enable enhanced networking on the instances.
- **C.** Use an instance type with 10 Gbps network performance.
- **D.** Use Dedicated Instances.
- **E.** Use Reserved Instances.


**Q43.** You nave multiple Amazon EC2 instances running in a cluster across multiple Availability Zones within the same region. What combination of the following should be used to ensure the highest network performance (packets per second), lowest latency, and lowest jitter? **(Select 3.)**

- **A.** Amazon EC2 placement groups
- **B.** Amazon Linux
- **C.** Amazon VPC
- **D.** Amazon HVM AMI
- **E.** Amazon PV AMI
- **F.** Enhanced networking


**Q44.** Which of the following are features of enhanced networking? **(Select 3.)**

- **A.** More Packets Per Second (PPS)
- **B.** Lower latency
- **C.** Less jitter
- **D.** Border Gateway Protocol (BGP) routing
- **E.** Multiple network interfaces


## Route 53 & DNS Routing


**Q45.** Which of the following statements are true about Amazon Route 53 resource records? **(Select 2.)**

- **A.** A CNAME record can be created for your zone apex.
- **B.** An Alias record can map one DNS name to another Amazon Route 53 DNS name.
- **C.** TTL can be set for an Alias record in Amazon Route 53.
- **D.** An Amazon Route 53 Alias record can point to any DNS record hosted anywhere.
- **E.** An Amazon Route 53 CNAME record can point to any DNS record hosted anywhere.


**Q46.** A Solutions Architect is designing a static website that will use the zone apex of a DNS domain (e.g. example.com). The Architect wants to use the Amazon Route 53 service. Which steps should the Architect take to implement a scalable and cost-effective solution? **(Select 2.)**

- **A.** Host the website on an Amazon EC2 instance, and map a Route 53 Alias record to the public IP address of the EC2 instance
- **B.** Create a Route 53 hosted zone, and set the NS records of the domain to use Route 53 name servers
- **C.** Serve the website from an Amazon S3 bucket, and map a Route 53 Alias record to the website endpoint
- **D.** Host the website using AWS Elastic Beanstalk, and map a Route 53 Alias record to the Beanstalk stack


**Q47.** What origin servers are supported by Amazon CloudFront? **(Select 3.)**

- **A.** An Amazon EC2 Auto Scaling Group
- **B.** An HTTP server running on Amazon Elastic Compute Cloud (Amazon EC2)
- **C.** An Amazon Simple Storage Service (Amazon S3) bucket
- **D.** An HTTP server running on-premises
- **E.** An Amazon Route 53 Hosted Zone


## VPC Connectivity: Endpoints, Peering, TGW


**Q48.** What AWS services now support VPC endpoints feature for optimizing security? **(Select 3.)**

- **A.** S3
- **B.** RDS
- **C.** Kinesis
- **D.** DNS Route 53
- **E.** DynamoDB


**Q49.** What are three characteristics of an Amazon Virtual Private Cloud? **(Select 3.)**

- **A.** Public and private IP addressing
- **B.** Persistent public IP addresses
- **C.** Broadcasts
- **D.** Multiple private IP addresses per network interface
- **E.** Dedicated single tenant hardware only
- **F.** HSRP


**Q50.** What properties of an Amazon VPC must be specified at the time of creation? **(Select 2.)**

- **A.** The CIDR block representing the IP address range
- **B.** Amazon VPC Peering relationships
- **C.** One or more subnets for the Amazon VPC
- **D.** The region for the Amazon VPC


## Lambda & Serverless Compute


**Q51.** What two features of an API Gateway minimize the effects of peak traffic events and minimize latency? **(Select 2.)**

- **A.** Caching
- **B.** Load balancing
- **C.** Throttling
- **D.** Firewalling
- **E.** Scaling


**Q52.** What network events are restricted by Lambda? **(Select 2.)**

- **A.** Only inbound TCP network connections are blocked by AWS Lambda
- **B.** All inbound network connections are blocked by AWS Lambda
- **C.** Outbound connections support only SSLsockets
- **D.** Outbound connections support only TCP/IP sockets
- **E.** All inbound and outbound connections are blocked


## High Availability & Fault Tolerance


**Q53.** Which of the following options will help increase the availability of a web server farm? **(Select 2.)**

- **A.** Use Amazon CloudFront to deliver content to the end users with low latency and high data transfer speeds.
- **B.** Deploy the instances in an Amazon Virtual Private Cloud (Amazon VPC).
- **C.** Launch the web server instances across multiple Availability Zones.
- **D.** Leverage Auto Scaling to recover from failed instances.
- **E.** Add more CPU and RAM to each instance.


## Monitoring: CloudWatch, CloudTrail & Config


**Q54.** How is CloudWatch integrated with Lambda? **(Select 2.)**

- **A.** Tenant must enable CloudWatch monitoring
- **B.** Log group is created for each function
- **C.** Network metrics such as latency are not monitored
- **D.** Log group is created for each event source
- **E.** Lambda functions are automatically monitored through Lambda service


## General Design


**Q55.** With regard to vulnerability scans and threat assessments of the AWS platform, which of the following statements are true? **(Select 2.)**

- **A.** AWS regularly performs scans of public-facing endpoint IP addresses for vulnerabilities.
- **B.** Scans performed by AWS include customer instances.
- **C.** Customers can perform their own scans at any time without advance notice.
- **D.** AWS security notifies the appropriate parties to remediate any identified vulnerabilities.


---


# Answer Key & Explanations


**Q1. B**  
_RDS Multi-AZ, Read Replicas & Aurora_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q2. C**  
_RDS Multi-AZ, Read Replicas & Aurora_  
Amazon Virtual Private Cloud (Amazon VPC) enables you to launch AWS resources into a virtual network that you've defined. This virtual network closely resembles a traditional network that you'd operate in your own data center, with the benefits of using the scalable infrastructure of AWS. Refer: https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon- vpc.html#:~:text=Amazon%20Virtual%20Private%20Cloud%20(Amazon,the%20scalable%20infrastructure%20of%20AWS.

**Q3. A**  
_VPC Security Groups & NACLs_  
Rules are evaluated starting with the lowest numbered rule. As soon as a rule matches traffic, it's applied immediately regardless of any higher-numbered rule that may contradict it. We have 3 rules here: 1. Rule 100 permits all traffic from any source. 2. Rule 101 denies all traffic coming from 110.238.109.37 3. The Default Rule (*) denies all traffic from any source. The Rule 100 will first be evaluated. If there is a match, then it will allow the request. Otherwise, it will then go to Rule 101 to repeat the same process until it goes to the default rule. In this case, when there is a request from 110.238.109.37, it will go through Rule 100 first. As Rule 100 says it will permit all traffic from any source, it will allow this request and will not further evaluate Rule 101 (which denies 110.238.109.37) nor the default rule.

**Q4. C**  
_VPC Security Groups & NACLs_  
None of the other options will have any effect on the ability to connect.

**Q5. D**  
_Auto Scaling & Elastic Load Balancing_  
_See the matching section of this task's `notes.md` for the underlying concept._
- *Why not A:* AWS Network Load Balancer (NLB) is an Amazon Web Services (AWS) tool that distributes end user traffic across multiple cloud resources to ensure low latency and high throughput for applications. ... When a target becomes slow or unavailable, the Network Load Balancer routes traffic to another target. Refer: https://aws.amazon.com/elasticloadbalancing/features/

**Q6. D**  
_DynamoDB Design & Capacity_  
DynamoDB uses eventually consistent reads, unless you specify otherwise. Read operations (such as GetItem, Query, and Scan) provide a ConsistentRead parameter. If you set this parameter to true, DynamoDB uses strongly consistent reads during the operation. Refer: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html

**Q7. D**  
_Route 53 & DNS Routing_  
You want your users to have the fastest network access possible. To do this, you would use latency-based routing. Geolocation routing would not achieve this as well as latency- based routing, which is specifically geared toward measuring the latency and thus would direct you to the AWS region in which you would have the lowest latency.

**Q8. D**  
_Route 53 & DNS Routing_  
Supported DNS record types - Amazon Route 53 Refer: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html#MXFormat

**Q9. D**  
_Route 53 & DNS Routing_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q10. A**  
_Route 53 & DNS Routing_  
The CNAME record maps a name to another name. It should be used only when there are no other records on that name.

**Q11. B**  
_Route 53 & DNS Routing_  
The resource record sets contained in a hosted zone must share the same suffix.

**Q12. D**  
_Route 53 & DNS Routing_  
An AAAA record is used to route traffic to an IPv6 address, whereas an A record is used to route traffic to an IPv4 address.

**Q13. C**  
_Route 53 & DNS Routing_  
A PTR record is used to resolve an IP address to a domain name, and it is commonly referred to as “reverse DNS.”

**Q14. D**  
_Route 53 & DNS Routing_  
The start of a zone is defined by the SOA; therefore, all zones must have an SOA record by default.

**Q15. C**  
_Route 53 & DNS Routing_  
A TXT record is used to store arbitrary and unformatted text with a host.

**Q16. D**  
_CloudFront & Edge Delivery_  
Amazon CloudFront is a web service that provides a CDN to speed up distribution of your static and dynamic web content—for example, .html , .css , .php , image, and media files—to end users. Amazon CloudFront delivers content through a worldwide network of edge locations. Amazon EC2, Amazon Route 53, and AWS Storage Gateway do not provide CDN services that are required to meet the needs for the photo sharing service.

**Q17. B**  
_CloudFront & Edge Delivery_  
CloudFront compares the request with the specifications in your distribution and forwards the request for the files to your origin server for the corresponding file type—for example, to your Amazon S3 bucket for image files and to your HTTP server for HTML files. Refer: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/HowCloudFrontWorks.html

**Q18. A**  
_CloudFront & Edge Delivery_  
SNI Custom SSL relies on the SNI extension of the Transport Layer Security protocol, which allows multiple domains to serve SSL traffic over the same IP address by including the hostname which the viewers are trying to connect to. You can host multiple TLS secured applications, each with its own TLS certificate, behind a single load balancer. In order to use SNI, all you need to do is bind multiple certificates to the same secure listener on your load balancer. ALB will automatically choose the optimal TLS certificate for each client. These features are provided at no additional charge. To meet the requirements in the scenario, you can upload all SSL certificates of the domains in the ALB using the console and bind multiple certificates to the same secure listener on your load balancer. ALB will automatically choose the optimal TLS certificate for each client using Server Name Indication (SNI).

**Q19. D**  
_CloudFront & Edge Delivery_  
Many companies that distribute content via the Internet want to restrict access to documents, business data, media streams, or content that is intended for selected users, such as users who have paid a fee. To serve this private content securely using Amazon CloudFront, you can require that users access your private content by using special Amazon CloudFront-signed URLs or signed cookies.

**Q20. C**  
_CloudFront & Edge Delivery_  
CloudFront compares the request with the specifications in your distribution and forwards the request for the files to your origin server for the corresponding file type—for example, to your Amazon S3 bucket for image files and to your HTTP server for HTML files. Refer: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/HowCloudFrontWorks.html

**Q21. D**  
_CloudFront & Edge Delivery_  
In CloudFront, an alternate domain name, also known as a CNAME, lets you use your own domain name (for example, www.example.com ) in your files' URLs instead of using the domain name that CloudFront assigns to your distribution. Refer: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/CNAMEs.html#:~:text=In%20CloudFront%2C%20an%20alternate%20domain,CloudFront%20assigns%20to%20your%20distribut

**Q22. D**  
_CloudFront & Edge Delivery_  
Amazon CloudFront is a fast content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to customers globally with low latency, high transfer speeds, all within a developer-friendly environment. Refer: https://aws.amazon.com/cloudfront/

**Q23. D**  
_CloudFront & Edge Delivery_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q24. B**  
_EBS Volumes & Snapshots_  
Multipart Upload allows you to upload a single object as a set of parts. After all parts of your object are uploaded, Amazon S3 then presents the data as a single object. With this feature you can create parallel uploads, pause and resume an object upload, and begin uploads before you know the total object size. Refer: https://aws.amazon.com/about-aws/whats-new/2010/11/10/Amazon-S3-Introducing-Multipart-Upload/

**Q25. C**  
_EC2 Instances, AMIs & Placement_  
Enhanced networking provides higher bandwidth, higher packet-per-second (PPS) performance, and consistently lower inter-instance latencies. If your packets-per-second rate appears to have reached its ceiling, you should consider moving to enhanced networking because you have likely reached the upper thresholds of the VIF driver. It is only available for certain instance types and only supported in VPC. You must also launch an HVM AMI with the appropriate drivers AWS currently supports enhanced networking capabilities using SR-IOV. SR-IOV provides direct access to network adapters, provides higher performance (packets-per-second) and lower latency You do not need to create a RAID 1 array (which is more for redundancy than performance anyway) A placement group is used to increase network performance between instances. In this case there is only a single instance so it won't help Adding multiple IP addresses is not a way to increase performance of the instance as the same amount of bandwidth is available to the Elastic Network Interface (ENI). References: https://digitalcloud.training/certification-training/aws-solutions-architect- associate/compute/amazon-ec2/ https://aws.amazon.com/premiumsupport/knowledge-center/enable-configure-enhanced-networking/

**Q26. B**  
_High Availability & Fault Tolerance_  
Elastic Load Balancing automatically distributes incoming application traffic across multiple targets, such as Amazon EC2 instances, containers, IP addresses, and Lambda functions. It can handle the varying load of your application traffic in a single Availability Zone or across multiple Availability Zones. Elastic Load Balancing offers three types of load balancers that all feature the high availability, automatic scaling, and robust security necessary to make your applications fault tolerant. Refer: https://aws.amazon.com/elasticloadbalancing/

**Q27. A**  
_VPC Connectivity: Endpoints, Peering, TGW_  
An Interface endpoint uses AWS PrivateLink and is an elastic network interface (ENI) with a private IP address that serves as an entry point for traffic destined to a supported service Using PrivateLink you can connect your VPC to supported AWS services, services hosted by other AWS accounts (VPC endpoint services), and supported AWS Marketplace partner services References: https://digitalcloud.training/certification-training/aws- solutions-architect-associate/networking-and-content-delivery/amazon-vpc/

**Q28. C**  
_AWS Organizations & Multi-Account_  
When we create a default VPC, we do the following to set it up for you - Create a VPC with a size /16 IPv4 CIDR block (172.31.0.0/16). This provides up to 65,536 private IPv4 addresses. Refer: https://docs.aws.amazon.com/vpc/latest/userguide/default-vpc.html

**Q29. C**  
_AWS Organizations & Multi-Account_  
You can detach secondary network interfaces when the instance is running or stopped. However, you can't detach the primary network interface. Refer: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html

**Q30. D**  
_Hybrid Connectivity: Direct Connect & VPN_  
Refer: https://aws.amazon.com/directconnect/faqs/

**Q31. C**  
_General Design_  
ENI can be attached to an instance when it's running (hot attach), when it's stopped (warm attach), or when the instance is being launched (cold attach).

**Q32. A, C, D, F**  
_DynamoDB Design & Capacity_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q33. A, C, D**  
_SQS, SNS & Decoupling_  
The attack surface is composed of the different Internet entry points that allow access to your application. The strategy to minimize the attack surface area is to (a) reduce the number of necessary Internet entry points, (b) eliminate non-critical Internet entry points, (c) separate end user traffic from management traffic, (d) obfuscate necessary Internet entry points to the level that untrusted end users cannot access them, and (e) decouple Internet entry points to minimize the effects

**Q34. B, E**  
_CloudFront & Edge Delivery_  
Many companies that distribute content over the Internet want to restrict access to documents, business data, media streams, or content that is intended for selected users, for example, users who have paid a fee. To securely serve this private content by using CloudFront, you can do the following: - Require that your users access your private content by using special CloudFront signed URLs or signed cookies. - Require that your users access your Amazon S3 content by using CloudFront URLs, not Amazon S3 URLs. Requiring CloudFront URLs isn't necessary, but it is recommended to prevent users from bypassing the restrictions that you specify in signed URLs or signed cookies. You can do this by setting up an origin access identity (OAI) for your Amazon S3 bucket. You can also configure the custom headers for a private HTTP server or an Amazon S3 bucket configured as a website endpoint. All objects and buckets by default are private. The pre-signed URLs are useful if you want your user/customer to be able to upload a specific object to your bucket, but you don't require them to have AWS security credentials or permissions. You can generate a pre-signed URL programmatically using the AWS SDK for Java or the AWS SDK for .NET. If you are using Microsoft Visual Studio, you can also use AWS Explorer to generate a pre-signed object URL without writing any code. Anyone who receives a valid pre-signed URL can then programmatically upload an object.
- *Why not A:* This option is incorrect because AWS Cloud Map is simply a cloud resource discovery service that enables you to name your application resources with custom names and automatically update the locations of your dynamically changing resources.
- *Why not C:* This option is incorrect. Although this could be a valid solution, it doesn't satisfy the requirement to serve the private content via CloudFront only, to secure the distribution of files. A better solution is to set up an origin access identity (OAI) then use Signed URL or Signed Cookies in your CloudFront web distribution.
- *Why not D:* This option is incorrect because AWS App Mesh is just a service mesh that provides application-level networking to make it easy for your services to communicate with each other across multiple types of compute infrastructure.

**Q35. A, C**  
_CloudFront & Edge Delivery_  
A signed URL includes additional information, for example, an expiration date and time, that gives you more control over access to your content. Refer: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-signed-urls.html CloudFront signed cookies allow you to control who can access your content when you don't want to change your current URLs or when you want to provide access to multiple restricted files, for example, all of the files in the subscribers' area of a website. This topic explains the considerations when using signed cookies and describes how to set signed cookies using canned and custom policies. Refer: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-signed-cookies.html

**Q36. A, C**  
_CloudFront & Edge Delivery_  
Regional Edge Caches are located between origin web servers and global edge locations and have a larger cache than any individual edge location, so your objects remain in cache longer at these locations. Regional Edge caches aim to get content closer to users and are enabled by default for CloudFront Distributions (so you don't need to update your distributions) There are no additional charges for using Regional Edge Caches You can write to regional edge caches too. References: https://digitalcloud.training/certification-training/aws-solutions-architect- associate/networking-and-content-delivery/amazon-cloudfront/ https://aws.amazon.com/about-aws/whats-new/2016/11/announcing-regional-edge- caches-for-amazon-cloudfront/

**Q37. C, D**  
_CloudFront & Edge Delivery_  
Route 53 supports the alias resource record set, which lets you map your zone apex (e.g. example.com) DNS name to your load balancer DNS name. IP addresses associated with Elastic Load Balancing can change at any time due to scaling or software updates. Route 53 responds to each request for an alias resource record set with one IP address for the load balancer. If a load balancer has more than one IP address, Elastic Load Balancing selects one of the IP addresses in a round-robin fashion and returns it to Route 53; Route 53 then responds to the request with that IP address. Refer: https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/setting-up-route53-zoneapex-elb.html

**Q38. A, E**  
_CloudFront & Edge Delivery_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q39. A, D**  
_CloudFront & Edge Delivery_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q40. A, D**  
_CloudFront & Edge Delivery_  
Amazon CloudFront is a fast content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to customers globally with low latency, high transfer speeds, all within a developer-friendly environment. Refer: https://aws.amazon.com/cloudfront/

**Q41. C, D**  
_CloudFront & Edge Delivery_  
The site in A is “popular” and supports “users around the world,” key indicators that CloudFront is appropriate. Similarly, the site in C is “heavily used,” and requires private content, which is supported by Amazon CloudFront. Both B and D are corporate use cases where the requests come from a single geographic location or appear to come from one (because of the VPN). These use cases will generally not see benefit from Amazon CloudFront.

**Q42. A, B, C**  
_EC2 Instances, AMIs & Placement_  
The other answers have nothing to do with networking.

**Q43. A, B, F**  
_EC2 Instances, AMIs & Placement_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q44. A, B, C**  
_EC2 Instances, AMIs & Placement_  
These are the benefits of enhanced networking.

**Q45. B, E**  
_Route 53 & DNS Routing_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q46. B, C**  
_Route 53 & DNS Routing_  
To use Route 53 for an existing domain the Architect needs to change the NS records to point to the Amazon Route 53 name servers. This will direct name resolution to Route 53 for the domain name. The most cost-effective solution for hosting the website will be to use an Amazon S3 bucket. To do this you create a bucket using the same name as the domain name (e.g. example.com) and use a Route 53 Alias record to map to it Using an EC2 instance instead of an S3 bucket would be more costly so that rules out 2 options that explicitly mention EC3 Elastic Beanstalk provisions EC2 instances so again this would be a more costly option References: https://docs.aws.amazon.com/AmazonS3/latest/dev/website-hosting-custom-domain-walkthrough.html

**Q47. B, C, D**  
_Route 53 & DNS Routing_  
Amazon CloudFront can use an Amazon S3 bucket or any HTTP server, whether or not it is running in Amazon EC2. A Route 53 Hosted Zone is a set of DNS resource records, while an Auto Scaling Group launches or terminates Amazon EC2 instances automatically. Neither can be specified as an origin server for a distribution.

**Q48. A, C, E**  
_VPC Connectivity: Endpoints, Peering, TGW_  
With AWS PrivateLink for Amazon S3, you can provision interface VPC endpoints (interface endpoints) in your virtual private cloud (VPC). These endpoints are directly accessible from applications that are on premises over VPN and AWS Direct Connect, or in a different AWS Region over VPC peering. Interface endpoints are represented by one or more elastic network interfaces (ENIs) that are assigned private IP addresses from subnets in your VPC. Requests that are made to interface endpoints for Amazon S3 are automatically routed to Amazon S3 on the Amazon network. You can also access interface endpoints in your VPC from on-premises applications through AWS Direct Connect or AWS Virtual Private Network (AWS VPN). https://docs.aws.amazon.com/AmazonS3/latest/userguide/privatelink-interface-endpoints.html For security reasons, many AWS customers run their applications within an Amazon Virtual Private Cloud environment (Amazon VPC). With Amazon VPC, you can launch Amazon EC2 instances into a virtual private cloud, which is logically isolated from other networks—including the public internet. With an Amazon VPC, you have control over its IP address range, subnets, routing tables, network gateways, and security settings. To access the public internet, your VPC must have an internet gateway—a virtual router that connects your VPC to the internet. This allows applications running on Amazon EC2 in your VPC to access internet resources, such as Amazon DynamoDB. By default, communications to and from DynamoDB use the HTTPS protocol, which protects network traffic by using SSL/TLS encryption. The following diagram shows how an EC2 instance in a VPC accesses DynamoDB: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/vpc- endpoints-dynamodb.html You can use an interface VPC endpoint to keep traffic between your Amazon VPC and Kinesis Data Streams from leaving the Amazon network. Interface VPC endpoints don't require an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection. Interface VPC endpoints are powered by AWS PrivateLink, an AWS technology that enables private communication between AWS services using an elastic network interface with private IPs in your Amazon VPC. https://docs.aws.amazon.com/streams/latest/dev/vpc.html

**Q49. A, B, D**  
_VPC Connectivity: Endpoints, Peering, TGW_  
Amazon Virtual Private Cloud (Amazon VPC) lets you provision a logically isolated section of the AWS Cloud where you can launch AWS resources in a virtual network that you define. You have complete control over your virtual networking environment, including selection of your own IP address range, creation of subnets, and configuration of route tables and network gateways. You can use both IPv4 and IPv6 in your VPC for secure and easy access to resources and applications. Refer: https://aws.amazon.com/vpc/

**Q50. A, D**  
_VPC Connectivity: Endpoints, Peering, TGW_  
The CIDR block is specified upon creation and cannot be changed. An Amazon VPC is associated with exactly one region which must be specified upon creation. You can add a subnet to an Amazon VPC any time after it has been created, provided its address range falls within the Amazon VPC CIDR block and does not overlap with the address range of any existing CIDR block. You can set up peering relationships between Amazon VPCs after they have been created.

**Q51. A, C**  
_Lambda & Serverless Compute_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q52. B, D**  
_Lambda & Serverless Compute_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q53. C, D**  
_High Availability & Fault Tolerance_  
Launching instances across multiple Availability Zones helps ensure the application is isolated from failures in a single Availability Zone, allowing the application to achieve higher availability. Whether you are running one Amazon EC2 instance or thousands, you can use Auto Scaling to detect impaired Amazon EC2 instances and unhealthy applications and replace the instances without your intervention. This ensures that your application is getting the compute capacity that you expect.

**Q54. B, E**  
_Monitoring: CloudWatch, CloudTrail & Config_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q55. A, D**  
_General Design_  
AWS regularly scans public-facing, non-customer endpoint IP addresses and notifies appropriate parties. AWS does not scan customer instances, and customers must request the ability to perform their own scans in advance, therefore answers are correct.
