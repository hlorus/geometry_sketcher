from bpy.types import Operator, Context
from bpy.props import BoolProperty
from bpy.utils import register_classes_factory

from ..declarations import Operators
from ..solver import Solver
from ..converters import update_geometry


class View3D_OT_update(Operator):
    """Solve all sketches and update converted geometry"""

    bl_idname = Operators.Update
    bl_label = "Force Update"

    solve: BoolProperty(name="Solve", default=True, description="Solve the sketches before converting the geometry")

    def execute(self, context: Context):
        if self.solve:
            solver = Solver(context, None, all=True)
            solver.solve()

        update_geometry(context.scene, self)
        return {"FINISHED"}


register, unregister = register_classes_factory((View3D_OT_update,))
