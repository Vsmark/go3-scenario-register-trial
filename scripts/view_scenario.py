# -*- coding: utf-8 -*-
"""Github code.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lVKaKh9EyRlHwDUh6UFrrzJG1xoQCZJc
"""

import pandas as pd

def view_scenario_register():
    # ✅ Use the RAW link for the .xlsx file
    xlsx_url = "https://raw.githubusercontent.com/Vsmark/go3-scenario-register-trial/main/scenario_register.xlsx"

    try:
        df = pd.read_excel(xlsx_url, index_col=0)
        print("✅ Successfully loaded the scenario register!\n")
        print(df.head(10))
    except Exception as e:
        print("❌ Could not load the scenario register.")
        print("Error:", e)

if __name__ == "__main__":
    view_scenario_register()

