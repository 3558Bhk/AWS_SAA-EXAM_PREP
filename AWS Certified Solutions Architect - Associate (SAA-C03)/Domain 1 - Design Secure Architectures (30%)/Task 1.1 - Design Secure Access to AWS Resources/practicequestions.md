# Task 1.1 - Design Secure Access to AWS Resources - Practice Questions

> **Domain 1 - Design Secure Architectures (30%)**  
> Curated from 18 practice sets: duplicates removed, outdated items retired, ordered **highest-frequency exam topics first**.  
> **56 multiple-choice (single answer)** followed by **29 multiple-response (select 2+)**. Total **85**.


**Topic order in this file:** IAM Roles, Policies & Permissions → S3 Security, Access & Durability → RDS Multi-AZ, Read Replicas & Aurora → VPC Security Groups & NACLs → Auto Scaling & Elastic Load Balancing → EC2 Instances, AMIs & Placement → CloudFront & Edge Delivery → Encryption & AWS KMS → Monitoring: CloudWatch, CloudTrail & Config → Federation, SSO & Cognito → Secrets, Parameters & Credentials → General Design → Well-Architected & General Design → EBS Volumes & Snapshots → Threat Detection & Compliance → Elastic Beanstalk & Deployment


---


# Section A - Multiple Choice (one correct answer)


## IAM Roles, Policies & Permissions


**Q1.** Which feature of AWS is designed to permit calls to the platform from an Amazon Elastic Compute Cloud (Amazon EC2) instance without needing access keys placed on the instance?

- **A.** IAM groups
- **B.** AWS Identity and Access Management (IAM) instance profile
- **C.** IAM roles
- **D.** Amazon EC2 key pairs


**Q2.** A____________ is an individual, system, or application that interacts with AWS programmatically.

- **A.** AWS Account
- **B.** user
- **C.** Role
- **D.** Group


**Q3.** You need a secure way to distribute your AWS credentials to an application running on Amazon Elastic Compute Cloud (Amazon EC2) instances in order to access supplementary AWS Cloud services. What approach provides your application access to use short-term credentials for signing requests while protecting those credentials from other users?

- **A.** Provision the Amazon EC2 instances with an instance profile that has the appropriate privileges.
- **B.** Add your credentials to the UserData parameter of each Amazon EC2 instance.
- **C.** Specify your access and secret keys directly in your application.
- **D.** Use a configuration file to store your access and secret keys on the Amazon EC2 instances.


**Q4.** A company is building software on AWS that requires access to various AWS services. Which configuration should be used to ensure mat AWS credentials (i.e., Access Key ID/Secret Access Key combination) are not compromised?

- **A.** Assign an IAM user to the Amazon EC2 Instance.
- **B.** Store the AWS Access Key ID/Secret Access Key combination in software comments.
- **C.** Enable Multi-Factor Authentication for your AWS root account.
- **D.** Assign an IAM role to the Amazon EC2 instance.


**Q5.** Your company has an on-premise LDAP directory service. As part of a gradual migration into AWS you would like to integrate the LDAP directory with AWS’s Identity and Access Management (IAM) solutions so that existing users can authenticate against AWS services. What method would you suggest using to enable this integration?

- **A.** Create a policy in IAM that references users in the on-premise LDAP directory
- **B.** Use AWS Simple AD and create a trust relationship with IAM
- **C.** Use SAML to develop a direct integration from the on-premise LDAP directory to the relevant AWS services
- **D.** Develop an on-premise custom identity provider (IdP) and use the AWS Security Token Service (STS) to provide temporary security credentials


**Q6.** What is the advantage of resource-based policies for cross-account access?

- **A.** Trusting account manages all permissions
- **B.** Resource-based policies are easier to deploy
- **C.** Trusted account permissions are replaced
- **D.** Trusted account permissions are not replaced


**Q7.** You work for Digital Cloud Training and have just created a number of IAM users in your AWS account. You need to ensure that the users are able to make API calls to AWS services. What else needs to be done?

- **A.** Enable Multi-Factor Authentication for the users
- **B.** Create a group and add the users to it
- **C.** Set a password for each user
- **D.** Create a set of Access Keys for the users


**Q8.** You are the Solutions Architect for your company's AWS account of approximately 300 IAM users. They have a new company policy that will change the access of 100 of the IAM users to have a particular sort of access to Amazon S3 buckets. What will you do to avoid the time-consuming task of applying the policy at the individual user?

- **A.** Create a new IAM group and then add the users that require access to the S3 bucket. Afterwards, apply the policy to IAM group.
- **B.** Create a new IAM role and add each user to the IAM role.
- **C.** Create a new S3 bucket access policy with unlimited access for each IAM user.
- **D.** Create a new policy and apply it to multiple IAM users using a shell script.


**Q9.** A __________ is the concept of allowing (or disallowing) an entity such as a user, group, or role some type of access to one or more resources.

- **A.** AWS Account
- **B.** permission
- **C.** user
- **D.** resource


**Q10.** What should you do in order to grant a different AWS account permission to your Amazon Simple Queue Service (Amazon SQS) queue?

- **A.** Share credentials to your AWS account and have the other account’s applications use your account’s credentials to access the Amazon SQS queue.
- **B.** Create a user for that account in AWS Identity and Access Management (IAM) and establish an IAM policy that grants access to the queue.
- **C.** Create an Amazon SQS policy that grants the other account access.
- **D.** Amazon Virtual Private Cloud (Amazon VPC) peering must be used to achieve this.


**Q11.** You launch an Amazon EC2 instance without an assigned AVVS identity and Access Management (IAM) role. Later, you decide that the instance should be running with an IAM role. Which action must you take in order to have a running Amazon EC2 instance with an IAM role assigned to it?

- **A.** Create a new IAM role with the same permissions as an existing IAM role, and assign it to the running instance.
- **B.** Create an image of the instance, and register the image with an IAM role assigned and an Amazon EBS volume mapping.
- **C.** Create an image of the instance, add a new IAM role with the same permissions as the desired IAM role, and deregister the image with the new role assigned.
- **D.** Create an image of the instance, and use this image to launch a new instance with the desired IAM role assigned.


**Q12.** A __________ is a document that provides a formal statement of one or more permissions.

- **A.** Role
- **B.** permission
- **C.** resource
- **D.** policy


**Q13.** After creating a new IAM user which of the following must be done before they can successfully make API calls?

- **A.** Assign a Password Policy to the user.
- **B.** Add a password to the user.
- **C.** Enable Multi-Factor Authentication for the user.
- **D.** Create a set of Access Keys for the user.


**Q14.** Every user you create in the IAM system starts with ___________.

- **A.** Full permissions
- **B.** Partial permissions
- **C.** No permissions


**Q15.** An application running on an external website is attempting to initiate a request to your company’s website on AWS using API calls. A problem has been reported in which the requests are failing with an error that includes the following text: “Cross-Origin Request Blocked: The Same Origin Policy disallows reading the remote resource"You have been asked to resolve the problem, what is the most likely solution?

- **A.** The IAM policy does not allow access to the API
- **B.** Enable CORS on the APIs resources using the selected methods under the API Gateway
- **C.** The ACL on the API needs to be updated
- **D.** The request is not secured with SSL/TLS


**Q16.** You work for a leading university as an AWS Infrastructure Engineer and also as a professor to aspiring AWS architects. As a way to familiarize your students with AWS, you gave them a project to host their applications to an EC2 instance. One of your students created an instance to host their online enrollment system project but is having a hard time connecting to their newly created EC2 instance. Your students have explored all of the troubleshooting guides by AWS and narrowed it down to login issues. Which of the following can you use to log into an EC2 instance?

- **A.** EC2 Connection Strings
- **B.** Key Pairs
- **C.** Access Keys
- **D.** Custom EC2 password


**Q17.** You have valuable media files hosted on AWS and want them to be served only to authenticated users of your web application. You are concerned that your content could be stolen and distributed for free. How can you protect your content?

- **A.** Use logging to track your content.
- **B.** Use AWS Identity and Access Management (IAM) policies to restrict access.
- **C.** Generate pre-signed URLs for content in the web application.
- **D.** Use static web hosting.


