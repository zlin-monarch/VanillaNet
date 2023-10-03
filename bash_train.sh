python3 -m torch.distributed.launch --nproc_per_node=8 main.py \
--model vanillanet_5 \
--data_path /path/to/imagenet-1k \
--batch_size 128 --update_freq 1  --epochs 300 --decay_epochs 100 \ 
--lr 3.5e-3 --weight_decay 0.35  --drop 0.05 \
--opt lamb --aa rand-m7-mstd0.5-inc1 --mixup 0.1 --bce_loss \
--output_dir /path/to/save_results \
--model_ema true --model_ema_eval true --model_ema_decay 0.99996 \
--use_amp true 