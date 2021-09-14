#!/usr/bin/env bash

#SBATCH --partition=mypartition
#SBATCH -N 1
#SBATCH --job-name=test
#SBATCH --output=/tmp/%j.out
#SBATCH --error=/tmp/%j.err

srun -Lfake_license.fake_feature /tmp/application.sh
