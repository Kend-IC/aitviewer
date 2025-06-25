# Copyright (C) 2023  ETH Zurich, Manuel Kaufmann, Velko Vechev, Dario Mylonopoulos
# from aitviewer.renderables.smpl import SMPLSequence
# from aitviewer.viewer import Viewer

# if __name__ == "__main__":
#     v = Viewer()
#     v.scene.add(SMPLSequence.t_pose())
#     v.run()

from aitviewer.renderables.smpl import SMPLSequence
from aitviewer.configuration import CONFIG as C
from aitviewer.viewer import Viewer
from aitviewer.renderables.smpl import SMPLLayer

C.window_type = "pyglet"

if __name__ == "__main__":
    smpl_layer = SMPLLayer(
        model_type="smplx",
        gender="male"
    )

    v = Viewer()
    v.scene.add(SMPLSequence.t_pose(smpl_layer=smpl_layer))
    v.run()