from constructs import Construct

from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns
)

class CdkWorkshopStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        vpc = ec2.Vpc("cdk-helloworld-poc-seb-vpc", max_azs=3)

        cluster = ecs.Cluster("cdk-helloworld-poc-seb-ecs", vpc=vpc)

        ecs_patterns.ApplicationLoadBalancedFargateService("cdk-helloworld-poc-fs",
            cluster=cluster,            # Required
            cpu=512,                    # Default is 256
            desired_count=2,            # Default is 1
            task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                image=ecs.ContainerImage.from_registry("amazon/amazon-ecs-sample")),
            memory_limit_mib=2048,      # Default is 512
            public_load_balancer=True)  # Default is False
