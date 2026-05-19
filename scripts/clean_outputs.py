from pathlib import Path
import shutil
root = Path(__file__).resolve().parents[1]
for p in root.glob('domains/*/outputs'):
    if p.exists():
        shutil.rmtree(p)
        p.mkdir()
print('Cleaned domain outputs.')
