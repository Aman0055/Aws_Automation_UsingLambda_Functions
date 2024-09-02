#Import all the modules and libraries
import boto3

#Open the Management Console 
aws_management_console = boto3.session.Session(profile_name= "default")

#Open Ec2 Console
ec2_console = aws_management_console.client(service_name="ec2")

#Use Boto3 Documentation : 
reponse = ec2_console.terminate_instances(
    InstanceIds = ['i-094b34bb96d0e3274'],
   
    
)

# Three operations are performed by the scripting of python boto3
# stop_instance () , start_instance(), terminate_instance()
