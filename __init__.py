import bpy

bl_info = {
    "name": "Tool Pie Menu",
    "author": "BlenderBoi",
    "version": (1, 1),
    "blender": (2, 80, 0),
    "location": "Spacebar",
    "description": "Pie Menu for Tools",
    "warning": "",
    "doc_url": "",
    "category": "Tools",
}



class PAINT_MT_Brush_Pie(bpy.types.Menu):

    bl_label = "Select Brush"

    @classmethod
    def poll(cls, context):
        if context.mode == "PAINT_TEXTURE":
            return True

    def draw(self, context):

        layout = self.layout

        pie = layout.menu_pie()



        pie.operator("wm.tool_set_by_id", text="Draw").name = "builtin_brush.Draw"
        pie.operator("wm.tool_set_by_id", text="Soften").name = "builtin_brush.Soften"
        pie.separator()
        pie.separator()

        pie.operator("wm.tool_set_by_id", text="Clone").name = "builtin_brush.Clone"
        pie.operator("wm.tool_set_by_id", text="Smear").name = "builtin_brush.Smear"

        pie.operator("wm.tool_set_by_id", text="Fill").name = "builtin_brush.Fill"
        pie.operator("wm.tool_set_by_id", text="Mask").name = "builtin_brush.Mask"



class VERTEX_MT_Brush_Pie(bpy.types.Menu):

    bl_label = "Select Brush"

    @classmethod
    def poll(cls, context):
        if context.mode == "PAINT_VERTEX":
            return True

    def draw(self, context):

        layout = self.layout

        pie = layout.menu_pie()



        pie.operator("wm.tool_set_by_id", text="Draw").name = "builtin_brush.Draw"
        pie.operator("wm.tool_set_by_id", text="Blur").name = "builtin_brush.Blur"
        pie.operator("wm.tool_set_by_id", text="Average").name = "builtin_brush.Average"
        pie.operator("wm.tool_set_by_id", text="Smear").name = "builtin_brush.Smear"




class GREASEPENCIL_VERTEX_MT_Brush_Pie(bpy.types.Menu):

    bl_label = "Select Brush"

    @classmethod
    def poll(cls, context):
        if context.mode == "VERTEX_GPENCIL":
            return True

    def draw(self, context):

        layout = self.layout

        pie = layout.menu_pie()



        pie.operator("wm.tool_set_by_id", text="Draw").name = "builtin_brush.Draw"
        pie.operator("wm.tool_set_by_id", text="Blur").name = "builtin_brush.Blur"
        pie.operator("wm.tool_set_by_id", text="Replace").name = "builtin_brush.Replace"
        pie.operator("wm.tool_set_by_id", text="Smear").name = "builtin_brush.Smear"




class GREASEPENCIL_EDIT_MT_Brush_Pie(bpy.types.Menu):

    bl_label = "Select Brush"

    @classmethod
    def poll(cls, context):
        if context.mode == "EDIT_GPENCIL":
            return True

    def draw(self, context):

        layout = self.layout

        pie = layout.menu_pie()



        pie.operator("wm.tool_set_by_id", text="Select Box", icon="SELECT_SET").name = "builtin.select_box"
        pie.operator("wm.tool_set_by_id", text="Move", icon="EMPTY_ARROWS").name = "builtin.move"
        pie.operator("wm.tool_set_by_id", text="Rotate", icon="ORIENTATION_GIMBAL").name = "builtin.rotate"
        pie.operator("wm.tool_set_by_id", text="Scale", icon="CON_SIZELIKE").name = "builtin.scale"

        pie.operator("wm.tool_set_by_id", text="Radius").name = "builtin.radius"

        pie.operator("wm.tool_set_by_id", text="Interpolate").name = "builtin.interpolate"

        pie.operator("wm.tool_set_by_id", text="Extrude").name = "builtin.extrude"

        pie.operator("wm.tool_set_by_id", text="Transform Fill").name = "builtin.transform_fill"





class GREASEPENCIL_WEIGHT_MT_Brush_Pie(bpy.types.Menu):

    bl_label = "Select Brush"

    @classmethod
    def poll(cls, context):
        if context.mode == "WEIGHT_GPENCIL":
            return True

    def draw(self, context):

        layout = self.layout

        pie = layout.menu_pie()

        pie.operator("wm.tool_set_by_id", text="Weight").name = "builtin_brush.Weight"

