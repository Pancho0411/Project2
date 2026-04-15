import sys
import xml.etree.ElementTree as ET
from pathlib import Path

# List of possibly dangerous/excessive permissions for a health app
DANGEROUS_PERMISSIONS = {
    "android.permission.ACCESS_FINE_LOCATION": "Uses precise tracking. High risk for identifying user locations.",
    "android.permission.CAMERA": "Able to open the camera for device pairing via a QR code. High risk as may be used to take unwanted malicious photos.",
    "android.permission.READ_SMS": "Can be used to read 2FA codes or private text messages.",
    "android.permission.READ_CONTACTS": "Severe privacy risk and is unnecessary for a health app.",
    "android.permission.RECORD_AUDIO": "Risk of ambient or unaware eavesdropping",
    "android.permission.GET_ACCOUNTS": "Can be used to expose the primary user's email and identity.",
    "android.permission.READ_EXTERNAL_STORAGE": "Grants access to potentially sensitive files outside the app. Less likely now that SD cards are largely phased out, but external USB storage is still used."
}

def analyze_manifest_permissions(decompiled_dir: str):
    base_dir = Path(decompiled_dir)
    # use recursion to find all manifests
    manifests = list(base_dir.rglob("AndroidManifest.xml"))

    if not manifests:
        print("No AndroidManifest.xml files found.")
        return

    # defines the Android XML namespace
    ns = {'android': 'http://schemas.android.com/apk/res/android'}

    for manifest_path in manifests:
        app_name = manifest_path.parent.name;
        print(f"Analyzing {app_name}")

        try:
            tree = ET.parse(manifest_path)
            root = tree.getroot()

            permissions = root.findall('.//uses-permission')

            flagged_count = 0
            for perm in permissions:
                # uses the namespace to extract the attribute
                perm_name = perm.get(f"{{{ns['android']}}}name")

                if perm_name in DANGEROUS_PERMISSIONS:
                    print(f"Found permission {perm_name}")
                    print(f"Risk of {DANGEROUS_PERMISSIONS[perm_name]}")
                    flagged_count += 1
            if flagged_count == 0:
                print("No dangerous permissions found.")

        except ET.ParseError:
            print(f"Failed to parse {app_name}")

if __name__ == "__main__":
    DECOMPILED_OUTPUT = "./DECOMPILED_APKS"
    analyze_manifest_permissions(DECOMPILED_OUTPUT)