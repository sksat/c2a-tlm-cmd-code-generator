# coding: UTF-8
"""
python 3.7以上を要求
"""

import json
import pprint
import sys

import my_mod.load_db
import my_mod.cmd_def
import my_mod.tlm_def
import my_mod.gstos


# import os.path
# import msvcrt               # Enter不要な入力用
# import subprocess


# 環境変数
DEBUG = 0
# 0 : Release
# 1 : all
SETTING_FILE_PATH = "settings.json"

def main():
    with open(SETTING_FILE_PATH, mode='r') as fh:
        settings = json.load(fh)
    # print(settings["c2a_root_dir"]);

    cmd_db = my_mod.load_db.LoadCmdCSV(settings)
    tlm_db = my_mod.load_db.LoadTlmCSV(settings)
    # pprint.pprint(cmd_db)
    # pprint.pprint(tlm_db)
    # print(tlm_db)

    my_mod.cmd_def.GenerateCmdDef(settings, cmd_db['sgc'])
    my_mod.cmd_def.GenerateBctDef(settings, cmd_db['bct'])
    my_mod.tlm_def.GenerateTlmDef(settings, tlm_db)
    if settings["is_generated_sib"]:
        my_mod.gstos.GenerateGstosFiles(settings, cmd_db['sgc'], tlm_db)

    print("Completed!")
    sys.exit(0)


if __name__ == '__main__':
    main()

