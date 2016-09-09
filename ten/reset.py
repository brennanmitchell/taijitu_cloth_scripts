import maya.cmds as mc

ten_body_controls = [
    "ten_rig_main_l_armEnd_FK_CTL",
    "ten_rig_main_l_armIK_CTL",
    "ten_rig_main_l_armMid_FK_CTL",
    "ten_rig_main_l_armPV_CTL",
    "ten_rig_main_l_armRoot_FK_CTL",
    "ten_rig_main_l_arm_switch_CTL",
    "ten_rig_main_l_eye_CTL",
    "ten_rig_main_l_foot_CTL",
    "ten_rig_main_l_hand_CTL",
    "ten_rig_main_l_index_CTL",
    "ten_rig_main_l_legIK_CTL",
    "ten_rig_main_l_legPV_CTL",
    "ten_rig_main_l_leg_end_FK_CTL",
    "ten_rig_main_l_leg_mid_FK_CTL",
    "ten_rig_main_l_leg_root_FK_CTL",
    "ten_rig_main_l_lower_eyelid_CTL",
    "ten_rig_main_l_middle_CTL",
    "ten_rig_main_l_pinky_CTL",
    "ten_rig_main_l_ring_CTL",
    "ten_rig_main_l_shoulder_CTL",
    "ten_rig_main_l_thumb_CTL",
    "ten_rig_main_m_COG_CTL",
    "ten_rig_main_m_IKSpinyThing_CTL",
    "ten_rig_main_m_eyes_CTL",
    "ten_rig_main_m_global_CTL",
    "ten_rig_main_m_head_CTL",
    "ten_rig_main_m_jaw_CTL",
    "ten_rig_main_m_mouth_position_CTL",
    "ten_rig_main_m_neck_CTL",
    "ten_rig_main_m_spine_FKchest_CTL",
    "ten_rig_main_m_spine_FKstomach_CTL",
    "ten_rig_main_m_spine_hips_CTL",
    "ten_rig_main_r_armEnd_FK_CTL",
    "ten_rig_main_r_armIK_CTL",
    "ten_rig_main_r_armMid_FK_CTL",
    "ten_rig_main_r_armPV_CTL",
    "ten_rig_main_r_armRoot_FK_CTL",
    "ten_rig_main_r_arm_switch_CTL",
    "ten_rig_main_r_eye_CTL",
    "ten_rig_main_r_foot_CTL",
    "ten_rig_main_r_hand_CTL",
    "ten_rig_main_r_index_CTL",
    "ten_rig_main_r_legIK_CTL",
    "ten_rig_main_r_legPV_CTL",
    "ten_rig_main_r_leg_end_FK_CTL",
    "ten_rig_main_r_leg_mid_FK_CTL",
    "ten_rig_main_r_leg_root_FK_CTL",
    "ten_rig_main_r_lower_eyelid_CTL",
    "ten_rig_main_r_middle_CTL",
    "ten_rig_main_r_mouth_corner_CTL",
    "ten_rig_main_r_pinky_CTL",
    "ten_rig_main_r_ring_CTL",
    "ten_rig_main_r_shoulder_CTL",
    "ten_rig_main_r_thumb_CTL"]

