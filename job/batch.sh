#!/usr/bin/env bash

#SBATCH --partition=mypartition
#SBATCH -N 1
#SBATCH --job-name=test
#SBATCH --output=/tmp/%j.out
#SBATCH --error=/tmp/%j.err
#SBATCH --licenses=fake_license.fake_feature@flexlm:42

srun /tmp/application.sh
