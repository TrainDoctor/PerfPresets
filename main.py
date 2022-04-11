import os,sys
sys.path.insert(0, os.getcwd()+"/vdf")
print(sys.path[0])

class Plugin:
    # The name of the plugin. This string will be displayed in the Plugin menu
    name = "Performance Presets"
    # The name of the plugin author 
    author = "TrainDoctor"

    # If the plugin should be reloaded from a call to /plugins/reload or a file change
    hot_reload = False

    # The HTML file that will be loaded when selecting the plugin in the list
    main_view_html = "main_view.html"

    # The HTML file that will be used to display a widget in the plugin main page
    # Comment this out if you don't plan to use a tile view. This will make a button with your plugin name appear
    tile_view_html = ""

    # Return true if a game is currently active, else return false
    async def game_active(self, *args):
        pass
    
    async def save_preset(self, *args):
        pass
    
    async def load_preset(self, *args):
        pass
    
    async def delete_preset(self, *args):
        pass

    # A normal method. It can be called from JavaScript using call_plugin_function("method_2", argument1, argument2)
    # async def method_2(self, *args):
    #     pass

    # Asyncio-compatible long-running code, executed in a task when the plugin is loaded
    async def __main(self):
        pass