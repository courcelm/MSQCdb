from django.db import models




class Metadata_Overview(models.Model):


    creation_date = models.DateTimeField(auto_now_add=True)

    experimentdate = models.DateTimeField()

    instrumentmethod = models.CharField(max_length=1000)

    thermo_raw_file = models.CharField(max_length=1000)

    sha1_hash = models.CharField(max_length=40)

    instrument_name = models.CharField(max_length=50)

    instrument_serial_number = models.CharField(max_length=50)

    instrument_model = models.CharField(max_length=50)

    comment1 = models.CharField(max_length=1000)

    comment2 = models.CharField(max_length=1000)

    operator = models.CharField(max_length=50)

    instrument_software_version = models.CharField(max_length=10)

    instrument_hardware_version = models.CharField(max_length=10)





class Metadata_Overview_Tune_File_Values(models.Model):


    metadata = models.ForeignKey(Metadata_Overview, related_name='metadata')

    source_type = models.CharField(max_length=50)

    capillary_temp_c = models.IntegerField()

    apci_vaporizer_temp_c = models.IntegerField()

    sheath_gas_flow_ = models.IntegerField()

    aux_gas_flow_ = models.IntegerField()

    sweep_gas_flow_ = models.IntegerField()

    injection_waveforms = models.IntegerField()

    ion_trap_zoom_agc_target = models.IntegerField()

    ion_trap_full_agc_target = models.IntegerField()

    ion_trap_sim_agc_target = models.IntegerField()

    ion_trap_msn_agc_target = models.IntegerField()

    ftms_injection_waveforms = models.IntegerField()

    ftms_full_agc_target = models.IntegerField()

    ftms_sim_agc_target = models.IntegerField()

    ftms_msn_agc_target = models.IntegerField()

    reagent_ion_source_polarity = models.CharField(max_length=50)

    reagent_ion_source_temp_c = models.IntegerField()

    reagent_ion_source_emission_current_ua = models.IntegerField()

    reagent_ion_source_electron_energy_v = models.IntegerField()

    reagent_ion_source_ci_pressure_psi = models.IntegerField()

    reagent_vial_1_ion_time = models.IntegerField()

    reagent_vial_1_agc_target = models.IntegerField()

    reagent_vial_2_ion_time = models.IntegerField()

    reagent_vial_2_agc_target = models.IntegerField()

    supplemental_activation_energy = models.IntegerField()





class Metadata_Overview_POSITIVE_POLARITY(models.Model):


    metadata = models.ForeignKey(Metadata_Overview, related_name='metadata')

    source_voltage_kv = models.FloatField()

    source_current_ua = models.IntegerField()

    capillary_voltage_v = models.IntegerField()

    tube_lens_v = models.IntegerField()

    skimmer_offset_v = models.IntegerField()

    multipole_rf_amplifier_vpp = models.IntegerField()

    multipole_00_offset_v = models.FloatField()

    lens_0_voltage_v = models.IntegerField()

    multipole_0_offset_v = models.FloatField()

    lens_1_voltage_v = models.IntegerField()

    gate_lens_offset_v = models.IntegerField()

    multipole_1_offset_v = models.FloatField()

    front_lens_v = models.IntegerField()

    ion_trap_zoom_micro_scans = models.IntegerField()

    ion_trap_zoom_max_ion_time_ms = models.IntegerField()

    ion_trap_full_micro_scans = models.IntegerField()

    ion_trap_full_max_ion_time_ms = models.IntegerField()

    ion_trap_sim_micro_scans = models.IntegerField()

    ion_trap_sim_max_ion_time_ms = models.IntegerField()

    ion_trap_msn_micro_scans = models.IntegerField()

    ion_trap_msn_max_ion_time_ms = models.IntegerField()

    ftms_full_micro_scans = models.IntegerField()

    ftms_full_max_ion_time_ms = models.IntegerField()

    ftms_sim_micro_scans = models.IntegerField()

    ftms_sim_max_ion_time_ms = models.IntegerField()

    ftms_msn_micro_scans = models.IntegerField()

    ftms_msn_max_ion_time_ms = models.IntegerField()

    reagent_ion_lens_1_v = models.IntegerField()

    reagent_ion_gate_lens_v = models.IntegerField()

    reagent_ion_lens_2_v = models.IntegerField()

    reagent_ion_lens_3_v = models.IntegerField()

    reagent_ion_back_lens_offset_v = models.FloatField()

    reagent_ion_back_multipole_offset_v = models.IntegerField()




