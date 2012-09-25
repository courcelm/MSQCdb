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

    reagent_ion_source_polarity = models.CharField(max_length=50, null=True, blank=True)

    reagent_ion_source_temp_c = models.IntegerField(null=True, blank=True)

    reagent_ion_source_emission_current_ua = models.IntegerField(null=True, blank=True)

    reagent_ion_source_electron_energy_v = models.IntegerField(null=True, blank=True)

    reagent_ion_source_ci_pressure_psi = models.IntegerField(null=True, blank=True)

    reagent_vial_1_ion_time = models.IntegerField(null=True, blank=True)

    reagent_vial_1_agc_target = models.IntegerField(null=True, blank=True)

    reagent_vial_2_ion_time = models.IntegerField(null=True, blank=True)

    reagent_vial_2_agc_target = models.IntegerField(null=True, blank=True)

    supplemental_activation_energy = models.IntegerField(null=True, blank=True)





class Metadata_Overview_POSITIVE_POLARITY(models.Model):


    metadata = models.ForeignKey(Metadata_Overview, related_name='metadata')

    source_voltage_kv = models.FloatField()

    source_current_ua = models.IntegerField()

    capillary_voltage_v = models.IntegerField(null=True, blank=True)

    tube_lens_v = models.IntegerField(null=True, blank=True)

    skimmer_offset_v = models.IntegerField()

    multipole_rf_amplifier_vpp = models.IntegerField()

    multipole_00_offset_v = models.FloatField()

    lens_0_voltage_v = models.FloatField()

    multipole_0_offset_v = models.FloatField()

    lens_1_voltage_v = models.FloatField()

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

    slens_rf_level_percent = models.IntegerField(null=True, blank=True)
    
    back_section_lpt_reagent_injection_v = models.IntegerField(null=True, blank=True)

    center_lens_reagent_injection_v = models.FloatField(null=True, blank=True)

    front_lens_reagent_injection_v = models.IntegerField(null=True, blank=True)

    center_lens_2_v = models.FloatField(null=True, blank=True)
    


class Metadata_Overview_NEGATIVE_POLARITY(models.Model):


    metadata = models.ForeignKey(Metadata_Overview, related_name='metadata')

    source_voltage_kv = models.FloatField()

    source_current_ua = models.IntegerField()

    capillary_voltage_v = models.IntegerField(null=True, blank=True)

    tube_lens_v = models.IntegerField(null=True, blank=True)

    skimmer_offset_v = models.IntegerField()

    multipole_rf_amplifier_vpp = models.IntegerField()

    multipole_00_offset_v = models.FloatField()

    lens_0_voltage_v = models.FloatField()

    multipole_0_offset_v = models.FloatField()

    lens_1_voltage_v = models.FloatField()

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

    slens_rf_level_percent = models.IntegerField(null=True, blank=True)
    
    back_section_lpt_reagent_injection_v = models.IntegerField(null=True, blank=True)

    center_lens_reagent_injection_v = models.FloatField(null=True, blank=True)

    front_lens_reagent_injection_v = models.IntegerField(null=True, blank=True)

    center_lens_2_v = models.FloatField(null=True, blank=True)



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