**Q18.** Within the IAM service a GROUP is regarded as a:

- **A.** It's the group of EC2 machines that gain the permissions specified in the GROUP.
- **B.** A collection of users.
- **C.** A collection of AWS accounts
- **D.** There's no GROUP in IAM, but only USERS and RESOURCES.


**Q19.** What is the default maximum number of MFA devices in use per AWS account (at the root account level)?

- **A.** 1
- **B.** 5
- **C.** 10
- **D.** 15


**Q20.** IAM provides several policy templates you can use to automatically assign permissions to the groups you create. The _____ policy template gives the Admins group permission to access all account resources, except your AWS account information

- **A.** AWS Cloud Formation Read Only Access
- **B.** Power User Access
- **C.** Administrator Access
- **D.** Read Only Access


**Q21.** How many access keys may an AWS Identity and Access Management (IAM) user have active at one time?

- **A.** ZERO
- **B.** 3
- **C.** 1
- **D.** 2


**Q22.** What is the format of an IAM policy?

- **A.** Key/value pairs
- **B.** Tab-delimited text
- **C.** XML
- **D.** JSON


**Q23.** What are the Amazon EC2 API tools?

- **A.** They are a set of graphical tools to manage EC2 instances.
- **B.** Command-line tools to the Amazon EC2 web service.
- **C.** They don't exist. The Amazon EC2 AMI tools, instead, are used to manage permissions.
- **D.** They don't exist. The Amazon API tools are a client interface to Amazon Web Services.


**Q24.** Is there a limit to how many groups a user can be in?

- **A.** Yes for all users
- **B.** No
- **C.** Yes unless special permission granted
- **D.** Yes for all users except root


**Q25.** Is there a limit to the number of groups you can have?

- **A.** Yes for all users except root
- **B.** Yes unless special permission granted
- **C.** Yes for all users
- **D.** No


**Q26.** A company needs to deploy services to an AWS region which they have not previously used. The company currently has an AWS identity and Access Management (IAM) role for the Amazon EC2 instances, which permits the instance to have access to Amazon DynamoDB. The company wants their EC2 instances in the new region to have the same privileges. How should the company achieve this?

- **A.** Assign the existing IAM role to the Amazon EC2 instances in the new region
- **B.** Create a new IAM role and associated policies within the new region
- **C.** Create an Amazon Machine Image (AMI) of the instance and copy it to the desired region using the AMI Copy feature
- **D.** Copy the IAM role and associated policies to the new region and attach it to the instances


**Q27.** What is required to prevent an instance from being launched and incurring costs?

- **A.** Terminate instance
- **B.** Stop and de-register instance
- **C.** Stop instance
- **D.** Terminate AMI and de-register instance
- **E.** Stop, deregister AMI and terminate instance


**Q28.** Which port number is used to serve requests by DNS?

- **A.** 389
- **B.** 161
- **C.** 53
- **D.** 22


## S3 Security, Access & Durability


**Q29.** A company is using multiple AWS accounts that are consolidated using AWS Organizations. They want to copy several S3 objects to another S3 bucket that belonged to a different AWS account which they also own. The Solutions Architect was instructed to set up the necessary permissions for this task and to ensure that the destination account owns the copied objects and not the account it was sent from. How can the Architect accomplish this requirement?

- **A.** Configure cross-account permissions in S3 by creating an IAM customer managed policy that allows an IAM user or role to copy objects from the source bucket in one account to the destination bucket in the other account. Then attach the policy to the IAM user or role that you want to use to copy objects between accounts.
- **B.** Set up cross-origin resource sharing (CORS) in S3 by creating a bucket policy that allows an IAM user or role to copy objects from the source bucket in one account to the destination bucket in the other account.
- **C.** Connect the two S3 buckets from two different AWS accounts to Amazon WorkDocs. Set up cross-account access to integrate the two S3 buckets. Use the Amazon WorkDocs console to copy the objects from one account to the other with modified object ownership assigned to the destination account.
- **D.** Enable the Requester Pays feature in the source S3 bucket. The fees would be waived through Consolidated Billing since both AWS accounts are part of AWS Organizations.


**Q30.** To have a record of who accessed your Amazon Simple Storage Service (Amazon S3) data and from where, you should do what?

- **A.** Enable Amazon CloudWatch logs.
- **B.** Enable versioning on the bucket.
- **C.** Create an AWS Identity and Access Management (IAM) bucket policy.
- **D.** Enable website hosting on the bucket.
- **E.** Enable server access logs on the bucket.


**Q31.** A customer wants to leverage Amazon Simple Storage Service (S3) and Amazon Glacier as part of their backup and archive infrastructure. The customer plans to use third-party software to support this integration. Which approach will limit the access of the third party software to only the Amazon S3 bucket named "company-backup"?

- **A.** A custom IAM user policy limited to the Amazon S3 API for the Amazon Glacier archive "company-backup".
- **B.** A custom IAM user policy limited to the Amazon S3 API in "company-backup".
- **C.** A custom bucket policy limited to the Amazon S3 API in "company-backup"
- **D.** A custom bucket policy limited to the Amazon S3 API in thee Amazon Glacier archive "company-backup"


## RDS Multi-AZ, Read Replicas & Aurora


**Q32.** You currently operate a web application In the AWS US-East region The application runs on an auto-scaled layer of EC2 instances and an RDS Multi-AZ database Your IT security compliance officer has tasked you to develop a reliable and durable logging solution to track changes made to your EC2.IAM And RDS resources. The solution must ensure the integrity and confidentiality of your log data. Which of these solutions would you recommend?

- **A.** Create three new CloudTrail trails with three new S3 buckets to store the logs one for the AWS Management console, one for AWS SDKs and one for command line tools Use IAM roles and S3 bucket policies on the S3 buckets that store your logs.
- **B.** Create a new CloudTrail with one new S3 bucket to store the logs Configure SNS to send log file delivery notifications to your management system Use IAM roles and S3 bucket policies on the S3 bucket mat stores your logs.
- **C.** Create a new CloudTrail trail with an existing S3 bucket to store the logs and with the global services option selected Use S3 ACLs and Multi Factor Authentication (MFA) Delete on the S3 bucket that stores your logs.
- **D.** Create a new CloudTrail trail with one new S3 bucket to store the logs and with the global services option selected Use IAM roles S3 bucket policies and Multi Factor Authentication (MFA) Delete on the S3 bucket that stores your logs.


**Q33.** In regards to IAM you can edit user properties later, but you cannot use the console to change the ___________.

- **A.** user name
- **B.** password
- **C.** default group


## VPC Security Groups & NACLs


**Q34.** A company needs to deploy virtual desktops for its customers in an AWS VPC and would like to leverage their existing on-premise security principals. AWS Workspaces will be used as the virtual desktop solution. Which set of AWS services and features will meet the company’s requirements?

- **A.** AWS Directory Service and AWS IAM
- **B.** A VPN connection, VPC NACLs and Security Groups
- **C.** Amazon EC2, and AWS IAM
- **D.** A VPN connection, and AWS Directory Services


**Q35.** You have launched an Amazon Linux Elastic Compute Cloud (Amazon EC2) instance into EC2-Classic, and the instance has successfully passed the System Status Check and Instance Status Check. You attempt to securely connect to the instance via Secure Shell (SSH) and receive the response, “WARNING: UNPROTECTED PRIVATE KEY FILE,” after which the login fails. Which of the following is the cause of the failed login?

- **A.** A security group rule is blocking the connection.
- **B.** A security group rule has not been associated with the private key.
- **C.** The permissions for the private key are too insecure for the key to be trusted.
- **D.** You are using the wrong private key.


## Auto Scaling & Elastic Load Balancing


**Q36.** HTTP Query-based requests are HTTP requests that use the HTTP verb GET or POST and a Query parameter named_____________.

- **A.** Action
- **B.** Reset
- **C.** Retrieve
- **D.** Value


## EC2 Instances, AMIs & Placement


**Q37.** You need to pass a custom script to new Amazon Linux instances created in your Auto Scaling group. Which feature allows you to accomplish this?

- **A.** AWS Config
- **B.** User data
- **C.** IAM roles
- **D.** EC2Config service


