#!/usr/bin/python3

from apiclient import client, logger

main = client.Client()
logger = logger.Logger()

logger.log(main.createMessage())
