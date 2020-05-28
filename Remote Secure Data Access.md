

## 1.  S3 bucket on AWS 
The data is uploaded by me after receiving zipped data from the client. If the data sources are multiple or they are too large to be shared via email or secure ftp then you would need to manage the S3 bucket  and its data uploads on your end and just grant me user access. If I manage the bucket, I would create a seperate bucket specifically for working with you and add the monthly costs to your invoice as a seperate line item. [Here is some pricing info for review.](https://aws.amazon.com/s3/pricing/?nc=sn&loc=4) Once we completed our work together I would delete bucket or you could remove me as a user if it was managed on your end. 

This is probably the best option without knowing alot about how you're accessing the data and what your data management system looks like. As I mentioned I work on [AWS EC2](https://aws.amazon.com/ec2/?nc=bc&pg=gs)'s for computing which is more secure and keeps clients data and code off my local machine. I would bill this usage as an invoiced line item seperate from the s3, my current set up is about $1/hour and it's only up and running when you need to write or run code. 


## 2.  VPN connection 
This is the second most common approach I have encountered. This requires an available virtual or physical computer with the appropriate connections to databases to be set-up as well as my user authentication. However it does keep all data on premises and eleviates the need to upload data to another storage location like an S3.

## 3. Private Github Repository 
This is best for smaller data, the max file size is 25GB. In this case 
data is uploaded by the client and I am added to the repository as a collaborator. This is free up to 500 MB, [here is the pricing information.](https://github.com/pricing) and is great for data science workflow and code version management.


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTQzOTk1MzQ3LDU3NTE3MTk5OSwtMTUwMD
c5Mzc3MSw4OTQxMzM0N119
-->