# Change Log

This file keeps track of all notable changes to license-manager-simulator

## Unreleased

## 0.2.0 -- 2022-08-19
* Move the API endpoints to a subapp in the URL http://<ip-address>:<port>/lm-sim

## 0.1.0 -- 2021-09-30
* Created CLI app to produce simulated flexlm output (from data pulled from API)
* Added fake SLURM job to credit and debit licenses
* Added unit tests
* Added FastAPI app to serve create-licenses and licenses-in-use endpoints
* Added CRUD logic over postgres database
* Created FlexLM Generator (render template with configuraiton values)
* Added output template (example)
* Added basic documentation (README,
