


set -x -e

run_id=$(date +%s)
echo "RUN ID: $run_ts"

echo "START TIME: $(date)"

echo 'log to'

echo training_log_$run_id.log
OUTPUT_PATH=output_$run_id



torchrun --nnodes=1 --nproc_per_node=1 train.py --config /home/ubuntu/animation_training/src/animate_diff_training/sprite_sheet_training_batch_1_2_3.yaml  --wandb  --output_dir $OUTPUT_PATH | tee -a training_log_$run_id.log
