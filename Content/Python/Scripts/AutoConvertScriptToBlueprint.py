import unreal

def get_selected_assets():
    
    editor_utility = unreal.EditorUtilityLibrary()
    selected_assets = editor_utility.get_selected_assets()
    
    return selected_assets


def make_blueprint(assets):
    # Specify the path where you want to create the Blueprint
    blueprint_path = "Content\Blueprints"

    # Load the class header file
    cpp_class = unreal.HeaderFileFunctionLibrary.load_header_file(assets)

    if cpp_class:
        # Create the Blueprint class from the C++ class
        unreal.EditorUtilityLibrary.create_blueprint(cpp_class, blueprint_path)
        unreal.log("Blueprint created successfully.")
    else:
        unreal.log_warning("C++ class header file not found.")

def run():
    selected_assets = get_selected_assets()
    make_blueprint(selected_assets)


run()