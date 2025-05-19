go3-scenario-register-trial
This repository is designed to help you understand the different scenarios in the ARPA 3 Grid Challenge. It contains two functions that you can easily use after importing the repository into your code editor.

Getting Started
Follow these steps to set up the repository in your Google Colab or code editor:
Importing Functions
----------------------------------------------------------------------
!git clone https://github.com/Vsmark/go3-scenario-register-trial.git
%cd go3-scenario-register-trial/scripts
!python view_scenario.py
----------------------------------------------------------------------
This function gets you the scenarios in your code editor.


Another function is analyze and display,(helps you run any of the scenario you put in)
---------------------Import this--------------------------------------
!git clone https://github.com/Vsmark/go3-scenario-register-trial.git
%cd go3-scenario-register-trial/scripts
!python building_register_arpa_grid_optimization_challenge_3.py
---------------------How to use--------------------------------------
from building_register_arpa_grid_optimization_challenge_3 import analyze_and_display
my_scenario = analyze_and_display(
    "path of the scenario (JSON File) ",
    " # Choose whatever name you want e.g. scenario112 # ")
---------------------------------------------------------------------

Notes
- Ensure that the path to your JSON file is correct.
- You can choose any name for your scenario as per your preference.
