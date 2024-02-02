# AutoRenamingAssets Pipeline Tool Unreal Engine
Created an AutoRenaming tool for unreal engine, which renames the selected assets based on the prefix of naming conventions you define

E.g., if a material is named Glass, this tool would rename it to M_Glass.

## How To Use
* Clone the repo or download the zip
* Open the Unreal project
* Browse Content/Python/Scripts
* Right-click on the AutomatedTools Widget and select Run Editor Utility Widget
* It should pop up a new window with a button; dock it wherever you want
* Browse to Content/Python/Assets
* I already have created some material assets to test, but if you want to create your own, create Material/Material Instance/Niagara FX assets here
* Select all the assets and hit the "Rename Selected Assets" button from the windows that popped up
* It should rename all the assets with a prefix that I wrote in the Python script
* The Python script is RenamingAssets.py

