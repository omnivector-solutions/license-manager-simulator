#!/bin/bash

set -e

stage=$1
snap_name="flexlm-simulator"

s3_loc="s3://omnivector-public-assets/snaps/$snap_name/$stage/"
echo "Copying snap to $s3_loc"
aws s3 cp --acl public-read ./flexlm-simulator_*_amd64.snap $s3_loc