**Q38.** What happens to the data on an instance if the instance reboots (intentionally or unintentionally)?

- **A.** Data persists
- **B.** Data will be lost
- **C.** Data may persist however cannot be sure


**Q39.** When will you incur costs with an Elastic IP address (EIP)?

- **A.** Costs are incurred regardless of whether the EIP is associated with a running instance.
- **B.** When it is allocated and associated with a running instance.
- **C.** When an EIP is allocated.
- **D.** When it is allocated and associated with a stopped instance.


## CloudFront & Edge Delivery


**Q40.** You are building a media-sharing web application that serves video files to end users on both PCs and mobile devices. The media files are stored as objects in an Amazon Simple Storage Service (Amazon S3) bucket, but are to be delivered through Amazon CloudFront. What is the simplest way to ensure that only Amazon CloudFront has access to the objects in the Amazon S3 bucket?

- **A.** Create Signed URLs for each Amazon S3 object.
- **B.** Use an AWS Identity and Access Management (IAM) bucket policy.
- **C.** Use public and private keys with signed cookies.
- **D.** Use an Amazon CloudFront Origin Access Identifier (OAI).


## Encryption & AWS KMS


**Q41.** You have launched a Windows Amazon Elastic Compute Cloud (Amazon EC2) instance and specified an Amazon EC2 key pair for the instance at launch. Which of the following accurately describes how to log in to the instance?

- **A.** A key pair is not needeSecurely connect to the instance via RDP.
- **B.** Use the Amazon EC2 key pair to decrypt the administrator password and then securely connect to the instance via Remote Desktop Protocol (RDP) as the administrator.
- **C.** Use the Amazon EC2 key pair to securely connect to the instance via Secure Shell (SSH).
- **D.** Use your AWS Identity and Access Management (IAM) user X.509 certificate to log in to the instance.


## Monitoring: CloudWatch, CloudTrail & Config


**Q42.** Which AWS Cloud service allows organizations to gain system-wide visibility into resource utilization, application performance, and operational health?

- **A.** Amazon CloudWatch
- **B.** AWS Identity and Access Management (IAM)
- **C.** AWS CloudFormation
- **D.** Amazon Simple Notification Service (Amazon SNS)


**Q43.** What is required to enable application and operating system generated logs and publish to CloudWatch Logs?

- **A.** enable access logs
- **B.** IAM cross-account enabled
- **C.** Syslog
- **D.** CloudWatch Log Agent


## Federation, SSO & Cognito


**Q44.** You work as an Enterprise Architect for a global organization which employs 20,000 people. The company is growing at around 5% per annum. The company strategy is to increasingly adopt AWS cloud services. There is an existing Microsoft Active Directory (AD) service that is used as the on-premise identity and access management system. You want to enable users to authenticate using their existing identities and access AWS resources (including the AWS Management Console) using single sign-on (SSO). What is the simplest way to enable SSO to the AWS management console using the existing domain?

- **A.** Install a Microsoft Active Directory Domain Controller on AWS and add it into your existing on-premise domain
- **B.** Use a large AWS Simple AD in AWS
- **C.** Launch an Enterprise Edition AWS Active Directory Service for Microsoft Active Directory and setup trust relationships with your on-premise domain
- **D.** Launch a large AWS Directory Service AD Connector to proxy all authentication back to your on-premise AD service for authentication


**Q45.** Your client is looking for a fully managed directory service in the AWS cloud. The service should provide an inexpensive Active Directory-compatible service with common directory features. The client is a medium-sized organization with 4000 users. As the client has a very limited budget it is important to select a cost-effective solution.What would you suggest?

- **A.** AWS Simple AD
- **B.** AWS Active Directory Service for Microsoft Active Directory
- **C.** Amazon Cognito
- **D.** AWS Single Sign-On


**Q46.** You are designing an identity, authorization and access management solution for the AWS cloud. The features you need include the ability to manage user accounts and group memberships, create and apply group policies, securely connect to Amazon EC2 instances, and provide Kerberos-based single sign-on (SSO). You do not need to establish trust relationships with other domains, use DNS dynamic update, implement schema extensions or use other advanced directory features. What would be the most cost-effective solution?

- **A.** Use AWS Simple AD
- **B.** Use AWS Directory Service for Microsoft AD
- **C.** Use Amazon Cloud Directory
- **D.** Use AD Connector


**Q47.** A photo-sharing service stores pictures in Amazon Simple Storage Service (S3) and allows application sign-in using an OpenID Connect-compatible identity provider. Which AWS Security Token Service approach to temporary access should you use for the Amazon S3 operations?

- **A.** Web Identity Federation
- **B.** AWS Identity and Access Management roles
- **C.** SAML-based Identity Federation
- **D.** Cross-Account Access


**Q48.** Which technique can be used to integrate AWS IAM (Identity and Access Management) with an on-premise LDAP (Lightweight Directory Access Protocol) directory service?

- **A.** Use AWS Security Token Service from an identity broker to issue short-lived AWS credentials.
- **B.** Use IAM roles to automatically rotate the IAM credentials when LDAP credentials are updated.
- **C.** Use SAML (Security Assertion Markup Language) to enable single sign-on between AWS and LDAP
- **D.** Use an IAM policy that references the LDAP account identifiers and the AWS credentials.
- **E.** Use the LDAP credentials to restrict a group of users from launching specific EC2 instance types.


**Q49.** What authentication method provides Federated Single Sign-On (SSO) for cloud applications?

- **A.** ADS
- **B.** TACACS
- **C.** SAML
- **D.** RADIUS
- **E.** ISE


**Q50.** An application that was recently moved into the AWS cloud has been experiencing some authentication issues. The application is currently configured to authenticate to an on-premise Microsoft Active Directory Domain Controller via a VPN connection. Upon troubleshooting the issues, it seems that latency across the VPN connection is causing authentication to fail. Your company is very cost sensitive at the moment and the administrators of the Microsoft AD do not want to manage any additional directories. You need to resolve the issues quickly. What is the best solution to solve the authentication issues taking cost considerations into account?

- **A.** Use the AWS Active Directory Service for Microsoft Active Directory and join your existing on-premise domain
- **B.** Install an additional Microsoft Active Directory Domain Controller for your existing domain on EC2 and configure the application to authenticate to the local DC
- **C.** Use the AWS Active Directory Service for Microsoft Active Directory and create a new domain. Establish a trust relationship with your existing on- premise domain
- **D.** Create an AWS Direct Connect connection to reduce the latency between your company and AWS


**Q51.** Company B is launching a new game app for mobile devices. Users will log into the game using their existing social media account to streamline data capture. Company B would like to directly save player data and scoring information from the mobile app to a DynamoDS table named Score Data When a user saves their game the progress data will be stored to the Game state S3 bucket. What is the best approach for storing data to DynamoDB and S3?

- **A.** Use an EC2 Instance that is launched with an EC2 role providing access to the Score Data DynamoDB table and the GameState S3 bucket that communicates with the mobile app via web services.
- **B.** Use temporary security credentials that assume a role providing access to the Score Data DynamoDB table and the Game State S3 bucket using web identity federation.
- **C.** Use an IAM user with access credentials assigned a role providing access to the Score Data DynamoDB table and the Game State S3 bucket for distribution with the mobile app.
- **D.** Use Login with Amazon allowing users to sign in with an Amazon account providing the mobile app with access to the Score Data DynamoDB table and the Game State S3 bucket.


**Q52.** A company needs to deploy virtual desktops to its customers in a virtual private cloud, leveraging existing security controls. Which set of AWS services and features will meet the company's requirements?

- **A.** Virtual Private Network connection. AWS Directory Services, and ClassicLink
- **B.** Amazon Elastic Compute Cloud, and AWS Identity and Access Management
- **C.** Virtual Private Network connection. AWS Directory Services, and Amazon Workspaces
- **D.** AWS Directory Service, Amazon Workspaces, and AWS Identity and Access Management


**Q53.** The development team at your company have created a new mobile application that will be used by users to access confidential data. The developers have used Amazon Cognito for authentication, authorization, and user management. Due to the sensitivity of the data, there is a requirement to add another method of authentication in addition to a username and password. You have been asked to recommend the best solution. What is your recommendation?