class Metadata_Overview_NEGATIVE_POLARITY(models.Model):


    metadata = models.ForeignKey(Metadata_Overview, related_name='metadata')

    source_voltage_kv = models.FloatField()

    source_current_ua = models.IntegerField()

    capillary_voltage_v = models.IntegerField()

    tube_lens_v = models.IntegerField()

    skimmer_offset_v = models.IntegerField()

    multipole_rf_amplifier_vpp = models.IntegerField()

    multipole_00_offset_v = models.FloatField()

    lens_0_voltage_v = models.IntegerField()

    multipole_0_offset_v = models.FloatField()

    lens_1_voltage_v = models.IntegerField()

    gate_lens_offset_v = models.IntegerField()

    multipole_1_offset_v = models.FloatField()

    front_lens_v = models.IntegerField()

    ion_trap_zoom_micro_scans = models.IntegerField()

    ion_trap_zoom_max_ion_time_ms = models.IntegerField()

    ion_trap_full_micro_scans = models.IntegerField()

    ion_trap_full_max_ion_time_ms = models.IntegerField()

    ion_trap_sim_micro_scans = models.IntegerField()

    ion_trap_sim_max_ion_time_ms = models.IntegerField()

    ion_trap_msn_micro_scans = models.IntegerField()

    ion_trap_msn_max_ion_time_ms = models.IntegerField()

    ftms_full_micro_scans = models.IntegerField()

    ftms_full_max_ion_time_ms = models.IntegerField()

    ftms_sim_micro_scans = models.IntegerField()

    ftms_sim_max_ion_time_ms = models.IntegerField()

    ftms_msn_micro_scans = models.IntegerField()

    ftms_msn_max_ion_time_ms = models.IntegerField()

    reagent_ion_lens_1_v = models.IntegerField()

    reagent_ion_gate_lens_v = models.IntegerField()

    reagent_ion_lens_2_v = models.IntegerField()

    reagent_ion_lens_3_v = models.IntegerField()

    reagent_ion_back_lens_offset_v = models.FloatField()

    reagent_ion_back_multipole_offset_v = models.IntegerField()





class Metadata_Overview_Additional_FT_Tune_File_Values(models.Model):


    metadata = models.ForeignKey(Metadata_Overview, related_name='metadata')

    ft_tune_item_1 = models.IntegerField()

    ft_tune_item_2 = models.IntegerField()

    ft_tune_item_3 = models.IntegerField()

    ft_tune_item_4 = models.IntegerField()

    ft_tune_item_5 = models.IntegerField()

    ft_tune_item_6 = models.IntegerField()

    ft_tune_item_7 = models.IntegerField()

    ft_tune_item_8 = models.IntegerField()

    ft_tune_item_9 = models.IntegerField()

    ft_tune_item_10 = models.IntegerField()





