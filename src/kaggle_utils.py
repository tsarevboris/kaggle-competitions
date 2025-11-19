from __future__ import annotations
from pathlib import Path
import subprocess
import zipfile

# Automatically detect repo root (src/ is inside project root)
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_ROOT / "data" / "raw"

def _run(cmd: list[str]) -> None:
    p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if p.returncode != 0:
        raise RuntimeError(f"Command failed: {' '.join(cmd)}\nSTDOUT:\n{p.stdout}\nSTDERR:\n{p.stderr}")

def download_competition(comp: str) -> Path:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    zip_path = RAW_DIR / f"{comp}.zip"
    extract_dir = RAW_DIR / comp

    if not zip_path.exists():
        _run(["kaggle", "competitions", "download", "-c", comp, "-p", str(RAW_DIR)])

    if not extract_dir.exists() or not any(extract_dir.iterdir()):
        with zipfile.ZipFile(zip_path, "r") as zf:
            zf.extractall(extract_dir)

    return extract_dir
