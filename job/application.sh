#!/usr/bin/env bash
set -e

# change the URL
URL="http://localhost:8000"

# number of licenses: from the CLI or 42
if [ -z $1 ]; then
	X=42
else
	X=$1
fi

payload="{\"quantity\": "$X", \
          \"user_name\": \""$USER"\", \
          \"lead_host\": \"$(hostname)\", \
          \"license_name\": \"fake_license.fake_feature\"}"

echo "Requesting $X licenses for user $USER"
status=$(curl -s -o /dev/null -w '%{http_code}' \
	      -X 'POST' \
	      -H 'Content-Type: application/json' \
	      -d "$payload" \
	      "$URL"/licenses-in-use/)
if [ "$status" = "201" ]; then
	echo "There are enought licenses available, lets run (sleep) the job"
	sleep 123
else
	echo "There are not enough licenses, let's crash the job"
	tail /NOT_ENOUGH_LICENSES
fi

echo "Puting the licenses back"
curl -s -o /dev/null \
     -X DELETE \
     -H 'Content-Type: application/json' \
     -d "$payload" \
     "$URL"/licenses-in-use/

echo "Job done"
