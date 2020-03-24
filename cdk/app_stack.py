from aws_cdk import (
    core,
    aws_lambda as _lambda,
    aws_ssm as _ssm,
)


class MyStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)


        layer = _lambda.LayerVersion(
            self,
            'PythonModuleLayer',
            code=_lambda.Code.asset('layer'),
            compatible_runtimes=[_lambda.Runtime.PYTHON_3_8],
        )

        webhook_url = _ssm.StringParameter.from_string_parameter_name(
            self,
            'TargetUrl',
            string_parameter_name='slack-webhook-url-number09-test'
        ).string_value

        my_lambda = _lambda.Function(
            self,
            'NotificationHandler',
            runtime=_lambda.Runtime.PYTHON_3_8,
            code=_lambda.Code.asset('src/lambda'),
            handler='handler.notification.handler',
            layers=[layer],
            environment={
                'webhook_url': webhook_url,
            }
        )
