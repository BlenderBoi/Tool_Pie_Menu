import bpy

bl_info = {
    "name": "Tool Pie Menu",
    "author": "BlenderBoi",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "Spacebar",
    "description": "Pie Menu for Tools",
    "warning": "",
    "doc_url": "",
    "category": "Tools",
}


class SCULPT_MT_Brush_Pie(bpy.types.Menu):

    bl_label = "Select Brush"

    @classmethod
    def poll(cls, context):
        if context.mode == "SCULPT":
            return True

    def draw(self, context):

        layout = self.layout

        pie = layout.menu_pie()

        pie.operator("wm.tool_set_by_id", text="Clay Strip", icon="BRUSH_CLAY_STRIPS").name = "builtin_brush.Clay Strips"

        pie.operator("wm.tool_set_by_id", text="Crease", icon="BRUSH_CREASE").name = "builtin_brush.Crease"


        pie.operator("wm.tool_set_by_id", text="Scrape", icon="BRUSH_SCRAPE").name = "builtin_brush.Scrape"

        pie.operator("wm.tool_set_by_id", text="Grab", icon="BRUSH_GRAB").name = "builtin_brush.Grab"

        pie.operator("wm.tool_set_by_id", text="Inflate", icon="BRUSH_INFLATE").name = "builtin_brush.Inflate"

        pie.operator("wm.tool_set_by_id", text="Draw Sharp", icon="BRUSH_SCULPT_DRAW").name = "builtin_brush.Draw Sharp"

        pie.operator("wm.tool_set_by_id", text="Blob", icon="BRUSH_BLOB").name = "builtin_brush.Blob"

        pie.operator("wm.tool_set_by_id", text="Pinch", icon="BRUSH_PINCH").name = "builtin_brush.Pinch"


class OBJECT_MT_Tool_Pie(bpy.types.Menu):

    bl_label = "Select Tool"

    @classmethod
    def poll(cls, context):
        if context.mode in ["OBJECT", "EDIT_MESH", "POSE", "EDIT_CURVE", "EDIT_ARMATURE"]:
            return True

    def draw(self, context):

        layout = self.layout

    	pie = layout.menu_pie()

    	pie.operator("wm.tool_set_by_id", text="Move", icon="EMPTY_ARROWS").name = "builtin.move"

    	pie.operator("wm.tool_set_by_id", text="Select Box", icon="SELECT_SET").name = "builtin.select_box"

    	pie.operator("wm.tool_set_by_id", text="Rotate", icon="ORIENTATION_GIMBAL").name = "builtin.rotate"

    	pie.operator("wm.tool_set_by_id", text="Scale", icon="CON_SIZELIKE").name = "builtin.scale"


        if context.mode == "EDIT_ARMATURE":
            pie.operator("wm.tool_set_by_id", text="Bone Size", icon="BONE_DATA").name = "builtin.bone_size"


classes = [SCULPT_MT_Brush_Pie, OBJECT_MT_Tool_Pie]

addon_keymaps = []

def register():

    for cls in classes:
        bpy.utils.register_class(cls)



    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon

    if kc:
        km = kc.keymaps.new(name = "3D View", space_type="VIEW_3D")
        kmi = km.keymap_items.new("wm.call_menu_pie", type="SPACE", value="PRESS")
        kmi.properties.name = "SCULPT_MT_Brush_Pie"
        addon_keymaps.append([km, kmi])

        km = kc.keymaps.new(name = "3D View", space_type="VIEW_3D")
        kmi = km.keymap_items.new("wm.call_menu_pie", type="SPACE", value="PRESS")
        kmi.properties.name = "OBJECT_MT_Tool_Pie"
        addon_keymaps.append([km, kmi])




def unregister():


    for cls in classes:
        bpy.utils.unregister_class(cls)


    addon_keymaps.clear()

if __name__ == "__main__":
    register()
