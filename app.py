#!/usr/bin/env python3

from aws_cdk import core

from cdk.app_stack import MyStack


app = core.App()
MyStack(app, "slack-notification", env={'region': 'ap-northeast-1'})

app.synth()
