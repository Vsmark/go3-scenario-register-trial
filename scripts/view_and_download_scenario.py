import pandas as pd
import requests

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

def download_scenario(save_path="scenario_overview.xlsx"):
    # ✅ Use the same RAW URL
    xlsx_url = "https://raw.githubusercontent.com/Vsmark/go3-scenario-register-trial/main/scenario_overview.xlsx"

    try:
        response = requests.get(xlsx_url)
        response.raise_for_status()  # Raise error if download fails
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"✅ File downloaded successfully as '{save_path}'")
    except Exception as e:
        print("❌ Failed to download the scenario overview.")
        print("Error:", e)

# Optional: Auto-run if you call this file as a script
if __name__ == "__main__":
    view_scenario_register()
    # Uncomment the next line if you want to auto-download on script run
    download_scenario("downloaded_scenario_overview.xlsx")
