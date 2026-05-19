from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

DOMAINS = ["blocksworld", "logistics", "campus"]


def run(cmd: list[str], cwd: Path) -> None:
    print("" + "=" * 80)
    print(f"Running in {cwd}: {' '.join(cmd)}")
    print("=" * 80)
    subprocess.run(cmd, cwd=cwd, check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run all reproducibility experiments")
    parser.add_argument("--quick", action="store_true", help="Use fewer runs for a fast smoke test")
    parser.add_argument("--domains", default=",".join(DOMAINS), help="Comma-separated domain list")
    args = parser.parse_args()

    root = Path(__file__).resolve().parent
    domains = [d.strip() for d in args.domains.split(",") if d.strip()]
    runs = "5" if args.quick else "50"

    for domain in domains:
        domain_dir = root / "domains" / domain
        if not domain_dir.exists():
            raise FileNotFoundError(f"Unknown domain folder: {domain_dir}")
        run([sys.executable, "full_pipeline.py", "--mode", "publication", "--runs", runs], cwd=domain_dir)

    print("All requested experiments completed. Check domains/*/outputs and results/.")


if __name__ == "__main__":
    main()
