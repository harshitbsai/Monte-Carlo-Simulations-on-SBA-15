#!/bin/bash
#SBATCH --job-name="GCMC_32.25_Chemical_Potential_UA"
#SBATCH --account=klab-materials
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=8
#SBATCH --cpus-per-task=8
#SBATCH --mem=100G
##SBATCH --gres=gpu:1
##SBATCH --partition=mb
#SBATCH --time=168:00:00
#SBATCH --export=ALL
#SBATCH --mail-user=hbalantr@uwyo.edu
#SBATCH --mail-type=START,END,FAIL

export OMP_NUM_THREADS=8

module load arcc/1.0
module load gcc/13.2.0
module load python/3.12.0

module use /project/klab-materials/software/codes/packages/k-lab-cassandra

module load 1.2.0

python /project/klab-materials/software/codes/packages/k-lab-cassandra/Scripts/Frag_Library_Setup/library_setup.py /project/klab-materials/software/codes/packages/k-lab-cassandra/Src/cassandra_gfortran_openMP.exe pore.inp propane.pdb t.pdb

/project/klab-materials/software/codes/packages/k-lab-cassandra/Src/cassandra_gfortran_openMP.exe  pore.inp
