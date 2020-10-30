#!/bin/bash

set -e

stage=$1
snap_name="license-manager-simulator"

s3_loc="s3://omnivector-public-assets/snaps/$snap_name/$stage/license-manager-simulator_0.1_amd64.snap"
echo "Copying $s3_loc to ."
aws s3 cp $s3_loc ./license-manager-simulator.snap
