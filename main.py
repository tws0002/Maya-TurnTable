import maya.cmds as cmds

import maya.cmds as cmds


class Turntable:

    def __init__(self):
        self.obj = cmds.ls('object')[0]
        cmds.ctxEditMode()
        cmds.CenterPivot('{}'.format(self.obj))
        cmds.ctxEditMode()
        cmds.makeIdentity('{}'.format(self.obj), t=True, r=True)

    def sethdri(self):
        hdr_list = ['night', 'overcast', 'studio', 'sunny']
        cmds.setAttr('hdrDome.tex0', '\\\\192.168.3.6\\assets\_Software\Maya\Scripts\maya\\turntable\hdri\\{}.hdr'
                     .format(hdr_list[0]), type='string')

    def setbackground(self):
        status = 0
        if status == 0:
            cmds.setAttr('hdrDomeShape.background_enable', 1)
            status = 1
        else:
            cmds.setAttr('hdrDomeShape.background_enable', 0)
            status = 0

    def setcamera(self, *args):
        cmds.viewFit('maincamera', '{}'.format(self.obj))
        cmds.setKeyframe('{}'.format(self.obj))


insta = Turntable()


def createwindow(insta):
    # create a window
    if cmds.window('tableturn', ex=True):
        cmds.deleteUI('tableturn')
    cmds.window('tableturn')
    cmds.columnLayout()
    cmds.button(label='foofoo', command=insta.setcamera)
    cmds.showWindow('tableturn')


createwindow(insta)