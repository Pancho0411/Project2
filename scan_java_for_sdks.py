import os
from pathlib import Path
from collections import defaultdict

# common analytics and ad network package signatures
COMMON_SDKS = {
    "com.google.firebase.analytics": "Firebase Analytics (Google)",
    "com.mixpanel.android": "Mixpanel Analytics",
    "com.amplitude.api": "Amplitude Analytics",
    "com.facebook.appevents": "Facebook App Events (Meta)",
    "com.flurry.android": "Flurry Analytics",
    "com.appsflyer": "AppsFlyer (Tracking/Attribution)",
    "com.google.android.gms.ads": "Google Mobile Ads",
    "com.inmobi": "InMobi Ads",
    "com.kochava.base": "Kochava Analytics"
}

def scan_java_for_sdks(decompiled_dir: str):
    base_dir = Path(decompiled_dir)

    app_dirs = [d for d in base_dir.iterdir() if d.is_dir()]

    if not app_dirs:
        print("No decompiled app directories found.")
        return

    for app_dir in app_dirs:
        print(f"\nScanning {app_dir.name}...")

        # tracks sdks found without printing them just yet
        found_sdks = set()

        # use recursion to find java files
        java_files = list(app_dir.rglob("*.java"))

        for java_file in java_files:
            try:
                with open(java_file, 'r', encoding="utf-8", errors="ignore") as f:
                    content = f.read()

                    for signature, sdk_name in COMMON_SDKS.items():
                        if sdk_name in found_sdks:
                            continue

                        if signature in content:
                            found_sdks.add(sdk_name)
            except Exception as e:
                print(f"Error scanning {java_file.name}: {e}")

        if found_sdks:
            print("Flagged third party libraries found.")
            for sdk in found_sdks:
                print(f"\t{sdk}")
            else:
                print("No flagged third party libraries found.")

if __name__ == "__main__":
    DECOMPILED_OUTPUT = "./DECOMPILED_APKS"
    scan_java_for_sdks(DECOMPILED_OUTPUT)