class Metadata_Overview_Calibration_File_Values(models.Model):


    metadata = models.ForeignKey(Metadata_Overview, related_name='metadata')

    multiple_rf_frequency = models.FloatField()

    main_rf_frequency = models.FloatField()

    qmslope0 = models.FloatField()

    qmslope1 = models.FloatField()

    qmslope2 = models.FloatField()

    qmslope3 = models.FloatField()

    qmslope4 = models.FloatField()

    qmint0 = models.FloatField()

    qmint1 = models.FloatField()

    qmint2 = models.FloatField()

    qmint3 = models.FloatField()

    qmint4 = models.FloatField()

    end_section_slope = models.IntegerField()

    end_section_int = models.IntegerField()

    pqd_ce_factor = models.FloatField()

    isow_slope = models.FloatField()

    isow_int = models.FloatField()

    reagent_mp_slope = models.FloatField()

    reagent_mp_int = models.FloatField()

    tickle_amp_slope0 = models.FloatField()

    tickle_amp_int0 = models.FloatField()

    tickle_amp_slope1 = models.FloatField()

    tickle_amp_int1 = models.FloatField()

    tickle_amp_slope2 = models.FloatField()

    tickle_amp_int2 = models.FloatField()

    tickle_amp_slope3 = models.FloatField()

    tickle_amp_int3 = models.FloatField()

    multiplier_1_normal_gain_pos = models.IntegerField()

    multiplier_1_high_gain_pos = models.IntegerField()

    multiplier_2_normal_gain_pos = models.IntegerField()

    multiplier_2_high_gain_pos = models.IntegerField()

    multiplier_1_normal_gain_neg = models.IntegerField()

    multiplier_1_high_gain_neg = models.IntegerField()

    multiplier_2_normal_gain_neg = models.IntegerField()

    multiplier_2_high_gain_neg = models.IntegerField()

    normal_res_eject_slope = models.FloatField()

    normal_res_eject_intercept = models.FloatField()

    zoom_res_eject_slope = models.FloatField()

    zoom_res_eject_intercept = models.FloatField()

    turbo_res_eject_slope = models.FloatField()

    turbo_res_eject_intercept = models.IntegerField()

    agc_res_eject_slope = models.FloatField()

    agc_res_eject_intercept = models.FloatField()

    ultrazoom_res_eject_slope = models.FloatField()

    ultrazoom_res_eject_intercept = models.FloatField()

    normal_mass_slope = models.FloatField()

    normal_mass_intercept = models.FloatField()

    zoom_mass_slope = models.FloatField()

    zoom_mass_intercept = models.FloatField()

    turbo_mass_slope = models.FloatField()

    turbo_mass_intercept = models.FloatField()

    agc_mass_slope = models.FloatField()

    agc_mass_intercept = models.FloatField()

    ultrazoom_mass_slope = models.FloatField()

    ultrazoom_mass_intercept = models.FloatField()

    vernier_fine_mass_slope = models.FloatField()

    vernier_fine_mass_intercept = models.IntegerField()

    vernier_coarse_mass_slope = models.IntegerField()

    vernier_coarse_mass_intercept = models.IntegerField()

    cap_device_min_v = models.FloatField()

    cap__device_max_v = models.FloatField()

    tube_lens_device_min_v = models.FloatField()

    tube_lens__device_max_v = models.FloatField()

    skimmer_device_min_v = models.FloatField()

    skimmer_device_max_v = models.FloatField()

    multipole_00_device_min_v = models.FloatField()

    multipole_00_device_max_v = models.FloatField()

    lens_0_device_min_v = models.FloatField()

    lens_0_device_max_v = models.FloatField()

    gate_lens_device_min_v = models.FloatField()

    gate_lens_device_max_v = models.FloatField()

    split_gate_device_min_v = models.FloatField()

    split_gate_device_max_v = models.FloatField()

    multipole_0_device_min_v = models.FloatField()

    multipole_0_device_max_v = models.FloatField()

    lens_1_device_min_v = models.FloatField()

    lens_1_device_max_v = models.FloatField()

    multipole_1_device_min_v = models.FloatField()

    multipole_1_device_max_v = models.FloatField()

    front_lens_device_min_v = models.FloatField()

    front_lens_device_max_v = models.FloatField()

    front_section_device_min_v = models.FloatField()

    front_section_device_max_v = models.FloatField()

    center_section_device_min_v = models.FloatField()

    center_section_device_max_v = models.FloatField()

    back_section_device_min_v = models.FloatField()

    back_section_device_max_v = models.FloatField()

    back_lens_device_min_v = models.FloatField()

    back_lens_device_max_v = models.FloatField()

    reagent_lens_1_device_min_v = models.FloatField()

    reagent_lens_1_device_max_v = models.FloatField()

    reagent_gate_lens_min_v = models.FloatField()

    reagent_gate_lens_max_v = models.FloatField()

    reagent_lens_2_device_min_v = models.FloatField()

    reagent_lens_2_device_max_v = models.FloatField()

    reagent_lens_3_device_min_v = models.FloatField()

    reagent_lens_3_device_max_v = models.FloatField()

    reagent_electron_lens_device_min_v = models.FloatField()

    reagent_electron_lens_device_max_v = models.FloatField()

    ft_cal_item_1 = models.FloatField()

    ft_cal_item_2 = models.FloatField()

    ft_cal_item_3 = models.FloatField()

    ft_cal_item_4 = models.FloatField()

    ft_cal_item_5 = models.FloatField()

    ft_cal_item_6 = models.FloatField()

    ft_cal_item_7 = models.FloatField()

    ft_cal_item_8 = models.FloatField()

    ft_cal_item_9 = models.FloatField()

    ft_cal_item_10 = models.FloatField()

    ft_cal_item_11 = models.FloatField()

    ft_cal_item_12 = models.FloatField()

    ft_cal_item_13 = models.FloatField()

    ft_cal_item_14 = models.FloatField()

    ft_cal_item_15 = models.FloatField()

    ft_cal_item_16 = models.FloatField()

    ft_cal_item_17 = models.FloatField()

    ft_cal_item_18 = models.FloatField()

    ft_cal_item_19 = models.FloatField()

    ft_cal_item_20 = models.FloatField()

    ft_cal_item_21 = models.FloatField()

    ft_cal_item_22 = models.FloatField()

    ft_cal_item_23 = models.FloatField()

    ft_cal_item_24 = models.FloatField()

    ft_cal_item_25 = models.FloatField()

    ft_cal_item_26 = models.FloatField()

    ft_cal_item_27 = models.FloatField()

    ft_cal_item_28 = models.FloatField()

    ft_cal_item_29 = models.FloatField()

    ft_cal_item_30 = models.FloatField()

    ft_cal_item_31 = models.FloatField()

    ft_cal_item_32 = models.FloatField()

    ft_cal_item_33 = models.FloatField()

    ft_cal_item_34 = models.FloatField()

    ft_cal_item_35 = models.FloatField()

    ft_cal_item_36 = models.FloatField()

    ft_cal_item_37 = models.FloatField()

    ft_cal_item_38 = models.FloatField()

    ft_cal_item_39 = models.FloatField()

    ft_cal_item_40 = models.FloatField()

    ft_cal_item_41 = models.FloatField()

    ft_cal_item_42 = models.FloatField()

    ft_cal_item_43 = models.FloatField()

    ft_cal_item_44 = models.FloatField()

    ft_cal_item_45 = models.FloatField()

    ft_cal_item_46 = models.FloatField()

    ft_cal_item_47 = models.FloatField()

    ft_cal_item_48 = models.FloatField()

    ft_cal_item_49 = models.FloatField()

    ft_cal_item_50 = models.FloatField()

    ft_cal_item_51 = models.FloatField()

    ft_cal_item_52 = models.FloatField()

    ft_cal_item_53 = models.FloatField()

    ft_cal_item_54 = models.FloatField()

    ft_cal_item_55 = models.FloatField()

    ft_cal_item_56 = models.FloatField()

    ft_cal_item_57 = models.FloatField()

    ft_cal_item_58 = models.FloatField()

    ft_cal_item_59 = models.FloatField()

    ft_cal_item_60 = models.FloatField()

    ft_cal_item_61 = models.FloatField()

    ft_cal_item_62 = models.FloatField()

    ft_cal_item_63 = models.FloatField()

    ft_cal_item_64 = models.FloatField()

    ft_cal_item_65 = models.FloatField()

    ft_cal_item_66 = models.FloatField()

    ft_cal_item_67 = models.FloatField()

    ft_cal_item_68 = models.FloatField()

    ft_cal_item_69 = models.FloatField()

    ft_cal_item_70 = models.FloatField()

    ft_cal_item_71 = models.FloatField()

    ft_cal_item_72 = models.FloatField()

    ft_cal_item_73 = models.FloatField()

    ft_cal_item_74 = models.FloatField()

    ft_cal_item_75 = models.FloatField()

    ft_cal_item_76 = models.FloatField()

    ft_cal_item_77 = models.FloatField()

    ft_cal_item_78 = models.FloatField()

    ft_cal_item_79 = models.FloatField()

    ft_cal_item_80 = models.FloatField()

    ft_cal_item_81 = models.FloatField()

    ft_cal_item_82 = models.FloatField()

    ft_cal_item_83 = models.FloatField()

    ft_cal_item_84 = models.FloatField()

    ft_cal_item_85 = models.FloatField()

    ft_cal_item_86 = models.FloatField()

    ft_cal_item_87 = models.FloatField()

    ft_cal_item_88 = models.FloatField()

    ft_cal_item_89 = models.FloatField()

    ft_cal_item_90 = models.FloatField()

    ft_cal_item_91 = models.FloatField()

    ft_cal_item_92 = models.FloatField()

    ft_cal_item_93 = models.FloatField()

    ft_cal_item_94 = models.FloatField()

    ft_cal_item_95 = models.FloatField()

    ft_cal_item_96 = models.FloatField()

    ft_cal_item_97 = models.FloatField()

    ft_cal_item_98 = models.FloatField()

    ft_cal_item_99 = models.FloatField()

    ft_cal_item_100 = models.FloatField()

    ft_cal_item_101 = models.FloatField()

    ft_cal_item_102 = models.FloatField()

    ft_cal_item_103 = models.FloatField()

    ft_cal_item_104 = models.FloatField()

    ft_cal_item_105 = models.FloatField()

    ft_cal_item_106 = models.FloatField()

    ft_cal_item_107 = models.FloatField()

    ft_cal_item_108 = models.FloatField()

    ft_cal_item_109 = models.FloatField()

    ft_cal_item_110 = models.FloatField()

    ft_cal_item_111 = models.FloatField()

    ft_cal_item_112 = models.FloatField()

    ft_cal_item_113 = models.FloatField()

    ft_cal_item_114 = models.FloatField()

    ft_cal_item_115 = models.FloatField()

    ft_cal_item_116 = models.FloatField()

    ft_cal_item_117 = models.FloatField()

    ft_cal_item_118 = models.FloatField()

    ft_cal_item_119 = models.FloatField()

    ft_cal_item_120 = models.FloatField()

    ft_cal_item_121 = models.FloatField()

    ft_cal_item_122 = models.FloatField()

    ft_cal_item_123 = models.FloatField()

    ft_cal_item_124 = models.FloatField()

    ft_cal_item_125 = models.FloatField()

    ft_cal_item_126 = models.FloatField()

    ft_cal_item_127 = models.FloatField()

    ft_cal_item_128 = models.FloatField()

    ft_cal_item_129 = models.FloatField()

    ft_cal_item_130 = models.FloatField()

    ft_cal_item_131 = models.FloatField()

    ft_cal_item_132 = models.FloatField()

    ft_cal_item_133 = models.FloatField()

    ft_cal_item_134 = models.FloatField()

    ft_cal_item_135 = models.FloatField()

    ft_cal_item_136 = models.FloatField()

    ft_cal_item_137 = models.FloatField()

    ft_cal_item_138 = models.FloatField()

    ft_cal_item_139 = models.FloatField()

    ft_cal_item_140 = models.FloatField()

    ft_cal_item_141 = models.FloatField()

    ft_cal_item_142 = models.FloatField()

    ft_cal_item_143 = models.FloatField()

    ft_cal_item_144 = models.FloatField()

    ft_cal_item_145 = models.FloatField()

    ft_cal_item_146 = models.FloatField()

    ft_cal_item_147 = models.FloatField()

    ft_cal_item_148 = models.FloatField()

    ft_cal_item_149 = models.FloatField()

    ft_cal_item_150 = models.FloatField()

    ft_cal_item_151 = models.FloatField()

    ft_cal_item_152 = models.FloatField()

    ft_cal_item_153 = models.FloatField()

    ft_cal_item_154 = models.FloatField()

    ft_cal_item_155 = models.FloatField()

    ft_cal_item_156 = models.FloatField()

    ft_cal_item_157 = models.FloatField()

    ft_cal_item_158 = models.FloatField()

    ft_cal_item_159 = models.FloatField()

    ft_cal_item_160 = models.FloatField()

    ft_cal_item_161 = models.FloatField()

    ft_cal_item_162 = models.FloatField()

    ft_cal_item_163 = models.FloatField()

    ft_cal_item_164 = models.FloatField()

    ft_cal_item_165 = models.FloatField()

    ft_cal_item_166 = models.FloatField()

    ft_cal_item_167 = models.FloatField()

    ft_cal_item_168 = models.FloatField()

    ft_cal_item_169 = models.FloatField()

    ft_cal_item_170 = models.FloatField()

    ft_cal_item_171 = models.FloatField()

    ft_cal_item_172 = models.FloatField()

    ft_cal_item_173 = models.FloatField()

    ft_cal_item_174 = models.FloatField()

    ft_cal_item_175 = models.FloatField()

    ft_cal_item_176 = models.FloatField()

    ft_cal_item_177 = models.FloatField()

    ft_cal_item_178 = models.FloatField()

    ft_cal_item_179 = models.FloatField()

    ft_cal_item_180 = models.FloatField()

    ft_cal_item_181 = models.FloatField()

    ft_cal_item_182 = models.FloatField()

    ft_cal_item_183 = models.FloatField()

    ft_cal_item_184 = models.FloatField()

    ft_cal_item_185 = models.FloatField()

    ft_cal_item_186 = models.FloatField()

    ft_cal_item_187 = models.FloatField()

    ft_cal_item_188 = models.FloatField()

    ft_cal_item_189 = models.FloatField()

    ft_cal_item_190 = models.FloatField()

    ft_cal_item_191 = models.FloatField()

    ft_cal_item_192 = models.FloatField()

    ft_cal_item_193 = models.FloatField()

    ft_cal_item_194 = models.FloatField()

    ft_cal_item_195 = models.FloatField()

    ft_cal_item_196 = models.FloatField()

    ft_cal_item_197 = models.FloatField()

    ft_cal_item_198 = models.FloatField()

    ft_cal_item_199 = models.FloatField()

    ft_cal_item_200 = models.FloatField()

    ft_cal_item_201 = models.FloatField()

    ft_cal_item_202 = models.FloatField()

    ft_cal_item_203 = models.FloatField()

    ft_cal_item_204 = models.FloatField()

    ft_cal_item_205 = models.FloatField()

    ft_cal_item_206 = models.FloatField()

    ft_cal_item_207 = models.FloatField()

    ft_cal_item_208 = models.FloatField()

    ft_cal_item_209 = models.FloatField()

    ft_cal_item_210 = models.FloatField()

    ft_cal_item_211 = models.FloatField()

    ft_cal_item_212 = models.FloatField()

    ft_cal_item_213 = models.FloatField()

    ft_cal_item_214 = models.FloatField()

    ft_cal_item_215 = models.FloatField()

    ft_cal_item_216 = models.FloatField()

    ft_cal_item_217 = models.FloatField()

    ft_cal_item_218 = models.FloatField()

    ft_cal_item_219 = models.FloatField()

    ft_cal_item_220 = models.FloatField()

    ft_cal_item_221 = models.FloatField()

    ft_cal_item_222 = models.FloatField()

    ft_cal_item_223 = models.FloatField()

    ft_cal_item_224 = models.FloatField()

    ft_cal_item_225 = models.FloatField()

    ft_cal_item_226 = models.FloatField()

    ft_cal_item_227 = models.FloatField()

    ft_cal_item_228 = models.FloatField()

    ft_cal_item_229 = models.FloatField()

    ft_cal_item_230 = models.FloatField()

    ft_cal_item_231 = models.FloatField()

    ft_cal_item_232 = models.FloatField()

    ft_cal_item_233 = models.FloatField()

    ft_cal_item_234 = models.FloatField()

    ft_cal_item_235 = models.FloatField()

    ft_cal_item_236 = models.FloatField()

    ft_cal_item_237 = models.FloatField()

    ft_cal_item_238 = models.FloatField()

    ft_cal_item_239 = models.FloatField()

    ft_cal_item_240 = models.FloatField()

    ft_cal_item_241 = models.FloatField()

    ft_cal_item_242 = models.FloatField()

    ft_cal_item_243 = models.FloatField()

    ft_cal_item_244 = models.FloatField()

    ft_cal_item_245 = models.FloatField()

    ft_cal_item_246 = models.FloatField()

    ft_cal_item_247 = models.FloatField()

    ft_cal_item_248 = models.FloatField()

    ft_cal_item_249 = models.FloatField()

    ft_cal_item_250 = models.FloatField()