class Metadata_Overview_Reagent_Ion_Source_Tune_File_Values(models.Model):


    metadata = models.ForeignKey(Metadata_Overview, related_name='metadata')

    reagent_ion_source_polarity = models.CharField(max_length=50, null=True, blank=True)

    reagent_ion_source_temp_c = models.IntegerField(null=True, blank=True)

    reagent_ion_source_emission_current_ua = models.IntegerField(null=True, blank=True)

    reagent_ion_source_electron_energy_v = models.IntegerField(null=True, blank=True)

    reagent_ion_source_ci_pressure_psi = models.IntegerField(null=True, blank=True)

    reagent_vial_1_ion_time = models.IntegerField(null=True, blank=True)

    reagent_vial_1_agc_target = models.IntegerField(null=True, blank=True)

    reagent_vial_2_ion_time = models.IntegerField(null=True, blank=True)

    reagent_vial_2_agc_target = models.IntegerField(null=True, blank=True)

    supplemental_activation_energy = models.IntegerField(null=True, blank=True)



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

    end_section_slope = models.FloatField()

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

    multiplier_1_normal_gain_pos = models.FloatField()

    multiplier_1_high_gain_pos = models.FloatField()

    multiplier_2_normal_gain_pos = models.FloatField()

    multiplier_2_high_gain_pos = models.FloatField()

    multiplier_1_normal_gain_neg = models.FloatField()

    multiplier_1_high_gain_neg = models.FloatField()
    
    multiplier_2_normal_gain_neg = models.FloatField()

    multiplier_2_high_gain_neg = models.FloatField()

    normal_res_eject_slope = models.FloatField(null=True, blank=True)

    normal_res_eject_intercept = models.FloatField(null=True, blank=True)

    zoom_res_eject_slope = models.FloatField(null=True, blank=True)

    zoom_res_eject_intercept = models.FloatField(null=True, blank=True)

    turbo_res_eject_slope = models.FloatField(null=True, blank=True)

    turbo_res_eject_intercept = models.IntegerField(null=True, blank=True)

    agc_res_eject_slope = models.FloatField(null=True, blank=True)

    agc_res_eject_intercept = models.FloatField(null=True, blank=True)

    ultrazoom_res_eject_slope = models.FloatField(null=True, blank=True)

    ultrazoom_res_eject_intercept = models.FloatField(null=True, blank=True)

    normal_mass_slope = models.FloatField(null=True, blank=True)

    normal_mass_intercept = models.FloatField(null=True, blank=True)

    zoom_mass_slope = models.FloatField(null=True, blank=True)

    zoom_mass_intercept = models.FloatField(null=True, blank=True)

    turbo_mass_slope = models.FloatField(null=True, blank=True)

    turbo_mass_intercept = models.FloatField(null=True, blank=True)

    agc_mass_slope = models.FloatField(null=True, blank=True)

    agc_mass_intercept = models.FloatField(null=True, blank=True)

    ultrazoom_mass_slope = models.FloatField(null=True, blank=True)

    ultrazoom_mass_intercept = models.FloatField(null=True, blank=True)

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

    reagent_electron_lens_device_min_v = models.CharField(max_length=50)

    reagent_electron_lens_device_max_v = models.FloatField()
    
    res_eject_slope_0__0_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_0__0_ = models.FloatField(null=True, blank=True)

    res_eject_slope_0__1_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_0__1_ = models.FloatField(null=True, blank=True)

    res_eject_slope_0__2_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_0__2_ = models.FloatField(null=True, blank=True)

    res_eject_slope_0__3_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_0__3_ = models.FloatField(null=True, blank=True)

    res_eject_slope_0__4_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_0__4_ = models.FloatField(null=True, blank=True)

    res_eject_slope_0__5_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_0__5_ = models.FloatField(null=True, blank=True)

    res_eject_slope_0__6_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_0__6_ = models.FloatField(null=True, blank=True)

    res_eject_slope_0__7_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_0__7_ = models.FloatField(null=True, blank=True)

    res_eject_slope_0__8_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_0__8_ = models.FloatField(null=True, blank=True)

    res_eject_slope_0__9_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_0__9_ = models.FloatField(null=True, blank=True)

    res_eject_slope_0__10_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_0__10_ = models.FloatField(null=True, blank=True)

    res_eject_slope_0__11_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_0__11_ = models.FloatField(null=True, blank=True)

    res_eject_slope_0__12_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_0__12_ = models.FloatField(null=True, blank=True)

    res_eject_slope_0__13_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_0__13_ = models.FloatField(null=True, blank=True)

    res_eject_slope_0__14_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_0__14_ = models.FloatField(null=True, blank=True)

    res_eject_slope_0__15_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_0__15_ = models.FloatField(null=True, blank=True)

    res_eject_slope_0__16_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_0__16_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_0__17_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_0__17_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_0__18_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_0__18_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_0__19_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_0__19_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_1__0_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_1__0_ = models.FloatField(null=True, blank=True)

    res_eject_slope_1__1_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_1__1_ = models.FloatField(null=True, blank=True)

    res_eject_slope_1__2_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_1__2_ = models.FloatField(null=True, blank=True)

    res_eject_slope_1__3_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_1__3_ = models.FloatField(null=True, blank=True)

    res_eject_slope_1__4_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_1__4_ = models.FloatField(null=True, blank=True)

    res_eject_slope_1__5_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_1__5_ = models.FloatField(null=True, blank=True)

    res_eject_slope_1__6_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_1__6_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_1__7_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_1__7_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_1__8_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_1__8_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_1__9_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_1__9_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_1__10_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_1__10_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_1__11_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_1__11_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_1__12_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_1__12_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_1__13_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_1__13_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_1__14_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_1__14_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_1__15_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_1__15_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_1__16_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_1__16_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_1__17_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_1__17_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_1__18_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_1__18_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_1__19_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_1__19_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_2__0_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_2__0_ = models.FloatField(null=True, blank=True)

    res_eject_slope_2__1_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_2__1_ = models.FloatField(null=True, blank=True)

    res_eject_slope_2__2_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_2__2_ = models.FloatField(null=True, blank=True)

    res_eject_slope_2__3_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_2__3_ = models.FloatField(null=True, blank=True)

    res_eject_slope_2__4_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_2__4_ = models.FloatField(null=True, blank=True)

    res_eject_slope_2__5_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_2__5_ = models.FloatField(null=True, blank=True)

    res_eject_slope_2__6_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_2__6_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_2__7_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_2__7_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_2__8_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_2__8_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_2__9_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_2__9_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_2__10_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_2__10_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_2__11_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_2__11_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_2__12_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_2__12_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_2__13_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_2__13_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_2__14_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_2__14_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_2__15_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_2__15_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_2__16_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_2__16_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_2__17_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_2__17_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_2__18_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_2__18_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_2__19_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_2__19_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_3__0_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_3__0_ = models.FloatField(null=True, blank=True)

    res_eject_slope_3__1_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_3__1_ = models.FloatField(null=True, blank=True)

    res_eject_slope_3__2_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_3__2_ = models.FloatField(null=True, blank=True)

    res_eject_slope_3__3_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_3__3_ = models.FloatField(null=True, blank=True)

    res_eject_slope_3__4_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_3__4_ = models.FloatField(null=True, blank=True)

    res_eject_slope_3__5_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_3__5_ = models.FloatField(null=True, blank=True)

    res_eject_slope_3__6_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_3__6_ = models.FloatField(null=True, blank=True)

    res_eject_slope_3__7_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_3__7_ = models.FloatField(null=True, blank=True)

    res_eject_slope_3__8_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_3__8_ = models.FloatField(null=True, blank=True)

    res_eject_slope_3__9_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_3__9_ = models.FloatField(null=True, blank=True)

    res_eject_slope_3__10_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_3__10_ = models.FloatField(null=True, blank=True)

    res_eject_slope_3__11_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_3__11_ = models.FloatField(null=True, blank=True)

    res_eject_slope_3__12_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_3__12_ = models.FloatField(null=True, blank=True)

    res_eject_slope_3__13_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_3__13_ = models.FloatField(null=True, blank=True)

    res_eject_slope_3__14_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_3__14_ = models.FloatField(null=True, blank=True)

    res_eject_slope_3__15_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_3__15_ = models.FloatField(null=True, blank=True)

    res_eject_slope_3__16_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_3__16_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_3__17_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_3__17_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_3__18_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_3__18_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_3__19_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_3__19_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_4__0_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_4__0_ = models.FloatField(null=True, blank=True)

    res_eject_slope_4__1_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_4__1_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_4__2_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_4__2_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_4__3_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_4__3_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_4__4_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_4__4_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_4__5_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_4__5_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_4__6_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_4__6_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_4__7_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_4__7_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_4__8_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_4__8_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_4__9_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_4__9_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_4__10_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_4__10_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_4__11_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_4__11_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_4__12_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_4__12_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_4__13_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_4__13_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_4__14_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_4__14_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_4__15_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_4__15_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_4__16_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_4__16_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_4__17_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_4__17_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_4__18_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_4__18_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_4__19_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_4__19_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_5__0_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_5__0_ = models.FloatField(null=True, blank=True)

    res_eject_slope_5__1_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_5__1_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_5__2_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_5__2_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_5__3_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_5__3_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_5__4_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_5__4_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_5__5_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_5__5_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_5__6_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_5__6_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_5__7_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_5__7_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_5__8_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_5__8_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_5__9_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_5__9_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_5__10_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_5__10_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_5__11_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_5__11_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_5__12_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_5__12_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_5__13_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_5__13_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_5__14_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_5__14_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_5__15_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_5__15_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_5__16_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_5__16_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_5__17_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_5__17_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_5__18_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_5__18_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_5__19_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_5__19_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_6__0_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_6__0_ = models.FloatField(null=True, blank=True)

    res_eject_slope_6__1_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_6__1_ = models.FloatField(null=True, blank=True)

    res_eject_slope_6__2_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_6__2_ = models.FloatField(null=True, blank=True)

    res_eject_slope_6__3_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_6__3_ = models.FloatField(null=True, blank=True)

    res_eject_slope_6__4_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_6__4_ = models.FloatField(null=True, blank=True)

    res_eject_slope_6__5_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_6__5_ = models.FloatField(null=True, blank=True)

    res_eject_slope_6__6_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_6__6_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_6__7_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_6__7_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_6__8_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_6__8_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_6__9_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_6__9_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_6__10_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_6__10_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_6__11_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_6__11_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_6__12_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_6__12_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_6__13_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_6__13_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_6__14_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_6__14_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_6__15_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_6__15_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_6__16_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_6__16_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_6__17_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_6__17_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_6__18_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_6__18_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_6__19_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_6__19_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_7__0_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_7__0_ = models.FloatField(null=True, blank=True)

    res_eject_slope_7__1_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_7__1_ = models.FloatField(null=True, blank=True)

    res_eject_slope_7__2_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_7__2_ = models.FloatField(null=True, blank=True)

    res_eject_slope_7__3_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_7__3_ = models.FloatField(null=True, blank=True)

    res_eject_slope_7__4_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_7__4_ = models.FloatField(null=True, blank=True)

    res_eject_slope_7__5_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_7__5_ = models.FloatField(null=True, blank=True)

    res_eject_slope_7__6_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_7__6_ = models.FloatField(null=True, blank=True)

    res_eject_slope_7__7_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_7__7_ = models.FloatField(null=True, blank=True)

    res_eject_slope_7__8_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_7__8_ = models.FloatField(null=True, blank=True)

    res_eject_slope_7__9_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_7__9_ = models.FloatField(null=True, blank=True)

    res_eject_slope_7__10_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_7__10_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_7__11_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_7__11_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_7__12_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_7__12_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_7__13_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_7__13_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_7__14_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_7__14_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_7__15_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_7__15_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_7__16_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_7__16_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_7__17_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_7__17_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_7__18_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_7__18_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_7__19_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_7__19_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_8__0_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_8__0_ = models.FloatField(null=True, blank=True)

    res_eject_slope_8__1_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_8__1_ = models.FloatField(null=True, blank=True)

    res_eject_slope_8__2_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_8__2_ = models.FloatField(null=True, blank=True)

    res_eject_slope_8__3_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_8__3_ = models.FloatField(null=True, blank=True)

    res_eject_slope_8__4_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_8__4_ = models.FloatField(null=True, blank=True)

    res_eject_slope_8__5_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_8__5_ = models.FloatField(null=True, blank=True)

    res_eject_slope_8__6_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_8__6_ = models.FloatField(null=True, blank=True)

    res_eject_slope_8__7_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_8__7_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_8__8_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_8__8_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_8__9_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_8__9_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_8__10_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_8__10_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_8__11_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_8__11_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_8__12_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_8__12_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_8__13_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_8__13_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_8__14_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_8__14_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_8__15_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_8__15_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_8__16_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_8__16_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_8__17_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_8__17_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_8__18_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_8__18_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_8__19_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_8__19_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_9__0_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_9__0_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_9__1_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_9__1_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_9__2_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_9__2_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_9__3_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_9__3_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_9__4_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_9__4_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_9__5_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_9__5_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_9__6_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_9__6_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_9__7_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_9__7_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_9__8_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_9__8_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_9__9_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_9__9_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_9__10_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_9__10_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_9__11_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_9__11_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_9__12_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_9__12_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_9__13_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_9__13_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_9__14_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_9__14_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_9__15_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_9__15_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_9__16_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_9__16_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_9__17_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_9__17_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_9__18_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_9__18_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_9__19_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_9__19_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_10__0_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_10__0_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_10__1_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_10__1_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_10__2_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_10__2_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_10__3_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_10__3_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_10__4_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_10__4_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_10__5_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_10__5_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_10__6_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_10__6_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_10__7_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_10__7_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_10__8_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_10__8_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_10__9_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_10__9_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_10__10_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_10__10_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_10__11_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_10__11_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_10__12_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_10__12_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_10__13_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_10__13_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_10__14_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_10__14_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_10__15_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_10__15_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_10__16_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_10__16_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_10__17_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_10__17_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_10__18_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_10__18_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_10__19_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_10__19_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_11__0_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_11__0_ = models.FloatField(null=True, blank=True)

    res_eject_slope_11__1_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_11__1_ = models.FloatField(null=True, blank=True)

    res_eject_slope_11__2_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_11__2_ = models.FloatField(null=True, blank=True)

    res_eject_slope_11__3_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_11__3_ = models.FloatField(null=True, blank=True)

    res_eject_slope_11__4_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_11__4_ = models.FloatField(null=True, blank=True)

    res_eject_slope_11__5_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_11__5_ = models.FloatField(null=True, blank=True)

    res_eject_slope_11__6_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_11__6_ = models.FloatField(null=True, blank=True)

    res_eject_slope_11__7_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_11__7_ = models.FloatField(null=True, blank=True)

    res_eject_slope_11__8_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_11__8_ = models.FloatField(null=True, blank=True)

    res_eject_slope_11__9_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_11__9_ = models.FloatField(null=True, blank=True)

    res_eject_slope_11__10_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_11__10_ = models.FloatField(null=True, blank=True)

    res_eject_slope_11__11_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_11__11_ = models.FloatField(null=True, blank=True)

    res_eject_slope_11__12_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_11__12_ = models.FloatField(null=True, blank=True)

    res_eject_slope_11__13_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_11__13_ = models.FloatField(null=True, blank=True)

    res_eject_slope_11__14_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_11__14_ = models.FloatField(null=True, blank=True)

    res_eject_slope_11__15_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_11__15_ = models.FloatField(null=True, blank=True)

    res_eject_slope_11__16_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_11__16_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_11__17_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_11__17_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_11__18_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_11__18_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_11__19_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_11__19_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_12__0_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_12__0_ = models.FloatField(null=True, blank=True)

    res_eject_slope_12__1_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_12__1_ = models.FloatField(null=True, blank=True)

    res_eject_slope_12__2_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_12__2_ = models.FloatField(null=True, blank=True)

    res_eject_slope_12__3_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_12__3_ = models.FloatField(null=True, blank=True)

    res_eject_slope_12__4_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_12__4_ = models.FloatField(null=True, blank=True)

    res_eject_slope_12__5_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_12__5_ = models.FloatField(null=True, blank=True)

    res_eject_slope_12__6_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_12__6_ = models.FloatField(null=True, blank=True)

    res_eject_slope_12__7_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_12__7_ = models.FloatField(null=True, blank=True)

    res_eject_slope_12__8_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_12__8_ = models.FloatField(null=True, blank=True)

    res_eject_slope_12__9_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_12__9_ = models.FloatField(null=True, blank=True)

    res_eject_slope_12__10_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_12__10_ = models.FloatField(null=True, blank=True)

    res_eject_slope_12__11_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_12__11_ = models.FloatField(null=True, blank=True)

    res_eject_slope_12__12_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_12__12_ = models.FloatField(null=True, blank=True)

    res_eject_slope_12__13_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_12__13_ = models.FloatField(null=True, blank=True)

    res_eject_slope_12__14_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_12__14_ = models.FloatField(null=True, blank=True)

    res_eject_slope_12__15_ = models.FloatField(null=True, blank=True)

    res_eject_intercept_12__15_ = models.FloatField(null=True, blank=True)

    res_eject_slope_12__16_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_12__16_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_12__17_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_12__17_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_12__18_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_12__18_ = models.IntegerField(null=True, blank=True)

    res_eject_slope_12__19_ = models.IntegerField(null=True, blank=True)

    res_eject_intercept_12__19_ = models.IntegerField(null=True, blank=True)

    mass_slope_0__0_ = models.FloatField(null=True, blank=True)

    mass_intercept_0__0_ = models.FloatField(null=True, blank=True)

    mass_slope_0__1_ = models.FloatField(null=True, blank=True)

    mass_intercept_0__1_ = models.FloatField(null=True, blank=True)

    mass_slope_0__2_ = models.FloatField(null=True, blank=True)

    mass_intercept_0__2_ = models.FloatField(null=True, blank=True)

    mass_slope_0__3_ = models.FloatField(null=True, blank=True)

    mass_intercept_0__3_ = models.FloatField(null=True, blank=True)

    mass_slope_0__4_ = models.FloatField(null=True, blank=True)

    mass_intercept_0__4_ = models.FloatField(null=True, blank=True)

    mass_slope_0__5_ = models.FloatField(null=True, blank=True)

    mass_intercept_0__5_ = models.FloatField(null=True, blank=True)

    mass_slope_0__6_ = models.FloatField(null=True, blank=True)

    mass_intercept_0__6_ = models.FloatField(null=True, blank=True)

    mass_slope_0__7_ = models.FloatField(null=True, blank=True)

    mass_intercept_0__7_ = models.FloatField(null=True, blank=True)

    mass_slope_0__8_ = models.FloatField(null=True, blank=True)

    mass_intercept_0__8_ = models.FloatField(null=True, blank=True)

    mass_slope_0__9_ = models.FloatField(null=True, blank=True)

    mass_intercept_0__9_ = models.FloatField(null=True, blank=True)

    mass_slope_0__10_ = models.FloatField(null=True, blank=True)

    mass_intercept_0__10_ = models.FloatField(null=True, blank=True)

    mass_slope_0__11_ = models.FloatField(null=True, blank=True)

    mass_intercept_0__11_ = models.FloatField(null=True, blank=True)

    mass_slope_0__12_ = models.FloatField(null=True, blank=True)

    mass_intercept_0__12_ = models.FloatField(null=True, blank=True)

    mass_slope_0__13_ = models.FloatField(null=True, blank=True)

    mass_intercept_0__13_ = models.FloatField(null=True, blank=True)

    mass_slope_0__14_ = models.FloatField(null=True, blank=True)

    mass_intercept_0__14_ = models.FloatField(null=True, blank=True)

    mass_slope_0__15_ = models.FloatField(null=True, blank=True)

    mass_intercept_0__15_ = models.FloatField(null=True, blank=True)

    mass_slope_0__16_ = models.IntegerField(null=True, blank=True)

    mass_intercept_0__16_ = models.IntegerField(null=True, blank=True)

    mass_slope_0__17_ = models.IntegerField(null=True, blank=True)

    mass_intercept_0__17_ = models.IntegerField(null=True, blank=True)

    mass_slope_0__18_ = models.IntegerField(null=True, blank=True)

    mass_intercept_0__18_ = models.IntegerField(null=True, blank=True)

    mass_slope_0__19_ = models.IntegerField(null=True, blank=True)

    mass_intercept_0__19_ = models.IntegerField(null=True, blank=True)

    mass_slope_1__0_ = models.FloatField(null=True, blank=True)

    mass_intercept_1__0_ = models.FloatField(null=True, blank=True)

    mass_slope_1__1_ = models.FloatField(null=True, blank=True)

    mass_intercept_1__1_ = models.FloatField(null=True, blank=True)

    mass_slope_1__2_ = models.FloatField(null=True, blank=True)

    mass_intercept_1__2_ = models.FloatField(null=True, blank=True)

    mass_slope_1__3_ = models.FloatField(null=True, blank=True)

    mass_intercept_1__3_ = models.FloatField(null=True, blank=True)

    mass_slope_1__4_ = models.FloatField(null=True, blank=True)

    mass_intercept_1__4_ = models.FloatField(null=True, blank=True)

    mass_slope_1__5_ = models.FloatField(null=True, blank=True)

    mass_intercept_1__5_ = models.FloatField(null=True, blank=True)

    mass_slope_1__6_ = models.FloatField(null=True, blank=True)

    mass_intercept_1__6_ = models.FloatField(null=True, blank=True)

    mass_slope_1__7_ = models.FloatField(null=True, blank=True)

    mass_intercept_1__7_ = models.FloatField(null=True, blank=True)

    mass_slope_1__8_ = models.FloatField(null=True, blank=True)

    mass_intercept_1__8_ = models.FloatField(null=True, blank=True)

    mass_slope_1__9_ = models.FloatField(null=True, blank=True)

    mass_intercept_1__9_ = models.FloatField(null=True, blank=True)

    mass_slope_1__10_ = models.IntegerField(null=True, blank=True)

    mass_intercept_1__10_ = models.IntegerField(null=True, blank=True)

    mass_slope_1__11_ = models.IntegerField(null=True, blank=True)

    mass_intercept_1__11_ = models.IntegerField(null=True, blank=True)

    mass_slope_1__12_ = models.IntegerField(null=True, blank=True)

    mass_intercept_1__12_ = models.IntegerField(null=True, blank=True)

    mass_slope_1__13_ = models.IntegerField(null=True, blank=True)

    mass_intercept_1__13_ = models.IntegerField(null=True, blank=True)

    mass_slope_1__14_ = models.IntegerField(null=True, blank=True)

    mass_intercept_1__14_ = models.IntegerField(null=True, blank=True)

    mass_slope_1__15_ = models.IntegerField(null=True, blank=True)

    mass_intercept_1__15_ = models.IntegerField(null=True, blank=True)

    mass_slope_1__16_ = models.IntegerField(null=True, blank=True)

    mass_intercept_1__16_ = models.IntegerField(null=True, blank=True)

    mass_slope_1__17_ = models.IntegerField(null=True, blank=True)

    mass_intercept_1__17_ = models.IntegerField(null=True, blank=True)

    mass_slope_1__18_ = models.IntegerField(null=True, blank=True)

    mass_intercept_1__18_ = models.IntegerField(null=True, blank=True)

    mass_slope_1__19_ = models.IntegerField(null=True, blank=True)

    mass_intercept_1__19_ = models.IntegerField(null=True, blank=True)

    mass_slope_2__0_ = models.FloatField(null=True, blank=True)

    mass_intercept_2__0_ = models.FloatField(null=True, blank=True)

    mass_slope_2__1_ = models.FloatField(null=True, blank=True)

    mass_intercept_2__1_ = models.FloatField(null=True, blank=True)

    mass_slope_2__2_ = models.FloatField(null=True, blank=True)

    mass_intercept_2__2_ = models.FloatField(null=True, blank=True)

    mass_slope_2__3_ = models.FloatField(null=True, blank=True)

    mass_intercept_2__3_ = models.FloatField(null=True, blank=True)

    mass_slope_2__4_ = models.FloatField(null=True, blank=True)

    mass_intercept_2__4_ = models.FloatField(null=True, blank=True)

    mass_slope_2__5_ = models.FloatField(null=True, blank=True)

    mass_intercept_2__5_ = models.FloatField(null=True, blank=True)

    mass_slope_2__6_ = models.FloatField(null=True, blank=True)

    mass_intercept_2__6_ = models.IntegerField(null=True, blank=True)

    mass_slope_2__7_ = models.IntegerField(null=True, blank=True)

    mass_intercept_2__7_ = models.IntegerField(null=True, blank=True)

    mass_slope_2__8_ = models.IntegerField(null=True, blank=True)

    mass_intercept_2__8_ = models.IntegerField(null=True, blank=True)

    mass_slope_2__9_ = models.IntegerField(null=True, blank=True)

    mass_intercept_2__9_ = models.IntegerField(null=True, blank=True)

    mass_slope_2__10_ = models.IntegerField(null=True, blank=True)

    mass_intercept_2__10_ = models.IntegerField(null=True, blank=True)

    mass_slope_2__11_ = models.IntegerField(null=True, blank=True)

    mass_intercept_2__11_ = models.IntegerField(null=True, blank=True)

    mass_slope_2__12_ = models.IntegerField(null=True, blank=True)

    mass_intercept_2__12_ = models.IntegerField(null=True, blank=True)

    mass_slope_2__13_ = models.IntegerField(null=True, blank=True)

    mass_intercept_2__13_ = models.IntegerField(null=True, blank=True)

    mass_slope_2__14_ = models.IntegerField(null=True, blank=True)

    mass_intercept_2__14_ = models.IntegerField(null=True, blank=True)

    mass_slope_2__15_ = models.IntegerField(null=True, blank=True)

    mass_intercept_2__15_ = models.IntegerField(null=True, blank=True)

    mass_slope_2__16_ = models.IntegerField(null=True, blank=True)

    mass_intercept_2__16_ = models.IntegerField(null=True, blank=True)

    mass_slope_2__17_ = models.IntegerField(null=True, blank=True)

    mass_intercept_2__17_ = models.IntegerField(null=True, blank=True)

    mass_slope_2__18_ = models.IntegerField(null=True, blank=True)

    mass_intercept_2__18_ = models.IntegerField(null=True, blank=True)

    mass_slope_2__19_ = models.IntegerField(null=True, blank=True)

    mass_intercept_2__19_ = models.IntegerField(null=True, blank=True)

    mass_slope_3__0_ = models.FloatField(null=True, blank=True)

    mass_intercept_3__0_ = models.FloatField(null=True, blank=True)

    mass_slope_3__1_ = models.FloatField(null=True, blank=True)

    mass_intercept_3__1_ = models.FloatField(null=True, blank=True)

    mass_slope_3__2_ = models.FloatField(null=True, blank=True)

    mass_intercept_3__2_ = models.FloatField(null=True, blank=True)

    mass_slope_3__3_ = models.FloatField(null=True, blank=True)

    mass_intercept_3__3_ = models.FloatField(null=True, blank=True)

    mass_slope_3__4_ = models.FloatField(null=True, blank=True)

    mass_intercept_3__4_ = models.FloatField(null=True, blank=True)

    mass_slope_3__5_ = models.FloatField(null=True, blank=True)

    mass_intercept_3__5_ = models.FloatField(null=True, blank=True)

    mass_slope_3__6_ = models.FloatField(null=True, blank=True)

    mass_intercept_3__6_ = models.FloatField(null=True, blank=True)

    mass_slope_3__7_ = models.FloatField(null=True, blank=True)

    mass_intercept_3__7_ = models.FloatField(null=True, blank=True)

    mass_slope_3__8_ = models.FloatField(null=True, blank=True)

    mass_intercept_3__8_ = models.FloatField(null=True, blank=True)

    mass_slope_3__9_ = models.FloatField(null=True, blank=True)

    mass_intercept_3__9_ = models.FloatField(null=True, blank=True)

    mass_slope_3__10_ = models.FloatField(null=True, blank=True)

    mass_intercept_3__10_ = models.FloatField(null=True, blank=True)

    mass_slope_3__11_ = models.FloatField(null=True, blank=True)

    mass_intercept_3__11_ = models.FloatField(null=True, blank=True)

    mass_slope_3__12_ = models.FloatField(null=True, blank=True)

    mass_intercept_3__12_ = models.FloatField(null=True, blank=True)

    mass_slope_3__13_ = models.FloatField(null=True, blank=True)

    mass_intercept_3__13_ = models.FloatField(null=True, blank=True)

    mass_slope_3__14_ = models.FloatField(null=True, blank=True)

    mass_intercept_3__14_ = models.FloatField(null=True, blank=True)

    mass_slope_3__15_ = models.FloatField(null=True, blank=True)

    mass_intercept_3__15_ = models.FloatField(null=True, blank=True)

    mass_slope_3__16_ = models.IntegerField(null=True, blank=True)

    mass_intercept_3__16_ = models.IntegerField(null=True, blank=True)

    mass_slope_3__17_ = models.IntegerField(null=True, blank=True)

    mass_intercept_3__17_ = models.IntegerField(null=True, blank=True)

    mass_slope_3__18_ = models.IntegerField(null=True, blank=True)

    mass_intercept_3__18_ = models.IntegerField(null=True, blank=True)

    mass_slope_3__19_ = models.IntegerField(null=True, blank=True)

    mass_intercept_3__19_ = models.IntegerField(null=True, blank=True)

    mass_slope_4__0_ = models.FloatField(null=True, blank=True)

    mass_intercept_4__0_ = models.FloatField(null=True, blank=True)

    mass_slope_4__1_ = models.FloatField(null=True, blank=True)

    mass_intercept_4__1_ = models.FloatField(null=True, blank=True)

    mass_slope_4__2_ = models.FloatField(null=True, blank=True)

    mass_intercept_4__2_ = models.FloatField(null=True, blank=True)

    mass_slope_4__3_ = models.FloatField(null=True, blank=True)

    mass_intercept_4__3_ = models.FloatField(null=True, blank=True)

    mass_slope_4__4_ = models.FloatField(null=True, blank=True)

    mass_intercept_4__4_ = models.FloatField(null=True, blank=True)

    mass_slope_4__5_ = models.FloatField(null=True, blank=True)

    mass_intercept_4__5_ = models.FloatField(null=True, blank=True)

    mass_slope_4__6_ = models.IntegerField(null=True, blank=True)

    mass_intercept_4__6_ = models.IntegerField(null=True, blank=True)

    mass_slope_4__7_ = models.IntegerField(null=True, blank=True)

    mass_intercept_4__7_ = models.IntegerField(null=True, blank=True)

    mass_slope_4__8_ = models.IntegerField(null=True, blank=True)

    mass_intercept_4__8_ = models.IntegerField(null=True, blank=True)

    mass_slope_4__9_ = models.IntegerField(null=True, blank=True)

    mass_intercept_4__9_ = models.IntegerField(null=True, blank=True)

    mass_slope_4__10_ = models.IntegerField(null=True, blank=True)

    mass_intercept_4__10_ = models.IntegerField(null=True, blank=True)

    mass_slope_4__11_ = models.IntegerField(null=True, blank=True)

    mass_intercept_4__11_ = models.IntegerField(null=True, blank=True)

    mass_slope_4__12_ = models.IntegerField(null=True, blank=True)

    mass_intercept_4__12_ = models.IntegerField(null=True, blank=True)

    mass_slope_4__13_ = models.IntegerField(null=True, blank=True)

    mass_intercept_4__13_ = models.IntegerField(null=True, blank=True)

    mass_slope_4__14_ = models.IntegerField(null=True, blank=True)

    mass_intercept_4__14_ = models.IntegerField(null=True, blank=True)

    mass_slope_4__15_ = models.IntegerField(null=True, blank=True)

    mass_intercept_4__15_ = models.IntegerField(null=True, blank=True)

    mass_slope_4__16_ = models.IntegerField(null=True, blank=True)

    mass_intercept_4__16_ = models.IntegerField(null=True, blank=True)

    mass_slope_4__17_ = models.IntegerField(null=True, blank=True)

    mass_intercept_4__17_ = models.IntegerField(null=True, blank=True)

    mass_slope_4__18_ = models.IntegerField(null=True, blank=True)

    mass_intercept_4__18_ = models.IntegerField(null=True, blank=True)

    mass_slope_4__19_ = models.IntegerField(null=True, blank=True)

    mass_intercept_4__19_ = models.IntegerField(null=True, blank=True)

    mass_slope_5__0_ = models.FloatField(null=True, blank=True)

    mass_intercept_5__0_ = models.FloatField(null=True, blank=True)

    mass_slope_5__1_ = models.FloatField(null=True, blank=True)

    mass_intercept_5__1_ = models.FloatField(null=True, blank=True)

    mass_slope_5__2_ = models.FloatField(null=True, blank=True)

    mass_intercept_5__2_ = models.FloatField(null=True, blank=True)

    mass_slope_5__3_ = models.FloatField(null=True, blank=True)

    mass_intercept_5__3_ = models.FloatField(null=True, blank=True)

    mass_slope_5__4_ = models.FloatField(null=True, blank=True)

    mass_intercept_5__4_ = models.FloatField(null=True, blank=True)

    mass_slope_5__5_ = models.FloatField(null=True, blank=True)

    mass_intercept_5__5_ = models.FloatField(null=True, blank=True)

    mass_slope_5__6_ = models.IntegerField(null=True, blank=True)

    mass_intercept_5__6_ = models.IntegerField(null=True, blank=True)

    mass_slope_5__7_ = models.IntegerField(null=True, blank=True)

    mass_intercept_5__7_ = models.IntegerField(null=True, blank=True)

    mass_slope_5__8_ = models.IntegerField(null=True, blank=True)

    mass_intercept_5__8_ = models.IntegerField(null=True, blank=True)

    mass_slope_5__9_ = models.IntegerField(null=True, blank=True)

    mass_intercept_5__9_ = models.IntegerField(null=True, blank=True)

    mass_slope_5__10_ = models.IntegerField(null=True, blank=True)

    mass_intercept_5__10_ = models.IntegerField(null=True, blank=True)

    mass_slope_5__11_ = models.IntegerField(null=True, blank=True)

    mass_intercept_5__11_ = models.IntegerField(null=True, blank=True)

    mass_slope_5__12_ = models.IntegerField(null=True, blank=True)

    mass_intercept_5__12_ = models.IntegerField(null=True, blank=True)

    mass_slope_5__13_ = models.IntegerField(null=True, blank=True)

    mass_intercept_5__13_ = models.IntegerField(null=True, blank=True)

    mass_slope_5__14_ = models.IntegerField(null=True, blank=True)

    mass_intercept_5__14_ = models.IntegerField(null=True, blank=True)

    mass_slope_5__15_ = models.IntegerField(null=True, blank=True)

    mass_intercept_5__15_ = models.IntegerField(null=True, blank=True)

    mass_slope_5__16_ = models.IntegerField(null=True, blank=True)

    mass_intercept_5__16_ = models.IntegerField(null=True, blank=True)

    mass_slope_5__17_ = models.IntegerField(null=True, blank=True)

    mass_intercept_5__17_ = models.IntegerField(null=True, blank=True)

    mass_slope_5__18_ = models.IntegerField(null=True, blank=True)

    mass_intercept_5__18_ = models.IntegerField(null=True, blank=True)

    mass_slope_5__19_ = models.IntegerField(null=True, blank=True)

    mass_intercept_5__19_ = models.IntegerField(null=True, blank=True)

    mass_slope_6__0_ = models.FloatField(null=True, blank=True)

    mass_intercept_6__0_ = models.FloatField(null=True, blank=True)

    mass_slope_6__1_ = models.FloatField(null=True, blank=True)

    mass_intercept_6__1_ = models.FloatField(null=True, blank=True)

    mass_slope_6__2_ = models.FloatField(null=True, blank=True)

    mass_intercept_6__2_ = models.FloatField(null=True, blank=True)

    mass_slope_6__3_ = models.FloatField(null=True, blank=True)

    mass_intercept_6__3_ = models.FloatField(null=True, blank=True)

    mass_slope_6__4_ = models.FloatField(null=True, blank=True)

    mass_intercept_6__4_ = models.FloatField(null=True, blank=True)

    mass_slope_6__5_ = models.FloatField(null=True, blank=True)

    mass_intercept_6__5_ = models.FloatField(null=True, blank=True)

    mass_slope_6__6_ = models.IntegerField(null=True, blank=True)

    mass_intercept_6__6_ = models.FloatField(null=True, blank=True)

    mass_slope_6__7_ = models.IntegerField(null=True, blank=True)

    mass_intercept_6__7_ = models.IntegerField(null=True, blank=True)

    mass_slope_6__8_ = models.IntegerField(null=True, blank=True)

    mass_intercept_6__8_ = models.IntegerField(null=True, blank=True)

    mass_slope_6__9_ = models.IntegerField(null=True, blank=True)

    mass_intercept_6__9_ = models.IntegerField(null=True, blank=True)

    mass_slope_6__10_ = models.IntegerField(null=True, blank=True)

    mass_intercept_6__10_ = models.IntegerField(null=True, blank=True)

    mass_slope_6__11_ = models.IntegerField(null=True, blank=True)

    mass_intercept_6__11_ = models.IntegerField(null=True, blank=True)

    mass_slope_6__12_ = models.IntegerField(null=True, blank=True)

    mass_intercept_6__12_ = models.IntegerField(null=True, blank=True)

    mass_slope_6__13_ = models.IntegerField(null=True, blank=True)

    mass_intercept_6__13_ = models.IntegerField(null=True, blank=True)

    mass_slope_6__14_ = models.IntegerField(null=True, blank=True)

    mass_intercept_6__14_ = models.IntegerField(null=True, blank=True)

    mass_slope_6__15_ = models.IntegerField(null=True, blank=True)

    mass_intercept_6__15_ = models.IntegerField(null=True, blank=True)

    mass_slope_6__16_ = models.IntegerField(null=True, blank=True)

    mass_intercept_6__16_ = models.IntegerField(null=True, blank=True)

    mass_slope_6__17_ = models.IntegerField(null=True, blank=True)

    mass_intercept_6__17_ = models.IntegerField(null=True, blank=True)

    mass_slope_6__18_ = models.IntegerField(null=True, blank=True)

    mass_intercept_6__18_ = models.IntegerField(null=True, blank=True)

    mass_slope_6__19_ = models.IntegerField(null=True, blank=True)

    mass_intercept_6__19_ = models.IntegerField(null=True, blank=True)

    mass_slope_7__0_ = models.FloatField(null=True, blank=True)

    mass_intercept_7__0_ = models.FloatField(null=True, blank=True)

    mass_slope_7__1_ = models.FloatField(null=True, blank=True)

    mass_intercept_7__1_ = models.FloatField(null=True, blank=True)

    mass_slope_7__2_ = models.FloatField(null=True, blank=True)

    mass_intercept_7__2_ = models.FloatField(null=True, blank=True)

    mass_slope_7__3_ = models.FloatField(null=True, blank=True)

    mass_intercept_7__3_ = models.FloatField(null=True, blank=True)

    mass_slope_7__4_ = models.FloatField(null=True, blank=True)

    mass_intercept_7__4_ = models.FloatField(null=True, blank=True)

    mass_slope_7__5_ = models.FloatField(null=True, blank=True)

    mass_intercept_7__5_ = models.FloatField(null=True, blank=True)

    mass_slope_7__6_ = models.FloatField(null=True, blank=True)

    mass_intercept_7__6_ = models.FloatField(null=True, blank=True)

    mass_slope_7__7_ = models.FloatField(null=True, blank=True)

    mass_intercept_7__7_ = models.FloatField(null=True, blank=True)

    mass_slope_7__8_ = models.FloatField(null=True, blank=True)

    mass_intercept_7__8_ = models.FloatField(null=True, blank=True)

    mass_slope_7__9_ = models.FloatField(null=True, blank=True)

    mass_intercept_7__9_ = models.FloatField(null=True, blank=True)

    mass_slope_7__10_ = models.IntegerField(null=True, blank=True)

    mass_intercept_7__10_ = models.IntegerField(null=True, blank=True)

    mass_slope_7__11_ = models.IntegerField(null=True, blank=True)

    mass_intercept_7__11_ = models.IntegerField(null=True, blank=True)

    mass_slope_7__12_ = models.IntegerField(null=True, blank=True)

    mass_intercept_7__12_ = models.IntegerField(null=True, blank=True)

    mass_slope_7__13_ = models.IntegerField(null=True, blank=True)

    mass_intercept_7__13_ = models.IntegerField(null=True, blank=True)

    mass_slope_7__14_ = models.IntegerField(null=True, blank=True)

    mass_intercept_7__14_ = models.IntegerField(null=True, blank=True)

    mass_slope_7__15_ = models.IntegerField(null=True, blank=True)

    mass_intercept_7__15_ = models.IntegerField(null=True, blank=True)

    mass_slope_7__16_ = models.IntegerField(null=True, blank=True)

    mass_intercept_7__16_ = models.IntegerField(null=True, blank=True)

    mass_slope_7__17_ = models.IntegerField(null=True, blank=True)

    mass_intercept_7__17_ = models.IntegerField(null=True, blank=True)

    mass_slope_7__18_ = models.IntegerField(null=True, blank=True)

    mass_intercept_7__18_ = models.IntegerField(null=True, blank=True)

    mass_slope_7__19_ = models.IntegerField(null=True, blank=True)

    mass_intercept_7__19_ = models.IntegerField(null=True, blank=True)

    mass_slope_8__0_ = models.FloatField(null=True, blank=True)

    mass_intercept_8__0_ = models.FloatField(null=True, blank=True)

    mass_slope_8__1_ = models.FloatField(null=True, blank=True)

    mass_intercept_8__1_ = models.FloatField(null=True, blank=True)

    mass_slope_8__2_ = models.FloatField(null=True, blank=True)

    mass_intercept_8__2_ = models.FloatField(null=True, blank=True)

    mass_slope_8__3_ = models.FloatField(null=True, blank=True)

    mass_intercept_8__3_ = models.FloatField(null=True, blank=True)

    mass_slope_8__4_ = models.FloatField(null=True, blank=True)

    mass_intercept_8__4_ = models.FloatField(null=True, blank=True)

    mass_slope_8__5_ = models.FloatField(null=True, blank=True)

    mass_intercept_8__5_ = models.FloatField(null=True, blank=True)

    mass_slope_8__6_ = models.IntegerField(null=True, blank=True)

    mass_intercept_8__6_ = models.IntegerField(null=True, blank=True)

    mass_slope_8__7_ = models.IntegerField(null=True, blank=True)

    mass_intercept_8__7_ = models.IntegerField(null=True, blank=True)

    mass_slope_8__8_ = models.IntegerField(null=True, blank=True)

    mass_intercept_8__8_ = models.IntegerField(null=True, blank=True)

    mass_slope_8__9_ = models.IntegerField(null=True, blank=True)

    mass_intercept_8__9_ = models.IntegerField(null=True, blank=True)

    mass_slope_8__10_ = models.IntegerField(null=True, blank=True)

    mass_intercept_8__10_ = models.IntegerField(null=True, blank=True)

    mass_slope_8__11_ = models.IntegerField(null=True, blank=True)

    mass_intercept_8__11_ = models.IntegerField(null=True, blank=True)

    mass_slope_8__12_ = models.IntegerField(null=True, blank=True)

    mass_intercept_8__12_ = models.IntegerField(null=True, blank=True)

    mass_slope_8__13_ = models.IntegerField(null=True, blank=True)

    mass_intercept_8__13_ = models.IntegerField(null=True, blank=True)

    mass_slope_8__14_ = models.IntegerField(null=True, blank=True)

    mass_intercept_8__14_ = models.IntegerField(null=True, blank=True)

    mass_slope_8__15_ = models.IntegerField(null=True, blank=True)

    mass_intercept_8__15_ = models.IntegerField(null=True, blank=True)

    mass_slope_8__16_ = models.IntegerField(null=True, blank=True)

    mass_intercept_8__16_ = models.IntegerField(null=True, blank=True)

    mass_slope_8__17_ = models.IntegerField(null=True, blank=True)

    mass_intercept_8__17_ = models.IntegerField(null=True, blank=True)

    mass_slope_8__18_ = models.IntegerField(null=True, blank=True)

    mass_intercept_8__18_ = models.IntegerField(null=True, blank=True)

    mass_slope_8__19_ = models.IntegerField(null=True, blank=True)

    mass_intercept_8__19_ = models.IntegerField(null=True, blank=True)

    mass_slope_9__0_ = models.FloatField(null=True, blank=True)

    mass_intercept_9__0_ = models.FloatField(null=True, blank=True)

    mass_slope_9__1_ = models.FloatField(null=True, blank=True)

    mass_intercept_9__1_ = models.FloatField(null=True, blank=True)

    mass_slope_9__2_ = models.FloatField(null=True, blank=True)

    mass_intercept_9__2_ = models.FloatField(null=True, blank=True)

    mass_slope_9__3_ = models.FloatField(null=True, blank=True)

    mass_intercept_9__3_ = models.FloatField(null=True, blank=True)

    mass_slope_9__4_ = models.FloatField(null=True, blank=True)

    mass_intercept_9__4_ = models.FloatField(null=True, blank=True)

    mass_slope_9__5_ = models.FloatField(null=True, blank=True)

    mass_intercept_9__5_ = models.FloatField(null=True, blank=True)

    mass_slope_9__6_ = models.IntegerField(null=True, blank=True)

    mass_intercept_9__6_ = models.FloatField(null=True, blank=True)

    mass_slope_9__7_ = models.IntegerField(null=True, blank=True)

    mass_intercept_9__7_ = models.IntegerField(null=True, blank=True)

    mass_slope_9__8_ = models.IntegerField(null=True, blank=True)

    mass_intercept_9__8_ = models.IntegerField(null=True, blank=True)

    mass_slope_9__9_ = models.IntegerField(null=True, blank=True)

    mass_intercept_9__9_ = models.IntegerField(null=True, blank=True)

    mass_slope_9__10_ = models.IntegerField(null=True, blank=True)

    mass_intercept_9__10_ = models.IntegerField(null=True, blank=True)

    mass_slope_9__11_ = models.IntegerField(null=True, blank=True)

    mass_intercept_9__11_ = models.IntegerField(null=True, blank=True)

    mass_slope_9__12_ = models.IntegerField(null=True, blank=True)

    mass_intercept_9__12_ = models.IntegerField(null=True, blank=True)

    mass_slope_9__13_ = models.IntegerField(null=True, blank=True)

    mass_intercept_9__13_ = models.IntegerField(null=True, blank=True)

    mass_slope_9__14_ = models.IntegerField(null=True, blank=True)

    mass_intercept_9__14_ = models.IntegerField(null=True, blank=True)

    mass_slope_9__15_ = models.IntegerField(null=True, blank=True)

    mass_intercept_9__15_ = models.IntegerField(null=True, blank=True)

    mass_slope_9__16_ = models.IntegerField(null=True, blank=True)

    mass_intercept_9__16_ = models.IntegerField(null=True, blank=True)

    mass_slope_9__17_ = models.IntegerField(null=True, blank=True)

    mass_intercept_9__17_ = models.IntegerField(null=True, blank=True)

    mass_slope_9__18_ = models.IntegerField(null=True, blank=True)

    mass_intercept_9__18_ = models.IntegerField(null=True, blank=True)

    mass_slope_9__19_ = models.IntegerField(null=True, blank=True)

    mass_intercept_9__19_ = models.IntegerField(null=True, blank=True)

    mass_slope_10__0_ = models.FloatField(null=True, blank=True)

    mass_intercept_10__0_ = models.FloatField(null=True, blank=True)

    mass_slope_10__1_ = models.FloatField(null=True, blank=True)

    mass_intercept_10__1_ = models.FloatField(null=True, blank=True)

    mass_slope_10__2_ = models.FloatField(null=True, blank=True)

    mass_intercept_10__2_ = models.FloatField(null=True, blank=True)

    mass_slope_10__3_ = models.FloatField(null=True, blank=True)

    mass_intercept_10__3_ = models.FloatField(null=True, blank=True)

    mass_slope_10__4_ = models.FloatField(null=True, blank=True)

    mass_intercept_10__4_ = models.FloatField(null=True, blank=True)

    mass_slope_10__5_ = models.FloatField(null=True, blank=True)

    mass_intercept_10__5_ = models.FloatField(null=True, blank=True)

    mass_slope_10__6_ = models.IntegerField(null=True, blank=True)

    mass_intercept_10__6_ = models.IntegerField(null=True, blank=True)

    mass_slope_10__7_ = models.IntegerField(null=True, blank=True)

    mass_intercept_10__7_ = models.IntegerField(null=True, blank=True)

    mass_slope_10__8_ = models.IntegerField(null=True, blank=True)

    mass_intercept_10__8_ = models.IntegerField(null=True, blank=True)

    mass_slope_10__9_ = models.IntegerField(null=True, blank=True)

    mass_intercept_10__9_ = models.IntegerField(null=True, blank=True)

    mass_slope_10__10_ = models.IntegerField(null=True, blank=True)

    mass_intercept_10__10_ = models.IntegerField(null=True, blank=True)

    mass_slope_10__11_ = models.IntegerField(null=True, blank=True)

    mass_intercept_10__11_ = models.IntegerField(null=True, blank=True)

    mass_slope_10__12_ = models.IntegerField(null=True, blank=True)

    mass_intercept_10__12_ = models.IntegerField(null=True, blank=True)

    mass_slope_10__13_ = models.IntegerField(null=True, blank=True)

    mass_intercept_10__13_ = models.IntegerField(null=True, blank=True)

    mass_slope_10__14_ = models.IntegerField(null=True, blank=True)

    mass_intercept_10__14_ = models.IntegerField(null=True, blank=True)

    mass_slope_10__15_ = models.IntegerField(null=True, blank=True)

    mass_intercept_10__15_ = models.IntegerField(null=True, blank=True)

    mass_slope_10__16_ = models.IntegerField(null=True, blank=True)

    mass_intercept_10__16_ = models.IntegerField(null=True, blank=True)

    mass_slope_10__17_ = models.IntegerField(null=True, blank=True)

    mass_intercept_10__17_ = models.IntegerField(null=True, blank=True)

    mass_slope_10__18_ = models.IntegerField(null=True, blank=True)

    mass_intercept_10__18_ = models.IntegerField(null=True, blank=True)

    mass_slope_10__19_ = models.IntegerField(null=True, blank=True)

    mass_intercept_10__19_ = models.IntegerField(null=True, blank=True)

    mass_slope_11__0_ = models.FloatField(null=True, blank=True)

    mass_intercept_11__0_ = models.FloatField(null=True, blank=True)

    mass_slope_11__1_ = models.FloatField(null=True, blank=True)

    mass_intercept_11__1_ = models.FloatField(null=True, blank=True)

    mass_slope_11__2_ = models.FloatField(null=True, blank=True)

    mass_intercept_11__2_ = models.FloatField(null=True, blank=True)

    mass_slope_11__3_ = models.FloatField(null=True, blank=True)

    mass_intercept_11__3_ = models.FloatField(null=True, blank=True)

    mass_slope_11__4_ = models.FloatField(null=True, blank=True)

    mass_intercept_11__4_ = models.FloatField(null=True, blank=True)

    mass_slope_11__5_ = models.FloatField(null=True, blank=True)

    mass_intercept_11__5_ = models.FloatField(null=True, blank=True)

    mass_slope_11__6_ = models.FloatField(null=True, blank=True)

    mass_intercept_11__6_ = models.FloatField(null=True, blank=True)

    mass_slope_11__7_ = models.FloatField(null=True, blank=True)

    mass_intercept_11__7_ = models.FloatField(null=True, blank=True)

    mass_slope_11__8_ = models.FloatField(null=True, blank=True)

    mass_intercept_11__8_ = models.FloatField(null=True, blank=True)

    mass_slope_11__9_ = models.FloatField(null=True, blank=True)

    mass_intercept_11__9_ = models.FloatField(null=True, blank=True)

    mass_slope_11__10_ = models.FloatField(null=True, blank=True)

    mass_intercept_11__10_ = models.FloatField(null=True, blank=True)

    mass_slope_11__11_ = models.FloatField(null=True, blank=True)

    mass_intercept_11__11_ = models.FloatField(null=True, blank=True)

    mass_slope_11__12_ = models.FloatField(null=True, blank=True)

    mass_intercept_11__12_ = models.FloatField(null=True, blank=True)

    mass_slope_11__13_ = models.FloatField(null=True, blank=True)

    mass_intercept_11__13_ = models.FloatField(null=True, blank=True)

    mass_slope_11__14_ = models.FloatField(null=True, blank=True)

    mass_intercept_11__14_ = models.FloatField(null=True, blank=True)

    mass_slope_11__15_ = models.FloatField(null=True, blank=True)

    mass_intercept_11__15_ = models.FloatField(null=True, blank=True)

    mass_slope_11__16_ = models.IntegerField(null=True, blank=True)

    mass_intercept_11__16_ = models.IntegerField(null=True, blank=True)

    mass_slope_11__17_ = models.IntegerField(null=True, blank=True)

    mass_intercept_11__17_ = models.IntegerField(null=True, blank=True)

    mass_slope_11__18_ = models.IntegerField(null=True, blank=True)

    mass_intercept_11__18_ = models.IntegerField(null=True, blank=True)

    mass_slope_11__19_ = models.IntegerField(null=True, blank=True)

    mass_intercept_11__19_ = models.IntegerField(null=True, blank=True)

    mass_slope_12__0_ = models.FloatField(null=True, blank=True)

    mass_intercept_12__0_ = models.FloatField(null=True, blank=True)

    mass_slope_12__1_ = models.FloatField(null=True, blank=True)

    mass_intercept_12__1_ = models.FloatField(null=True, blank=True)

    mass_slope_12__2_ = models.FloatField(null=True, blank=True)

    mass_intercept_12__2_ = models.FloatField(null=True, blank=True)

    mass_slope_12__3_ = models.FloatField(null=True, blank=True)

    mass_intercept_12__3_ = models.FloatField(null=True, blank=True)

    mass_slope_12__4_ = models.FloatField(null=True, blank=True)

    mass_intercept_12__4_ = models.FloatField(null=True, blank=True)

    mass_slope_12__5_ = models.FloatField(null=True, blank=True)

    mass_intercept_12__5_ = models.FloatField(null=True, blank=True)

    mass_slope_12__6_ = models.FloatField(null=True, blank=True)

    mass_intercept_12__6_ = models.FloatField(null=True, blank=True)

    mass_slope_12__7_ = models.FloatField(null=True, blank=True)

    mass_intercept_12__7_ = models.FloatField(null=True, blank=True)

    mass_slope_12__8_ = models.FloatField(null=True, blank=True)

    mass_intercept_12__8_ = models.FloatField(null=True, blank=True)

    mass_slope_12__9_ = models.FloatField(null=True, blank=True)

    mass_intercept_12__9_ = models.FloatField(null=True, blank=True)

    mass_slope_12__10_ = models.FloatField(null=True, blank=True)

    mass_intercept_12__10_ = models.FloatField(null=True, blank=True)

    mass_slope_12__11_ = models.FloatField(null=True, blank=True)

    mass_intercept_12__11_ = models.FloatField(null=True, blank=True)

    mass_slope_12__12_ = models.FloatField(null=True, blank=True)

    mass_intercept_12__12_ = models.FloatField(null=True, blank=True)

    mass_slope_12__13_ = models.FloatField(null=True, blank=True)

    mass_intercept_12__13_ = models.FloatField(null=True, blank=True)

    mass_slope_12__14_ = models.FloatField(null=True, blank=True)

    mass_intercept_12__14_ = models.FloatField(null=True, blank=True)

    mass_slope_12__15_ = models.FloatField(null=True, blank=True)

    mass_intercept_12__15_ = models.FloatField(null=True, blank=True)

    mass_slope_12__16_ = models.IntegerField(null=True, blank=True)

    mass_intercept_12__16_ = models.IntegerField(null=True, blank=True)

    mass_slope_12__17_ = models.IntegerField(null=True, blank=True)

    mass_intercept_12__17_ = models.IntegerField(null=True, blank=True)

    mass_slope_12__18_ = models.IntegerField(null=True, blank=True)

    mass_intercept_12__18_ = models.IntegerField(null=True, blank=True)

    mass_slope_12__19_ = models.IntegerField(null=True, blank=True)

    mass_intercept_12__19_ = models.IntegerField(null=True, blank=True)

    center_lens_highlow_transfer_pos_v = models.FloatField(null=True, blank=True)

    back_section_highlow_transfer_pos_v = models.FloatField(null=True, blank=True)

    center_lens_highlow_transfer_neg_v = models.FloatField(null=True, blank=True)

    back_section_highlow_transfer_neg_v = models.FloatField(null=True, blank=True)

    center_lens_lowhigh_transfer_pos_v = models.FloatField(null=True, blank=True)

    front_section_lowhigh_transfer_pos_v = models.FloatField(null=True, blank=True)

    center_lens_lowhigh_transfer_neg_v = models.FloatField(null=True, blank=True)

    front_section_lowhigh_transfer_neg_v = models.FloatField(null=True, blank=True)

    scan_phase_0 = models.FloatField(null=True, blank=True)

    scan_phase_1 = models.IntegerField(null=True, blank=True)

    scan_phase_2 = models.IntegerField(null=True, blank=True)

    scan_phase_3 = models.IntegerField(null=True, blank=True)

    scan_phase_4 = models.IntegerField(null=True, blank=True)

    scan_phase_5 = models.IntegerField(null=True, blank=True)

    scan_phase_6 = models.FloatField(null=True, blank=True)

    scan_phase_7 = models.IntegerField(null=True, blank=True)

    scan_phase_8 = models.FloatField(null=True, blank=True)

    scan_phase_9 = models.IntegerField(null=True, blank=True)

    scan_phase_10 = models.IntegerField(null=True, blank=True)

    scan_phase_11 = models.IntegerField(null=True, blank=True)

    scan_phase_12 = models.IntegerField(null=True, blank=True)

    multiplier_1_res_ej_phase_pos = models.FloatField(null=True, blank=True)

    multiplier_2_res_ej_phase_pos = models.FloatField(null=True, blank=True)

    multiplier_1_res_ej_phase_neg = models.FloatField(null=True, blank=True)

    multiplier_2_res_ej_phase_neg = models.FloatField(null=True, blank=True)

    center_lens_lpt_device_min_v = models.FloatField(null=True, blank=True)

    center_lens_lpt_device_max_v = models.FloatField(null=True, blank=True)

    front_section_lpt_device_min_v = models.FloatField(null=True, blank=True)

    front_section_lpt_device_max_v = models.FloatField(null=True, blank=True)

    center_section_lpt_device_min_v = models.FloatField(null=True, blank=True)

    center_section_lpt_device_max_v = models.FloatField(null=True, blank=True)

    back_section_lpt_device_min_v = models.FloatField(null=True, blank=True)

    back_section_lpt_device_max_v = models.FloatField(null=True, blank=True)

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
    
    ft_cal_item_251 = models.FloatField(null=True, blank=True)

    ft_cal_item_252 = models.FloatField(null=True, blank=True)

    ft_cal_item_253 = models.FloatField(null=True, blank=True)

    ft_cal_item_254 = models.FloatField(null=True, blank=True)

    ft_cal_item_255 = models.FloatField(null=True, blank=True)

    ft_cal_item_256 = models.FloatField(null=True, blank=True)

    ft_cal_item_257 = models.FloatField(null=True, blank=True)

    ft_cal_item_258 = models.FloatField(null=True, blank=True)

    ft_cal_item_259 = models.FloatField(null=True, blank=True)

    ft_cal_item_260 = models.FloatField(null=True, blank=True)

    ft_cal_item_261 = models.FloatField(null=True, blank=True)

    ft_cal_item_262 = models.FloatField(null=True, blank=True)

    ft_cal_item_263 = models.FloatField(null=True, blank=True)

    ft_cal_item_264 = models.FloatField(null=True, blank=True)

    ft_cal_item_265 = models.FloatField(null=True, blank=True)

    ft_cal_item_266 = models.FloatField(null=True, blank=True)

    ft_cal_item_267 = models.FloatField(null=True, blank=True)

    ft_cal_item_268 = models.FloatField(null=True, blank=True)

    ft_cal_item_269 = models.FloatField(null=True, blank=True)

    ft_cal_item_270 = models.FloatField(null=True, blank=True)

    ft_cal_item_271 = models.FloatField(null=True, blank=True)

    ft_cal_item_272 = models.FloatField(null=True, blank=True)

    ft_cal_item_273 = models.FloatField(null=True, blank=True)

    ft_cal_item_274 = models.FloatField(null=True, blank=True)

    ft_cal_item_275 = models.FloatField(null=True, blank=True)

    ft_cal_item_276 = models.FloatField(null=True, blank=True)

    ft_cal_item_277 = models.FloatField(null=True, blank=True)

    ft_cal_item_278 = models.FloatField(null=True, blank=True)

    ft_cal_item_279 = models.FloatField(null=True, blank=True)

    ft_cal_item_280 = models.FloatField(null=True, blank=True)

    ft_cal_item_281 = models.FloatField(null=True, blank=True)

    ft_cal_item_282 = models.FloatField(null=True, blank=True)

    ft_cal_item_283 = models.FloatField(null=True, blank=True)

    ft_cal_item_284 = models.FloatField(null=True, blank=True)

    ft_cal_item_285 = models.FloatField(null=True, blank=True)

    ft_cal_item_286 = models.FloatField(null=True, blank=True)

    ft_cal_item_287 = models.FloatField(null=True, blank=True)

    ft_cal_item_288 = models.FloatField(null=True, blank=True)

    ft_cal_item_289 = models.FloatField(null=True, blank=True)

    ft_cal_item_290 = models.FloatField(null=True, blank=True)

    ft_cal_item_291 = models.FloatField(null=True, blank=True)

    ft_cal_item_292 = models.FloatField(null=True, blank=True)

    ft_cal_item_293 = models.FloatField(null=True, blank=True)

    ft_cal_item_294 = models.FloatField(null=True, blank=True)

    ft_cal_item_295 = models.FloatField(null=True, blank=True)

    ft_cal_item_296 = models.FloatField(null=True, blank=True)

    ft_cal_item_297 = models.FloatField(null=True, blank=True)

    ft_cal_item_298 = models.FloatField(null=True, blank=True)

    ft_cal_item_299 = models.FloatField(null=True, blank=True)

    ft_cal_item_300 = models.FloatField(null=True, blank=True)

    ft_cal_item_301 = models.FloatField(null=True, blank=True)

    ft_cal_item_302 = models.FloatField(null=True, blank=True)

    ft_cal_item_303 = models.FloatField(null=True, blank=True)

    ft_cal_item_304 = models.FloatField(null=True, blank=True)

    ft_cal_item_305 = models.FloatField(null=True, blank=True)

    ft_cal_item_306 = models.FloatField(null=True, blank=True)

    ft_cal_item_307 = models.FloatField(null=True, blank=True)

    ft_cal_item_308 = models.FloatField(null=True, blank=True)

    ft_cal_item_309 = models.FloatField(null=True, blank=True)

    ft_cal_item_310 = models.FloatField(null=True, blank=True)

    ft_cal_item_311 = models.FloatField(null=True, blank=True)

    ft_cal_item_312 = models.FloatField(null=True, blank=True)

    ft_cal_item_313 = models.FloatField(null=True, blank=True)

    ft_cal_item_314 = models.FloatField(null=True, blank=True)

    ft_cal_item_315 = models.FloatField(null=True, blank=True)

    ft_cal_item_316 = models.FloatField(null=True, blank=True)

    ft_cal_item_317 = models.FloatField(null=True, blank=True)

    ft_cal_item_318 = models.FloatField(null=True, blank=True)

    ft_cal_item_319 = models.FloatField(null=True, blank=True)

    ft_cal_item_320 = models.FloatField(null=True, blank=True)

    ft_cal_item_321 = models.FloatField(null=True, blank=True)

    ft_cal_item_322 = models.FloatField(null=True, blank=True)

    ft_cal_item_323 = models.FloatField(null=True, blank=True)

    ft_cal_item_324 = models.FloatField(null=True, blank=True)

    ft_cal_item_325 = models.FloatField(null=True, blank=True)

    ft_cal_item_326 = models.FloatField(null=True, blank=True)

    ft_cal_item_327 = models.FloatField(null=True, blank=True)

    ft_cal_item_328 = models.FloatField(null=True, blank=True)

    ft_cal_item_329 = models.FloatField(null=True, blank=True)

    ft_cal_item_330 = models.FloatField(null=True, blank=True)

    ft_cal_item_331 = models.FloatField(null=True, blank=True)

    ft_cal_item_332 = models.FloatField(null=True, blank=True)

    ft_cal_item_333 = models.FloatField(null=True, blank=True)

    ft_cal_item_334 = models.FloatField(null=True, blank=True)

    ft_cal_item_335 = models.FloatField(null=True, blank=True)

    ft_cal_item_336 = models.FloatField(null=True, blank=True)

    ft_cal_item_337 = models.FloatField(null=True, blank=True)

    ft_cal_item_338 = models.FloatField(null=True, blank=True)

    ft_cal_item_339 = models.FloatField(null=True, blank=True)

    ft_cal_item_340 = models.FloatField(null=True, blank=True)

    ft_cal_item_341 = models.FloatField(null=True, blank=True)

    ft_cal_item_342 = models.FloatField(null=True, blank=True)

    ft_cal_item_343 = models.FloatField(null=True, blank=True)

    ft_cal_item_344 = models.FloatField(null=True, blank=True)

    ft_cal_item_345 = models.FloatField(null=True, blank=True)

    ft_cal_item_346 = models.FloatField(null=True, blank=True)

    ft_cal_item_347 = models.FloatField(null=True, blank=True)

    ft_cal_item_348 = models.FloatField(null=True, blank=True)

    ft_cal_item_349 = models.FloatField(null=True, blank=True)

    ft_cal_item_350 = models.FloatField(null=True, blank=True)

    ft_cal_item_351 = models.FloatField(null=True, blank=True)

    ft_cal_item_352 = models.FloatField(null=True, blank=True)

    ft_cal_item_353 = models.FloatField(null=True, blank=True)

    ft_cal_item_354 = models.FloatField(null=True, blank=True)

    ft_cal_item_355 = models.FloatField(null=True, blank=True)

    ft_cal_item_356 = models.FloatField(null=True, blank=True)

    ft_cal_item_357 = models.FloatField(null=True, blank=True)

    ft_cal_item_358 = models.FloatField(null=True, blank=True)

    ft_cal_item_359 = models.FloatField(null=True, blank=True)

    ft_cal_item_360 = models.FloatField(null=True, blank=True)

    ft_cal_item_361 = models.FloatField(null=True, blank=True)

    ft_cal_item_362 = models.FloatField(null=True, blank=True)

    ft_cal_item_363 = models.FloatField(null=True, blank=True)

    ft_cal_item_364 = models.FloatField(null=True, blank=True)

    ft_cal_item_365 = models.FloatField(null=True, blank=True)

    ft_cal_item_366 = models.FloatField(null=True, blank=True)

    ft_cal_item_367 = models.FloatField(null=True, blank=True)

    ft_cal_item_368 = models.FloatField(null=True, blank=True)

    ft_cal_item_369 = models.FloatField(null=True, blank=True)

    ft_cal_item_370 = models.FloatField(null=True, blank=True)

    ft_cal_item_371 = models.FloatField(null=True, blank=True)

    ft_cal_item_372 = models.FloatField(null=True, blank=True)

    ft_cal_item_373 = models.FloatField(null=True, blank=True)

    ft_cal_item_374 = models.FloatField(null=True, blank=True)

    ft_cal_item_375 = models.FloatField(null=True, blank=True)

    ft_cal_item_376 = models.FloatField(null=True, blank=True)

    ft_cal_item_377 = models.FloatField(null=True, blank=True)

    ft_cal_item_378 = models.FloatField(null=True, blank=True)

    ft_cal_item_379 = models.FloatField(null=True, blank=True)

    ft_cal_item_380 = models.FloatField(null=True, blank=True)

    ft_cal_item_381 = models.FloatField(null=True, blank=True)

    ft_cal_item_382 = models.FloatField(null=True, blank=True)

    ft_cal_item_383 = models.FloatField(null=True, blank=True)

    ft_cal_item_384 = models.FloatField(null=True, blank=True)

    ft_cal_item_385 = models.FloatField(null=True, blank=True)

    ft_cal_item_386 = models.FloatField(null=True, blank=True)

    ft_cal_item_387 = models.FloatField(null=True, blank=True)

    ft_cal_item_388 = models.FloatField(null=True, blank=True)

    ft_cal_item_389 = models.FloatField(null=True, blank=True)

    ft_cal_item_390 = models.FloatField(null=True, blank=True)

    ft_cal_item_391 = models.FloatField(null=True, blank=True)

    ft_cal_item_392 = models.FloatField(null=True, blank=True)

    ft_cal_item_393 = models.FloatField(null=True, blank=True)

    ft_cal_item_394 = models.FloatField(null=True, blank=True)

    ft_cal_item_395 = models.FloatField(null=True, blank=True)

    ft_cal_item_396 = models.FloatField(null=True, blank=True)

    ft_cal_item_397 = models.FloatField(null=True, blank=True)

    ft_cal_item_398 = models.FloatField(null=True, blank=True)

    ft_cal_item_399 = models.FloatField(null=True, blank=True)

    ft_cal_item_400 = models.FloatField(null=True, blank=True)

    ft_cal_item_401 = models.FloatField(null=True, blank=True)

    ft_cal_item_402 = models.FloatField(null=True, blank=True)

    ft_cal_item_403 = models.FloatField(null=True, blank=True)

    ft_cal_item_404 = models.FloatField(null=True, blank=True)

    ft_cal_item_405 = models.FloatField(null=True, blank=True)

    ft_cal_item_406 = models.FloatField(null=True, blank=True)

    ft_cal_item_407 = models.FloatField(null=True, blank=True)

    ft_cal_item_408 = models.FloatField(null=True, blank=True)

    ft_cal_item_409 = models.FloatField(null=True, blank=True)

    ft_cal_item_410 = models.FloatField(null=True, blank=True)

    ft_cal_item_411 = models.FloatField(null=True, blank=True)

    ft_cal_item_412 = models.FloatField(null=True, blank=True)

    ft_cal_item_413 = models.FloatField(null=True, blank=True)

    ft_cal_item_414 = models.FloatField(null=True, blank=True)

    ft_cal_item_415 = models.FloatField(null=True, blank=True)

    ft_cal_item_416 = models.FloatField(null=True, blank=True)

    ft_cal_item_417 = models.FloatField(null=True, blank=True)

    ft_cal_item_418 = models.FloatField(null=True, blank=True)

    ft_cal_item_419 = models.FloatField(null=True, blank=True)

    ft_cal_item_420 = models.FloatField(null=True, blank=True)

    ft_cal_item_421 = models.FloatField(null=True, blank=True)

    ft_cal_item_422 = models.FloatField(null=True, blank=True)

    ft_cal_item_423 = models.FloatField(null=True, blank=True)

    ft_cal_item_424 = models.FloatField(null=True, blank=True)

    ft_cal_item_425 = models.FloatField(null=True, blank=True)

    ft_cal_item_426 = models.FloatField(null=True, blank=True)

    ft_cal_item_427 = models.FloatField(null=True, blank=True)

    ft_cal_item_428 = models.FloatField(null=True, blank=True)

    ft_cal_item_429 = models.FloatField(null=True, blank=True)

    ft_cal_item_430 = models.FloatField(null=True, blank=True)

    ft_cal_item_431 = models.FloatField(null=True, blank=True)

    ft_cal_item_432 = models.FloatField(null=True, blank=True)

    ft_cal_item_433 = models.FloatField(null=True, blank=True)

    ft_cal_item_434 = models.FloatField(null=True, blank=True)

    ft_cal_item_435 = models.FloatField(null=True, blank=True)

    ft_cal_item_436 = models.FloatField(null=True, blank=True)

    ft_cal_item_437 = models.FloatField(null=True, blank=True)

    ft_cal_item_438 = models.FloatField(null=True, blank=True)

    ft_cal_item_439 = models.FloatField(null=True, blank=True)

    ft_cal_item_440 = models.FloatField(null=True, blank=True)

    ft_cal_item_441 = models.FloatField(null=True, blank=True)

    ft_cal_item_442 = models.FloatField(null=True, blank=True)

    ft_cal_item_443 = models.FloatField(null=True, blank=True)

    ft_cal_item_444 = models.FloatField(null=True, blank=True)

    ft_cal_item_445 = models.FloatField(null=True, blank=True)

    ft_cal_item_446 = models.FloatField(null=True, blank=True)

    ft_cal_item_447 = models.FloatField(null=True, blank=True)

    ft_cal_item_448 = models.FloatField(null=True, blank=True)

    ft_cal_item_449 = models.FloatField(null=True, blank=True)

    ft_cal_item_450 = models.FloatField(null=True, blank=True)

    ft_cal_item_451 = models.FloatField(null=True, blank=True)

    ft_cal_item_452 = models.FloatField(null=True, blank=True)

    ft_cal_item_453 = models.FloatField(null=True, blank=True)

    ft_cal_item_454 = models.FloatField(null=True, blank=True)

    ft_cal_item_455 = models.FloatField(null=True, blank=True)

    ft_cal_item_456 = models.FloatField(null=True, blank=True)

    ft_cal_item_457 = models.FloatField(null=True, blank=True)

    ft_cal_item_458 = models.FloatField(null=True, blank=True)

    ft_cal_item_459 = models.FloatField(null=True, blank=True)

    ft_cal_item_460 = models.FloatField(null=True, blank=True)

    ft_cal_item_461 = models.FloatField(null=True, blank=True)

    ft_cal_item_462 = models.FloatField(null=True, blank=True)

    ft_cal_item_463 = models.FloatField(null=True, blank=True)

    ft_cal_item_464 = models.FloatField(null=True, blank=True)

    ft_cal_item_465 = models.FloatField(null=True, blank=True)

    ft_cal_item_466 = models.FloatField(null=True, blank=True)

    ft_cal_item_467 = models.FloatField(null=True, blank=True)

    ft_cal_item_468 = models.FloatField(null=True, blank=True)

    ft_cal_item_469 = models.FloatField(null=True, blank=True)

    ft_cal_item_470 = models.FloatField(null=True, blank=True)

    ft_cal_item_471 = models.FloatField(null=True, blank=True)

    ft_cal_item_472 = models.FloatField(null=True, blank=True)

    ft_cal_item_473 = models.FloatField(null=True, blank=True)

    ft_cal_item_474 = models.FloatField(null=True, blank=True)

    ft_cal_item_475 = models.FloatField(null=True, blank=True)

    ft_cal_item_476 = models.FloatField(null=True, blank=True)

    ft_cal_item_477 = models.FloatField(null=True, blank=True)

    ft_cal_item_478 = models.FloatField(null=True, blank=True)

    ft_cal_item_479 = models.FloatField(null=True, blank=True)

    ft_cal_item_480 = models.FloatField(null=True, blank=True)

    ft_cal_item_481 = models.FloatField(null=True, blank=True)

    ft_cal_item_482 = models.FloatField(null=True, blank=True)

    ft_cal_item_483 = models.FloatField(null=True, blank=True)

    ft_cal_item_484 = models.FloatField(null=True, blank=True)

    ft_cal_item_485 = models.FloatField(null=True, blank=True)

    ft_cal_item_486 = models.FloatField(null=True, blank=True)

    ft_cal_item_487 = models.FloatField(null=True, blank=True)

    ft_cal_item_488 = models.FloatField(null=True, blank=True)

    ft_cal_item_489 = models.FloatField(null=True, blank=True)

    ft_cal_item_490 = models.FloatField(null=True, blank=True)

    ft_cal_item_491 = models.FloatField(null=True, blank=True)

    ft_cal_item_492 = models.FloatField(null=True, blank=True)

    ft_cal_item_493 = models.FloatField(null=True, blank=True)

    ft_cal_item_494 = models.FloatField(null=True, blank=True)

    ft_cal_item_495 = models.FloatField(null=True, blank=True)

    ft_cal_item_496 = models.FloatField(null=True, blank=True)

    ft_cal_item_497 = models.FloatField(null=True, blank=True)

    ft_cal_item_498 = models.FloatField(null=True, blank=True)

    ft_cal_item_499 = models.FloatField(null=True, blank=True)

    ft_cal_item_500 = models.FloatField(null=True, blank=True)