class GREASEPENCIL_DRAW_MT_Brush_Pie(bpy.types.Menu):

    bl_label = "Select Brush"

    @classmethod
    def poll(cls, context):
        if context.mode == "PAINT_GPENCIL":
            return True

    def draw(self, context):

        layout = self.layout

        pie = layout.menu_pie()

        pie.operator("wm.tool_set_by_id", text="Draw").name = "builtin_brush.Draw"
        pie.operator("wm.tool_set_by_id", text="Erase").name = "builtin_brush.Erase"
        pie.separator()
        #pie.prop(context.scene.tool_settings, "use_keyframe_insert_auto", text="Auto Key", icon="RADIOBUT_ON")
        pie.separator()
        pie.operator("wm.tool_set_by_id", text="Fill").name = "builtin_brush.Fill"
        pie.operator("wm.tool_set_by_id", text="Eyedropper").name = "builtin.eyedropper"

        pie.operator("wm.tool_set_by_id", text="Tint").name = "builtin_brush.Tint"

        pie.operator("wm.tool_set_by_id", text="Cutter").name = "builtin.cutter"

class GREASEPENCIL_SCULPT_MT_Brush_Pie(bpy.types.Menu):

    bl_label = "Select Brush"

    @classmethod
    def poll(cls, context):
        if context.mode == "SCULPT_GPENCIL":
            return True

    def draw(self, context):

        layout = self.layout

        pie = layout.menu_pie()


        pie.operator("wm.tool_set_by_id", text="Grab").name = "builtin_brush.Grab"

        pie.operator("wm.tool_set_by_id", text="Thickness").name = "builtin_brush.Thickness"

        pie.operator("wm.tool_set_by_id", text="Randomize").name = "builtin_brush.Randomize"
        pie.operator("wm.tool_set_by_id", text="Twist").name = "builtin_brush.Twist"
        pie.operator("wm.tool_set_by_id", text="Push").name = "builtin_brush.Push"

        pie.operator("wm.tool_set_by_id", text="Smooth").name = "builtin_brush.Smooth"

        pie.operator("wm.tool_set_by_id", text="Pinch").name = "builtin.Pinch"
#        pie.operator("wm.tool_set_by_id", text="Clone").name = "builtin_brush.Clone"

        pie.operator("wm.tool_set_by_id", text="Strength").name = "builtin_brush.Strength"



class WEIGHT_MT_Tool_Pie(bpy.types.Menu):

    bl_label = "Select Brush"

    @classmethod
    def poll(cls, context):
        if context.mode == "PAINT_WEIGHT":
            return True

    def draw(self, context):

        layout = self.layout

        pie = layout.menu_pie()

        pie.operator("wm.tool_set_by_id", text="Draw").name = "builtin_brush.Draw"

        pie.operator("wm.tool_set_by_id", text="Blur").name = "builtin_brush.Blur"

        pie.separator()
        pie.separator()
        pie.operator("wm.tool_set_by_id", text="Sample").name = "builtin.sample_weight"
        pie.operator("wm.tool_set_by_id", text="Smear").name = "builtin_brush.Smear"
        pie.operator("wm.tool_set_by_id", text="Gradient").name = "builtin.gradient"
        pie.operator("wm.tool_set_by_id", text="Average").name = "builtin_brush.Average"

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
        if context.mode in ["OBJECT", "EDIT_MESH", "POSE", "EDIT_CURVE", "EDIT_ARMATURE", "EDIT_LATTICE"]:
            return True

    def draw(self, context):

        layout = self.layout

        pie = layout.menu_pie()

        pie.operator("wm.tool_set_by_id", text="Select Box", icon="SELECT_SET").name = "builtin.select_box"
        pie.operator("wm.tool_set_by_id", text="Move", icon="EMPTY_ARROWS").name = "builtin.move"


        pie.operator("wm.tool_set_by_id", text="Rotate", icon="ORIENTATION_GIMBAL").name = "builtin.rotate"

        pie.operator("wm.tool_set_by_id", text="Scale", icon="CON_SIZELIKE").name = "builtin.scale"


        if context.mode == "EDIT_ARMATURE":
            pie.operator("wm.tool_set_by_id", text="Bone Size").name = "builtin.bone_size"
            pie.operator("wm.tool_set_by_id", text="Extrude").name = "builtin.extrude"
            pie.operator("wm.tool_set_by_id", text="Bone Roll").name = "builtin.roll"
            pie.operator("wm.tool_set_by_id", text="Shear").name = "builtin.shear"

        if context.mode == "POSE":
            pie.separator()
            pie.operator("wm.tool_set_by_id", text="Breakdowner").name = "builtin.breakdowner"

        if context.mode == "EDIT_LATTICE":
            pie.separator()
            pie.separator()
            pie.separator()
            pie.operator("wm.tool_set_by_id", text="Shear").name = "builtin.shear"


        if context.mode == "EDIT_CURVE":
            pie.operator("wm.tool_set_by_id", text="Radius").name = "builtin.radius"
            pie.operator("wm.tool_set_by_id", text="Draw").name = "builtin.draw"
            pie.operator("wm.tool_set_by_id", text="Tilt").name = "builtin.tilt"
            pie.operator("wm.tool_set_by_id", text="Extrude").name = "builtin.extrude"

