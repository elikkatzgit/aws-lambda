import boto3
import logging

#setup simple logging for INFO
logger = logging.getLogger()
logger.setLevel(logging.INFO)

#define the entities
ec2 = boto3.resource('ec2',region_name='eu-west-3')
ses = boto3.client('ses')

email_from = 'XXX@gmail.com'
email_to = 'XXX@gmail.com'
emaiL_subject = 'Stopped Instances'
#email_body = 'Body'

def lambda_handler(event, context):
    # Use the filter() method of the instances collection to retrieve
    # all running EC2 instances.
    filters = [{
            'Name': 'tag:AutoOff',
            'Values': ['True']
        },
        {
            'Name': 'instance-state-name', 
            'Values': ['running']
        }
    ]
    
    #filter the instances
    instances = ec2.instances.filter(Filters=filters)
    RunningInstances = [instance.id for instance in instances]
    
    #make sure there are actually instances to shut down. 
    if len(RunningInstances) > 0:
        print('Going to stop instances: ' + str(RunningInstances)) 
        #perform the shutdown
        #shuttingDown = ec2.instances.filter(InstanceIds=RunningInstances).stop()
        
        #Sending mail notification
        response = ses.send_email(
            Source = email_from,
            Destination={
                'ToAddresses': [
                    email_to,
                ]
            },
            Message={
                'Subject': {
                    'Data': emaiL_subject
                },
                'Body': {
                    'Text': {
                        'Data': "The following were stopped:" + str(RunningInstances)
                    }
                }
            }
        )
    
    else:
        print ("Nothing to do here")
