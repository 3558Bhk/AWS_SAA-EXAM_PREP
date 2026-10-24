# Task 1.3 - Determine Appropriate Data Security Controls - Practice Questions

> **Domain 1 - Design Secure Architectures (30%)**  
> Curated from 18 practice sets: duplicates removed, outdated items retired, ordered **highest-frequency exam topics first**.  
> **35 multiple-choice (single answer)** followed by **18 multiple-response (select 2+)**. Total **53**.


**Topic order in this file:** IAM Roles, Policies & Permissions → RDS Multi-AZ, Read Replicas & Aurora → Encryption & AWS KMS → EBS Volumes & Snapshots → High Availability & Fault Tolerance → Monitoring: CloudWatch, CloudTrail & Config → AWS Organizations & Multi-Account → Threat Detection & Compliance → General Design → S3 Security, Access & Durability → S3 Storage Classes & Lifecycle → Cost Management & Optimization Tools


---


# Section A - Multiple Choice (one correct answer)


## IAM Roles, Policies & Permissions


**Q1.** An AWS customer is deploying an application mat is composed of an AutoScaling group of EC2 Instances. The customers security policy requires that every outbound connection from these instances to any other service within the customers Virtual Private Cloud must be authenticated using a unique x 509 certificate that contains the specific instance-id. In addition an x 509 certificates must Designed by the customer's Key management service in order to be trusted for authentication. Which of the following configurations will support these requirements?