classes = [VERTEX_MT_Brush_Pie, PAINT_MT_Brush_Pie, WEIGHT_MT_Tool_Pie, GREASEPENCIL_VERTEX_MT_Brush_Pie, GREASEPENCIL_EDIT_MT_Brush_Pie, GREASEPENCIL_WEIGHT_MT_Brush_Pie, GREASEPENCIL_SCULPT_MT_Brush_Pie, GREASEPENCIL_DRAW_MT_Brush_Pie, SCULPT_MT_Brush_Pie, OBJECT_MT_Tool_Pie]

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


        km = kc.keymaps.new(name = "3D View", space_type="VIEW_3D")
        kmi = km.keymap_items.new("wm.call_menu_pie", type="SPACE", value="PRESS")
        kmi.properties.name = "WEIGHT_MT_Tool_Pie"
        addon_keymaps.append([km, kmi])

        km = kc.keymaps.new(name = "3D View", space_type="VIEW_3D")
        kmi = km.keymap_items.new("wm.call_menu_pie", type="SPACE", value="PRESS")
        kmi.properties.name = "GREASEPENCIL_DRAW_MT_Brush_Pie"
        addon_keymaps.append([km, kmi])


        km = kc.keymaps.new(name = "3D View", space_type="VIEW_3D")
        kmi = km.keymap_items.new("wm.call_menu_pie", type="SPACE", value="PRESS")
        kmi.properties.name = "GREASEPENCIL_SCULPT_MT_Brush_Pie"
        addon_keymaps.append([km, kmi])


        km = kc.keymaps.new(name = "3D View", space_type="VIEW_3D")
        kmi = km.keymap_items.new("wm.call_menu_pie", type="SPACE", value="PRESS")
        kmi.properties.name = "GREASEPENCIL_WEIGHT_MT_Brush_Pie"
        addon_keymaps.append([km, kmi])


        km = kc.keymaps.new(name = "3D View", space_type="VIEW_3D")
        kmi = km.keymap_items.new("wm.call_menu_pie", type="SPACE", value="PRESS")
        kmi.properties.name = "GREASEPENCIL_EDIT_MT_Brush_Pie"
        addon_keymaps.append([km, kmi])


        km = kc.keymaps.new(name = "3D View", space_type="VIEW_3D")
        kmi = km.keymap_items.new("wm.call_menu_pie", type="SPACE", value="PRESS")
        kmi.properties.name = "GREASEPENCIL_VERTEX_MT_Brush_Pie"
        addon_keymaps.append([km, kmi])


        km = kc.keymaps.new(name = "3D View", space_type="VIEW_3D")
        kmi = km.keymap_items.new("wm.call_menu_pie", type="SPACE", value="PRESS")
        kmi.properties.name = "PAINT_MT_Brush_Pie"
        addon_keymaps.append([km, kmi])


        km = kc.keymaps.new(name = "3D View", space_type="VIEW_3D")
        kmi = km.keymap_items.new("wm.call_menu_pie", type="SPACE", value="PRESS")
        kmi.properties.name = "VERTEX_MT_Brush_Pie"
        addon_keymaps.append([km, kmi])

def unregister():


    for cls in classes:
        bpy.utils.unregister_class(cls)


    addon_keymaps.clear()

if __name__ == "__main__":
    register()
