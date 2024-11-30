#!/usr/bin/env python3
import json
import os
import shutil
import subprocess
import sys
import tempfile
import tomllib
import urllib.request
from pathlib import Path

import common
from assemble_packwiz import SubmissionLockfileFormat
from common import Ansi


def main():
    modrinth_api = "https://api.modrinth.com/v2"
    repo_root = common.get_repo_root()
    constants_file = repo_root / "constants.jsonc"
    submissions_file = repo_root / "submissions.json"
    submission_lock_file = repo_root / "submissions-lock.json"
    packwiz_pack_toml = repo_root / "pack" / "pack.toml"
    packwiz = common.check_packwiz()
    
    common.fix_packwiz_pack(packwiz_pack_toml)

    constants = common.jsonc_at_home(common.read_file(constants_file))
    
    # Download the json
    event_name = constants["event"]
    if event_name == None:
        print(f"{Ansi.WARN}No event name defined. Treating it as if there were zero submissions{Ansi.RESET}")
        print(f"Was this unintentional? Check {constants_file.relative_to(repo_root)} and make sure it defines \"event\"")
        submission_data = []
    else:
        submissions_url = f"https://platform.modfest.net/event/{event_name}/submissions"
        with urllib.request.urlopen(submissions_url) as submissions:
            submission_data = json.load(submissions)

    credits = []
    for s in submission_data:
        credits.append({
            "discipline": s["name"],
            "titles": [
                {
                    "title": "author",
                    "names": s["authors"]
                }
            ]
        })
    print(json.dumps(credits))

if __name__ == "__main__":
    main()
