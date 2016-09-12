import maya.mel as mel #Allows for evaluation of MEL
import maya.cmds as mc

#Clears Rotation on a List of Objects
def clearRotate(list):
    for i in list:
        if mc.getAttr(i + '.rotateX', lock=True) == False:
            mc.setAttr(i + '.rotateX', 0)
        if mc.getAttr(i + '.rotateY', lock=True) == False:
            mc.setAttr(i + '.rotateY', 0)
        if mc.getAttr(i + '.rotateZ', lock=True) == False:
            mc.setAttr(i + '.rotateZ', 0) 

#Clears Translation on a List of Objects
def clearTranslate(list):
    for i in list:
        if mc.getAttr(i + '.translateX', lock=True) == False:
            mc.setAttr(i + '.translateX', 0)
        if mc.getAttr(i + '.translateY', lock=True) == False:    
            mc.setAttr(i + '.translateY', 0)
        if mc.getAttr(i + '.translateZ', lock=True) == False:
            mc.setAttr(i + '.translateZ', 0)

#Selects/Returns Full Rig
def selectRig():
    #Determine Body Controls
    ArmR = [
    'ten_rig_main_r_shoulder_CTL',
    'ten_rig_main_r_armRoot_FK_CTL',
    'ten_rig_main_r_armMid_FK_CTL',
    'ten_rig_main_r_armEnd_FK_CTL']
    HandR = [
    'ten_rig_main_r_thumb_CTL',
    'ten_rig_main_r_index_CTL',
    'ten_rig_main_r_middle_CTL',
    'ten_rig_main_r_ring_CTL',
    'ten_rig_main_r_pinky_CTL',
    'ten_rig_main_r_hand_CTL']
    ArmL = [
    'ten_rig_main_l_shoulder_CTL',
    'ten_rig_main_l_armRoot_FK_CTL',
    'ten_rig_main_l_armMid_FK_CTL',
    'ten_rig_main_l_armEnd_FK_CTL']
    HandL = [
    'ten_rig_main_l_thumb_CTL',
    'ten_rig_main_l_index_CTL',
    'ten_rig_main_l_middle_CTL',
    'ten_rig_main_l_ring_CTL',
    'ten_rig_main_l_pinky_CTL',
    'ten_rig_main_l_hand_CTL']
    Torso = [
    'ten_rig_main_m_neck_CTL',
    'ten_rig_main_m_IKSpinyThing_CTL',
    'ten_rig_main_m_spine_FKstomach_CTL',
    'ten_rig_main_m_spine_hips_CTL',
    'ten_rig_main_m_COG_CTL']
    LegR = [
    'ten_rig_main_r_legIK_CTL',
    'ten_rig_main_r_legPV_CTL',
    'ten_rig_main_r_foot_CTL']
    LegL = [
    'ten_rig_main_l_legIK_CTL',
    'ten_rig_main_l_legPV_CTL',
    'ten_rig_main_l_foot_CTL']

    #Determine Head/Face Controls
    Head = [
    'ten_rig_main_m_head_CTL',
    'ten_rig_main_head_cc_01',
    'ten_rig_main_head_bottom_squash_cc_01',
    'ten_rig_main_head_mid_squash_cc_01',
    'ten_rig_main_head_top_squash_cc_01']
    Ears = [
    'ten_rig_main_ear_r_cc_01',
    'ten_rig_main_earlobe_r_cc_01',
    'ten_rig_main_ear_l_cc_01',
    'ten_rig_main_earlobe_l_cc_01']
    Eyes = [
    'ten_rig_main_eye_r_full_cc_01',
    'ten_rig_main_eye_l_full_cc_01',
    'ten_rig_main_r_eyelid_GRP|ten_rig_main_l_upper_eyelid_CTL_os_GRP|ten_rig_main_l_upper_eyelid_CTL',
    'ten_rig_main_l_eyelid_GRP|ten_rig_main_l_upper_eyelid_CTL_os_GRP|ten_rig_main_l_upper_eyelid_CTL',
    'ten_rig_main_eye_r_cc_01',
    'ten_rig_main_eye_l_cc_01',
    'ten_rig_main_r_lower_eyelid_CTL',
    'ten_rig_main_l_lower_eyelid_CTL']
    Lookat = [
    'ten_rig_main_m_eyes_CTL',
    'ten_rig_main_r_eye_CTL',
    'ten_rig_main_l_eye_CTL']
    Brow = [
    'ten_rig_main_eyebrow_r_full_cc_01',
    'ten_rig_main_eyebrow_r_OUT_cc_01',
    'ten_rig_main_eyebrow_r_MID_cc_01',
    'ten_rig_main_eyebrow_r_INN_cc_01',
    'ten_rig_main_eyebrow_l_full_cc_01',
    'ten_rig_main_eyebrow_l_OUT_cc_01',
    'ten_rig_main_eyebrow_l_MID_cc_01',
    'ten_rig_main_eyebrow_l_INN_cc_01']
    Squint = [
    'ten_rig_main_squint_r_full_cc_01',
    'ten_rig_main_squint_r_OUT_cc_01',
    'ten_rig_main_squint_r_MID_cc_01',
    'ten_rig_main_squint_r_INN_cc_01',
    'ten_rig_main_squint_l_full_cc_01',
    'ten_rig_main_squint_l_OUT_cc_01',
    'ten_rig_main_squint_l_MID_cc_01',
    'ten_rig_main_squint_l_INN_cc_01']
    Nose = [
    'ten_rig_main_nose_full_cc_01',
    'ten_rig_main_nostril_sneer_r_cc_01',
    'ten_rig_main_nostril_sneer_l_cc_01']
    Cheeks = [
    'ten_rig_main_cheek_r_cc_01',
    'ten_rig_main_cheek_l_cc_01']
    Mouth = [
    'ten_rig_main_mouth_full_cc_01',
    'ten_rig_main_lips_r_corner_cc_01',
    'ten_rig_main_lips_l_corner_cc_01',
    'ten_rig_main_upper_lip_full_cc_01',
    'ten_rig_main_upper_lip_RGT_cc_01',
    'ten_rig_main_upper_lip_MID_cc_01',
    'ten_rig_main_upper_lip_LFT_cc_01',
    'ten_rig_main_lower_lip_full_cc_01',
    'ten_rig_main_lower_lip_RGT_cc_01',
    'ten_rig_main_lower_lip_MID_cc_01',
    'ten_rig_main_lower_lip_LFT_cc_01']
    Chin = [
    'ten_rig_main_m_jaw_CTL',
    'ten_rig_main_jaw_cc_01']
    
    #Assemble Body Rig
    fullRig = ArmR + HandR + ArmL + HandL + Torso + LegR + LegL
    #Assemble Head/Facial Rig
    fullRig += Head + Ears + Eyes + Squint + Nose + Cheeks + Mouth + Chin

    #Create Selection from 'fullRig'
    mc.select(fullRig, replace=True)
    return fullRig

