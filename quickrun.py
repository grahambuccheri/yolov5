import subprocess
from pathlib import Path

def get_user_input():
    batch = input("Enter the value for --batch (default: 32): ") or "32"
    epochs = input("Enter the value for --epochs (default: 300): ") or "300"
    weights = input("Enter the value for --weights (default: ''  Press Enter to skip): ") or ""
    data_dir = input("Enter the directory path for --data (e.g., FireID-2): ")
    cfg_model = input("Enter the model size for --cfg (s, m, l, or x): ").lower()

    data_path = Path(data_dir) / "data.yaml"
    cfg_path = f"models/yolov5{cfg_model}.yaml"

    return batch, epochs, weights, str(data_path), cfg_path

def run_command(batch, epochs, weights, data_path, cfg_path):
    command = [
        "python3",
        "train.py",
        "--batch", batch,
        "--epochs", epochs,
        "--data", data_path,
        "--weights", weights,
        "--cfg", cfg_path,
        "--cache"
    ]

    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command failed with exit code {e.returncode}")

if __name__ == "__main__":
    batch, epochs, weights, data_path, cfg_path = get_user_input()
    run_command(batch, epochs, weights, data_path, cfg_path)