- **A.** Configure the Auto Scaling group to send an SNS notification of the launch of a new instance to the trusted key management service. Have the Key management service generate a signed certificate and send it directly to the newly launched instance.
- **B.** Configure an IAM Role that grants access to an Amazon S3 object containing a signed certificate and configure me Auto Scaling group to launch instances with this role Have the instances bootstrap get the certificate from Amazon S3 upon first boot.
- **C.** Configure the launched instances to generate a new certificate upon first boot Have the Key management service poll the AutoScaling group for associated instances and send new instances a certificate signature (hat contains the specific instance-id.
- **D.** Embed a certificate into the Amazon Machine Image that is used by the Auto Scaling group Have the launched instances generate a certificate signature request with the instance's assigned instance-id to the Key management service for signature.


**Q2.** A Linux instance running in your VPC requires some configuration changes to be implemented locally and you need to run some commands. Which of the following can be used to securely connect to the instance?

- **A.** SSL/TLS certificate
- **B.** Public key
- **C.** Key pairs
- **D.** EC2 password


## RDS Multi-AZ, Read Replicas & Aurora


**Q3.** You can modify the backup retention period; valid values are 0 (for no backup retention) to a maximum of ___________ days.

- **A.** 35
- **B.** 15
- **C.** 45
- **D.** 5


**Q4.** Amazon RDS creates an SSL certificate and installs the certificate on the DB Instance when Amazon RDS provisions the instance. These certificates are signed by a certificate authority. The _____ is stored athttps://rds.amazonaws.com/doc/rds-ssl-ca-cert.pem.

- **A.** protected key
- **B.** public key
- **C.** private key
- **D.** foreign key


## Encryption & AWS KMS


**Q5.** A company needs to launch an Amazon EC2 instance with a persistent block storage to host its application. The stored data must be encrypted at rest. Which of the following is the most suitable storage solution in this scenario?

- **A.** Amazon EBS volume with server-side encryption (SSE) enabled.
- **B.** Amazon EC2 Instance Store with SSL encryption.
- **C.** Encrypted Amazon EC2 Instance Store using AWS KMS.
- **D.** Encrypted Amazon EBS volume using AWS KMS.


**Q6.** Which cryptographic method is used by AWS Key Management Service (AWS KMS) to encrypt data?

- **A.** Shared secret
- **B.** Envelope encryption
- **C.** Password-based encryption
- **D.** Asymmetric


**Q7.** Your company requires that all data sent to external storage be encrypted before being sent. Which Amazon Simple Storage Service (Amazon S3) encryption solution will meet this requirement?

- **A.** Server-side encryption with AWS Key Management Service (AWS KMS) keys (SSEKMS)
- **B.** Client-side encryption with customer-managed keys
- **C.** Server-Side Encryption (SSE) with AWS-managed keys (SSE-S3)
- **D.** SSE with customer-provided keys (SSE-C)


**Q8.** An existing application stores sensitive information on a non-boot Amazon EBS data volume attached to an Amazon Elastic Compute Cloud instance. Which of the following approaches would protect the sensitive data on an Amazon EBS volume?

- **A.** Snapshot the current Amazon EBS volume. Restore the snapshot to a new, encrypted Amazon EBS volume. Mount the Amazon EBS volume
- **B.** Unmount the EBS volume. Toggle the encryption attribute to True. Re-mount the Amazon EBS volume.
- **C.** Create and mount a new, encrypted Amazon EBS volume. Move the data to the new volume. Delete the old Amazon EBS volume.
- **D.** Upload your customer keys to AWS CloudHSM. Associate the Amazon EBS volume with AWS CloudHSM. Re-mount the Amazon EBS volume.


**Q9.** How can you secure data at rest on an EBS volume?

- **A.** Create an IAM policy that restricts read and write access to the volume.
- **B.** Use an encrypted file system on top of the EBS volume.
- **C.** Attach the volume to an instance using EC2's SSL interface.
- **D.** Write the data randomly instead of sequentially.
- **E.** Encrypt the volume using the S3 server-side encryption service.


**Q10.** Which of the following describes the scheme used by an Amazon Redshift cluster leveraging AWS Key Management Service (AWS KMS) to encrypt data-at-rest?

- **A.** Amazon Redshift uses a one-tier, key-based architecture for encryption.
- **B.** Amazon Redshift uses a two-tier, key-based architecture for encryption.
- **C.** Amazon Redshift uses a four-tier, key-based architecture for encryption.
- **D.** Amazon Redshift uses a three-tier, key-based architecture for encryption.


**Q11.** Which encryption algorithm is used by Amazon Simple Storage Service (Amazon S3) to encrypt data at rest with Service- Side Encryption (SSE)?

- **A.** RSA 2048
- **B.** Advanced Encryption Standard (AES)-256
- **C.** RSA 1024
- **D.** AES-128


**Q12.** What statement correctly describes support for AWS encryption of S3 objects?

- **A.** Client-side encryption of S3 objects is not supported
- **B.** SSLis only supported with Glacier storage
- **C.** S3 buckets are encrypted only
- **D.** Tenants manage encryption for server-side encryption of S3 objects
- **E.** Amazon S3 batch operation manages encryption for server-side encryption of S3 objects


**Q13.** While signing in REST/ Query requests, for additional security, you should transmit your requests using Secure Sockets Layer (SSL) by using _________

- **A.** Internet Protocol Security(IPsec)
- **B.** TLS (Transport Layer Security)
- **C.** HTTP
- **D.** HTTPS


**Q14.** Which set of Amazon S3 features helps to prevent and recover from accidental data loss?

- **A.** Object versioning and Multi-factor authentication
- **B.** Object lifecycle and service access logging
- **C.** Website hosting and Amazon S3 policies
- **D.** Access controls and server-side encryption


**Q15.** What does the "Server Side Encryption" option on Amazon S3 provide?

- **A.** It encrypts the files that you send to Amazon S3, on the server side.
- **B.** It doesn't exist for Amazon S3, but only for Amazon EC2.
- **C.** It allows to upload files using an SSL endpoint, for a secure transfer.
- **D.** It provides an encrypted virtual disk in the Cloud.


**Q16.** Your company has started using the AWS CloudHSM for secure key storage. A recent administrative error resulted in the loss of credentials to access the CloudHSM. You need access to data that was encrypted using keys stored on the hardware security module. How can you recover the keys that are no longer accessible?

- **A.** There is no way to recover your keys if you lose your credentials
- **B.** Reset the CloudHSM device and create a new set of credentials
- **C.** Restore a snapshot of the CloudHSM
- **D.** Log a case with AWS support and they will use MFA to recover the credentials


**Q17.** Which security scheme is used by the AWS Multi-Factor Authentication (AWS MFA) token?

- **A.** Perfect Forward Secrecy (PFC)
- **B.** Time-Based One-Time Password (TOTP)
- **C.** Ephemeral Diffie Hellman (EDH)
- **D.** Split-Key Encryption (SKE)


**Q18.** Which technology does Amazon WorkSpaces use to provide data security?

- **A.** Secure Sockets Layer (SSL)/Transport Layer Security (TLS)
- **B.** PC-over-IP (PCoIP)
- **C.** AES-128
- **D.** Advanced Encryption Standard (AES)-256


**Q19.** Which of the following is the security protocol supported by Amazon VPC?

- **A.** Point-to-Point Tunneling Protocol (PPTP)
- **B.** SSH
- **C.** IPsec
- **D.** Advanced Encryption Standard (AES)


## EBS Volumes & Snapshots


**Q20.** Which is an operational process performed by AWS for data security?

- **A.** Replication of data across multiple AWS regions
- **B.** Secure wiping of Amazon EBS data when an Amazon EBS volume is unmounted
- **C.** Background virus scans of Amazon Elastic Block Store (Amazon EBS) volumes and Amazon EBS snapshots
- **D.** Advanced Encryption Standard (AES)-256 encryption of data stored on any shared storage device
- **E.** Decommissioning of storage devices using industry-standard practices


**Q21.** How are snapshots for an EBS volume created when it is the root device for an instance?

- **A.** Unencrypt volume and snapshot dynamically
- **B.** Pause instance, unmount volume and snapshot
- **C.** Terminate instance and snapshot
- **D.** Stop instance, unmount volume and snapshot


**Q22.** One of your EC2 instances runs an application process that saves user data to an attached EBS volume. The EBS volume was attached to the EC2 instance after it was launched and is unencrypted. You would like to encrypt the data that is stored on the volume as it is considered sensitive however you cannot shutdown the instance due to other application processes that are running. What is the best method of applying encryption to the sensitive data without any downtime?

- **A.** Create and mount a new encrypted EBS volume. Move the data to the new volume and then delete the old volume
- **B.** Unmount the volume and enable server-side encryption. Re-mount the EBS volume
- **C.** Create an encrypted snapshot of the current EBS volume. Restore the snapshot to the EBS volume
- **D.** Leverage the AWS Encryption CLI to encrypt the data on the volume


## High Availability & Fault Tolerance


**Q23.** You are a Solutions Architect at Digital Cloud Training. One of your clients has requested that you design a solution for distributing load across a number of EC2 instances across multiple AZs within a region. Customers will connect to several different applications running on the client’s servers through their browser using multiple domain names and SSL certificates. The certificates are stored in AWS Certificate Manager (ACM). What is the optimal architecture to ensure high availability, cost effectiveness, and performance?

- **A.** Launch a single ALB and bind multiple SSL certificates to the same secure listener. Clients will use the Server Name Indication (SNI) extension
- **B.** Launch multiple ALBs and bind separate SSL certificates to each ELB
- **C.** Launch a single ALB and bind multiple SSL certificates to multiple secure listeners
- **D.** Launch a single ALB, configure host-based routing for the domain names and bind an SSL certificate to each routing rule


**Q24.** You want to host multiple Hypertext Transfer Protocol Secure (HTTPS) websites on a fleet of Amazon EC2 instances behind an Elastic Load Balancing load balancer with a single X.509 certificate. How must you configure the Secure Sockets Layer (SSL) certificate so that clients connecting to the load balancer are not presented with a warning when they connect?

- **A.** Create multiple SSL certificates with a SAN value for each website name.
- **B.** Create one SSL certificate with the Server Name Indication (SNI) value checked.
- **C.** Create one SSL certificate with a Subject Alternative Name (SAN) value for each website name.
- **D.** Create SSL certificates for each Availability Zone with a SAN value for each website name.


## Monitoring: CloudWatch, CloudTrail & Config


**Q25.** How does Amazon AWS isolate metrics from different applications for monitoring, store and reporting purposes?

- **A.** Beanstalk
- **B.** EC2 instances
- **C.** CloudTrail
- **D.** Docker
- **E.** namespaces


**Q26.** You are working for a startup company that has resources deployed on the AWS Cloud. Your company is now going through a set of scheduled audits by an external auditing firm for compliance. Which of the following services available in AWS can be utilized to help ensure the right information are present for auditing purposes?

- **A.** Amazon CloudWatch
- **B.** AWS CloudTrail
- **C.** Amazon EC2
- **D.** Amazon VPC


**Q27.** Your company is reviewing their information security processes. One of the items that came out of a recent audit is that there is insufficient data recorded about requests made to a few S3 buckets. The security team requires an audit trail for operations on the S3 buckets that includes the requester, bucket name, request time, request action, and response status. Which action would you take to enable this logging?

- **A.** Enable S3 event notifications for the specific actions and setup an SNS notification
- **B.** Create a CloudWatch metric that monitors the S3 bucket operations and triggers an alarm
- **C.** Create a CloudTrail trail that audits S3 bucket operations
- **D.** Enable server access logging for the S3 buckets to save access logs to a specified destination bucket


**Q28.** While performing the volume status checks, if the status is insufficient-data, what does it mean?

- **A.** The checks may still be in progress on the volume
- **B.** The check has failed
- **C.** The check has passed


## AWS Organizations & Multi-Account


**Q29.** How can you connect to a new Linux instance using SSH?

- **A.** Using the private half of the instance’s key pair
- **B.** Using a certificate
- **C.** Using Multi-Factor Authentication (MFA)
- **D.** Decrypt the root password.


## Threat Detection & Compliance


**Q30.** Which of the following statements is true when it comes to the risk and compliance advantages of the AWS environment?

- **A.** The critical components of a workload must be moved entirely into the AWS Cloud in order to be compliant with various certifications and third-party attestations, but the non-critical components do not.
- **B.** Workloads must be moved entirely into the AWS Cloud in order to be compliant with various certifications and third-party attestations.
- **C.** Few, many, or all components of a workload can be moved to the AWS Cloud, but it is the customer’s responsibility to ensure that their entire workload remains compliant with various certifications and third-party attestations.
- **D.** The non-critical components of a workload must be moved entirely into the AWS Cloud in order to be compliant with various certifications and third- party attestations, but the critical components do not.


**Q31.** Which of the following is NOT a recommended approach for customers trying to achieve strong compliance and governance over an entire IT control environment?

- **A.** Take a holistic approach: review information available from AWS together with all other information, and document all compliance requirements.
- **B.** Verify that all control objectives are met and all key controls are designed and operating effectively.
- **C.** Identify and document controls owned by all third parties.
- **D.** Implement generic control objectives that are not specifically designed to meet their organization’s compliance requirements.


**Q32.** AWS provides IT control information to customers in which of the following ways?

- **A.** By using specific control definitions or through SAS 70
- **B.** By using specific control definitions or through general control standard compliance
- **C.** By complying with ISO 27001 and SOC 1 Type II
- **D.** By using general control standard compliance and by complying with ISO 27001


## General Design


**Q33.** The AWS control environment is in place for the secure delivery of AWS Cloud service offerings. Which of the following does the collective control environment NOT explicitly include?

- **A.** Energy
- **B.** Technology
- **C.** Processes
- **D.** People


**Q34.** The Amazon EC2 web service can be accessed using the _____ web services messaging protocol. This interface is described by a Web Services Description Language (WSDL) document.

- **A.** SOAP
- **B.** CORBA
- **C.** DCOM
- **D.** XML-RPC


**Q35.** Amazon EC2 provides a repository of public data sets that can be seamlessly integrated into AWS cloud-based applications.What is the monthly charge for using the public data sets?

- **A.** 1$ per dataset per month
- **B.** A 1 time charge of 10$ for all the datasets.
- **C.** 10$ per month for all the datasets
- **D.** There is no charge for using the public data sets


# Section B - Multiple Response (select all that apply)


## S3 Security, Access & Durability


**Q36.** Your application stores critical data in Amazon Simple Storage Service (Amazon S3), which must be protected against inadvertent or intentional deletion. How can this data be protected? **(Select 2.)**

- **A.** Use cross-region replication to copy data to another bucket automatically.
- **B.** Use a lifecycle policy to migrate data to Amazon Glacier.
- **C.** Enable MFA Delete on the bucket.
- **D.** Enable versioning on the bucket.
- **E.** Set a vault lock.


**Q37.** What two statements correctly describe versioning for protecting data at rest on S3 buckets? **(Select 2.)**

- **A.** Restores deleted files
- **B.** Enabled by default
- **C.** disabled by default
- **D.** Saves multiple versions of a single file
- **E.** Overwrites most current file version


## S3 Storage Classes & Lifecycle


**Q38.** Your company uses Amazon Glacier to store files that must be retained for compliance reasons and are rarely accessed. An auditor has requested access to some information that is stored in a Glacier archive. You have initiated an archive retrieval job. Which factors are important to know about the process from this point? **(Select 2.)**

- **A.** Following retrieval, you have 24 hours to download your data
- **B.** The retrieved data will always be encrypted
- **C.** There is a charge if you delete data within 90 days
- **D.** Amazon Glacier must complete a job before you can get its output


**Q39.** What statement correctly describes the operation of AWS Glacier archive? **(Select 2.)**

- **A.** archive supports single and aggregated files
- **B.** Archive is an unencrypted vault
- **C.** Archive supports aggregated files only
- **D.** Archive is a group of vaults
- **E.** Maximum file size is 1 TB


## Encryption & AWS KMS


**Q40.** A music company is generating confidential data that is saved on their on-premises data center. As a backup solution, the company wants to upload their data on Amazon S3. The company has a policy that any data stored outside its own data center must be encrypted. This way, even if the data is hacked, nobody will be able to read it without the encryption keys. Which of the following methods can achieve this? (Select TWO.) **(Select 2.)**

- **A.** Use SSL to encrypt the data while in transit to Amazon S3.
- **B.** Use Amazon S3 server-side encryption with customer-provided keys.
- **C.** Use Amazon S3 bucket policies to restrict access to the data at rest.
- **D.** Use Amazon S3 server-side encryption with EC2 key pair.
- **E.** Encrypt the data on the client-side using your own master key then upload the data to Amazon S3.


**Q41.** A new security mandate requires that all personnel data held in the cloud is encrypted at rest. Which two methods allow you to encrypt data stored in S3 buckets at rest cost-efficiently? **(Select 2.)**

- **A.** Make use of AWS S3 bucket policies to control access to the data at rest
- **B.** Use AWS S3 server-side encryption with Key Management Service keys or Customer-provided keys
- **C.** Use CloudHSM
- **D.** Encrypt the data at the source using the client's CMK keys before transferring it to S3


**Q42.** A company is storing data on Amazon Simple Storage Service (S3). The company's security policy mandates that data is encrypted at rest. Which of the following methods can achieve this? Choose 3 answers **(Select 3.)**

- **A.** Use Amazon S3 server-side encryption with EC2 key pair.
- **B.** Use SSL to encrypt the data while in transit to Amazon S3.
- **C.** Use Amazon S3 server-side encryption with AWS Key Management Service managed keys.
- **D.** Encrypt the data on the client-side before ingesting to Amazon S3 using their own master key.
- **E.** Use Amazon S3 bucket policies to restrict access to the data at rest.
- **F.** Use Amazon S3 server-side encryption with customer-provided keys.


**Q43.** For data privacy, a healthcare company has been asked to comply with the Health Insurance Portability and Accountability Act (HIPAA). The company stores all its backups on an Amazon S3 bucket. It is required that data stored on the S3 bucket must be encrypted. What is the best option to do this? (Select TWO.) **(Select 2.)**

- **A.** Store the data in encrypted EBS snapshots.
- **B.** Store the data on EBS volumes with encryption enabled instead of using Amazon S3.
- **C.** Enable Server-Side Encryption on an S3 bucket to make use of AES-128 encryption.
- **D.** Enable Server-Side Encryption on an S3 bucket to make use of AES-256 encryption.
- **E.** Before sending the data to Amazon S3 over HTTPS, encrypt the data locally first using your own encryption keys.


**Q44.** You are a new Solutions Architect in a large insurance firm. To maintain compliance with HIPAA laws, all data being backed up or stored on Amazon S3 needs to be encrypted at rest. In this scenario, what is the best method of encryption for your data, assuming S3 is being used for storing financial-related data? (Select TWO.) **(Select 2.)**

- **A.** Enable SSE on an S3 bucket to make use of AES-256 encryption
- **B.** Use AWS Shield to protect your data at rest
- **C.** Encrypt the data using your own encryption keys then copy the data to Amazon S3 over HTTPS endpoints.
- **D.** Store the data in encrypted EBS snapshots
- **E.** Store the data on EBS volumes with encryption enabled instead of using Amazon S3


**Q45.** What two methods are recommended by AWS for protecting EBS data at rest? **(Select 2.)**

- **A.** Snapshots
- **B.** Encryption
- **C.** VPN
- **D.** Replication


**Q46.** You are designing a connectivity solution between on-premises infrastructure and Amazon VPC Your server’s on-premises will de- communicating with your VPC instances. You will de-establishing IPSec tunnels over the internet. You will be using VPN gateways and terminating the IPsec tunnels on AWS-supported customer gateways. Which of the following objectives would you achieve by implementing an IPSec tunnel as outlined above? **(Select 4.)**

- **A.** End-to-end protection of data in transit
- **B.** Peer identity authentication between VPN gateway and customer gateway
- **C.** Data integrity protection across the Internet
- **D.** Protection of data in transit over the Internet
- **E.** Data encryption across the Internet
- **F.** End-to-end Identity authentication


**Q47.** A security officer has requested that all data associated with a specific customer is encrypted. The data resides on Elastic Block Store (EBS) volumes. Which of the following statements about using EBS encryption are correct? **(Select 2.)**

- **A.** There is no direct way to change the encryption state of a volume
- **B.** Data in transit between an instance and an encrypted volume is also encrypted
- **C.** All instance types support encryption
- **D.** All attached EBS volumes must share the same encryption state


**Q48.** You are trying to decrypt ciphertext with AWS KMS and the decryption operation is failing. Which of the following are possible causes? **(Select 2.)**

- **A.** The plaintext was encrypted along with an encryption context, and you are not providing the identical encryption context when calling the Decrypt API.
- **B.** The private key does not match the public key in the ciphertext.
- **C.** You are not providing the correct symmetric key to the Decrypt API.
- **D.** The ciphertext you are trying to decrypt is not valid.


**Q49.** DynamoDB tables may contain sensitive data that needs to be protected. Which of the following is a way for you to protect DynamoDB table content? **(Select 2.)**

- **A.** DynamoDB can store data encrypted with a client-side encryption library solution
- **B.** DynamoDB can be used with the AWS Key Management Service to encrypt the data before storing the data in DynamoDB.
- **C.** DynamoDB encrypts all data server-side by default so nothing is required.
- **D.** DynamoDB obfuscates all data stored so encryption is not required.
- **E.** DynamoDB should not be used to store sensitive information requiring protection.


**Q50.** Your compliance department has mandated a new requirement that all data on Amazon Elastic Block Storage (Amazon EBS) volumes must be encrypted. Which of the following steps would you follow for your existing Amazon EBS volumes to comply with the new requirement? **(Select 3.)**

- **A.** Copy the data from the unencrypted Amazon EBS volume to the Amazon EBS volume with encryption enabled.
- **B.** Create a new Amazon EBS volume with encryption enabled.
- **C.** Modify the existing Amazon EBS volume properties to enable encryption.
- **D.** Attach an Amazon EBS volume with encryption enabled to the instance that hosts the data, then migrate the data to the encryption-enabled Amazon EBS volume.
- **E.** Move the existing Amazon EBS volume into an Amazon Virtual Private Cloud (Amazon VPC).


## EBS Volumes & Snapshots


**Q51.** AWS communicates with customers regarding its security and control environment through a variety of different mechanisms. Which of the following are valid mechanisms? **(Select 3.)**

- **A.** Directly providing customers with certificates, reports, and other documentation (under NDA in some cases)
- **B.** Publishing information about security and AWS control practices via the website, whitepapers, and blogs
- **C.** Allowing customers’ auditors direct access to AWS data centers, infrastructure, and senior staff
- **D.** Obtaining industry certifications and independent third-party attestations


## Monitoring: CloudWatch, CloudTrail & Config


**Q52.** Which of the following are true regarding AWS CloudTrail? **(Select 3.)**

- **A.** CloudTrail is enabled on a per-region basis
- **B.** Logs can be delivered to a single Amazon S3 bucket for aggregation.
- **C.** CloudTrail is enabled for all available services within a region.
- **D.** CloudTrail is enabled globally
- **E.** CloudTrail is enabled by default
- **F.** CloudTrail is enabled on a per-service basis.


## Cost Management & Optimization Tools


**Q53.** What feature is part of Amazon Trusted Advisor? **(Select 2.)**

- **A.** Troubleshooting tool
- **B.** Security compliance
- **C.** Security certificates
- **D.** EC2 configuration tool


---


# Answer Key & Explanations


**Q1. B**  
_IAM Roles, Policies & Permissions_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q2. C**  
_IAM Roles, Policies & Permissions_  
A key pair consists of a public key that AWS stores, and a private key file that you store For Windows AMIs, the private key file is required to obtain the password used to log into your instance For Linux AMIs, the private key file allows you to securely SSH into your instance The "EC2 password" might refer to the operating system password. By default you cannot login this way to Linux and must use a key pair. However, this can be enabled by setting a password and updating the /etc/ssh/sshd_config file You cannot login to an EC2 instance using certificates/public keys, References: https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ec2/

**Q3. A**  
_RDS Multi-AZ, Read Replicas & Aurora_  
After you create a DB instance, you can modify the backup retention period. You can set the backup retention period to between 0 and 35 days. Setting the backup retention period to 0 disables automated backups. Manual snapshot limits (100 per region) do not apply to automated backups. Refer: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html

**Q4. C**  
_RDS Multi-AZ, Read Replicas & Aurora_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q5. D**  
_Encryption & AWS KMS_  
Amazon Elastic Block Store (Amazon EBS) provides block-level storage volumes for use with EC2 instances. EBS volumes behave like raw, unformatted block devices. You can mount these volumes as devices on your instances. EBS volumes that are attached to an instance are exposed as storage volumes that persist independently from the life of the instance. Amazon EBS is the persistent block storage volume among the options given. It is mainly used as the root volume to store the operating system of an EC2 instance. To encrypt an EBS volume at rest, you can use AWS KMS customer master keys for the encryption of both the boot and data volumes of an EC2 instance.
- *Why not A:* This option is incorrect because EBS volumes are only encrypted using AWS KMS. Server-side encryption (SSE) is actually an option for Amazon S3, but not for Amazon EC2.
- *Why not B:* This option is incorrect because the scenario requires persistent block storage and not temporary storage. Also, enabling SSL is not a requirement in the scenario as it is primarily used to encrypt data in transit.
- *Why not C:* This option is incorrect because the scenario requires persistent block storage and not temporary storage. Also, enabling SSL is not a requirement in the scenario as it is primarily used to encrypt data in transit.

**Q6. B**  
_Encryption & AWS KMS_  
AWS KMS uses envelope encryption to protect data. AWS KMS creates a data key, encrypts it under a Customer Master Key (CMK), and returns plaintext and encrypted versions of the data key to you. You use the plaintext key to encrypt data and store the encrypted key alongside the encrypted data. You can retrieve a plaintext data key only if you have the encrypted data key and you have permission to use the corresponding master key.

**Q7. B**  
_Encryption & AWS KMS_  
If data must be encrypted before being sent to Amazon S3, client-side encryption must be used.

**Q8. A**  
_Encryption & AWS KMS_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q9. B**  
_Encryption & AWS KMS_  
Refer: https://cloudacademy.com/blog/how-to-encrypt-an-ebs-volume-the-new-amazon-ebs-encryption/

**Q10. C**  
_Encryption & AWS KMS_  
When you choose AWS KMS for key management with Amazon Redshift, there is a four-tier hierarchy of encryption keys. These keys are the master key, a cluster key, a database key, and data encryption keys.

**Q11. B**  
_Encryption & AWS KMS_  
Amazon S3 SSE uses one of the strongest block ciphers available, 256-bit AES.

**Q12. E**  
_Encryption & AWS KMS_  
To encrypt your existing Amazon S3 objects with a single request, you can use Amazon S3 batch operations. You provide S3 Batch Operations with a list of objects to operate on, and Batch Operations calls the respective API to perform the specified operation. You can use the copy operation to copy the existing unencrypted objects and write the new encrypted objects to the same bucket. A single Batch Operations job can perform the specified operation on billions of objects containing exabytes of data. Refer: https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html

**Q13. D**  
_Encryption & AWS KMS_  
For additional security, you should transmit your requests using Secure Sockets Layer (SSL) by using HTTPS. SSL encrypts the transmission, protecting your request or the response from being viewed in transit. For more information about securing your Query requests, see Making Secure Requests to Amazon Web Services . Refer: https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/using-query- api.html#:~:text=For%20additional%20security%2C%20you%20should,Requests%20to%20Amazon%20Web%20Services%20.

**Q14. A**  
_Encryption & AWS KMS_  
With S3 Versioning, you can easily preserve, retrieve, and restore every version of an object stored in Amazon S3, which allows you to recover from unintended user actions and application failures. To prevent accidental deletions, enable Multi-Factor Authentication (MFA) Delete on an S3 bucket. Refer: https://aws.amazon.com/s3/features/#:~:text=With%20S3%20Versioning%2C%20you%20can,Delete%20on%20an%20S3%20bucket.

**Q15. D**  
_Encryption & AWS KMS_  
Amazon S3 server-side encryption uses one of the strongest block ciphers available to encrypt your data, 256-bit Advanced Encryption Standard (AES-256). Server-side encryption encrypts only the object data, not object metadata. Refer: https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingServerSideEncryption.html

**Q16. A**  
_Encryption & AWS KMS_  
Amazon does not have access to your keys or credentials and therefore has no way to recover your keys if you lose your credentials. References: https://aws.amazon.com/cloudhsm/faqs/

**Q17. B**  
_Encryption & AWS KMS_  
A virtual MFA device uses a software application that generates six-digit authentication codes that are compatible with the TOTP standard, as described in RFC 6238.

**Q18. B**  
_Encryption & AWS KMS_  
Amazon WorkSpaces uses PCoIP, which provides an interactive video stream without transmitting actual data.

**Q19. C**  
_Encryption & AWS KMS_  
IPsec is the security protocol supported by Amazon VPC.

**Q20. E**  
_EBS Volumes & Snapshots_  
All decommissioned magnetic storage devices are degaussed and physically destroyed in accordance with industry-standard practices.

**Q21. D**  
_EBS Volumes & Snapshots_  
You can take a snapshot of an attached volume that is in use. However, snapshots only capture data that has been written to your Amazon EBS volume at the time the snapshot command is issued. This might exclude any data that has been cached by any applications or the operating system. If you can pause any file writes to the volume long enough to take a snapshot, your snapshot should be complete. However, if you can't pause all file writes to the volume, you should unmount the volume from within the instance, issue the snapshot command, and then remount the volume to ensure a consistent and complete snapshot. You can remount and use your volume while the snapshot status is pending. Refer: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-creating-snapshot.html

**Q22. A**  
_EBS Volumes & Snapshots_  
You cannot restore a snapshot of a root volume without downtime There is no direct way to change the encryption state of a volume Either create an encrypted volume and copy data to it or take a snapshot, encrypt it, and create a new encrypted volume from the snapshot. References: https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/

**Q23. A**  
_High Availability & Fault Tolerance_  
You can use a single ALB and bind multiple SSL certificates to the same listener With Server Name Indication (SNI) a client indicates the hostname to connect to. SNI supports multiple secure websites using a single secure listener You cannot have the same port in multiple listeners so adding multiple listeners would not work. Also, when using standard HTTP/HTTPS the port will always be 80/443 so you must be able to receive traffic on the same ports for multiple applications and still be able to forward to the correct instances. This is where host-based routing comes in With host-based routing you can route client requests based on the Host field (domain name) of the HTTP header allowing you to route to multiple domains from the same load balancer (and share the same listener) You do not need multiple ALBs and it would not be cost-effective. References: https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/elastic-load-balancing/

**Q24. C**  
_High Availability & Fault Tolerance_  
An SSL certificate must specify the name of the website in either the subject name or listed as a value in the SAN extension of the certificate in order for connecting clients to not receive a warning.

**Q25. E**  
_Monitoring: CloudWatch, CloudTrail & Config_  
Container Insights provides automatic dashboards in the CloudWatch console. These dashboards summarize the compute performance, errors, and alarms by cluster, pod/task, and service. For Amazon EKS and k8s, dashboards are also available for nodes/EC2 instances and namespaces. Each dashboard summarizes the list of running pods/tasks or containers by CPU and memory for the selected time window, and allows you to contextually - based on time window and selected pod/task or container - dive deeper into application logs, AWS X-Ray traces, and performance events. You can always retrieve metrics data for any Amazon EC2 instance based on the retention schedules described above. However, the CloudWatch console limits the search of metrics to 2 weeks after a metric is last ingested to ensure that the most up to date instances are shown in your namespace. Refer: https://aws.amazon.com/cloudwatch/features/

**Q26. B**  
_Monitoring: CloudWatch, CloudTrail & Config_  
AWS CloudTrail is a service that enables governance, compliance, operational auditing, and risk auditing of your AWS account. With CloudTrail, you can log, continuously monitor, and retain account activity related to actions across your AWS infrastructure. CloudTrail provides event history of your AWS account activity, including actions taken through the AWS Management Console, AWS SDKs, command line tools, and other AWS services. This event history simplifies security analysis, resource change tracking, and troubleshooting. CloudTrail provides visibility into user activity by recording actions taken on your account. CloudTrail records important information about each action, including who made the request, the services used, the actions performed, parameters for the actions, and the response elements returned by the AWS service. This information helps you to track changes made to your AWS resources and troubleshoot operational issues. CloudTrail makes it easier to ensure compliance with internal policies and regulatory standards.
- *Why not A:* This option is incorrect because this is a monitoring tool for your AWS resources. Like the above options, it does not provide the needed information to satisfy the requirement in the scenario.
- *Why not C:* This option is incorrect because EC2 is a service that provides secure, resizable compute capacity in the cloud and does not provide the needed information in this scenario just like the option above.
- *Why not D:* This option is incorrect because a VPC is a logically isolated section of the AWS Cloud where you can launch AWS resources in a virtual network that you define. It does not provide you the auditing information that were asked for in this scenario.

**Q27. D**  
_Monitoring: CloudWatch, CloudTrail & Config_  
Server access logging provides detailed records for the requests that are made to a bucket. To track requests for access to your bucket, you can enable server access logging. Each access log record provides details about a single access request, such as the requester, bucket name, request time, request action, response status, and an error code, if relevant For capturing IAM/user identity information in logs you would need to configure AWS CloudTrail Data Events (however this does not audit the bucket operations required in the question) Amazon S3 event notifications can be sent in response to actions in Amazon S3 like PUTs, POSTs, COPYs, or DELETEs.S3 event notifications records the request action but not the other requirements of the security team CloudWatch metrics do not include the bucket operations specified in the question References: https://digitalcloud.training/certification- training/aws-solutions-architect-associate/storage/amazon-s3/ https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerLogs.html

**Q28. A**  
_Monitoring: CloudWatch, CloudTrail & Config_  
Volume status checks are automated tests that run every 5 minutes and return a pass or fail status. If all checks pass, the status of the volume is ok. If a check fails, the status of the volume is impaired. If the status is insufficient-data, the checks may still be in progress on the volume. You can view the results of volume status checks to identify any impaired volumes and take any necessary actions. Refer: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-volume-status.html

**Q29. A**  
_AWS Organizations & Multi-Account_  
The public half of the key pair is stored on the instance, and the private half can then be used to connect via SSH.

**Q30. C**  
_Threat Detection & Compliance_  
Any number of components of a workload can be moved into AWS, but it is the customer’s responsibility to ensure that the entire workload remains compliant with various certifications and third-party attestations.

**Q31. D**  
_Threat Detection & Compliance_  
Customers should ensure that they implement control objectives that are designed to meet their organization’s own unique compliance requirements, therefore answer is correct.

**Q32. B**  
_Threat Detection & Compliance_  
AWS provides IT control information to customers through either specific control definitions or general control standard compliance.

**Q33. A**  
_General Design_  
The collective control environment includes people, processes, and technology necessary to establish and maintain an environment that supports the operating effectiveness of AWS control framework. Energy is not a discretely identified part of the control environment, therefore this the correct answer.

**Q34. A**  
_General Design_  
AWS comes in two web service delivery flavors: SOAP (which originally stood for Simple Object Access Protocol) is a protocol that involves XML data exchange between client and server.

**Q35. D**  
_General Design_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q36. C, D**  
_S3 Security, Access & Durability_  
Versioning protects data against inadvertent or intentional deletion by storing all versions of the object, and MFA Delete requires a one-time code from a Multi-Factor Authentication (MFA) device to delete objects. Cross-region replication and migration to the Amazon Glacier storage class do not protect against deletion. Vault locks are a feature of Amazon Glacier, not a feature of Amazon S3.

**Q37. A, C**  
_S3 Security, Access & Durability_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q38. A, D**  
_S3 Storage Classes & Lifecycle_  
There is a charge if you delete data within 90 days – however we are not talking about deleting data here, just retrieving it Retrieved data is available for 24 hours by default (can be changed) Amazon Glacier must complete a job before you can get its output Glacier automatically encrypts data at rest using AES 256 symmetric keys and supports secure transfer of data over SSL Retrieved data will not be encrypted if it was uploaded unencrypted You do not need an MFA device to access the retrieved files. References: https://digitalcloud.training/certification-training/aws-solutions-architect- associate/storage/amazon-s3/

**Q39. C, E**  
_S3 Storage Classes & Lifecycle_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q40. B, E**  
_Encryption & AWS KMS_  
Data protection refers to protecting data while in-transit (as it travels to and from Amazon S3) and at rest (while it is stored on disks in Amazon S3 data centers). You can protect data in transit by using SSL or by using client-side encryption. You have the following options for protecting data at rest in Amazon S3: Use Server-Side Encryption – You request Amazon S3 to encrypt your object before saving it on disks in its data centers and decrypt it when you download the objects. Use Server-Side Encryption with Amazon S3-Managed Keys (SSE-S3) Use Server-Side Encryption with AWS KMS-Managed Keys (SSE-KMS) Use Server-Side Encryption with Customer-Provided Keys (SSE-C) Use Client-Side Encryption – You can encrypt data client-side and upload the encrypted data to Amazon S3. In this case, you manage the encryption process, the encryption keys, and related tools. Use Client-Side Encryption with AWS KMS–Managed Customer Master Key (CMK) Use Client-Side Encryption Using a Client-Side Master Key

**Q41. B, D**  
_Encryption & AWS KMS_  
When using S3 encryption your data is always encrypted at rest and you can choose to use KMS managed keys or customer-provided keys. If you encrypt the data at the source and transfer it in an encrypted state it will also be encrypted in-transit With client side encryption data is encrypted on the client side and transferred in an encrypted state and with server-side encryption data is encrypted by S3 before it is written to disk (data is decrypted when it is downloaded) You can use bucket policies to control encryption of data that is uploaded but use of encryption is not stated in the answer given. Simply using bucket policies to control access to the data does not meet the security mandate that data must be encrypted Multipart upload helps with uploading large files but does not encrypt your data CloudHSM can be used to encrypt data but as a dedicated service it is charged on an hourly basis and is less cost-efficient compared to S3 encryption or encrypting the data at the source. References: https://digitalcloud.training/certification-training/aws- solutions-architect-associate/storage/amazon-s3/

**Q42. C, D, F**  
_Encryption & AWS KMS_  
Reference: http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html

**Q43. D, E**  
_Encryption & AWS KMS_  
Server-side encryption is about data encryption at restóthat is, Amazon S3 encrypts your data at the object level as it writes it to disks in its data centers and decrypts it for you when you access it. As long as you authenticate your request and you have access permissions, there is no difference in the way you access encrypted or unencrypted objects. For example, if you share your objects using a pre-signed URL, that URL works the same way for both encrypted and unencrypted objects. You have three mutually exclusive options depending on how you choose to manage the encryption keys: Use Server-Side Encryption with Amazon S3-Managed Keys (SSE-S3) Use Server-Side Encryption with AWS KMS-Managed Keys (SSE-KMS) Use Server-Side Encryption with Customer-Provided Keys (SSE-C)
- *Why not C:* This option is incorrect as S3 doesn't provide AES-128 encryption, only AES-256.

**Q44. A, C**  
_Encryption & AWS KMS_  
Data protection refers to protecting data while in-transit (as it travels to and from Amazon S3) and at rest (while it is stored on disks in Amazon S3 data centers). You can protect data in transit by using SSL or by using client-side encryption. You have the following options for protecting data at rest in Amazon S3. Use Server-Side Encryption – You request Amazon S3 to encrypt your object before saving it on disks in its data centers and decrypt it when you download the objects. Use Client-Side Encryption – You can encrypt data client-side and upload the encrypted data to Amazon S3. In this case, you manage the encryption process, the encryption keys, and related tools.

**Q45. A, B**  
_Encryption & AWS KMS_  
You can achieve data protection in transit in two ways: encrypt the connection using Secure Sockets Layer (SSL), or use client-side encryption (where the object is encrypted before it is sent). Both methods are valid for protecting your application data. Refer: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/security-data-protection-encryption.html

**Q46. B, C, D, E**  
_Encryption & AWS KMS_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q47. A, B**  
_Encryption & AWS KMS_  
All EBS types and all instance families support encryption Not all instance types support encryption There is no direct way to change the encryption state of a volume Data in transit between an instance and an encrypted volume is also encrypted You can have encrypted and non- encrypted EBS volumes on a single instance References: https://digitalcloud.training/certification-training/aws-solutions-architect- associate/compute/amazon-ebs/

**Q48. A, D**  
_Encryption & AWS KMS_  
Encryption context is a set of key/value pairs that you can pass to AWS KMS when you call the Encrypt, Decrypt, ReEncrypt, GenerateDataKey, and GenerateDataKeyWithoutPlaintext APIs. Although the encryption context is not included in the ciphertext, it is cryptographically bound to the ciphertext during encryption and must be passed again when you call the Decrypt (or ReEncrypt) API. Invalid ciphertext for decryption is plaintext that has been encrypted in a different AWS account or ciphertext th

**Q49. A, B**  
_Encryption & AWS KMS_  
Amazon DynamoDB does not have a server-side feature to encrypt items within a table. You need to use a solution outside of DynamoDB such as a client-side library to encrypt items before storing them, or a key management service like AWS Key Management Service to manage keys that are used to encrypt items before storing them in DynamoDB.

**Q50. A, B, D**  
_Encryption & AWS KMS_  
There is no direct way to encrypt an existing unencrypted volume. However, you can migrate data between encrypted and unencrypted volumes.

**Q51. A, B, D**  
_EBS Volumes & Snapshots_  
The option describe valid mechanisms that AWS uses to communicate with customers regarding its security and control environment. AWS does not allow customers’ auditors direct access to AWS data centers, infrastructure, or staff.

**Q52. A, B, C**  
_Monitoring: CloudWatch, CloudTrail & Config_  
_See the matching section of this task's `notes.md` for the underlying concept._

**Q53. A, D**  
_Cost Management & Optimization Tools_  
Refer: https://aws.amazon.com/about-aws/whats-new/2014/07/23/introducing-aws-trusted-advisor-console/