- **A.** Integrate a third-party identity provider (IdP)
- **B.** Use multi-factor authentication (MFA) with a Cognito user pool
- **C.** Enable multi-factor authentication (MFA) in IAM
- **D.** Integrate IAM with a user pool in Cognito


## Secrets, Parameters & Credentials


**Q54.** IAM's Policy Evaluation Logic always starts with a default ____________ for every request, except for those that use the AWS account's root security credentials b

- **A.** Permit
- **B.** Deny
- **C.** Cancel


## General Design


**Q55.** What IAM class enables an EC2 instance to access a file object in an S3 bucket?

- **A.** group
- **B.** role
- **C.** root
- **D.** user
- **E.** Auto-Scaling
- **F.** data replication


## Well-Architected & General Design


**Q56.** Can I attach more than one policy to a particular entity?

- **A.** Only if within VPC
- **B.** Only if within GovCloud
- **C.** No
- **D.** Yes always


# Section B - Multiple Response (select all that apply)


## IAM Roles, Policies & Permissions


**Q57.** You are creating a design for an internal-only AWS service that uses EC2 instances to process information on S3 and store the results in DynamoDB. You need to allow access to several developers who will be testing code and need to apply security best practices to the architecture. Which of the security practices below are recommended? **(Select 2.)**

- **A.** Store the access keys and secret IDs within the application
- **B.** Disable root API access keys and secret key
- **C.** Use bastion hosts to enforce control and visibility
- **D.** Assign an IAM user for each EC2 instance


**Q58.** Which of the following are best practices for managing AWS Identity and Access Management (IAM) user access keys? **(Select 3.)**

- **A.** Use different access keys for different applications.
- **B.** Keep unused access keys for an indefinite period of time.
- **C.** Rotate access keys periodically.
- **D.** Embed access keys directly into application code.
- **E.** Configure Multi-Factor Authentication (MFA) for your most sensitive operations.


**Q59.** You try to connect via SSH to a newly created Amazon EC2 instance and get one of the following error messages: "Network error: Connection timed out" or "Error connecting to [instance], reason: -> Connection timed out: connect," You have confirmed that the network and security group rules are configured correctly and the instance is passing status checks. What steps should you take to identify the source of the behavior? **(Select 2.)**

- **A.** Verify that the private key file corresponds to the Amazon EC2 key pair assigned at launch.
- **B.** Verify that your federation trust to AWS has been established.
- **C.** Verify that your IAM user policy has permission to launch Amazon EC2 instances.
- **D.** Verify that you are connecting with the appropriate user name for your AMI.
- **E.** Verify that the Amazon EC2 Instance was launched with the proper IAM role.


**Q60.** Which of the following methods will allow an application using an AWS SDK to be authenticated as a principal to access AWS Cloud services? **(Select 2.)**

- **A.** Create an IAM user and store both parts of the access key for the user in the application’s configuration.
- **B.** Create an IAM user and store the user name and password for the user in the application’s configuration.
- **C.** Make all the API calls over an SSL connection.
- **D.** Run the application on an Amazon EC2 instance with an assigned IAM role.


**Q61.** Your company would like to restrict the ability of most users to change their own passwords whilst continuing to allow a select group of users within specific user groups. What is the best way to achieve this? **(Select 2.)**

- **A.** Under the IAM Password Policy deselect the option to allow users to change their own passwords
- **B.** Create an IAM Policy that grants users the ability to change their own password and attach it to the groups that contain the users
- **C.** Create an IAM Role that grants users the ability to change their own password and attach it to the groups that contain the users
- **D.** Disable the ability for all users to change their own passwords using the AWS Security Token Service


**Q62.** What are three recommended best practices when configuring Identity and Access Management (IAM) security services? **(Select 3.)**

- **A.** Remove unnecessary credentials
- **B.** Create an IAM user with administrator privileges
- **C.** IAM groups are not recommended for storage security
- **D.** share your password and/or access keys with members of your group only
- **E.** Lock or delete your root access keys when not required


**Q63.** Which of the following items are required to allow an application deployed on an EC2 instance to write data to a DynamoDB table? Assume that no security keys are allowed to be stored on the EC2 instance. **(Select 2.)**

- **A.** Launch an EC2 Instance with the IAM Role included in the launch configuration.
- **B.** Add an IAM User to a running EC2 instance.
- **C.** Add an IAM Role to a running EC2 instance.
- **D.** Create an IAM User that allows write access to the DynamoDB table.
- **E.** Create an IAM Role that allows write access to the DynamoDB table.


**Q64.** Your fortune 500 company has under taken a TCO analysis evaluating the use of Amazon S3 versus acquiring more hardware The outcome was that ail employees would be granted access to use Amazon S3 for storage of their personal documents. Which of the following will you need to consider so you can set up a solution that incorporates single sign-on from your corporate AD or LDAP directory and restricts access for each user to a designated user folder in a bucket? **(Select 3.)**

- **A.** Configuring IAM role
- **B.** Using AWS Security Token Service to generate temporary tokens
- **C.** Setting up a matching IAM user for every user in your corporate directory that needs
- **D.** Setting up a federation proxy or identity provider
- **E.** Tagging each folder in the bucket


**Q65.** A developer is writing some code and wants to work programmatically with IAM. Which feature of IAM allows you direct access to the IAM web service using HTTPS to call service actions and what is the method of authentication that must be used? **(Select 2.)**

- **A.** IAM role
- **B.** OpenID Connect
- **C.** Query API
- **D.** Access key ID and secret access key


**Q66.** A Solutions Architect is designing an authentication solution using the AWS STS that will provide temporary, limited-privilege credentials for IAM users or for users that you authenticate (federated users). What supported sources are available to the Architect for users? **(Select 2.)**

- **A.** OpenID Connect
- **B.** A local user on a user's PC
- **C.** EC2 instance
- **D.** Another AWS account


**Q67.** You are building a large order processing system and are responsible for securing the database. Which actions will you take to protect the data? **(Select 3.)**

- **A.** Install anti-virus software on the Amazon RDS DB Instance.
- **B.** Configure security groups and network Access Control Lists (ACLs) to limit network access.
- **C.** Adjust AWS Identity and Access Management (IAM) permissions for administrators.
- **D.** Configure database users, and grant permissions to database objects.


**Q68.** Your security team is very concerned about the vulnerability of the IAM administrator user accounts (the accounts used to configure all IAM features and accounts). What steps can be taken to lock down these accounts? **(Select 3.)**

- **A.** Add a CAPTCHA test to the accounts.
- **B.** Apply a source IP address condition to the policy that only grants permissions when the user is on the corporate network.
- **C.** Implement a password policy on the AWS account.
- **D.** Limit logins to a particular U.S. state.
- **E.** Add multi-factor authentication (MFA) to the accounts.


**Q69.** What two statements correctly describe how to add or modify IAM roles to a running EC2 instance? **(Select 2.)**

- **A.** Attach an IAM role to the user account and relaunch the EC2 instance
- **B.** Replace an IAM role attached to an existing EC2 instance from the EC2 console
- **C.** Add the EC2 instance to a group where the role is a member
- **D.** Attach an IAM role to an existing EC2 instance from the EC2 console


**Q70.** You want to grant the individuals on your network team the ability to fully manipulateAmazon EC2 instances. Which of the following accomplish this goal? (Choose 2answers) **(Select 2.)**

- **A.** Assign the managed policy, EC2FullAccess, to a group named NetworkTeam, and assign all the team members’ IAM user accounts to that group.
- **B.** Create a NetworkTeam IAM group, and have each team member log in to the AWS Management Console using the user name/password for the group.
- **C.** Create a new policy allowing EC2:* actions, and name the policy NetworkTeam.
- **D.** Create a new policy that grants EC2:* actions on all resources, and assign that policy to each individual’s IAM user account on the network team.


**Q71.** Which of the following are found in an IAM policy? **(Select 2.)**

- **A.** Region
- **B.** Password
- **C.** Service Name
- **D.** Action


## RDS Multi-AZ, Read Replicas & Aurora