def APose():
    mc.rotate(0, 0, -45, 'ten_rig_main_r_armRoot_FK_CTL')
    mc.rotate(0, 0, -45, 'ten_rig_main_l_armRoot_FK_CTL')

def setKey(fullRig):
    #Key Translation
    mc.setKeyframe(fullRig, at='translateX')
    mc.setKeyframe(fullRig, at='translateY')
    mc.setKeyframe(fullRig, at='translateZ')
    #Key Rotation
    mc.setKeyframe(fullRig, at='rotateX')
    mc.setKeyframe(fullRig, at='rotateY')
    mc.setKeyframe(fullRig, at='rotateZ')
    
def alignToRigLoc(object):
    mc.setAttr(object + '.translateX', mc.getAttr('ten_rig_main_m_global_CTL.translateX'))
    mc.setAttr(object + '.translateY', mc.getAttr('ten_rig_main_m_global_CTL.translateY'))
    mc.setAttr(object + '.translateZ', mc.getAttr('ten_rig_main_m_global_CTL.translateZ'))
    
    mc.setAttr(object + '.rotateX', mc.getAttr('ten_rig_main_m_global_CTL.rotateX'))
    mc.setAttr(object + '.rotateY', mc.getAttr('ten_rig_main_m_global_CTL.rotateY'))
    mc.setAttr(object + '.rotateZ', mc.getAttr('ten_rig_main_m_global_CTL.rotateZ'))
    
##############
# BEGIN CODE #
##############

#Set current time to -20
mc.currentTime(-20)

#Collect Full Rig
fullRig = selectRig()

#Set TPose (Clear Transformations)
clearRotate(fullRig)
clearTranslate(fullRig)

#Set APose (Adjust Arms)
APose()

#Set Keyframes
setKey(fullRig)

#Import/Move Cloth OBJ
mc.file('/groups/dusk/production/assets/ten_robe_sim/model/main/ten_robe_sim_model_main.mb', i=True)
alignToRigLoc('ten_Robe_Sim')
alignToRigLoc('ten_Pants_Sim')
alignToRigLoc('ten_Collider')

#Wrap Ten Collider to Rig
mc.select('ten_Collider', replace=True)
mc.select('ten_rig_main_Ten_Skin_RENDER', add=True)
mc.CreateWrap()

#Set Up Collider
mc.select('ten_Collider', replace=True)
mel.eval('makeCollideNCloth;')

#Set Up Cloth
mc.select('ten_Robe_Sim', replace=True)
mel.eval('createNCloth 0;')

#Set Cloth Parameters
mc.setAttr('nClothShape1.thickness', 0.003)
mc.setAttr('nClothShape1.stretchResistance', 200)
mc.setAttr('nClothShape1.friction', .3)
mc.setAttr('nClothShape1.bendAngleDropoff', 0.4)
mc.setAttr('nClothShape1.pointMass', 0.6)
mc.setAttr('nClothShape1.damp', 0.8)
mc.setAttr('nClothShape1.scalingRelation', 1) #Scaling Relation to "Object Space"

#Set Nucleus Parameters
mc.setAttr('nucleus1.startFrame', -20)
mc.setAttr('nucleus1.spaceScale', 0.45)
mc.setAttr('nucleus1.subSteps', 6)
mc.setAttr('nucleus1.maxCollisionIterations', 8)

#Set Up Pin Constraints
mc.select('ten_Robe_Sim.vtx[2310:2334]', 'ten_Robe_Sim.vtx[3088:3111]', replace=True)
mc.select('ten_Robe_Sim.vtx[699:701]', 'ten_Robe_Sim.vtx[1652]', 'ten_Robe_Sim.vtx[1691]', 'ten_Robe_Sim.vtx[1694]', 'ten_Robe_Sim.vtx[1725]', add=True)
mc.select('ten_Collider', toggle=True)
mel.eval('createNConstraint pointToSurface 0;')

#Resources:
    #stackoverflow.com/questions/27104218/maya-different-behaviours-in-standalone-and-embedded-mode
