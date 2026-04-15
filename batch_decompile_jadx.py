import subprocess
import os
from pathlib import Path

def batch_decompile_jadx(apk_directory: str, output_directory: str):
    apk_dir = Path(apk_directory)
    out_dir = Path(output_directory)

    # Creates base directory
    out_dir.mkdir(parents=True, exist_ok=True)

    # Grabs apks
    apk_files = list(apk_dir.glob('*.apk'))

    if not apk_files:
        print(f"No APKs found in {apk_dir}")
        return

    print(f"Decompiling {len(apk_files)} APK files")

    for apk in apk_files:
        # Create output folder
        apk_out_path = out_dir / apk.stem

        print(f"Decompiling {apk.name}")

        # JADX command array to automate it running
        # -d: set the destination directory
        jadx_command = [
            "jadx.bat",
            "-d", str(apk_out_path),
            str(apk)
        ]

        try:
            result = subprocess.run(
                jadx_command,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True
            )
            if result.returncode == 0:
                print(f"Decompiled {apk.name} to {apk_out_path}")
            else:
                print(f"Decompiled with warnings: {apk.name}")

        except subprocess.CalledProcessError as e:
            print(f"Failed to decompile {apk.name}")
            print(f"Error: {e.stderr}\n")

if __name__ == "__main__":
    SOURCE_APKS = "./APKS"
    DECOMPILED_APKS = "./DECOMPILED_APKS"
    batch_decompile_jadx(SOURCE_APKS, DECOMPILED_APKS)