**Q72.** Your AWS account administrator left your company today. The administrator had access to the root user and a personal IAM administrator account. With these accounts, he generated other IAM accounts and keys. Which of the following should you do today to protect your AWS infrastructure? **(Select 4.)**

- **A.** Put an IP restriction on the root user.
- **B.** Delete the administrator’s personal IAM account.
- **C.** Rotate keys and change passwords for IAM accounts.
- **D.** Change the password and add MFA to the root user.
- **E.** Delete all IAM accounts.
- **F.** Relaunch all Amazon EC2 instances with new roles.


## S3 Security, Access & Durability


**Q73.** You need to configure an Amazon S3 bucket to serve static assets for your public-facing web application. Which methods ensure that all objects uploaded to the bucket are set to public read? **(Select 2.)**

- **A.** Configure the bucket ACL to set all objects to public read.
- **B.** Amazon S3 objects default to public read, so no action is needed.
- **C.** Configure the bucket policy to set all objects to public read.
- **D.** Use AWS Identity and Access Management roles to set the bucket to public read.
- **E.** Set permissions on the object to public read during upload.


## VPC Security Groups & NACLs


**Q74.** How can you secure an Amazon ElastiCache cluster? **(Select 3.)**

- **A.** Restrict network access using a network Access Control List (ACL).
- **B.** Change the Memcached root password.
- **C.** Restrict network access using security groups.
- **D.** Restrict Application Programming Interface (API) actions using AWS Identity and Access Management (IAM) policies.


## EBS Volumes & Snapshots


**Q75.** What is required to copy an encrypted EBS snapshot cross-account? **(Select 2.)**

- **A.** Distribute the custom key from CloudFront
- **B.** Share the encrypted EBS snapshots publicly
- **C.** Share the custom key for the snapshot with the target account
- **D.** Copy the unencrypted EBS snapshot to an S3 bucket
- **E.** Enable root access security on both accounts
- **F.** Share the encrypted EBS snapshot with the target account


## Encryption & AWS KMS


**Q76.** What AWS feature is recommended for optimizing data security? **(Select 2.)**

- **A.** Federated LDAP
- **B.** Two-factor authentication
- **C.** SAML
- **D.** Username and encrypted password
- **E.** Multi-factor authentication


## Monitoring: CloudWatch, CloudTrail & Config


**Q77.** A customer needs corporate IT governance and cost oversight of all AWS resources consumed by its divisions. The divisions want to maintain administrative control of the discrete AWS resources they consume and keep those resources separate from the resources of other divisions. Which of the following options, when used together will support the autonomy/control of divisions while enabling corporate IT to maintain governance and cost oversight? **(Select 2.)**

- **A.** Create separate VPCs for each division within the corporate IT AWS account.
- **B.** Use AWS Consolidated Billing and disable AWS root account access for the child accounts.
- **C.** Enable IAM cross-account access for all corporate IT administrators in each child account.
- **D.** Use AWS Consolidated Billing to link the divisions' accounts to a parent corporate account
- **E.** Write all child AWS CloudTrail and Amazon CloudWatch logs to each child account's Amazon S3 'Log' bucket.


## Federation, SSO & Cognito


**Q78.** A company is preparing to give AWS Management Console access to developers Company policy mandates identity federation and role-based access control. Roles are currently assigned using groups in the corporate Active Directory. What combination of the following will give developers access to the AWS console? **(Select 2.)**

- **A.** AWS identity and Access Management roles
- **B.** AWS Directory Service AD Connector
- **C.** AWS identity and Access Management users
- **D.** AWS Identity and Access Management groups
- **E.** AWS Directory Service Simple AD


**Q79.** What are two primary similarities between AD Connector and Simple AD for cloud directory services? **(Select 2.)**

- **A.** AD Connector requires an on-premises ADS directory
- **B.** Simple AD is fully managed and setup in minutes
- **C.** Simple AD requires an on-premises ADS directory
- **D.** Simple AD is more scalable than AD Connector
- **E.** Simple AD provides enhanced integration with IAM


**Q80.** What are two primary differences between AD Connector and Simple AD for cloud directory services? **(Select 2.)**

- **A.** Simple AD provides enhanced integration with IAM
- **B.** Simple AD is fully managed and setup in minutes
- **C.** AD Connector requires an on-premises ADS directory
- **D.** Simple AD is more scalable than AD Connector
- **E.** Simple AD requires an on-premises ADS directory


**Q81.** Which of the following are based on temporary security tokens? **(Select 2.)**

- **A.** MFA
- **B.** Amazon EC2 roles
- **C.** Federation
- **D.** Root user


## Secrets, Parameters & Credentials


**Q82.** Which of the following are benefits of using Amazon EC2 roles? **(Select 2.)**

- **A.** Credentials do not need to be stored on the Amazon EC2 instance.
- **B.** No policies are required.
- **C.** Integration with Active Directory is automatic.
- **D.** Key rotation is not necessary.


## Threat Detection & Compliance


**Q83.** To improve security in your AWS account you have decided to enable multi-factor authentication (MFA). You can authenticate using an MFA device in which two ways? **(Select 2.)**

- **A.** Using a key pair
- **B.** Through the AWS Management Console
- **C.** Locally to EC2 instances
- **D.** Using the AWS API


## Elastic Beanstalk & Deployment


**Q84.** What configuration settings are required from the remote VPC in order to create cross-account peering? **(Select 3.)**

- **A.** CMK keys
- **B.** account username
- **C.** VPC ID
- **D.** account ID
- **E.** VPC CIDR block
- **F.** volume type


## Well-Architected & General Design


**Q85.** What are the best practices for account management within Amazon AWS? **(Select 3.)**

- **A.** Create a single AWS account with multiple IAM users that have root privilege
- **B.** Create multiple AWS accounts with multiple IAM users per AWS account
- **C.** Do not use root account for common administrative tasks
- **D.** Create multiple root user accounts for redundancy
- **E.** Use root account for all administrative tasks


---


# Answer Key & Explanations


**Q1. B**  
_IAM Roles, Policies & Permissions_  
An instance profile is a container for an IAM role that you can use to pass role information to an Amazon EC2 instance when the instance starts.

**Q2. B**  
_IAM Roles, Policies & Permissions_  
IAM makes it easy to provide multiple users secure access to your AWS resources. IAM enables you to - Manage IAM users and their access: You can create users in AWS's identity management system, assign users individual security credentials (such as access keys, passwords, multi- factor authentication devices), or request temporary security credentials to provide users access to AWS services and resources. You can specify permissions to control which operations a user can perform. Refer: https://aws.amazon.com/iam/faqs/

**Q3. A**  
_IAM Roles, Policies & Permissions_  
An instance profile is a container for an AWS Identity and Access Management (IAM) role that you can use to pass role information to an Amazon EC2 instance when the instance starts. The IAM role should have a policy attached that only allows access to the AWS Cloud services necessary to perform its function.

**Q4. C**  
_IAM Roles, Policies & Permissions_  
Refer: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_virtual.html

**Q5. D**  
_IAM Roles, Policies & Permissions_  
The AWS Security Token Service (STS) is a web service that enables you to request temporary, limited-privilege credentials for IAM users or for users that you authenticate (federated users). If your identity store is not compatible with SAML 2.0, then you can build a custom identity broker application to perform a similar function. The broker application authenticates users, requests temporary credentials for users from AWS, and then provides them to the user to access AWS resources You cannot create trust relationships between SimpleAD and IAM You cannot use references in an IAM policy to an on-premise AD SAML may not be supported by the on-premise LDAP directory so you would need to develop a custom IdP and use STS References: https://digitalcloud.training/certification-training/aws-solutions-architect-associate/security-identity-compliance/aws-iam/ https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.html

**Q6. D**  
_IAM Roles, Policies & Permissions_  
Cross-account access with a resource-based policy has some advantages over cross-account access with a role. With a resource that is accessed through a resource-based policy, the principal still works in the trusted account and does not have to give up his or her permissions to receive the role permissions. Refer: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_compare-resource-policies.html

