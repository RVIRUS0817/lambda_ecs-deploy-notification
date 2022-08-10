#!/usr/bin/python
# -*- coding: utf-8 -*-

import boto3
import os
import urllib.request,urllib.parse
import json
def lambda_handler(event, context):
    msgdata = event['detail']['eventName']
    resources = event['resources'][0]
    reason = event['detail']['reason']
    client = boto3.client('ecs')
    fields = []

    fields.append({
        'title': resources,
        'value': msgdata,
        'short': True,
    })
    data = {
        'attachments': [{
            'pretext': reason,
            'color': 'good',
            'fields': fields,
        }]
    }
    # Slack
    url = os.environ['SLACK_URL']
    req = urllib.request.Request(url, json.dumps(data).encode(), {'Content-Type': 'application/json'})
    res = urllib.request.urlopen(req)
    res.read()
    res.close
