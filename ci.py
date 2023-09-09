import wandb
print(f'The version of wandb is: {wandb.__version__}')
assert wandb.__version__ == '0.15.10', f'Expected version 0.15.10, but got {wandb.__version__}'