**Q7. D**  
_IAM Roles, Policies & Permissions_  
Access keys are a combination of an access key ID and a secret access key and you can assign two active access keys to a user at a time. These can be used to make programmatic calls to AWS when using the API in program code or at a command prompt when using the AWS CLI or the AWS PowerShell tools A password is needed for logging into the console but not for making API calls to AWS services. Similarly you don't need to create a group and add the users to it to provide access to make API calls to AWS services Multi-factor authentication can be used to control access to AWS service APIs but the question is not asking how to better secure the calls but just being able to make them References: https://digitalcloud.training/certification- training/aws-solutions-architect-associate/security-identity-compliance/aws-iam/

**Q8. A**  
_IAM Roles, Policies & Permissions_  
In this scenario, the best option is to group the set of users in an IAM Group and then apply a policy with the required access to the Amazon S3 bucket. This will enable you to easily add, remove, and manage the users instead of manually adding a policy to each and every 100 IAM users.
- *Why not B:* This option is incorrect because you need to use an IAM Group and not an IAM role.
- *Why not C:* This option is incorrect because you need a new IAM Group and the method is also time-consuming.
- *Why not D:* This option is incorrect because you need a new IAM Group for this scenario and not assign a policy to each user via a shell script. This method can save you time but afterwards, it will be difficult to manage all 100 users that are not contained in an IAM Group.

**Q9. A**  
_IAM Roles, Policies & Permissions_  
An AWS account ID is a 12-digit number, such as 123456789012, that you use to construct Amazon Resource Names (ARNs). When you refer to resources, such as an IAM user or an S3 Glacier vault, the account ID distinguishes your resources from resources in other AWS accounts. Refer: https://docs.aws.amazon.com/general/latest/gr/acct-identifiers.html

**Q10. C**  
_IAM Roles, Policies & Permissions_  
The main difference between Amazon SQS policies and IAM policies is that an Amazon SQS policy enables you to grant a different AWS account permission to your Amazon SQS queues, but an IAM policy does not.

**Q11. D**  
_IAM Roles, Policies & Permissions_  
Link - http://docs.aws.amazon.com/IAM/latest/UserGuide/roles-usingrole-ec2instance.html

**Q12. D**  
_IAM Roles, Policies & Permissions_  
IAM Policy is a document that formally states one or more permissions. Refer:

**Q13. D**  
_IAM Roles, Policies & Permissions_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q14. C**  
_IAM Roles, Policies & Permissions_  
Every user you create in IAM starts with 'No permission'. One or more IAM users can be created in AWS account. IAM user can be created for someone who needs access to the AWS console, or when a new application is needed to make API calls to AWS.

**Q15. B**  
_IAM Roles, Policies & Permissions_  
Can enable Cross Origin Resource Sharing (CORS) for multiple domain use with Javascript/AJAX: - Can be used to enable requests from domains other the APIs domain - Allows the sharing of resources between different domains - The method (GET, PUT, POST etc) for which you will enable CORS must be available in the API Gateway API before you enable CORS - If CORS is not enabled and an API resource received requests from another domain the request will be blocked - Enable CORS on the APIs resources using the selected methods under the API Gateway IAM policies are not used to control CORS and there is no ACL on the API to update This error would display whether using SSL/TLS or not. References: https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-delivery/amazon-api-gateway/

**Q16. B**  
_IAM Roles, Policies & Permissions_  
Amazon EC2 uses publicñkey cryptography to encrypt and decrypt login information. Publicñkey cryptography uses a public key to encrypt a piece of data, such as a password, then the recipient uses the private key to decrypt the data. The public and private keys are known as a key pair. To log in to your instance, you must create a key pair, specify the name of the key pair when you launch the instance, and provide the private key when you connect to the instance. On a Linux instance, the public key content is placed in an entry within ~/.ssh/authorized_keys. This is done at boot time and enables you to securely access your instance using the private key instead of a password.

**Q17. C**  
_IAM Roles, Policies & Permissions_  
Pre-signed URLs allow you to grant time-limited permission to download objects from an Amazon Simple Storage Service (Amazon S3) bucket. Static web hosting generally requires world-read access to all content. AWS IAM policies do not know who the authenticated users of the web app are. Logging can help track content loss, but not prevent it.

**Q18. B**  
_IAM Roles, Policies & Permissions_  
Within the IAM service a GROUP is regarded as a A collection of AWS accounts. It's the group of EC2 machines that gain the permissions specified in the GROUP. There's no GROUP in IAM, but only USERS and RESOURCES. Refer: https://aws.amazon.com/iam/faqs/

**Q19. A**  
_IAM Roles, Policies & Permissions_  
You can enable only one MFA device per AWS account root user or IAM user. Refer: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable.html#:~:text=You%20can%20enable%20only%20one,root%20user%20or%20IAM%20user.

**Q20. C**  
_IAM Roles, Policies & Permissions_  
Refer: https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started.html

**Q21. D**  
_IAM Roles, Policies & Permissions_  
IAM permits users to have no more than two active access keys at one time.

**Q22. D**  
_IAM Roles, Policies & Permissions_  
An IAM policy is a JSON document.

**Q23. B**  
_IAM Roles, Policies & Permissions_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q24. A**  
_IAM Roles, Policies & Permissions_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q25. C**  
_IAM Roles, Policies & Permissions_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q26. A**  
_IAM Roles, Policies & Permissions_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q27. E**  
_IAM Roles, Policies & Permissions_  
You can delete your instance when you no longer need it. This is referred to as terminating your instance. As soon as the state of an instance changes to shutting-down or terminated, you stop incurring charges for that instance. You can't connect to or start an instance after you've terminated it. However, you can launch additional instances using the same AMI. Refer: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html

**Q28. C**  
_IAM Roles, Policies & Permissions_  
DNS uses port number 53 to serve requests.

**Q29. A**  
_S3 Security, Access & Durability_  
By default, an S3 object is owned by the account that uploaded the object. That's why granting the destination account the permissions to perform the cross-account copy makes sure that the destination owns the copied objects. You can also change the ownership of an object by changing its access control list (ACL) to bucket-owner-full-control. However, object ACLs can be difficult to manage for multiple objects, so it's a best practice to grant programmatic cross-account permissions to the destination account. Object ownership is important for managing permissions using a bucket policy. For a bucket policy to apply to an object in the bucket, the object must be owned by the account that owns the bucket. You can also manage object permissions using the object's ACL. However, object ACLs can be difficult to manage for multiple objects, so it's a best practice to use the bucket policy as a centralized method for setting permissions. To be sure that a destination account owns an S3 object copied from another account, grant the destination account the permissions to perform the cross- account copy. Follow these steps to configure cross-account permissions to copy objects from a source bucket in Account A to a destination bucket in Account B: - Attach a bucket policy to the source bucket in Account A. - Attach an AWS Identity and Access Management (IAM) policy to a user or role in Account B. - Use the IAM user or role in Account B to perform the cross-account copy.
- *Why not B:* This option is incorrect because CORS simply defines a way for client web applications that are loaded in one domain to interact with resources in a different domain, and not on a different AWS account.
- *Why not C:* This option is incorrect because Amazon WorkDocs is commonly used to easily collaborate, share content, provide rich feedback, and collaboratively edit documents with other users. There is no direct way for you to integrate WorkDocs and an Amazon S3 bucket owned by a different AWS account. A better solution here is to use cross-account permissions in S3 to meet the requirement.
- *Why not D:* This option is incorrect because the Requester Pays feature is primarily used if you want the requester, instead of the bucket owner, to pay the cost of the data transfer request and download from the S3 bucket. This solution lacks the necessary IAM Permissions to satisfy the requirement. The most suitable solution here is to configure cross-account permissions in S3.

**Q30. E**  
_S3 Security, Access & Durability_  
Amazon S3 server access logs store a record of what requestor accessed the objects in your bucket, including the requesting IP address

**Q31. B**  
_S3 Security, Access & Durability_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q32. D**  
_RDS Multi-AZ, Read Replicas & Aurora_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q33. A**  
_RDS Multi-AZ, Read Replicas & Aurora_  
To change a user's name or path, you must use the AWS CLI, Tools for Windows PowerShell, or AWS API. There is no option in the console to rename a user. Refer: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_manage.html

**Q34. D**  
_VPC Security Groups & NACLs_  
A security principle is a-crum_add_start--->

