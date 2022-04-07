#!/bin/bash
protoc -I . --python_betterproto_out=models protos/api.proto