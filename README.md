go3-scenario-register-trial
This repository helps you explore different scenarios in the ARPA 3 Grid Challenge. It provides two easy-to-use functions to load and analyze scenarios.

Getting Started
Clone the repository using the command:
!git clone https://github.com/Vsmark/go3-scenario-register-trial.git

Change directory to the scripts folder:
%cd go3-scenario-register-trial/scripts

Run view_scenario.py to see the available scenarios:
!python view_scenario.py

Analyze and Display a Scenario
Clone the repository and go to the scripts folder (if you haven’t already):
!git clone https://github.com/Vsmark/go3-scenario-register-trial.git
%cd go3-scenario-register-trial/scripts

Run the main analysis script:
!python building_register_arpa_grid_optimization_challenge_3.py

In your Python code, import the function and use it like this:
from building_register_arpa_grid_optimization_challenge_3 import analyze_and_display

my_scenario = analyze_and_display("path/to/your/scenario.json", "scenario_name")

Notes
Make sure the path to your scenario JSON file is correct.

You can choose any name for your scenario.