**Q35. C**  
_VPC Security Groups & NACLs_  
If your private key can be read or written to by anyone but you, then SSH ignores your key.

**Q36. A**  
_Auto Scaling & Elastic Load Balancing_  
Elastic Load Balancing provides APIs that you can call by submitting a Query request. Query requests are HTTP or HTTPS requests that use the HTTP verb GET or POST and a Query parameter named Action or Operation that specifies the API you are calling. Refer: https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/using-query-api.html

**Q37. D**  
_EC2 Instances, AMIs & Placement_  
Windows AMIs for Windows Server 2012 R2 and earlier include an optional service, the EC2Config service ( EC2Config.exe ). EC2Config starts when the instance boots and performs tasks during startup and each time you stop or start the instance. EC2Config can also perform tasks on demand. Refer: https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ec2config-service.html

**Q38. A**  
_EC2 Instances, AMIs & Placement_  
If an instance reboots (intentionally or unintentionally), data in the instance store persists. ... The instance stops. The instance terminates. Refer: If an instance reboots (intentionally or unintentionally), data in the instance store persists. The instance stops. The instance terminates.

**Q39. C**  
_EC2 Instances, AMIs & Placement_  
An Elastic IP address doesn’t incur charges as long as all the following conditions are true: The Elastic IP address is associated with an EC2 instance. The instance associated with the Elastic IP address is running. The instance has only one Elastic IP address attached to it. Note: If the address is from a BYOIP address pool, you're never charged for that address. Refer: https://aws.amazon.com/premiumsupport/knowledge-center/elastic-ip-charges/

**Q40. D**  
_CloudFront & Edge Delivery_  
Amazon CloudFront OAI is a special identity that can be used to restrict access to an Amazon S3 bucket only to an Amazon CloudFront distribution. Signed URLs, signed cookies, and IAM bucket policies can help to protect content served through Amazon CloudFront, but OAIs are the simplest way to ensure that only Amazon CloudFront has access to a bucket.

**Q41. B**  
_Encryption & AWS KMS_  
The administrator password is encrypted with the public key of the key pair, and you provide the private key to decrypt the password. Then log in to the instance as the administrator with the decrypted password.

**Q42. A**  
_Monitoring: CloudWatch, CloudTrail & Config_  
Amazon CloudWatch is a monitoring service for AWS Cloud resources and the applications organizations run on AWS. It allows organizations to collect and track metrics, collect and monitor log files, and set alarms. AWS IAM, Amazon SNS, and AWS CloudFormation do not provide visibility into resource utilization, application performance, and the operational health of your AWS resources.

**Q43. D**  
_Monitoring: CloudWatch, CloudTrail & Config_  
To collect logs from your Amazon EC2 instances and on-premises servers into CloudWatch Logs, AWS offers two options: Recommended – The unified CloudWatch agent. It enables you to collect both logs and advanced metrics with one agent. It offers support across operating systems, including servers running Windows Server. Refer: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_GettingStarted.html

**Q44. C**  
_Federation, SSO & Cognito_  
With the AWS Active Directory Service for Microsoft Active Directory you can setup trust relationships to extend authentication from on- premises Active Directories into the AWS cloud. You can also use Active Directory credentials to authenticate to the AWS management console without having to set up SAML authentication. It is a fully managed AWS service on AWS infrastructure and is the best choice if you have more than 5000 users and/or need a trust relationship set up. You could install a Microsoft AD DC on an EC2 instance and add it to the existing domain. However, you would then have to setup federation / SAML infrastructure for SSO. This is not therefore the simplest solution AWS Simple AD does not support trust relationships or synchronisation with Active Directory AD Connector would be a good solution for this use case however only supports up to 5,000 users. References: https://digitalcloud.training/certification-training/aws-solutions-architect-associate/security-identity-compliance/aws-directory-service/

**Q45. A**  
_Federation, SSO & Cognito_  
Simple AD is an inexpensive Active Directory-compatible service with common directory features. It is a standalone, fully managed, directory on the AWS cloud and is generally the least expensive option. It is the best choice for less than 5000 users and when you don’t need advanced AD features Active Directory Service for Microsoft Active Directory is the best choice if you have more than 5000 users and/or need a trust relationship set up. It provides advanced AD features that you don't get with SimpleAD Amazon Cognito is an authentication service for web and mobile apps AWS Single Sign- On (SSO) is a cloud SSO service that makes it easy to centrally manage SSO access to multiple AWS accounts and business applications References: https://digitalcloud.training/certification-training/aws-solutions-architect-associate/security-identity-compliance/aws-directory-service/

**Q46. A**  
_Federation, SSO & Cognito_  
AWS Simple AD is an inexpensive Active Directory-compatible service with common directory features. It is a standalone, fully managed, directory on the AWS cloud. Simple AD is generally the least expensive option and the best choice for less than 50000 users and don’t need advanced AD features. It is powered by SAMBA 4 Active Directory compatible server AD Connector is a directory gateway for redirecting directory requests to an Active Directory service. As you only require simple features and are looking for cost-effectiveness this would not be the best option as you must maintain an Active Directory service The AWS Directory Service for Microsoft AD is a fully managed AWS service on AWS infrastructure.It is the best choice if you have more than 5000 users and/or need a trust relationship set up. In this case you don't need those features and it would be more expensive so isn't the best options Amazon Cloud Directory enables you to build flexible cloud-native directories for organizing hierarchies of data along multiple dimensions, it is not used for authentication use cases. References: https://digitalcloud.training/certification-training/aws-solutions-architect-associate/security-identity- compliance/aws-directory-service/

**Q47. A**  
_Federation, SSO & Cognito_  
AWS Identity and Access Management (IAM) supports identity federation, which enables external identities, such as users in your corporate directory, to sign in to the AWS Management Console via single sign-on (SSO). Refer: https://aws.amazon.com/blogs/security/tag/web-identity-federation/

**Q48. C**  
_Federation, SSO & Cognito_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q49. E**  
_Federation, SSO & Cognito_  
_See the matching section of this task's `notes.md` for the underlying concept._
- *Why not C:* Refer: https://aws.amazon.com/identity/federation

**Q50. B**  
_Federation, SSO & Cognito_  
Direct Connect is an incorrect option as it can take months to provision and a quick resolution has been requested The best answer is to Install an additional Microsoft Active Directory Domain Controller for your existing domain on EC2: - When you build your own you can join an existing on- premise Active Directory domain/directory (replication mode) - You must establish a VPN (on top of Direct Connect if you have it) - Replication mode is less secure than establishing trust relationships AWS Microsoft AD does not support replication mode where replication to an on-premise AD takes place The option to use the AWS Active Directory Service for Microsoft Active Directory and create a new domain is incorrect as it involves creating a new directory which the administrators don't want. References: https://digitalcloud.training/certification-training/aws-solutions-architect-associate/security-identity- compliance/aws-directory-service/

**Q51. A**  
_Federation, SSO & Cognito_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q52. D**  
_Federation, SSO & Cognito_  
Refer: https://aws.amazon.com/iam/

**Q53. B**  
_Federation, SSO & Cognito_  
You can use MFA with a Cognito user pool (not in IAM) and this satisfies the requirement. A user pool is a user directory in Amazon Cognito. With a user pool, your users can sign in to your web or mobile app through Amazon Cognito. Your users can also sign in through social identity providers like Facebook or Amazon, and through SAML identity providers Integrating IAM with a Cognito user pool or integrating a 3rd party IdP does not add another factor of authentication - "factors" include something you know (e.g. password), something you have (e.g. token device), and something you are (e.g. retina scan or fingerprint) References: https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-mfa.html

**Q54. B**  
_Secrets, Parameters & Credentials_  
There's no method in the IAM system to allow or deny access to the operating system of a specific instance. IAM does allow access to specific instance.

**Q55. A**  
_General Design_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q56. D**  
_Well-Architected & General Design_  
If you want to define more than one permission for an entity (user or role), you can use multiple statements in a single policy. You can also attach multiple policies. If you try to define multiple permissions in a single statement, your policy might not grant the access that you expect. As a best practice, break up policies by resource type. https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html

