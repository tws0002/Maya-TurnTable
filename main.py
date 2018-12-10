import maya.cmds as cmds


class Turntable:

    def __init__(self):
        def __init__(self):
            self.obj = cmds.ls('object')[0]
            cmds.ctxEditMode()
            cmds.CenterPivot('{}'.format(self.obj))
            cmds.ctxEditMode()
            cmds.setAttr('{}.translateX'.format(self.obj), 0)
            cmds.setAttr('{}.translateY'.format(self.obj), 0)
            cmds.setAttr('{}.translateZ'.format(self.obj), 0)

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

    def setcamera(self):
        cmds.viewFit('{}'.format(self.obj))

    def rotateobj(self):


# rotate 360 degrees
# variable for setting speed?


# bbox = cmds.exactWorldBoundingBox( 'pSphere1')


# fit camera to selected object
cmds.viewFit()