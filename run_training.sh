


set -x -e

run_id=$(date +%s)
echo "RUN ID: $run_ts"

echo "START TIME: $(date)"

echo 'log to'

echo training_log_$run_id.log



 torchrun --nnodes=1 --nproc_per_node=1 train.py --config configs/training/v1/sprite_sheet_training.yaml --wandb | tee -a training_log_$run_id.log