**Q57. B, C**  
_IAM Roles, Policies & Permissions_  
Best practices for securing operating systems and applications include: Disable root API access keys and secret key Restrict access to instances from limited IP ranges using Security Groups Password protect the .pem file on user machines Delete keys from the authorized_keys file on your instances when someone leaves your organization or no longer requires access Rotate credentials (DB, Access Keys) Regularly run least privilege checks using IAM user Access Advisor and IAM user Last Used Access Keys Use bastion hosts to enforce control and visibility References: https://d1.awsstatic.com/whitepapers/Security/AWS_Security_Best_Practices.pdf

**Q58. A, C, E**  
_IAM Roles, Policies & Permissions_  
You should protect AWS user access keys like you would your credit card numbers or any other sensitive secret. Use different access keys for different applications so that you can isolate the permissions and revoke the access keys for individual applications if an access key is exposed. Remember to change access keys on a regular basis. For increased security, it is recommended to configure MFA for any sensitive operations. Remember to remove any IAM users that are no longer needed.

**Q59. A, D**  
_IAM Roles, Policies & Permissions_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q60. A, D**  
_IAM Roles, Policies & Permissions_  
Programmatic access is authenticated with an access key, not with user names/passwords. IAM roles provide a temporary security token to an application using an SDK.

**Q61. A, B**  
_IAM Roles, Policies & Permissions_  
A password policy can be defined for enforcing password length, complexity etc. (applies to all users) You can allow or disallow the ability to change passwords using an IAM policy and you should attach this to the group that contains the users, not to the individual users themselves You cannot use an IAM role to perform this function The AWS STS is not used for controlling password policies. References: https://digitalcloud.training/certification- training/aws-solutions-architect-associate/security-identity-compliance/aws-iam/

**Q62. B, D, E**  
_IAM Roles, Policies & Permissions_  
Refer: https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html

**Q63. A, E**  
_IAM Roles, Policies & Permissions_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q64. B, D, E**  
_IAM Roles, Policies & Permissions_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q65. C, D**  
_IAM Roles, Policies & Permissions_  
AWS recommend that you use the AWS SDKs to make programmatic API calls to IAM. However, you can also use the IAM Query API to make direct calls to the IAM web service. An access key ID and secret access key must be used for authentication when using the Query API OpenID Connect is a provider for connecting external directories API gateway is a separate service for accepting and processing API calls An IAM role is not used for authentication to the Query API References: https://digitalcloud.training/certification-training/aws-solutions-architect-associate/security-identity- compliance/aws-iam/

**Q66. A, D**  
_IAM Roles, Policies & Permissions_  
The AWS Security Token Service (STS) is a web service that enables you to request temporary, limited-privilege credentials for IAM users or for users that you authenticate (federated users) Federation can come from three sources: - Federation (typically AD) - Federation with Mobile Apps (e.g. Facebook, Amazon, Google or other Open ID providers) - Cross account access (another AWS account) The question has asked for supported sources for users. Cognito user pools contain users, but identity pools do not You cannot use STS with local users on a PC or an EC2 instance References: https://digitalcloud.training/certification-training/aws-solutions-architect-associate/security-identity-compliance/aws-iam/

**Q67. B, C, D**  
_IAM Roles, Policies & Permissions_  
Protecting your database requires a multilayered approach that secures the infrastructure, the network, and the database itself. Amazon RDS is a managed service and direct access to the OS is not available.

**Q68. B, C, E**  
_IAM Roles, Policies & Permissions_  
Neither B nor E are features supported by IAM.

**Q69. B, D**  
_IAM Roles, Policies & Permissions_  
Attaching an IAM role to an instance To attach an IAM role to an instance that has no role, the instance can be in the stopped or running state. To attach an IAM role to an instance (console) Open the Amazon EC2 console at https://console.amazonaws.cn/ec2/. In the navigation pane, choose Instances. Select the instance, choose Actions, Instance Settings, Attach/Replace IAM role. Select the IAM role to attach to your instance, and choose Apply. Refer: https://docs.amazonaws.cn/en_us/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html To replace the IAM role on an instance that already has an attached IAM role, the instance must be in the running state. You can do this if you want to change the IAM role for an instance without detaching the existing one first. For example, you can do this to ensure that API actions performed by applications running on the instance are not interrupted. To replace an IAM role for an instance (console) Open the Amazon EC2 console at https://console.amazonaws.cn/ec2/. In the navigation pane, choose Instances. Select the instance, choose Actions, Instance Settings, Attach/Replace IAM role. Select the IAM role to attach to your instance, and choose Apply. Refer: https://docs.amazonaws.cn/en_us/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html

**Q70. A, D**  
_IAM Roles, Policies & Permissions_  
Access requires an appropriate policy associated with a principal. Response A is merely a policy with no principal, and response D is not a principal as IAM groups do not have user names and passwords. Response B is the best solution; response C will also work but it is much harder to manage.

**Q71. C, D**  
_IAM Roles, Policies & Permissions_  
IAM policies are independent of region, so no region is specified in the policy. IAM policies are about authorization for an already- authenticated principal, so no password is needed.

**Q72. A, B, C, D**  
_RDS Multi-AZ, Read Replicas & Aurora_  
Locking down your root user and all accounts to which the administrator had access is the key here. Deleting all IAM accounts is not necessary, and it would cause great disruption to your operations. Amazon EC2 roles use temporary security tokens, so relaunching Amazon EC2 instances is not necessary.

**Q73. C, E**  
_S3 Security, Access & Durability_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q74. A, C, D**  
_VPC Security Groups & NACLs_  
Limit access at the network level using security groups or network ACLs, and limit infrastructure changes using IAM.

**Q75. C, F**  
_EBS Volumes & Snapshots_  
Cross-Account Copying To create a copy of the encrypted EBS snapshot in another account you need to complete four simple steps: 1. Share the custom key associated with the snapshot with the target account. 2. Share the encrypted EBS snapshot with the target account. 3. In the context of the target account, locate the shared snapshot and make a copy of it. 4. Use the newly created copy to create a new volume. Refer: https://aws.amazon.com/blogs/aws/new-cross-account-copying-of-encrypted-ebs- snapshots/#:~:text=To%20create%20a%20copy%20of,snapshot%20with%20the%20target%20account.&text=In%20the%20context%20of%20the,to%20create%20a%20new%20volu

**Q76. C, D**  
_Encryption & AWS KMS_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q77. D, E**  
_Monitoring: CloudWatch, CloudTrail & Config_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q78. A, B**  
_Federation, SSO & Cognito_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q79. A, C**  
_Federation, SSO & Cognito_  
AD Connector simply connects your existing on-premises Active Directory to AWS. AD Connector is your best choice when you want to use your existing on-premises directory with AWS services. Simple AD is an inexpensive Active Directory–compatible service with the common directory features. In most cases, Simple AD is the least expensive option and your best choice if you have 5,000 or fewer users and don’t need the more advanced Microsoft Active Directory features. https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_connector_best_practices.html https://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html

**Q80. C, E**  
_Federation, SSO & Cognito_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q81. B, C**  
_Federation, SSO & Cognito_  
Amazon EC2 roles provide a temporary token to applications running on the instance; federation maps policies to identities from other sources via temporary tokens.

**Q82. A, D**  
_Secrets, Parameters & Credentials_  
Amazon EC2 roles must still be assigned a policy. Integration with Active Directory involves integration between Active Directory and IAM via SAML.

**Q83. B, D**  
_Threat Detection & Compliance_  
You can authenticate using an MFA device in the following ways: Through the AWS Management Console – the user is prompted for a user name, password and authentication code Using the AWS API – restrictions are added to IAM policies and developers can request temporary security credentials and pass MFA parameters in their AWS STS API requests Using the AWS CLI by obtaining temporary security credentials from STS (aws sts get-session-token). References: https://digitalcloud.training/certification-training/aws-solutions-architect-associate/security-identity- compliance/aws-iam/

**Q84. C, D, E**  
_Elastic Beanstalk & Deployment_  
You need a peer VPC ID, a peer AWS account ID, and a cross-account access role for the peering connection. Refer: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/peer-with-vpc-in-another-account.html

**Q85. B, C, E**  
_Well-Architected & General Design_  
_See the matching section of this task's `notes.md` for the underlying concept._
