#!/usr/bin/env bash
set -e
URL="http://localhost:8000"

# number of licenses
X=1

# request X licenses
status=$(curl -s -o /dev/null -w '%{http_code}' \
              -X 'POST' \
              -H 'Content-Type: application/json' \
              -d "{\"quantity\": $X,
                  \"user_name\": \"string\",
                  \"lead_host\": \"string\",
                  \"license_name\": \"string\"}" \
              "$URL"/licenses-in-use/)
if [ "$status" = "201" ]; then
        # there are licenses available, lets run the job
        sleep 200
else
        # not enough licenses, let's crash the job
        tail /NOT_ENOUGH_LICENSES
fi

# put the licenses back
curl  -s -o /dev/null \
      -X 'DELETE' \
      -H 'Content-Type: application/json' \
      -d "{\"quantity\": $X,
           \"user_name\": \"string\",
           \"lead_host\": \"string\",
           \"license_name\": \"string\"}" \
      "$URL"/licenses-in-use/
