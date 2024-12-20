import sys
import os.path
import zipfile

from resolve_download import *
from build_metainfo import *

if __name__ == "__main__":
    is_studio = '--studio' in sys.argv
    is_beta = '--beta' in sys.argv
    app_tag = "davinci-resolve-studio" if is_studio else "davinci-resolve"

    print("Building for tag " + app_tag)

    if os.getenv("RESOLVE_DOWNLOAD_ID") is not None:
        download_id = os.getenv("RESOLVE_DOWNLOAD_ID")
    else:
        print("Requesting version information...")
        (version, release_id, download_id) = get_latest_version_information(
            refer_id='77ef91f67a9e411bbbe299e595b4cfcc',
            app_tag=app_tag,
            stable=is_beta is False,
        )

    if not os.path.isfile("resolve.zip"):
        print(f"Download latest version of DaVinci Resolve{' Studio' if is_studio else ''}...")
        download_using_id(download_id)
    else:
        print(f"Using user supplied resolve.zip (testing)")

    print("Extracting resolve installation...")
    with zipfile.ZipFile("./resolve.zip", 'r') as zip_file:
        zip_file.extractall('.')

    print(f"Building meta info...")
    build_metainfo(
        app_id='com.blackmagic.ResolveStudio' if is_studio else 'com.blackmagic.Resolve',
        app_description="DaVinci Resolve Studio" if is_studio else 'DaVinci Resolve',
        app_tag=app_tag,
    )