ten_head_controls = [
    "ten_rig_main_cheek_l_cc_01",
    "ten_rig_main_cheek_r_cc_01",
    "ten_rig_main_ear_l_cc_01",
    "ten_rig_main_ear_r_cc_01",
    "ten_rig_main_earlobe_l_cc_01",
    "ten_rig_main_earlobe_r_cc_01",
    "ten_rig_main_eye_l_cc_01",
    "ten_rig_main_eye_l_full_cc_01",
    "ten_rig_main_eye_r_cc_01",
    "ten_rig_main_eye_r_full_cc_01",
    "ten_rig_main_eyebrow_l_INN_cc_01",
    "ten_rig_main_eyebrow_l_MID_cc_01",
    "ten_rig_main_eyebrow_l_OUT_cc_01",
    "ten_rig_main_eyebrow_l_full_cc_01",
    "ten_rig_main_eyebrow_r_INN_cc_01",
    "ten_rig_main_eyebrow_r_MID_cc_01",
    "ten_rig_main_eyebrow_r_OUT_cc_01",
    "ten_rig_main_eyebrow_r_full_cc_01",
    "ten_rig_main_head_bottom_squash_cc_01",
    "ten_rig_main_head_cc_01","ten_rig_main_head_mid_squash_cc_01",
    "ten_rig_main_head_top_squash_cc_01",
    "ten_rig_main_intermediate_ear_l_cc_01",
    "ten_rig_main_intermediate_ear_r_cc_01",
    "ten_rig_main_intermediate_earlobe_l_cc_01",
    "ten_rig_main_intermediate_earlobe_r_cc_01",
    "ten_rig_main_intermediate_eye_l_full_cc_01",
    "ten_rig_main_intermediate_eye_r_full_cc_01",
    "ten_rig_main_intermediate_head_bottom_squash_cc_01",
    "ten_rig_main_intermediate_head_mid_squash_cc_01",
    "ten_rig_main_intermediate_head_top_squash_cc_01",
    "ten_rig_main_intermediate_mouth_full_cc_01",
    "ten_rig_main_jaw_cc_01",
    "ten_rig_main_lips_l_corner_cc_01",
    "ten_rig_main_lips_r_corner_cc_01",
    "ten_rig_main_lower_lip_LFT_cc_01",
    "ten_rig_main_lower_lip_MID_cc_01",
    "ten_rig_main_lower_lip_RGT_cc_01",
    "ten_rig_main_lower_lip_full_cc_01",
    "ten_rig_main_mouth_full_cc_01",
    "ten_rig_main_nose_full_cc_01",
    "ten_rig_main_nose_tip_cc_01",
    "ten_rig_main_nostril_sneer_l_cc_01",
    "ten_rig_main_nostril_sneer_r_cc_01",
    "ten_rig_main_pupil_l_cc_01",
    "ten_rig_main_pupil_r_cc_01",
    "ten_rig_main_squint_l_INN_cc_01",
    "ten_rig_main_squint_l_MID_cc_01",
    "ten_rig_main_squint_l_OUT_cc_01",
    "ten_rig_main_squint_l_cc_01",
    "ten_rig_main_squint_l_full_cc_01",
    "ten_rig_main_squint_r_INN_cc_01",
    "ten_rig_main_squint_r_MID_cc_01",
    "ten_rig_main_squint_r_OUT_cc_01",
    "ten_rig_main_squint_r_cc_01",
    "ten_rig_main_squint_r_full_cc_01",
    "ten_rig_main_upper_lip_LFT_cc_01",
    "ten_rig_main_upper_lip_MID_cc_01",
    "ten_rig_main_upper_lip_RGT_cc_01",
    "ten_rig_main_upper_lip_full_cc_01"]

mc.select(ten_body_controls+ten_head_controls, replace=True)
controls = mc.ls(selection=True)

for c in controls:
    if mc.getAttr("%s.translateX" % c, settable=True):
        mc.setAttr("%s.translateX" % c, 0)
        
    if mc.getAttr("%s.translateY" % c, settable=True):
        mc.setAttr("%s.translateY" % c, 0)
    
    if mc.getAttr("%s.translateZ" % c, settable=True):
        mc.setAttr("%s.translateZ" % c, 0)
    
    if mc.getAttr("%s.rotateX" % c, settable=True):
        mc.setAttr("%s.rotateX" % c, 0)
    
    if mc.getAttr("%s.rotateY" % c, settable=True):
        mc.setAttr("%s.rotateY" % c, 0)
        
    if mc.getAttr("%s.rotateZ" % c, settable=True):
        mc.setAttr("%s.rotateZ" % c, 0)
    
mc.select(['ten_rig_main_l_armRoot_FK_CTL'], replace=True)
left_arm = mc.ls(selection=True)
mc.setAttr("%s.rotateZ" % left_arm[0], -45)

mc.select(['ten_rig_main_r_armRoot_FK_CTL'], replace=True)
left_arm = mc.ls(selection=True)
mc.setAttr("%s.rotateZ" % left_arm[0], -45)
