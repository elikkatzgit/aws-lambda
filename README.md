
Login to your AWS console

- Go to SES service 
1. Verified identities > Create entity with your gmail account
2. Go to your email and verify your email address by clicking a link

- Go to IAM service
1. Roles > create role > Trusted entity type = AWS service > Use case = ec2
2. Select Permissions policies: AmazonEC2FullAccess and AmazonSESFullAccess > Next
3. Give the role name and descrition > Create Role

- Go to lambda service
6. Create function > Author from scratch > ENTER Function name > runtime = Python 3.X > Create Function
7. Paste the code (Edit the region string or remove it to detect on all account) > Deploy
8. Configuration > Permissions > Execution role > add the role created
9. Back to code > test > publish

That's it :-)
