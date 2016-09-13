#!/bin/sh

#sbatch -J eval --time=15:00 -p gputest --nodes=1 --gres=gpu:2 --mem-per-cpu=16000  --output=eval.out --exclusive --error=eval.err commands.sh 

sbatch -J extract --time=2-23:59:59 -p gpu --nodes=1 --gres=gpu:2 --mem-per-cpu=16000  --output=extract.out --error=extract.err commands.sh 

#sbatch -J cap --time=30:00 -p test -n 1 --nodes=1 --cpus-per-task=8 --mem-per-cpu=4000 --output=cap.out --error=cap.err commands.sh 
