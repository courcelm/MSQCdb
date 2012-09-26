from django.db import models




class MetadataOverview(models.Model):


    creation_date = models.DateTimeField(auto_now_add=True)

    experimentdate = models.DateTimeField(null=True, blank=True)

    instrumentmethod = models.CharField(max_length=1000, null=True, blank=True)

    thermo_raw_file = models.CharField(max_length=1000, null=True, blank=True)

    sha1_hash = models.CharField(max_length=40, null=True, blank=True)

    instrument_name = models.CharField(max_length=50, null=True, blank=True)

    instrument_serial_number = models.CharField(max_length=50, null=True, blank=True)

    instrument_model = models.CharField(max_length=50, null=True, blank=True)

    comment1 = models.CharField(max_length=1000, null=True, blank=True)

    comment2 = models.CharField(max_length=1000, null=True, blank=True)

    operator = models.CharField(max_length=50, null=True, blank=True)

    instrument_software_version = models.CharField(max_length=10, null=True, blank=True)

    instrument_hardware_version = models.CharField(max_length=10, null=True, blank=True)


    class Meta:
        unique_together = ('thermo_raw_file', 'instrument_name')


class MetadataOverviewTuneFileValue(models.Model):


    metadata = models.ForeignKey(MetadataOverview, related_name='%(class)s_metadata')

    source_type = models.CharField(max_length=50, null=True, blank=True)

    capillary_temp_c = models.IntegerField(null=True, blank=True)

    apci_vaporizer_temp_c = models.IntegerField(null=True, blank=True)

    sheath_gas_flow = models.IntegerField(null=True, blank=True)

    aux_gas_flow = models.IntegerField(null=True, blank=True)

    sweep_gas_flow = models.IntegerField(null=True, blank=True)

    injection_waveforms = models.IntegerField(null=True, blank=True)

    ion_trap_zoom_agc_target = models.IntegerField(null=True, blank=True)

    ion_trap_full_agc_target = models.IntegerField(null=True, blank=True)

    ion_trap_sim_agc_target = models.IntegerField(null=True, blank=True)

    ion_trap_msn_agc_target = models.IntegerField(null=True, blank=True)

    ftms_injection_waveforms = models.IntegerField(null=True, blank=True)

    ftms_full_agc_target = models.IntegerField(null=True, blank=True)

    ftms_sim_agc_target = models.IntegerField(null=True, blank=True)

    ftms_msn_agc_target = models.IntegerField(null=True, blank=True)

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





class MetadataOverviewPositivePolarity(models.Model):


    metadata = models.ForeignKey(MetadataOverview, related_name='%(class)s_metadata')

    source_voltage_kv = models.FloatField(null=True, blank=True)

    source_current_ua = models.IntegerField(null=True, blank=True)

    capillary_voltage_v = models.IntegerField(null=True, blank=True)

    tube_lens_v = models.IntegerField(null=True, blank=True)

    skimmer_offset_v = models.IntegerField(null=True, blank=True)

    multipole_rf_amplifier_vpp = models.IntegerField(null=True, blank=True)

    multipole_00_offset_v = models.FloatField(null=True, blank=True)

    lens_0_voltage_v = models.FloatField(null=True, blank=True)

    multipole_0_offset_v = models.FloatField(null=True, blank=True)

    lens_1_voltage_v = models.FloatField(null=True, blank=True)

    gate_lens_offset_v = models.IntegerField(null=True, blank=True)

    multipole_1_offset_v = models.FloatField(null=True, blank=True)

    front_lens_v = models.IntegerField(null=True, blank=True)

    ion_trap_zoom_micro_scans = models.IntegerField(null=True, blank=True)

    ion_trap_zoom_max_ion_time_ms = models.IntegerField(null=True, blank=True)

    ion_trap_full_micro_scans = models.IntegerField(null=True, blank=True)

    ion_trap_full_max_ion_time_ms = models.IntegerField(null=True, blank=True)

    ion_trap_sim_micro_scans = models.IntegerField(null=True, blank=True)

    ion_trap_sim_max_ion_time_ms = models.IntegerField(null=True, blank=True)

    ion_trap_msn_micro_scans = models.IntegerField(null=True, blank=True)

    ion_trap_msn_max_ion_time_ms = models.IntegerField(null=True, blank=True)

    ftms_full_micro_scans = models.IntegerField(null=True, blank=True)

    ftms_full_max_ion_time_ms = models.IntegerField(null=True, blank=True)

    ftms_sim_micro_scans = models.IntegerField(null=True, blank=True)

    ftms_sim_max_ion_time_ms = models.IntegerField(null=True, blank=True)

    ftms_msn_micro_scans = models.IntegerField(null=True, blank=True)

    ftms_msn_max_ion_time_ms = models.IntegerField(null=True, blank=True)

    reagent_ion_lens_1_v = models.IntegerField(null=True, blank=True)

    reagent_ion_gate_lens_v = models.IntegerField(null=True, blank=True)

    reagent_ion_lens_2_v = models.IntegerField(null=True, blank=True)

    reagent_ion_lens_3_v = models.IntegerField(null=True, blank=True)

    reagent_ion_back_lens_offset_v = models.FloatField(null=True, blank=True)

    reagent_ion_back_multipole_offset_v = models.IntegerField(null=True, blank=True)

    slens_rf_level_percent = models.IntegerField(null=True, blank=True)
    
    back_section_lpt_reagent_injection_v = models.IntegerField(null=True, blank=True)

    center_lens_reagent_injection_v = models.FloatField(null=True, blank=True)

    front_lens_reagent_injection_v = models.IntegerField(null=True, blank=True)

    center_lens_2_v = models.FloatField(null=True, blank=True)
    
    
    

class MetadataOverviewNegativePolarity(models.Model):


    metadata = models.ForeignKey(MetadataOverview, related_name='%(class)s_metadata')

    source_voltage_kv = models.FloatField(null=True, blank=True)

    source_current_ua = models.IntegerField(null=True, blank=True)

    capillary_voltage_v = models.IntegerField(null=True, blank=True)

    tube_lens_v = models.IntegerField(null=True, blank=True)

    skimmer_offset_v = models.IntegerField(null=True, blank=True)

    multipole_rf_amplifier_vpp = models.IntegerField(null=True, blank=True)

    multipole_00_offset_v = models.FloatField(null=True, blank=True)

    lens_0_voltage_v = models.FloatField(null=True, blank=True)

    multipole_0_offset_v = models.FloatField(null=True, blank=True)

    lens_1_voltage_v = models.FloatField(null=True, blank=True)

    gate_lens_offset_v = models.IntegerField(null=True, blank=True)

    multipole_1_offset_v = models.FloatField(null=True, blank=True)

    front_lens_v = models.IntegerField(null=True, blank=True)

    ion_trap_zoom_micro_scans = models.IntegerField(null=True, blank=True)

    ion_trap_zoom_max_ion_time_ms = models.IntegerField(null=True, blank=True)

    ion_trap_full_micro_scans = models.IntegerField(null=True, blank=True)

    ion_trap_full_max_ion_time_ms = models.IntegerField(null=True, blank=True)

    ion_trap_sim_micro_scans = models.IntegerField(null=True, blank=True)

    ion_trap_sim_max_ion_time_ms = models.IntegerField(null=True, blank=True)

    ion_trap_msn_micro_scans = models.IntegerField(null=True, blank=True)

    ion_trap_msn_max_ion_time_ms = models.IntegerField(null=True, blank=True)

    ftms_full_micro_scans = models.IntegerField(null=True, blank=True)

    ftms_full_max_ion_time_ms = models.IntegerField(null=True, blank=True)

    ftms_sim_micro_scans = models.IntegerField(null=True, blank=True)

    ftms_sim_max_ion_time_ms = models.IntegerField(null=True, blank=True)

    ftms_msn_micro_scans = models.IntegerField(null=True, blank=True)

    ftms_msn_max_ion_time_ms = models.IntegerField(null=True, blank=True)

    reagent_ion_lens_1_v = models.IntegerField(null=True, blank=True)

    reagent_ion_gate_lens_v = models.IntegerField(null=True, blank=True)

    reagent_ion_lens_2_v = models.IntegerField(null=True, blank=True)

    reagent_ion_lens_3_v = models.IntegerField(null=True, blank=True)

    reagent_ion_back_lens_offset_v = models.FloatField(null=True, blank=True)

    reagent_ion_back_multipole_offset_v = models.IntegerField(null=True, blank=True)

    slens_rf_level_percent = models.IntegerField(null=True, blank=True)
    
    back_section_lpt_reagent_injection_v = models.IntegerField(null=True, blank=True)

    center_lens_reagent_injection_v = models.FloatField(null=True, blank=True)

    front_lens_reagent_injection_v = models.IntegerField(null=True, blank=True)

    center_lens_2_v = models.FloatField(null=True, blank=True)
                                        
                                        


class MetadataOverviewReagentIonSourceTuneFileValue(models.Model):


    metadata = models.ForeignKey(MetadataOverview, related_name='%(class)s_metadata')

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
    
    

class MetadataOverviewAdditionalFtTuneFileValue(models.Model):


    metadata = models.ForeignKey(MetadataOverview, related_name='%(class)s_metadata')

    ft_tune_item_1 = models.IntegerField(null=True, blank=True)

    ft_tune_item_2 = models.IntegerField(null=True, blank=True)

    ft_tune_item_3 = models.IntegerField(null=True, blank=True)

    ft_tune_item_4 = models.IntegerField(null=True, blank=True)

    ft_tune_item_5 = models.IntegerField(null=True, blank=True)

    ft_tune_item_6 = models.IntegerField(null=True, blank=True)

    ft_tune_item_7 = models.IntegerField(null=True, blank=True)

    ft_tune_item_8 = models.IntegerField(null=True, blank=True)

    ft_tune_item_9 = models.IntegerField(null=True, blank=True)

    ft_tune_item_10 = models.IntegerField(null=True, blank=True)





class MetadataOverviewCalibrationFileValue(models.Model):


    metadata = models.ForeignKey(MetadataOverview, related_name='%(class)s_metadata')

    multiple_rf_frequency = models.FloatField(null=True, blank=True)

    main_rf_frequency = models.FloatField(null=True, blank=True)

    qmslope0 = models.FloatField(null=True, blank=True)

    qmslope1 = models.FloatField(null=True, blank=True)

    qmslope2 = models.FloatField(null=True, blank=True)

    qmslope3 = models.FloatField(null=True, blank=True)

    qmslope4 = models.FloatField(null=True, blank=True)

    qmint0 = models.FloatField(null=True, blank=True)

    qmint1 = models.FloatField(null=True, blank=True)

    qmint2 = models.FloatField(null=True, blank=True)

    qmint3 = models.FloatField(null=True, blank=True)

    qmint4 = models.FloatField(null=True, blank=True)

    end_section_slope = models.FloatField(null=True, blank=True)

    end_section_int = models.IntegerField(null=True, blank=True)

    pqd_ce_factor = models.FloatField(null=True, blank=True)

    isow_slope = models.FloatField(null=True, blank=True)

    isow_int = models.FloatField(null=True, blank=True)

    reagent_mp_slope = models.FloatField(null=True, blank=True)

    reagent_mp_int = models.FloatField(null=True, blank=True)

    tickle_amp_slope0 = models.FloatField(null=True, blank=True)

    tickle_amp_int0 = models.FloatField(null=True, blank=True)

    tickle_amp_slope1 = models.FloatField(null=True, blank=True)

    tickle_amp_int1 = models.FloatField(null=True, blank=True)

    tickle_amp_slope2 = models.FloatField(null=True, blank=True)

    tickle_amp_int2 = models.FloatField(null=True, blank=True)

    tickle_amp_slope3 = models.FloatField(null=True, blank=True)

    tickle_amp_int3 = models.FloatField(null=True, blank=True)

    multiplier_1_normal_gain_pos = models.FloatField(null=True, blank=True)

    multiplier_1_high_gain_pos = models.FloatField(null=True, blank=True)

    multiplier_2_normal_gain_pos = models.FloatField(null=True, blank=True)

    multiplier_2_high_gain_pos = models.FloatField(null=True, blank=True)

    multiplier_1_normal_gain_neg = models.FloatField(null=True, blank=True)

    multiplier_1_high_gain_neg = models.FloatField(null=True, blank=True)

    multiplier_2_normal_gain_neg = models.FloatField(null=True, blank=True)

    multiplier_2_high_gain_neg = models.FloatField(null=True, blank=True)

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

    vernier_fine_mass_slope = models.FloatField(null=True, blank=True)

    vernier_fine_mass_intercept = models.IntegerField(null=True, blank=True)

    vernier_coarse_mass_slope = models.IntegerField(null=True, blank=True)

    vernier_coarse_mass_intercept = models.IntegerField(null=True, blank=True)
    
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

    cap_device_min_v = models.FloatField(null=True, blank=True)

    cap_device_max_v = models.FloatField(null=True, blank=True)

    tube_lens_device_min_v = models.FloatField(null=True, blank=True)

    tube_lens_device_max_v = models.FloatField(null=True, blank=True)

    skimmer_device_min_v = models.FloatField(null=True, blank=True)

    skimmer_device_max_v = models.FloatField(null=True, blank=True)

    multipole_00_device_min_v = models.FloatField(null=True, blank=True)

    multipole_00_device_max_v = models.FloatField(null=True, blank=True)

    lens_0_device_min_v = models.FloatField(null=True, blank=True)

    lens_0_device_max_v = models.FloatField(null=True, blank=True)

    gate_lens_device_min_v = models.FloatField(null=True, blank=True)

    gate_lens_device_max_v = models.FloatField(null=True, blank=True)

    split_gate_device_min_v = models.FloatField(null=True, blank=True)

    split_gate_device_max_v = models.FloatField(null=True, blank=True)

    multipole_0_device_min_v = models.FloatField(null=True, blank=True)

    multipole_0_device_max_v = models.FloatField(null=True, blank=True)

    lens_1_device_min_v = models.FloatField(null=True, blank=True)

    lens_1_device_max_v = models.FloatField(null=True, blank=True)

    multipole_1_device_min_v = models.FloatField(null=True, blank=True)

    multipole_1_device_max_v = models.FloatField(null=True, blank=True)

    front_lens_device_min_v = models.FloatField(null=True, blank=True)

    front_lens_device_max_v = models.FloatField(null=True, blank=True)

    front_section_device_min_v = models.FloatField(null=True, blank=True)

    front_section_device_max_v = models.FloatField(null=True, blank=True)

    center_section_device_min_v = models.FloatField(null=True, blank=True)

    center_section_device_max_v = models.FloatField(null=True, blank=True)

    back_section_device_min_v = models.FloatField(null=True, blank=True)

    back_section_device_max_v = models.FloatField(null=True, blank=True)

    back_lens_device_min_v = models.FloatField(null=True, blank=True)

    back_lens_device_max_v = models.FloatField(null=True, blank=True)

    reagent_lens_1_device_min_v = models.FloatField(null=True, blank=True)

    reagent_lens_1_device_max_v = models.FloatField(null=True, blank=True)

    reagent_gate_lens_min_v = models.FloatField(null=True, blank=True)

    reagent_gate_lens_max_v = models.FloatField(null=True, blank=True)

    reagent_lens_2_device_min_v = models.FloatField(null=True, blank=True)

    reagent_lens_2_device_max_v = models.FloatField(null=True, blank=True)

    reagent_lens_3_device_min_v = models.FloatField(null=True, blank=True)

    reagent_lens_3_device_max_v = models.FloatField(null=True, blank=True)

    reagent_electron_lens_device_min_v = models.FloatField(null=True, blank=True)

    reagent_electron_lens_device_max_v = models.FloatField(null=True, blank=True)

    center_lens_lpt_device_min_v = models.FloatField(null=True, blank=True)

    center_lens_lpt_device_max_v = models.FloatField(null=True, blank=True)

    front_section_lpt_device_min_v = models.FloatField(null=True, blank=True)

    front_section_lpt_device_max_v = models.FloatField(null=True, blank=True)

    center_section_lpt_device_min_v = models.FloatField(null=True, blank=True)

    center_section_lpt_device_max_v = models.FloatField(null=True, blank=True)

    back_section_lpt_device_min_v = models.FloatField(null=True, blank=True)

    back_section_lpt_device_max_v = models.FloatField(null=True, blank=True)
    
    


class MetadataOverviewCalibrationFileValueResEject(models.Model):


    metadata = models.ForeignKey(MetadataOverview, related_name='%(class)s_metadata')

    res_eject_slope_0_0 = models.FloatField(null=True, blank=True)

    res_eject_intercept_0_0 = models.FloatField(null=True, blank=True)

    res_eject_slope_0_1 = models.FloatField(null=True, blank=True)

    res_eject_intercept_0_1 = models.FloatField(null=True, blank=True)

    res_eject_slope_0_2 = models.FloatField(null=True, blank=True)

    res_eject_intercept_0_2 = models.FloatField(null=True, blank=True)

    res_eject_slope_0_3 = models.FloatField(null=True, blank=True)

    res_eject_intercept_0_3 = models.FloatField(null=True, blank=True)

    res_eject_slope_0_4 = models.FloatField(null=True, blank=True)

    res_eject_intercept_0_4 = models.FloatField(null=True, blank=True)

    res_eject_slope_0_5 = models.FloatField(null=True, blank=True)

    res_eject_intercept_0_5 = models.FloatField(null=True, blank=True)

    res_eject_slope_0_6 = models.FloatField(null=True, blank=True)

    res_eject_intercept_0_6 = models.FloatField(null=True, blank=True)

    res_eject_slope_0_7 = models.FloatField(null=True, blank=True)

    res_eject_intercept_0_7 = models.FloatField(null=True, blank=True)

    res_eject_slope_0_8 = models.FloatField(null=True, blank=True)

    res_eject_intercept_0_8 = models.FloatField(null=True, blank=True)

    res_eject_slope_0_9 = models.FloatField(null=True, blank=True)

    res_eject_intercept_0_9 = models.FloatField(null=True, blank=True)

    res_eject_slope_0_10 = models.FloatField(null=True, blank=True)

    res_eject_intercept_0_10 = models.FloatField(null=True, blank=True)

    res_eject_slope_0_11 = models.FloatField(null=True, blank=True)

    res_eject_intercept_0_11 = models.FloatField(null=True, blank=True)

    res_eject_slope_0_12 = models.FloatField(null=True, blank=True)

    res_eject_intercept_0_12 = models.FloatField(null=True, blank=True)

    res_eject_slope_0_13 = models.FloatField(null=True, blank=True)

    res_eject_intercept_0_13 = models.FloatField(null=True, blank=True)

    res_eject_slope_0_14 = models.FloatField(null=True, blank=True)

    res_eject_intercept_0_14 = models.FloatField(null=True, blank=True)

    res_eject_slope_0_15 = models.FloatField(null=True, blank=True)

    res_eject_intercept_0_15 = models.FloatField(null=True, blank=True)

    res_eject_slope_0_16 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_0_16 = models.IntegerField(null=True, blank=True)

    res_eject_slope_0_17 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_0_17 = models.IntegerField(null=True, blank=True)

    res_eject_slope_0_18 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_0_18 = models.IntegerField(null=True, blank=True)

    res_eject_slope_0_19 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_0_19 = models.IntegerField(null=True, blank=True)

    res_eject_slope_1_0 = models.FloatField(null=True, blank=True)

    res_eject_intercept_1_0 = models.FloatField(null=True, blank=True)

    res_eject_slope_1_1 = models.FloatField(null=True, blank=True)

    res_eject_intercept_1_1 = models.FloatField(null=True, blank=True)

    res_eject_slope_1_2 = models.FloatField(null=True, blank=True)

    res_eject_intercept_1_2 = models.FloatField(null=True, blank=True)

    res_eject_slope_1_3 = models.FloatField(null=True, blank=True)

    res_eject_intercept_1_3 = models.FloatField(null=True, blank=True)

    res_eject_slope_1_4 = models.FloatField(null=True, blank=True)

    res_eject_intercept_1_4 = models.FloatField(null=True, blank=True)

    res_eject_slope_1_5 = models.FloatField(null=True, blank=True)

    res_eject_intercept_1_5 = models.FloatField(null=True, blank=True)

    res_eject_slope_1_6 = models.FloatField(null=True, blank=True)

    res_eject_intercept_1_6 = models.IntegerField(null=True, blank=True)

    res_eject_slope_1_7 = models.FloatField(null=True, blank=True)

    res_eject_intercept_1_7 = models.IntegerField(null=True, blank=True)

    res_eject_slope_1_8 = models.FloatField(null=True, blank=True)

    res_eject_intercept_1_8 = models.IntegerField(null=True, blank=True)

    res_eject_slope_1_9 = models.FloatField(null=True, blank=True)

    res_eject_intercept_1_9 = models.IntegerField(null=True, blank=True)

    res_eject_slope_1_10 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_1_10 = models.IntegerField(null=True, blank=True)

    res_eject_slope_1_11 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_1_11 = models.IntegerField(null=True, blank=True)

    res_eject_slope_1_12 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_1_12 = models.IntegerField(null=True, blank=True)

    res_eject_slope_1_13 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_1_13 = models.IntegerField(null=True, blank=True)

    res_eject_slope_1_14 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_1_14 = models.IntegerField(null=True, blank=True)

    res_eject_slope_1_15 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_1_15 = models.IntegerField(null=True, blank=True)

    res_eject_slope_1_16 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_1_16 = models.IntegerField(null=True, blank=True)

    res_eject_slope_1_17 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_1_17 = models.IntegerField(null=True, blank=True)

    res_eject_slope_1_18 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_1_18 = models.IntegerField(null=True, blank=True)

    res_eject_slope_1_19 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_1_19 = models.IntegerField(null=True, blank=True)

    res_eject_slope_2_0 = models.FloatField(null=True, blank=True)

    res_eject_intercept_2_0 = models.FloatField(null=True, blank=True)

    res_eject_slope_2_1 = models.FloatField(null=True, blank=True)

    res_eject_intercept_2_1 = models.FloatField(null=True, blank=True)

    res_eject_slope_2_2 = models.FloatField(null=True, blank=True)

    res_eject_intercept_2_2 = models.FloatField(null=True, blank=True)

    res_eject_slope_2_3 = models.FloatField(null=True, blank=True)

    res_eject_intercept_2_3 = models.FloatField(null=True, blank=True)

    res_eject_slope_2_4 = models.FloatField(null=True, blank=True)

    res_eject_intercept_2_4 = models.FloatField(null=True, blank=True)

    res_eject_slope_2_5 = models.FloatField(null=True, blank=True)

    res_eject_intercept_2_5 = models.FloatField(null=True, blank=True)

    res_eject_slope_2_6 = models.FloatField(null=True, blank=True)

    res_eject_intercept_2_6 = models.IntegerField(null=True, blank=True)

    res_eject_slope_2_7 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_2_7 = models.IntegerField(null=True, blank=True)

    res_eject_slope_2_8 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_2_8 = models.IntegerField(null=True, blank=True)

    res_eject_slope_2_9 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_2_9 = models.IntegerField(null=True, blank=True)

    res_eject_slope_2_10 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_2_10 = models.IntegerField(null=True, blank=True)

    res_eject_slope_2_11 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_2_11 = models.IntegerField(null=True, blank=True)

    res_eject_slope_2_12 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_2_12 = models.IntegerField(null=True, blank=True)

    res_eject_slope_2_13 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_2_13 = models.IntegerField(null=True, blank=True)

    res_eject_slope_2_14 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_2_14 = models.IntegerField(null=True, blank=True)

    res_eject_slope_2_15 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_2_15 = models.IntegerField(null=True, blank=True)

    res_eject_slope_2_16 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_2_16 = models.IntegerField(null=True, blank=True)

    res_eject_slope_2_17 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_2_17 = models.IntegerField(null=True, blank=True)

    res_eject_slope_2_18 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_2_18 = models.IntegerField(null=True, blank=True)

    res_eject_slope_2_19 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_2_19 = models.IntegerField(null=True, blank=True)

    res_eject_slope_3_0 = models.FloatField(null=True, blank=True)

    res_eject_intercept_3_0 = models.FloatField(null=True, blank=True)

    res_eject_slope_3_1 = models.FloatField(null=True, blank=True)

    res_eject_intercept_3_1 = models.FloatField(null=True, blank=True)

    res_eject_slope_3_2 = models.FloatField(null=True, blank=True)

    res_eject_intercept_3_2 = models.FloatField(null=True, blank=True)

    res_eject_slope_3_3 = models.FloatField(null=True, blank=True)

    res_eject_intercept_3_3 = models.FloatField(null=True, blank=True)

    res_eject_slope_3_4 = models.FloatField(null=True, blank=True)

    res_eject_intercept_3_4 = models.FloatField(null=True, blank=True)

    res_eject_slope_3_5 = models.FloatField(null=True, blank=True)

    res_eject_intercept_3_5 = models.FloatField(null=True, blank=True)

    res_eject_slope_3_6 = models.FloatField(null=True, blank=True)

    res_eject_intercept_3_6 = models.FloatField(null=True, blank=True)

    res_eject_slope_3_7 = models.FloatField(null=True, blank=True)

    res_eject_intercept_3_7 = models.FloatField(null=True, blank=True)

    res_eject_slope_3_8 = models.FloatField(null=True, blank=True)

    res_eject_intercept_3_8 = models.FloatField(null=True, blank=True)

    res_eject_slope_3_9 = models.FloatField(null=True, blank=True)

    res_eject_intercept_3_9 = models.FloatField(null=True, blank=True)

    res_eject_slope_3_10 = models.FloatField(null=True, blank=True)

    res_eject_intercept_3_10 = models.FloatField(null=True, blank=True)

    res_eject_slope_3_11 = models.FloatField(null=True, blank=True)

    res_eject_intercept_3_11 = models.FloatField(null=True, blank=True)

    res_eject_slope_3_12 = models.FloatField(null=True, blank=True)

    res_eject_intercept_3_12 = models.FloatField(null=True, blank=True)

    res_eject_slope_3_13 = models.FloatField(null=True, blank=True)

    res_eject_intercept_3_13 = models.FloatField(null=True, blank=True)

    res_eject_slope_3_14 = models.FloatField(null=True, blank=True)

    res_eject_intercept_3_14 = models.FloatField(null=True, blank=True)

    res_eject_slope_3_15 = models.FloatField(null=True, blank=True)

    res_eject_intercept_3_15 = models.FloatField(null=True, blank=True)

    res_eject_slope_3_16 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_3_16 = models.IntegerField(null=True, blank=True)

    res_eject_slope_3_17 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_3_17 = models.IntegerField(null=True, blank=True)

    res_eject_slope_3_18 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_3_18 = models.IntegerField(null=True, blank=True)

    res_eject_slope_3_19 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_3_19 = models.IntegerField(null=True, blank=True)

    res_eject_slope_4_0 = models.FloatField(null=True, blank=True)

    res_eject_intercept_4_0 = models.FloatField(null=True, blank=True)

    res_eject_slope_4_1 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_4_1 = models.IntegerField(null=True, blank=True)

    res_eject_slope_4_2 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_4_2 = models.IntegerField(null=True, blank=True)

    res_eject_slope_4_3 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_4_3 = models.IntegerField(null=True, blank=True)

    res_eject_slope_4_4 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_4_4 = models.IntegerField(null=True, blank=True)

    res_eject_slope_4_5 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_4_5 = models.IntegerField(null=True, blank=True)

    res_eject_slope_4_6 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_4_6 = models.IntegerField(null=True, blank=True)

    res_eject_slope_4_7 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_4_7 = models.IntegerField(null=True, blank=True)

    res_eject_slope_4_8 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_4_8 = models.IntegerField(null=True, blank=True)

    res_eject_slope_4_9 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_4_9 = models.IntegerField(null=True, blank=True)

    res_eject_slope_4_10 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_4_10 = models.IntegerField(null=True, blank=True)

    res_eject_slope_4_11 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_4_11 = models.IntegerField(null=True, blank=True)

    res_eject_slope_4_12 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_4_12 = models.IntegerField(null=True, blank=True)

    res_eject_slope_4_13 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_4_13 = models.IntegerField(null=True, blank=True)

    res_eject_slope_4_14 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_4_14 = models.IntegerField(null=True, blank=True)

    res_eject_slope_4_15 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_4_15 = models.IntegerField(null=True, blank=True)

    res_eject_slope_4_16 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_4_16 = models.IntegerField(null=True, blank=True)

    res_eject_slope_4_17 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_4_17 = models.IntegerField(null=True, blank=True)

    res_eject_slope_4_18 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_4_18 = models.IntegerField(null=True, blank=True)

    res_eject_slope_4_19 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_4_19 = models.IntegerField(null=True, blank=True)

    res_eject_slope_5_0 = models.FloatField(null=True, blank=True)

    res_eject_intercept_5_0 = models.FloatField(null=True, blank=True)

    res_eject_slope_5_1 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_5_1 = models.IntegerField(null=True, blank=True)

    res_eject_slope_5_2 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_5_2 = models.IntegerField(null=True, blank=True)

    res_eject_slope_5_3 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_5_3 = models.IntegerField(null=True, blank=True)

    res_eject_slope_5_4 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_5_4 = models.IntegerField(null=True, blank=True)

    res_eject_slope_5_5 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_5_5 = models.IntegerField(null=True, blank=True)

    res_eject_slope_5_6 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_5_6 = models.IntegerField(null=True, blank=True)

    res_eject_slope_5_7 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_5_7 = models.IntegerField(null=True, blank=True)

    res_eject_slope_5_8 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_5_8 = models.IntegerField(null=True, blank=True)

    res_eject_slope_5_9 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_5_9 = models.IntegerField(null=True, blank=True)

    res_eject_slope_5_10 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_5_10 = models.IntegerField(null=True, blank=True)

    res_eject_slope_5_11 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_5_11 = models.IntegerField(null=True, blank=True)

    res_eject_slope_5_12 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_5_12 = models.IntegerField(null=True, blank=True)

    res_eject_slope_5_13 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_5_13 = models.IntegerField(null=True, blank=True)

    res_eject_slope_5_14 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_5_14 = models.IntegerField(null=True, blank=True)

    res_eject_slope_5_15 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_5_15 = models.IntegerField(null=True, blank=True)

    res_eject_slope_5_16 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_5_16 = models.IntegerField(null=True, blank=True)

    res_eject_slope_5_17 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_5_17 = models.IntegerField(null=True, blank=True)

    res_eject_slope_5_18 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_5_18 = models.IntegerField(null=True, blank=True)

    res_eject_slope_5_19 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_5_19 = models.IntegerField(null=True, blank=True)

    res_eject_slope_6_0 = models.FloatField(null=True, blank=True)

    res_eject_intercept_6_0 = models.FloatField(null=True, blank=True)

    res_eject_slope_6_1 = models.FloatField(null=True, blank=True)

    res_eject_intercept_6_1 = models.FloatField(null=True, blank=True)

    res_eject_slope_6_2 = models.FloatField(null=True, blank=True)

    res_eject_intercept_6_2 = models.FloatField(null=True, blank=True)

    res_eject_slope_6_3 = models.FloatField(null=True, blank=True)

    res_eject_intercept_6_3 = models.FloatField(null=True, blank=True)

    res_eject_slope_6_4 = models.FloatField(null=True, blank=True)

    res_eject_intercept_6_4 = models.FloatField(null=True, blank=True)

    res_eject_slope_6_5 = models.FloatField(null=True, blank=True)

    res_eject_intercept_6_5 = models.FloatField(null=True, blank=True)

    res_eject_slope_6_6 = models.FloatField(null=True, blank=True)

    res_eject_intercept_6_6 = models.IntegerField(null=True, blank=True)

    res_eject_slope_6_7 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_6_7 = models.IntegerField(null=True, blank=True)

    res_eject_slope_6_8 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_6_8 = models.IntegerField(null=True, blank=True)

    res_eject_slope_6_9 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_6_9 = models.IntegerField(null=True, blank=True)

    res_eject_slope_6_10 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_6_10 = models.IntegerField(null=True, blank=True)

    res_eject_slope_6_11 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_6_11 = models.IntegerField(null=True, blank=True)

    res_eject_slope_6_12 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_6_12 = models.IntegerField(null=True, blank=True)

    res_eject_slope_6_13 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_6_13 = models.IntegerField(null=True, blank=True)

    res_eject_slope_6_14 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_6_14 = models.IntegerField(null=True, blank=True)

    res_eject_slope_6_15 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_6_15 = models.IntegerField(null=True, blank=True)

    res_eject_slope_6_16 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_6_16 = models.IntegerField(null=True, blank=True)

    res_eject_slope_6_17 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_6_17 = models.IntegerField(null=True, blank=True)

    res_eject_slope_6_18 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_6_18 = models.IntegerField(null=True, blank=True)

    res_eject_slope_6_19 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_6_19 = models.IntegerField(null=True, blank=True)

    res_eject_slope_7_0 = models.FloatField(null=True, blank=True)

    res_eject_intercept_7_0 = models.FloatField(null=True, blank=True)

    res_eject_slope_7_1 = models.FloatField(null=True, blank=True)

    res_eject_intercept_7_1 = models.FloatField(null=True, blank=True)

    res_eject_slope_7_2 = models.FloatField(null=True, blank=True)

    res_eject_intercept_7_2 = models.FloatField(null=True, blank=True)

    res_eject_slope_7_3 = models.FloatField(null=True, blank=True)

    res_eject_intercept_7_3 = models.FloatField(null=True, blank=True)

    res_eject_slope_7_4 = models.FloatField(null=True, blank=True)

    res_eject_intercept_7_4 = models.FloatField(null=True, blank=True)

    res_eject_slope_7_5 = models.FloatField(null=True, blank=True)

    res_eject_intercept_7_5 = models.FloatField(null=True, blank=True)

    res_eject_slope_7_6 = models.FloatField(null=True, blank=True)

    res_eject_intercept_7_6 = models.FloatField(null=True, blank=True)

    res_eject_slope_7_7 = models.FloatField(null=True, blank=True)

    res_eject_intercept_7_7 = models.FloatField(null=True, blank=True)

    res_eject_slope_7_8 = models.FloatField(null=True, blank=True)

    res_eject_intercept_7_8 = models.FloatField(null=True, blank=True)

    res_eject_slope_7_9 = models.FloatField(null=True, blank=True)

    res_eject_intercept_7_9 = models.FloatField(null=True, blank=True)

    res_eject_slope_7_10 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_7_10 = models.IntegerField(null=True, blank=True)

    res_eject_slope_7_11 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_7_11 = models.IntegerField(null=True, blank=True)

    res_eject_slope_7_12 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_7_12 = models.IntegerField(null=True, blank=True)

    res_eject_slope_7_13 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_7_13 = models.IntegerField(null=True, blank=True)

    res_eject_slope_7_14 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_7_14 = models.IntegerField(null=True, blank=True)

    res_eject_slope_7_15 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_7_15 = models.IntegerField(null=True, blank=True)

    res_eject_slope_7_16 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_7_16 = models.IntegerField(null=True, blank=True)

    res_eject_slope_7_17 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_7_17 = models.IntegerField(null=True, blank=True)

    res_eject_slope_7_18 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_7_18 = models.IntegerField(null=True, blank=True)

    res_eject_slope_7_19 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_7_19 = models.IntegerField(null=True, blank=True)

    res_eject_slope_8_0 = models.FloatField(null=True, blank=True)

    res_eject_intercept_8_0 = models.FloatField(null=True, blank=True)

    res_eject_slope_8_1 = models.FloatField(null=True, blank=True)

    res_eject_intercept_8_1 = models.FloatField(null=True, blank=True)

    res_eject_slope_8_2 = models.FloatField(null=True, blank=True)

    res_eject_intercept_8_2 = models.FloatField(null=True, blank=True)

    res_eject_slope_8_3 = models.FloatField(null=True, blank=True)

    res_eject_intercept_8_3 = models.FloatField(null=True, blank=True)

    res_eject_slope_8_4 = models.FloatField(null=True, blank=True)

    res_eject_intercept_8_4 = models.FloatField(null=True, blank=True)

    res_eject_slope_8_5 = models.FloatField(null=True, blank=True)

    res_eject_intercept_8_5 = models.FloatField(null=True, blank=True)

    res_eject_slope_8_6 = models.FloatField(null=True, blank=True)

    res_eject_intercept_8_6 = models.FloatField(null=True, blank=True)

    res_eject_slope_8_7 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_8_7 = models.IntegerField(null=True, blank=True)

    res_eject_slope_8_8 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_8_8 = models.IntegerField(null=True, blank=True)

    res_eject_slope_8_9 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_8_9 = models.IntegerField(null=True, blank=True)

    res_eject_slope_8_10 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_8_10 = models.IntegerField(null=True, blank=True)

    res_eject_slope_8_11 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_8_11 = models.IntegerField(null=True, blank=True)

    res_eject_slope_8_12 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_8_12 = models.IntegerField(null=True, blank=True)

    res_eject_slope_8_13 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_8_13 = models.IntegerField(null=True, blank=True)

    res_eject_slope_8_14 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_8_14 = models.IntegerField(null=True, blank=True)

    res_eject_slope_8_15 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_8_15 = models.IntegerField(null=True, blank=True)

    res_eject_slope_8_16 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_8_16 = models.IntegerField(null=True, blank=True)

    res_eject_slope_8_17 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_8_17 = models.IntegerField(null=True, blank=True)

    res_eject_slope_8_18 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_8_18 = models.IntegerField(null=True, blank=True)

    res_eject_slope_8_19 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_8_19 = models.IntegerField(null=True, blank=True)

    res_eject_slope_9_0 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_9_0 = models.IntegerField(null=True, blank=True)

    res_eject_slope_9_1 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_9_1 = models.IntegerField(null=True, blank=True)

    res_eject_slope_9_2 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_9_2 = models.IntegerField(null=True, blank=True)

    res_eject_slope_9_3 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_9_3 = models.IntegerField(null=True, blank=True)

    res_eject_slope_9_4 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_9_4 = models.IntegerField(null=True, blank=True)

    res_eject_slope_9_5 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_9_5 = models.IntegerField(null=True, blank=True)

    res_eject_slope_9_6 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_9_6 = models.IntegerField(null=True, blank=True)

    res_eject_slope_9_7 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_9_7 = models.IntegerField(null=True, blank=True)

    res_eject_slope_9_8 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_9_8 = models.IntegerField(null=True, blank=True)

    res_eject_slope_9_9 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_9_9 = models.IntegerField(null=True, blank=True)

    res_eject_slope_9_10 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_9_10 = models.IntegerField(null=True, blank=True)

    res_eject_slope_9_11 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_9_11 = models.IntegerField(null=True, blank=True)

    res_eject_slope_9_12 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_9_12 = models.IntegerField(null=True, blank=True)

    res_eject_slope_9_13 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_9_13 = models.IntegerField(null=True, blank=True)

    res_eject_slope_9_14 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_9_14 = models.IntegerField(null=True, blank=True)

    res_eject_slope_9_15 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_9_15 = models.IntegerField(null=True, blank=True)

    res_eject_slope_9_16 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_9_16 = models.IntegerField(null=True, blank=True)

    res_eject_slope_9_17 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_9_17 = models.IntegerField(null=True, blank=True)

    res_eject_slope_9_18 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_9_18 = models.IntegerField(null=True, blank=True)

    res_eject_slope_9_19 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_9_19 = models.IntegerField(null=True, blank=True)

    res_eject_slope_10_0 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_10_0 = models.IntegerField(null=True, blank=True)

    res_eject_slope_10_1 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_10_1 = models.IntegerField(null=True, blank=True)

    res_eject_slope_10_2 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_10_2 = models.IntegerField(null=True, blank=True)

    res_eject_slope_10_3 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_10_3 = models.IntegerField(null=True, blank=True)

    res_eject_slope_10_4 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_10_4 = models.IntegerField(null=True, blank=True)

    res_eject_slope_10_5 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_10_5 = models.IntegerField(null=True, blank=True)

    res_eject_slope_10_6 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_10_6 = models.IntegerField(null=True, blank=True)

    res_eject_slope_10_7 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_10_7 = models.IntegerField(null=True, blank=True)

    res_eject_slope_10_8 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_10_8 = models.IntegerField(null=True, blank=True)

    res_eject_slope_10_9 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_10_9 = models.IntegerField(null=True, blank=True)

    res_eject_slope_10_10 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_10_10 = models.IntegerField(null=True, blank=True)

    res_eject_slope_10_11 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_10_11 = models.IntegerField(null=True, blank=True)

    res_eject_slope_10_12 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_10_12 = models.IntegerField(null=True, blank=True)

    res_eject_slope_10_13 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_10_13 = models.IntegerField(null=True, blank=True)

    res_eject_slope_10_14 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_10_14 = models.IntegerField(null=True, blank=True)

    res_eject_slope_10_15 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_10_15 = models.IntegerField(null=True, blank=True)

    res_eject_slope_10_16 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_10_16 = models.IntegerField(null=True, blank=True)

    res_eject_slope_10_17 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_10_17 = models.IntegerField(null=True, blank=True)

    res_eject_slope_10_18 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_10_18 = models.IntegerField(null=True, blank=True)

    res_eject_slope_10_19 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_10_19 = models.IntegerField(null=True, blank=True)

    res_eject_slope_11_0 = models.FloatField(null=True, blank=True)

    res_eject_intercept_11_0 = models.FloatField(null=True, blank=True)

    res_eject_slope_11_1 = models.FloatField(null=True, blank=True)

    res_eject_intercept_11_1 = models.FloatField(null=True, blank=True)

    res_eject_slope_11_2 = models.FloatField(null=True, blank=True)

    res_eject_intercept_11_2 = models.FloatField(null=True, blank=True)

    res_eject_slope_11_3 = models.FloatField(null=True, blank=True)

    res_eject_intercept_11_3 = models.FloatField(null=True, blank=True)

    res_eject_slope_11_4 = models.FloatField(null=True, blank=True)

    res_eject_intercept_11_4 = models.FloatField(null=True, blank=True)

    res_eject_slope_11_5 = models.FloatField(null=True, blank=True)

    res_eject_intercept_11_5 = models.FloatField(null=True, blank=True)

    res_eject_slope_11_6 = models.FloatField(null=True, blank=True)

    res_eject_intercept_11_6 = models.FloatField(null=True, blank=True)

    res_eject_slope_11_7 = models.FloatField(null=True, blank=True)

    res_eject_intercept_11_7 = models.FloatField(null=True, blank=True)

    res_eject_slope_11_8 = models.FloatField(null=True, blank=True)

    res_eject_intercept_11_8 = models.FloatField(null=True, blank=True)

    res_eject_slope_11_9 = models.FloatField(null=True, blank=True)

    res_eject_intercept_11_9 = models.FloatField(null=True, blank=True)

    res_eject_slope_11_10 = models.FloatField(null=True, blank=True)

    res_eject_intercept_11_10 = models.FloatField(null=True, blank=True)

    res_eject_slope_11_11 = models.FloatField(null=True, blank=True)

    res_eject_intercept_11_11 = models.FloatField(null=True, blank=True)

    res_eject_slope_11_12 = models.FloatField(null=True, blank=True)

    res_eject_intercept_11_12 = models.FloatField(null=True, blank=True)

    res_eject_slope_11_13 = models.FloatField(null=True, blank=True)

    res_eject_intercept_11_13 = models.FloatField(null=True, blank=True)

    res_eject_slope_11_14 = models.FloatField(null=True, blank=True)

    res_eject_intercept_11_14 = models.FloatField(null=True, blank=True)

    res_eject_slope_11_15 = models.FloatField(null=True, blank=True)

    res_eject_intercept_11_15 = models.FloatField(null=True, blank=True)

    res_eject_slope_11_16 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_11_16 = models.IntegerField(null=True, blank=True)

    res_eject_slope_11_17 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_11_17 = models.IntegerField(null=True, blank=True)

    res_eject_slope_11_18 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_11_18 = models.IntegerField(null=True, blank=True)

    res_eject_slope_11_19 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_11_19 = models.IntegerField(null=True, blank=True)

    res_eject_slope_12_0 = models.FloatField(null=True, blank=True)

    res_eject_intercept_12_0 = models.FloatField(null=True, blank=True)

    res_eject_slope_12_1 = models.FloatField(null=True, blank=True)

    res_eject_intercept_12_1 = models.FloatField(null=True, blank=True)

    res_eject_slope_12_2 = models.FloatField(null=True, blank=True)

    res_eject_intercept_12_2 = models.FloatField(null=True, blank=True)

    res_eject_slope_12_3 = models.FloatField(null=True, blank=True)

    res_eject_intercept_12_3 = models.FloatField(null=True, blank=True)

    res_eject_slope_12_4 = models.FloatField(null=True, blank=True)

    res_eject_intercept_12_4 = models.FloatField(null=True, blank=True)

    res_eject_slope_12_5 = models.FloatField(null=True, blank=True)

    res_eject_intercept_12_5 = models.FloatField(null=True, blank=True)

    res_eject_slope_12_6 = models.FloatField(null=True, blank=True)

    res_eject_intercept_12_6 = models.FloatField(null=True, blank=True)

    res_eject_slope_12_7 = models.FloatField(null=True, blank=True)

    res_eject_intercept_12_7 = models.FloatField(null=True, blank=True)

    res_eject_slope_12_8 = models.FloatField(null=True, blank=True)

    res_eject_intercept_12_8 = models.FloatField(null=True, blank=True)

    res_eject_slope_12_9 = models.FloatField(null=True, blank=True)

    res_eject_intercept_12_9 = models.FloatField(null=True, blank=True)

    res_eject_slope_12_10 = models.FloatField(null=True, blank=True)

    res_eject_intercept_12_10 = models.FloatField(null=True, blank=True)

    res_eject_slope_12_11 = models.FloatField(null=True, blank=True)

    res_eject_intercept_12_11 = models.FloatField(null=True, blank=True)

    res_eject_slope_12_12 = models.FloatField(null=True, blank=True)

    res_eject_intercept_12_12 = models.FloatField(null=True, blank=True)

    res_eject_slope_12_13 = models.FloatField(null=True, blank=True)

    res_eject_intercept_12_13 = models.FloatField(null=True, blank=True)

    res_eject_slope_12_14 = models.FloatField(null=True, blank=True)

    res_eject_intercept_12_14 = models.FloatField(null=True, blank=True)

    res_eject_slope_12_15 = models.FloatField(null=True, blank=True)

    res_eject_intercept_12_15 = models.FloatField(null=True, blank=True)

    res_eject_slope_12_16 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_12_16 = models.IntegerField(null=True, blank=True)

    res_eject_slope_12_17 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_12_17 = models.IntegerField(null=True, blank=True)

    res_eject_slope_12_18 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_12_18 = models.IntegerField(null=True, blank=True)

    res_eject_slope_12_19 = models.IntegerField(null=True, blank=True)

    res_eject_intercept_12_19 = models.IntegerField(null=True, blank=True)





class MetadataOverviewCalibrationFileValueMass(models.Model):


    metadata = models.ForeignKey(MetadataOverview, related_name='%(class)s_metadata')

    mass_slope_0_0 = models.FloatField(null=True, blank=True)

    mass_intercept_0_0 = models.FloatField(null=True, blank=True)

    mass_slope_0_1 = models.FloatField(null=True, blank=True)

    mass_intercept_0_1 = models.FloatField(null=True, blank=True)

    mass_slope_0_2 = models.FloatField(null=True, blank=True)

    mass_intercept_0_2 = models.FloatField(null=True, blank=True)

    mass_slope_0_3 = models.FloatField(null=True, blank=True)

    mass_intercept_0_3 = models.FloatField(null=True, blank=True)

    mass_slope_0_4 = models.FloatField(null=True, blank=True)

    mass_intercept_0_4 = models.FloatField(null=True, blank=True)

    mass_slope_0_5 = models.FloatField(null=True, blank=True)

    mass_intercept_0_5 = models.FloatField(null=True, blank=True)

    mass_slope_0_6 = models.FloatField(null=True, blank=True)

    mass_intercept_0_6 = models.FloatField(null=True, blank=True)

    mass_slope_0_7 = models.FloatField(null=True, blank=True)

    mass_intercept_0_7 = models.FloatField(null=True, blank=True)

    mass_slope_0_8 = models.FloatField(null=True, blank=True)

    mass_intercept_0_8 = models.FloatField(null=True, blank=True)

    mass_slope_0_9 = models.FloatField(null=True, blank=True)

    mass_intercept_0_9 = models.FloatField(null=True, blank=True)

    mass_slope_0_10 = models.FloatField(null=True, blank=True)

    mass_intercept_0_10 = models.FloatField(null=True, blank=True)

    mass_slope_0_11 = models.FloatField(null=True, blank=True)

    mass_intercept_0_11 = models.FloatField(null=True, blank=True)

    mass_slope_0_12 = models.FloatField(null=True, blank=True)

    mass_intercept_0_12 = models.FloatField(null=True, blank=True)

    mass_slope_0_13 = models.FloatField(null=True, blank=True)

    mass_intercept_0_13 = models.FloatField(null=True, blank=True)

    mass_slope_0_14 = models.FloatField(null=True, blank=True)

    mass_intercept_0_14 = models.FloatField(null=True, blank=True)

    mass_slope_0_15 = models.FloatField(null=True, blank=True)

    mass_intercept_0_15 = models.FloatField(null=True, blank=True)

    mass_slope_0_16 = models.IntegerField(null=True, blank=True)

    mass_intercept_0_16 = models.IntegerField(null=True, blank=True)

    mass_slope_0_17 = models.IntegerField(null=True, blank=True)

    mass_intercept_0_17 = models.IntegerField(null=True, blank=True)

    mass_slope_0_18 = models.IntegerField(null=True, blank=True)

    mass_intercept_0_18 = models.IntegerField(null=True, blank=True)

    mass_slope_0_19 = models.IntegerField(null=True, blank=True)

    mass_intercept_0_19 = models.IntegerField(null=True, blank=True)

    mass_slope_1_0 = models.FloatField(null=True, blank=True)

    mass_intercept_1_0 = models.FloatField(null=True, blank=True)

    mass_slope_1_1 = models.FloatField(null=True, blank=True)

    mass_intercept_1_1 = models.FloatField(null=True, blank=True)

    mass_slope_1_2 = models.FloatField(null=True, blank=True)

    mass_intercept_1_2 = models.FloatField(null=True, blank=True)

    mass_slope_1_3 = models.FloatField(null=True, blank=True)

    mass_intercept_1_3 = models.FloatField(null=True, blank=True)

    mass_slope_1_4 = models.FloatField(null=True, blank=True)

    mass_intercept_1_4 = models.FloatField(null=True, blank=True)

    mass_slope_1_5 = models.FloatField(null=True, blank=True)

    mass_intercept_1_5 = models.FloatField(null=True, blank=True)

    mass_slope_1_6 = models.FloatField(null=True, blank=True)

    mass_intercept_1_6 = models.FloatField(null=True, blank=True)

    mass_slope_1_7 = models.FloatField(null=True, blank=True)

    mass_intercept_1_7 = models.FloatField(null=True, blank=True)

    mass_slope_1_8 = models.FloatField(null=True, blank=True)

    mass_intercept_1_8 = models.FloatField(null=True, blank=True)

    mass_slope_1_9 = models.FloatField(null=True, blank=True)

    mass_intercept_1_9 = models.FloatField(null=True, blank=True)

    mass_slope_1_10 = models.IntegerField(null=True, blank=True)

    mass_intercept_1_10 = models.IntegerField(null=True, blank=True)

    mass_slope_1_11 = models.IntegerField(null=True, blank=True)

    mass_intercept_1_11 = models.IntegerField(null=True, blank=True)

    mass_slope_1_12 = models.IntegerField(null=True, blank=True)

    mass_intercept_1_12 = models.IntegerField(null=True, blank=True)

    mass_slope_1_13 = models.IntegerField(null=True, blank=True)

    mass_intercept_1_13 = models.IntegerField(null=True, blank=True)

    mass_slope_1_14 = models.IntegerField(null=True, blank=True)

    mass_intercept_1_14 = models.IntegerField(null=True, blank=True)

    mass_slope_1_15 = models.IntegerField(null=True, blank=True)

    mass_intercept_1_15 = models.IntegerField(null=True, blank=True)

    mass_slope_1_16 = models.IntegerField(null=True, blank=True)

    mass_intercept_1_16 = models.IntegerField(null=True, blank=True)

    mass_slope_1_17 = models.IntegerField(null=True, blank=True)

    mass_intercept_1_17 = models.IntegerField(null=True, blank=True)

    mass_slope_1_18 = models.IntegerField(null=True, blank=True)

    mass_intercept_1_18 = models.IntegerField(null=True, blank=True)

    mass_slope_1_19 = models.IntegerField(null=True, blank=True)

    mass_intercept_1_19 = models.IntegerField(null=True, blank=True)

    mass_slope_2_0 = models.FloatField(null=True, blank=True)

    mass_intercept_2_0 = models.FloatField(null=True, blank=True)

    mass_slope_2_1 = models.FloatField(null=True, blank=True)

    mass_intercept_2_1 = models.FloatField(null=True, blank=True)

    mass_slope_2_2 = models.FloatField(null=True, blank=True)

    mass_intercept_2_2 = models.FloatField(null=True, blank=True)

    mass_slope_2_3 = models.FloatField(null=True, blank=True)

    mass_intercept_2_3 = models.FloatField(null=True, blank=True)

    mass_slope_2_4 = models.FloatField(null=True, blank=True)

    mass_intercept_2_4 = models.FloatField(null=True, blank=True)

    mass_slope_2_5 = models.FloatField(null=True, blank=True)

    mass_intercept_2_5 = models.FloatField(null=True, blank=True)

    mass_slope_2_6 = models.FloatField(null=True, blank=True)

    mass_intercept_2_6 = models.IntegerField(null=True, blank=True)

    mass_slope_2_7 = models.IntegerField(null=True, blank=True)

    mass_intercept_2_7 = models.IntegerField(null=True, blank=True)

    mass_slope_2_8 = models.IntegerField(null=True, blank=True)

    mass_intercept_2_8 = models.IntegerField(null=True, blank=True)

    mass_slope_2_9 = models.IntegerField(null=True, blank=True)

    mass_intercept_2_9 = models.IntegerField(null=True, blank=True)

    mass_slope_2_10 = models.IntegerField(null=True, blank=True)

    mass_intercept_2_10 = models.IntegerField(null=True, blank=True)

    mass_slope_2_11 = models.IntegerField(null=True, blank=True)

    mass_intercept_2_11 = models.IntegerField(null=True, blank=True)

    mass_slope_2_12 = models.IntegerField(null=True, blank=True)

    mass_intercept_2_12 = models.IntegerField(null=True, blank=True)

    mass_slope_2_13 = models.IntegerField(null=True, blank=True)

    mass_intercept_2_13 = models.IntegerField(null=True, blank=True)

    mass_slope_2_14 = models.IntegerField(null=True, blank=True)

    mass_intercept_2_14 = models.IntegerField(null=True, blank=True)

    mass_slope_2_15 = models.IntegerField(null=True, blank=True)

    mass_intercept_2_15 = models.IntegerField(null=True, blank=True)

    mass_slope_2_16 = models.IntegerField(null=True, blank=True)

    mass_intercept_2_16 = models.IntegerField(null=True, blank=True)

    mass_slope_2_17 = models.IntegerField(null=True, blank=True)

    mass_intercept_2_17 = models.IntegerField(null=True, blank=True)

    mass_slope_2_18 = models.IntegerField(null=True, blank=True)

    mass_intercept_2_18 = models.IntegerField(null=True, blank=True)

    mass_slope_2_19 = models.IntegerField(null=True, blank=True)

    mass_intercept_2_19 = models.IntegerField(null=True, blank=True)

    mass_slope_3_0 = models.FloatField(null=True, blank=True)

    mass_intercept_3_0 = models.FloatField(null=True, blank=True)

    mass_slope_3_1 = models.FloatField(null=True, blank=True)

    mass_intercept_3_1 = models.FloatField(null=True, blank=True)

    mass_slope_3_2 = models.FloatField(null=True, blank=True)

    mass_intercept_3_2 = models.FloatField(null=True, blank=True)

    mass_slope_3_3 = models.FloatField(null=True, blank=True)

    mass_intercept_3_3 = models.FloatField(null=True, blank=True)

    mass_slope_3_4 = models.FloatField(null=True, blank=True)

    mass_intercept_3_4 = models.FloatField(null=True, blank=True)

    mass_slope_3_5 = models.FloatField(null=True, blank=True)

    mass_intercept_3_5 = models.FloatField(null=True, blank=True)

    mass_slope_3_6 = models.FloatField(null=True, blank=True)

    mass_intercept_3_6 = models.FloatField(null=True, blank=True)

    mass_slope_3_7 = models.FloatField(null=True, blank=True)

    mass_intercept_3_7 = models.FloatField(null=True, blank=True)

    mass_slope_3_8 = models.FloatField(null=True, blank=True)

    mass_intercept_3_8 = models.FloatField(null=True, blank=True)

    mass_slope_3_9 = models.FloatField(null=True, blank=True)

    mass_intercept_3_9 = models.FloatField(null=True, blank=True)

    mass_slope_3_10 = models.FloatField(null=True, blank=True)

    mass_intercept_3_10 = models.FloatField(null=True, blank=True)

    mass_slope_3_11 = models.FloatField(null=True, blank=True)

    mass_intercept_3_11 = models.FloatField(null=True, blank=True)

    mass_slope_3_12 = models.FloatField(null=True, blank=True)

    mass_intercept_3_12 = models.FloatField(null=True, blank=True)

    mass_slope_3_13 = models.FloatField(null=True, blank=True)

    mass_intercept_3_13 = models.FloatField(null=True, blank=True)

    mass_slope_3_14 = models.FloatField(null=True, blank=True)

    mass_intercept_3_14 = models.FloatField(null=True, blank=True)

    mass_slope_3_15 = models.FloatField(null=True, blank=True)

    mass_intercept_3_15 = models.FloatField(null=True, blank=True)

    mass_slope_3_16 = models.IntegerField(null=True, blank=True)

    mass_intercept_3_16 = models.IntegerField(null=True, blank=True)

    mass_slope_3_17 = models.IntegerField(null=True, blank=True)

    mass_intercept_3_17 = models.IntegerField(null=True, blank=True)

    mass_slope_3_18 = models.IntegerField(null=True, blank=True)

    mass_intercept_3_18 = models.IntegerField(null=True, blank=True)

    mass_slope_3_19 = models.IntegerField(null=True, blank=True)

    mass_intercept_3_19 = models.IntegerField(null=True, blank=True)

    mass_slope_4_0 = models.FloatField(null=True, blank=True)

    mass_intercept_4_0 = models.FloatField(null=True, blank=True)

    mass_slope_4_1 = models.FloatField(null=True, blank=True)

    mass_intercept_4_1 = models.FloatField(null=True, blank=True)

    mass_slope_4_2 = models.FloatField(null=True, blank=True)

    mass_intercept_4_2 = models.FloatField(null=True, blank=True)

    mass_slope_4_3 = models.FloatField(null=True, blank=True)

    mass_intercept_4_3 = models.FloatField(null=True, blank=True)

    mass_slope_4_4 = models.FloatField(null=True, blank=True)

    mass_intercept_4_4 = models.FloatField(null=True, blank=True)

    mass_slope_4_5 = models.FloatField(null=True, blank=True)

    mass_intercept_4_5 = models.FloatField(null=True, blank=True)

    mass_slope_4_6 = models.IntegerField(null=True, blank=True)

    mass_intercept_4_6 = models.IntegerField(null=True, blank=True)

    mass_slope_4_7 = models.IntegerField(null=True, blank=True)

    mass_intercept_4_7 = models.IntegerField(null=True, blank=True)

    mass_slope_4_8 = models.IntegerField(null=True, blank=True)

    mass_intercept_4_8 = models.IntegerField(null=True, blank=True)

    mass_slope_4_9 = models.IntegerField(null=True, blank=True)

    mass_intercept_4_9 = models.IntegerField(null=True, blank=True)

    mass_slope_4_10 = models.IntegerField(null=True, blank=True)

    mass_intercept_4_10 = models.IntegerField(null=True, blank=True)

    mass_slope_4_11 = models.IntegerField(null=True, blank=True)

    mass_intercept_4_11 = models.IntegerField(null=True, blank=True)

    mass_slope_4_12 = models.IntegerField(null=True, blank=True)

    mass_intercept_4_12 = models.IntegerField(null=True, blank=True)

    mass_slope_4_13 = models.IntegerField(null=True, blank=True)

    mass_intercept_4_13 = models.IntegerField(null=True, blank=True)

    mass_slope_4_14 = models.IntegerField(null=True, blank=True)

    mass_intercept_4_14 = models.IntegerField(null=True, blank=True)

    mass_slope_4_15 = models.IntegerField(null=True, blank=True)

    mass_intercept_4_15 = models.IntegerField(null=True, blank=True)

    mass_slope_4_16 = models.IntegerField(null=True, blank=True)

    mass_intercept_4_16 = models.IntegerField(null=True, blank=True)

    mass_slope_4_17 = models.IntegerField(null=True, blank=True)

    mass_intercept_4_17 = models.IntegerField(null=True, blank=True)

    mass_slope_4_18 = models.IntegerField(null=True, blank=True)

    mass_intercept_4_18 = models.IntegerField(null=True, blank=True)

    mass_slope_4_19 = models.IntegerField(null=True, blank=True)

    mass_intercept_4_19 = models.IntegerField(null=True, blank=True)

    mass_slope_5_0 = models.FloatField(null=True, blank=True)

    mass_intercept_5_0 = models.FloatField(null=True, blank=True)

    mass_slope_5_1 = models.FloatField(null=True, blank=True)

    mass_intercept_5_1 = models.FloatField(null=True, blank=True)

    mass_slope_5_2 = models.FloatField(null=True, blank=True)

    mass_intercept_5_2 = models.FloatField(null=True, blank=True)

    mass_slope_5_3 = models.FloatField(null=True, blank=True)

    mass_intercept_5_3 = models.FloatField(null=True, blank=True)

    mass_slope_5_4 = models.FloatField(null=True, blank=True)

    mass_intercept_5_4 = models.FloatField(null=True, blank=True)

    mass_slope_5_5 = models.FloatField(null=True, blank=True)

    mass_intercept_5_5 = models.FloatField(null=True, blank=True)

    mass_slope_5_6 = models.IntegerField(null=True, blank=True)

    mass_intercept_5_6 = models.IntegerField(null=True, blank=True)

    mass_slope_5_7 = models.IntegerField(null=True, blank=True)

    mass_intercept_5_7 = models.IntegerField(null=True, blank=True)

    mass_slope_5_8 = models.IntegerField(null=True, blank=True)

    mass_intercept_5_8 = models.IntegerField(null=True, blank=True)

    mass_slope_5_9 = models.IntegerField(null=True, blank=True)

    mass_intercept_5_9 = models.IntegerField(null=True, blank=True)

    mass_slope_5_10 = models.IntegerField(null=True, blank=True)

    mass_intercept_5_10 = models.IntegerField(null=True, blank=True)

    mass_slope_5_11 = models.IntegerField(null=True, blank=True)

    mass_intercept_5_11 = models.IntegerField(null=True, blank=True)

    mass_slope_5_12 = models.IntegerField(null=True, blank=True)

    mass_intercept_5_12 = models.IntegerField(null=True, blank=True)

    mass_slope_5_13 = models.IntegerField(null=True, blank=True)

    mass_intercept_5_13 = models.IntegerField(null=True, blank=True)

    mass_slope_5_14 = models.IntegerField(null=True, blank=True)

    mass_intercept_5_14 = models.IntegerField(null=True, blank=True)

    mass_slope_5_15 = models.IntegerField(null=True, blank=True)

    mass_intercept_5_15 = models.IntegerField(null=True, blank=True)

    mass_slope_5_16 = models.IntegerField(null=True, blank=True)

    mass_intercept_5_16 = models.IntegerField(null=True, blank=True)

    mass_slope_5_17 = models.IntegerField(null=True, blank=True)

    mass_intercept_5_17 = models.IntegerField(null=True, blank=True)

    mass_slope_5_18 = models.IntegerField(null=True, blank=True)

    mass_intercept_5_18 = models.IntegerField(null=True, blank=True)

    mass_slope_5_19 = models.IntegerField(null=True, blank=True)

    mass_intercept_5_19 = models.IntegerField(null=True, blank=True)

    mass_slope_6_0 = models.FloatField(null=True, blank=True)

    mass_intercept_6_0 = models.FloatField(null=True, blank=True)

    mass_slope_6_1 = models.FloatField(null=True, blank=True)

    mass_intercept_6_1 = models.FloatField(null=True, blank=True)

    mass_slope_6_2 = models.FloatField(null=True, blank=True)

    mass_intercept_6_2 = models.FloatField(null=True, blank=True)

    mass_slope_6_3 = models.FloatField(null=True, blank=True)

    mass_intercept_6_3 = models.FloatField(null=True, blank=True)

    mass_slope_6_4 = models.FloatField(null=True, blank=True)

    mass_intercept_6_4 = models.FloatField(null=True, blank=True)

    mass_slope_6_5 = models.FloatField(null=True, blank=True)

    mass_intercept_6_5 = models.FloatField(null=True, blank=True)

    mass_slope_6_6 = models.IntegerField(null=True, blank=True)

    mass_intercept_6_6 = models.FloatField(null=True, blank=True)

    mass_slope_6_7 = models.IntegerField(null=True, blank=True)

    mass_intercept_6_7 = models.IntegerField(null=True, blank=True)

    mass_slope_6_8 = models.IntegerField(null=True, blank=True)

    mass_intercept_6_8 = models.IntegerField(null=True, blank=True)

    mass_slope_6_9 = models.IntegerField(null=True, blank=True)

    mass_intercept_6_9 = models.IntegerField(null=True, blank=True)

    mass_slope_6_10 = models.IntegerField(null=True, blank=True)

    mass_intercept_6_10 = models.IntegerField(null=True, blank=True)

    mass_slope_6_11 = models.IntegerField(null=True, blank=True)

    mass_intercept_6_11 = models.IntegerField(null=True, blank=True)

    mass_slope_6_12 = models.IntegerField(null=True, blank=True)

    mass_intercept_6_12 = models.IntegerField(null=True, blank=True)

    mass_slope_6_13 = models.IntegerField(null=True, blank=True)

    mass_intercept_6_13 = models.IntegerField(null=True, blank=True)

    mass_slope_6_14 = models.IntegerField(null=True, blank=True)

    mass_intercept_6_14 = models.IntegerField(null=True, blank=True)

    mass_slope_6_15 = models.IntegerField(null=True, blank=True)

    mass_intercept_6_15 = models.IntegerField(null=True, blank=True)

    mass_slope_6_16 = models.IntegerField(null=True, blank=True)

    mass_intercept_6_16 = models.IntegerField(null=True, blank=True)

    mass_slope_6_17 = models.IntegerField(null=True, blank=True)

    mass_intercept_6_17 = models.IntegerField(null=True, blank=True)

    mass_slope_6_18 = models.IntegerField(null=True, blank=True)

    mass_intercept_6_18 = models.IntegerField(null=True, blank=True)

    mass_slope_6_19 = models.IntegerField(null=True, blank=True)

    mass_intercept_6_19 = models.IntegerField(null=True, blank=True)

    mass_slope_7_0 = models.FloatField(null=True, blank=True)

    mass_intercept_7_0 = models.FloatField(null=True, blank=True)

    mass_slope_7_1 = models.FloatField(null=True, blank=True)

    mass_intercept_7_1 = models.FloatField(null=True, blank=True)

    mass_slope_7_2 = models.FloatField(null=True, blank=True)

    mass_intercept_7_2 = models.FloatField(null=True, blank=True)

    mass_slope_7_3 = models.FloatField(null=True, blank=True)

    mass_intercept_7_3 = models.FloatField(null=True, blank=True)

    mass_slope_7_4 = models.FloatField(null=True, blank=True)

    mass_intercept_7_4 = models.FloatField(null=True, blank=True)

    mass_slope_7_5 = models.FloatField(null=True, blank=True)

    mass_intercept_7_5 = models.FloatField(null=True, blank=True)

    mass_slope_7_6 = models.FloatField(null=True, blank=True)

    mass_intercept_7_6 = models.FloatField(null=True, blank=True)

    mass_slope_7_7 = models.FloatField(null=True, blank=True)

    mass_intercept_7_7 = models.FloatField(null=True, blank=True)

    mass_slope_7_8 = models.FloatField(null=True, blank=True)

    mass_intercept_7_8 = models.FloatField(null=True, blank=True)

    mass_slope_7_9 = models.FloatField(null=True, blank=True)

    mass_intercept_7_9 = models.FloatField(null=True, blank=True)

    mass_slope_7_10 = models.IntegerField(null=True, blank=True)

    mass_intercept_7_10 = models.IntegerField(null=True, blank=True)

    mass_slope_7_11 = models.IntegerField(null=True, blank=True)

    mass_intercept_7_11 = models.IntegerField(null=True, blank=True)

    mass_slope_7_12 = models.IntegerField(null=True, blank=True)

    mass_intercept_7_12 = models.IntegerField(null=True, blank=True)

    mass_slope_7_13 = models.IntegerField(null=True, blank=True)

    mass_intercept_7_13 = models.IntegerField(null=True, blank=True)

    mass_slope_7_14 = models.IntegerField(null=True, blank=True)

    mass_intercept_7_14 = models.IntegerField(null=True, blank=True)

    mass_slope_7_15 = models.IntegerField(null=True, blank=True)

    mass_intercept_7_15 = models.IntegerField(null=True, blank=True)

    mass_slope_7_16 = models.IntegerField(null=True, blank=True)

    mass_intercept_7_16 = models.IntegerField(null=True, blank=True)

    mass_slope_7_17 = models.IntegerField(null=True, blank=True)

    mass_intercept_7_17 = models.IntegerField(null=True, blank=True)

    mass_slope_7_18 = models.IntegerField(null=True, blank=True)

    mass_intercept_7_18 = models.IntegerField(null=True, blank=True)

    mass_slope_7_19 = models.IntegerField(null=True, blank=True)

    mass_intercept_7_19 = models.IntegerField(null=True, blank=True)

    mass_slope_8_0 = models.FloatField(null=True, blank=True)

    mass_intercept_8_0 = models.FloatField(null=True, blank=True)

    mass_slope_8_1 = models.FloatField(null=True, blank=True)

    mass_intercept_8_1 = models.FloatField(null=True, blank=True)

    mass_slope_8_2 = models.FloatField(null=True, blank=True)

    mass_intercept_8_2 = models.FloatField(null=True, blank=True)

    mass_slope_8_3 = models.FloatField(null=True, blank=True)

    mass_intercept_8_3 = models.FloatField(null=True, blank=True)

    mass_slope_8_4 = models.FloatField(null=True, blank=True)

    mass_intercept_8_4 = models.FloatField(null=True, blank=True)

    mass_slope_8_5 = models.FloatField(null=True, blank=True)

    mass_intercept_8_5 = models.FloatField(null=True, blank=True)

    mass_slope_8_6 = models.IntegerField(null=True, blank=True)

    mass_intercept_8_6 = models.IntegerField(null=True, blank=True)

    mass_slope_8_7 = models.IntegerField(null=True, blank=True)

    mass_intercept_8_7 = models.IntegerField(null=True, blank=True)

    mass_slope_8_8 = models.IntegerField(null=True, blank=True)

    mass_intercept_8_8 = models.IntegerField(null=True, blank=True)

    mass_slope_8_9 = models.IntegerField(null=True, blank=True)

    mass_intercept_8_9 = models.IntegerField(null=True, blank=True)

    mass_slope_8_10 = models.IntegerField(null=True, blank=True)

    mass_intercept_8_10 = models.IntegerField(null=True, blank=True)

    mass_slope_8_11 = models.IntegerField(null=True, blank=True)

    mass_intercept_8_11 = models.IntegerField(null=True, blank=True)

    mass_slope_8_12 = models.IntegerField(null=True, blank=True)

    mass_intercept_8_12 = models.IntegerField(null=True, blank=True)

    mass_slope_8_13 = models.IntegerField(null=True, blank=True)

    mass_intercept_8_13 = models.IntegerField(null=True, blank=True)

    mass_slope_8_14 = models.IntegerField(null=True, blank=True)

    mass_intercept_8_14 = models.IntegerField(null=True, blank=True)

    mass_slope_8_15 = models.IntegerField(null=True, blank=True)

    mass_intercept_8_15 = models.IntegerField(null=True, blank=True)

    mass_slope_8_16 = models.IntegerField(null=True, blank=True)

    mass_intercept_8_16 = models.IntegerField(null=True, blank=True)

    mass_slope_8_17 = models.IntegerField(null=True, blank=True)

    mass_intercept_8_17 = models.IntegerField(null=True, blank=True)

    mass_slope_8_18 = models.IntegerField(null=True, blank=True)

    mass_intercept_8_18 = models.IntegerField(null=True, blank=True)

    mass_slope_8_19 = models.IntegerField(null=True, blank=True)

    mass_intercept_8_19 = models.IntegerField(null=True, blank=True)

    mass_slope_9_0 = models.FloatField(null=True, blank=True)

    mass_intercept_9_0 = models.FloatField(null=True, blank=True)

    mass_slope_9_1 = models.FloatField(null=True, blank=True)

    mass_intercept_9_1 = models.FloatField(null=True, blank=True)

    mass_slope_9_2 = models.FloatField(null=True, blank=True)

    mass_intercept_9_2 = models.FloatField(null=True, blank=True)

    mass_slope_9_3 = models.FloatField(null=True, blank=True)

    mass_intercept_9_3 = models.FloatField(null=True, blank=True)

    mass_slope_9_4 = models.FloatField(null=True, blank=True)

    mass_intercept_9_4 = models.FloatField(null=True, blank=True)

    mass_slope_9_5 = models.FloatField(null=True, blank=True)

    mass_intercept_9_5 = models.FloatField(null=True, blank=True)

    mass_slope_9_6 = models.IntegerField(null=True, blank=True)

    mass_intercept_9_6 = models.FloatField(null=True, blank=True)

    mass_slope_9_7 = models.IntegerField(null=True, blank=True)

    mass_intercept_9_7 = models.IntegerField(null=True, blank=True)

    mass_slope_9_8 = models.IntegerField(null=True, blank=True)

    mass_intercept_9_8 = models.IntegerField(null=True, blank=True)

    mass_slope_9_9 = models.IntegerField(null=True, blank=True)

    mass_intercept_9_9 = models.IntegerField(null=True, blank=True)

    mass_slope_9_10 = models.IntegerField(null=True, blank=True)

    mass_intercept_9_10 = models.IntegerField(null=True, blank=True)

    mass_slope_9_11 = models.IntegerField(null=True, blank=True)

    mass_intercept_9_11 = models.IntegerField(null=True, blank=True)

    mass_slope_9_12 = models.IntegerField(null=True, blank=True)

    mass_intercept_9_12 = models.IntegerField(null=True, blank=True)

    mass_slope_9_13 = models.IntegerField(null=True, blank=True)

    mass_intercept_9_13 = models.IntegerField(null=True, blank=True)

    mass_slope_9_14 = models.IntegerField(null=True, blank=True)

    mass_intercept_9_14 = models.IntegerField(null=True, blank=True)

    mass_slope_9_15 = models.IntegerField(null=True, blank=True)

    mass_intercept_9_15 = models.IntegerField(null=True, blank=True)

    mass_slope_9_16 = models.IntegerField(null=True, blank=True)

    mass_intercept_9_16 = models.IntegerField(null=True, blank=True)

    mass_slope_9_17 = models.IntegerField(null=True, blank=True)

    mass_intercept_9_17 = models.IntegerField(null=True, blank=True)

    mass_slope_9_18 = models.IntegerField(null=True, blank=True)

    mass_intercept_9_18 = models.IntegerField(null=True, blank=True)

    mass_slope_9_19 = models.IntegerField(null=True, blank=True)

    mass_intercept_9_19 = models.IntegerField(null=True, blank=True)

    mass_slope_10_0 = models.FloatField(null=True, blank=True)

    mass_intercept_10_0 = models.FloatField(null=True, blank=True)

    mass_slope_10_1 = models.FloatField(null=True, blank=True)

    mass_intercept_10_1 = models.FloatField(null=True, blank=True)

    mass_slope_10_2 = models.FloatField(null=True, blank=True)

    mass_intercept_10_2 = models.FloatField(null=True, blank=True)

    mass_slope_10_3 = models.FloatField(null=True, blank=True)

    mass_intercept_10_3 = models.FloatField(null=True, blank=True)

    mass_slope_10_4 = models.FloatField(null=True, blank=True)

    mass_intercept_10_4 = models.FloatField(null=True, blank=True)

    mass_slope_10_5 = models.FloatField(null=True, blank=True)

    mass_intercept_10_5 = models.FloatField(null=True, blank=True)

    mass_slope_10_6 = models.IntegerField(null=True, blank=True)

    mass_intercept_10_6 = models.IntegerField(null=True, blank=True)

    mass_slope_10_7 = models.IntegerField(null=True, blank=True)

    mass_intercept_10_7 = models.IntegerField(null=True, blank=True)

    mass_slope_10_8 = models.IntegerField(null=True, blank=True)

    mass_intercept_10_8 = models.IntegerField(null=True, blank=True)

    mass_slope_10_9 = models.IntegerField(null=True, blank=True)

    mass_intercept_10_9 = models.IntegerField(null=True, blank=True)

    mass_slope_10_10 = models.IntegerField(null=True, blank=True)

    mass_intercept_10_10 = models.IntegerField(null=True, blank=True)

    mass_slope_10_11 = models.IntegerField(null=True, blank=True)

    mass_intercept_10_11 = models.IntegerField(null=True, blank=True)

    mass_slope_10_12 = models.IntegerField(null=True, blank=True)

    mass_intercept_10_12 = models.IntegerField(null=True, blank=True)

    mass_slope_10_13 = models.IntegerField(null=True, blank=True)

    mass_intercept_10_13 = models.IntegerField(null=True, blank=True)

    mass_slope_10_14 = models.IntegerField(null=True, blank=True)

    mass_intercept_10_14 = models.IntegerField(null=True, blank=True)

    mass_slope_10_15 = models.IntegerField(null=True, blank=True)

    mass_intercept_10_15 = models.IntegerField(null=True, blank=True)

    mass_slope_10_16 = models.IntegerField(null=True, blank=True)

    mass_intercept_10_16 = models.IntegerField(null=True, blank=True)

    mass_slope_10_17 = models.IntegerField(null=True, blank=True)

    mass_intercept_10_17 = models.IntegerField(null=True, blank=True)

    mass_slope_10_18 = models.IntegerField(null=True, blank=True)

    mass_intercept_10_18 = models.IntegerField(null=True, blank=True)

    mass_slope_10_19 = models.IntegerField(null=True, blank=True)

    mass_intercept_10_19 = models.IntegerField(null=True, blank=True)

    mass_slope_11_0 = models.FloatField(null=True, blank=True)

    mass_intercept_11_0 = models.FloatField(null=True, blank=True)

    mass_slope_11_1 = models.FloatField(null=True, blank=True)

    mass_intercept_11_1 = models.FloatField(null=True, blank=True)

    mass_slope_11_2 = models.FloatField(null=True, blank=True)

    mass_intercept_11_2 = models.FloatField(null=True, blank=True)

    mass_slope_11_3 = models.FloatField(null=True, blank=True)

    mass_intercept_11_3 = models.FloatField(null=True, blank=True)

    mass_slope_11_4 = models.FloatField(null=True, blank=True)

    mass_intercept_11_4 = models.FloatField(null=True, blank=True)

    mass_slope_11_5 = models.FloatField(null=True, blank=True)

    mass_intercept_11_5 = models.FloatField(null=True, blank=True)

    mass_slope_11_6 = models.FloatField(null=True, blank=True)

    mass_intercept_11_6 = models.FloatField(null=True, blank=True)

    mass_slope_11_7 = models.FloatField(null=True, blank=True)

    mass_intercept_11_7 = models.FloatField(null=True, blank=True)

    mass_slope_11_8 = models.FloatField(null=True, blank=True)

    mass_intercept_11_8 = models.FloatField(null=True, blank=True)

    mass_slope_11_9 = models.FloatField(null=True, blank=True)

    mass_intercept_11_9 = models.FloatField(null=True, blank=True)

    mass_slope_11_10 = models.FloatField(null=True, blank=True)

    mass_intercept_11_10 = models.FloatField(null=True, blank=True)

    mass_slope_11_11 = models.FloatField(null=True, blank=True)

    mass_intercept_11_11 = models.FloatField(null=True, blank=True)

    mass_slope_11_12 = models.FloatField(null=True, blank=True)

    mass_intercept_11_12 = models.FloatField(null=True, blank=True)

    mass_slope_11_13 = models.FloatField(null=True, blank=True)

    mass_intercept_11_13 = models.FloatField(null=True, blank=True)

    mass_slope_11_14 = models.FloatField(null=True, blank=True)

    mass_intercept_11_14 = models.FloatField(null=True, blank=True)

    mass_slope_11_15 = models.FloatField(null=True, blank=True)

    mass_intercept_11_15 = models.FloatField(null=True, blank=True)

    mass_slope_11_16 = models.IntegerField(null=True, blank=True)

    mass_intercept_11_16 = models.IntegerField(null=True, blank=True)

    mass_slope_11_17 = models.IntegerField(null=True, blank=True)

    mass_intercept_11_17 = models.IntegerField(null=True, blank=True)

    mass_slope_11_18 = models.IntegerField(null=True, blank=True)

    mass_intercept_11_18 = models.IntegerField(null=True, blank=True)

    mass_slope_11_19 = models.IntegerField(null=True, blank=True)

    mass_intercept_11_19 = models.IntegerField(null=True, blank=True)

    mass_slope_12_0 = models.FloatField(null=True, blank=True)

    mass_intercept_12_0 = models.FloatField(null=True, blank=True)

    mass_slope_12_1 = models.FloatField(null=True, blank=True)

    mass_intercept_12_1 = models.FloatField(null=True, blank=True)

    mass_slope_12_2 = models.FloatField(null=True, blank=True)

    mass_intercept_12_2 = models.FloatField(null=True, blank=True)

    mass_slope_12_3 = models.FloatField(null=True, blank=True)

    mass_intercept_12_3 = models.FloatField(null=True, blank=True)

    mass_slope_12_4 = models.FloatField(null=True, blank=True)

    mass_intercept_12_4 = models.FloatField(null=True, blank=True)

    mass_slope_12_5 = models.FloatField(null=True, blank=True)

    mass_intercept_12_5 = models.FloatField(null=True, blank=True)

    mass_slope_12_6 = models.FloatField(null=True, blank=True)

    mass_intercept_12_6 = models.FloatField(null=True, blank=True)

    mass_slope_12_7 = models.FloatField(null=True, blank=True)

    mass_intercept_12_7 = models.FloatField(null=True, blank=True)

    mass_slope_12_8 = models.FloatField(null=True, blank=True)

    mass_intercept_12_8 = models.FloatField(null=True, blank=True)

    mass_slope_12_9 = models.FloatField(null=True, blank=True)

    mass_intercept_12_9 = models.FloatField(null=True, blank=True)

    mass_slope_12_10 = models.FloatField(null=True, blank=True)

    mass_intercept_12_10 = models.FloatField(null=True, blank=True)

    mass_slope_12_11 = models.FloatField(null=True, blank=True)

    mass_intercept_12_11 = models.FloatField(null=True, blank=True)

    mass_slope_12_12 = models.FloatField(null=True, blank=True)

    mass_intercept_12_12 = models.FloatField(null=True, blank=True)

    mass_slope_12_13 = models.FloatField(null=True, blank=True)

    mass_intercept_12_13 = models.FloatField(null=True, blank=True)

    mass_slope_12_14 = models.FloatField(null=True, blank=True)

    mass_intercept_12_14 = models.FloatField(null=True, blank=True)

    mass_slope_12_15 = models.FloatField(null=True, blank=True)

    mass_intercept_12_15 = models.FloatField(null=True, blank=True)

    mass_slope_12_16 = models.IntegerField(null=True, blank=True)

    mass_intercept_12_16 = models.IntegerField(null=True, blank=True)

    mass_slope_12_17 = models.IntegerField(null=True, blank=True)

    mass_intercept_12_17 = models.IntegerField(null=True, blank=True)

    mass_slope_12_18 = models.IntegerField(null=True, blank=True)

    mass_intercept_12_18 = models.IntegerField(null=True, blank=True)

    mass_slope_12_19 = models.IntegerField(null=True, blank=True)

    mass_intercept_12_19 = models.IntegerField(null=True, blank=True)
    
    
    
    
class MetadataOverviewCalibrationFileValueFtCal(models.Model):


    metadata = models.ForeignKey(MetadataOverview, related_name='%(class)s_metadata')

    ft_cal_item_1 = models.FloatField(null=True, blank=True)

    ft_cal_item_2 = models.FloatField(null=True, blank=True)

    ft_cal_item_3 = models.FloatField(null=True, blank=True)

    ft_cal_item_4 = models.FloatField(null=True, blank=True)

    ft_cal_item_5 = models.FloatField(null=True, blank=True)

    ft_cal_item_6 = models.FloatField(null=True, blank=True)

    ft_cal_item_7 = models.FloatField(null=True, blank=True)

    ft_cal_item_8 = models.FloatField(null=True, blank=True)

    ft_cal_item_9 = models.FloatField(null=True, blank=True)

    ft_cal_item_10 = models.FloatField(null=True, blank=True)

    ft_cal_item_11 = models.FloatField(null=True, blank=True)

    ft_cal_item_12 = models.FloatField(null=True, blank=True)

    ft_cal_item_13 = models.FloatField(null=True, blank=True)

    ft_cal_item_14 = models.FloatField(null=True, blank=True)

    ft_cal_item_15 = models.FloatField(null=True, blank=True)

    ft_cal_item_16 = models.FloatField(null=True, blank=True)

    ft_cal_item_17 = models.FloatField(null=True, blank=True)

    ft_cal_item_18 = models.FloatField(null=True, blank=True)

    ft_cal_item_19 = models.FloatField(null=True, blank=True)

    ft_cal_item_20 = models.FloatField(null=True, blank=True)

    ft_cal_item_21 = models.FloatField(null=True, blank=True)

    ft_cal_item_22 = models.FloatField(null=True, blank=True)

    ft_cal_item_23 = models.FloatField(null=True, blank=True)

    ft_cal_item_24 = models.FloatField(null=True, blank=True)

    ft_cal_item_25 = models.FloatField(null=True, blank=True)

    ft_cal_item_26 = models.FloatField(null=True, blank=True)

    ft_cal_item_27 = models.FloatField(null=True, blank=True)

    ft_cal_item_28 = models.FloatField(null=True, blank=True)

    ft_cal_item_29 = models.FloatField(null=True, blank=True)

    ft_cal_item_30 = models.FloatField(null=True, blank=True)

    ft_cal_item_31 = models.FloatField(null=True, blank=True)

    ft_cal_item_32 = models.FloatField(null=True, blank=True)

    ft_cal_item_33 = models.FloatField(null=True, blank=True)

    ft_cal_item_34 = models.FloatField(null=True, blank=True)

    ft_cal_item_35 = models.FloatField(null=True, blank=True)

    ft_cal_item_36 = models.FloatField(null=True, blank=True)

    ft_cal_item_37 = models.FloatField(null=True, blank=True)

    ft_cal_item_38 = models.FloatField(null=True, blank=True)

    ft_cal_item_39 = models.FloatField(null=True, blank=True)

    ft_cal_item_40 = models.FloatField(null=True, blank=True)

    ft_cal_item_41 = models.FloatField(null=True, blank=True)

    ft_cal_item_42 = models.FloatField(null=True, blank=True)

    ft_cal_item_43 = models.FloatField(null=True, blank=True)

    ft_cal_item_44 = models.FloatField(null=True, blank=True)

    ft_cal_item_45 = models.FloatField(null=True, blank=True)

    ft_cal_item_46 = models.FloatField(null=True, blank=True)

    ft_cal_item_47 = models.FloatField(null=True, blank=True)

    ft_cal_item_48 = models.FloatField(null=True, blank=True)

    ft_cal_item_49 = models.FloatField(null=True, blank=True)

    ft_cal_item_50 = models.FloatField(null=True, blank=True)

    ft_cal_item_51 = models.FloatField(null=True, blank=True)

    ft_cal_item_52 = models.FloatField(null=True, blank=True)

    ft_cal_item_53 = models.FloatField(null=True, blank=True)

    ft_cal_item_54 = models.FloatField(null=True, blank=True)

    ft_cal_item_55 = models.FloatField(null=True, blank=True)

    ft_cal_item_56 = models.FloatField(null=True, blank=True)

    ft_cal_item_57 = models.FloatField(null=True, blank=True)

    ft_cal_item_58 = models.FloatField(null=True, blank=True)

    ft_cal_item_59 = models.FloatField(null=True, blank=True)

    ft_cal_item_60 = models.FloatField(null=True, blank=True)

    ft_cal_item_61 = models.FloatField(null=True, blank=True)

    ft_cal_item_62 = models.FloatField(null=True, blank=True)

    ft_cal_item_63 = models.FloatField(null=True, blank=True)

    ft_cal_item_64 = models.FloatField(null=True, blank=True)

    ft_cal_item_65 = models.FloatField(null=True, blank=True)

    ft_cal_item_66 = models.FloatField(null=True, blank=True)

    ft_cal_item_67 = models.FloatField(null=True, blank=True)

    ft_cal_item_68 = models.FloatField(null=True, blank=True)

    ft_cal_item_69 = models.FloatField(null=True, blank=True)

    ft_cal_item_70 = models.FloatField(null=True, blank=True)

    ft_cal_item_71 = models.FloatField(null=True, blank=True)

    ft_cal_item_72 = models.FloatField(null=True, blank=True)

    ft_cal_item_73 = models.FloatField(null=True, blank=True)

    ft_cal_item_74 = models.FloatField(null=True, blank=True)

    ft_cal_item_75 = models.FloatField(null=True, blank=True)

    ft_cal_item_76 = models.FloatField(null=True, blank=True)

    ft_cal_item_77 = models.FloatField(null=True, blank=True)

    ft_cal_item_78 = models.FloatField(null=True, blank=True)

    ft_cal_item_79 = models.FloatField(null=True, blank=True)

    ft_cal_item_80 = models.FloatField(null=True, blank=True)

    ft_cal_item_81 = models.FloatField(null=True, blank=True)

    ft_cal_item_82 = models.FloatField(null=True, blank=True)

    ft_cal_item_83 = models.FloatField(null=True, blank=True)

    ft_cal_item_84 = models.FloatField(null=True, blank=True)

    ft_cal_item_85 = models.FloatField(null=True, blank=True)

    ft_cal_item_86 = models.FloatField(null=True, blank=True)

    ft_cal_item_87 = models.FloatField(null=True, blank=True)

    ft_cal_item_88 = models.FloatField(null=True, blank=True)

    ft_cal_item_89 = models.FloatField(null=True, blank=True)

    ft_cal_item_90 = models.FloatField(null=True, blank=True)

    ft_cal_item_91 = models.FloatField(null=True, blank=True)

    ft_cal_item_92 = models.FloatField(null=True, blank=True)

    ft_cal_item_93 = models.FloatField(null=True, blank=True)

    ft_cal_item_94 = models.FloatField(null=True, blank=True)

    ft_cal_item_95 = models.FloatField(null=True, blank=True)

    ft_cal_item_96 = models.FloatField(null=True, blank=True)

    ft_cal_item_97 = models.FloatField(null=True, blank=True)

    ft_cal_item_98 = models.FloatField(null=True, blank=True)

    ft_cal_item_99 = models.FloatField(null=True, blank=True)

    ft_cal_item_100 = models.FloatField(null=True, blank=True)

    ft_cal_item_101 = models.FloatField(null=True, blank=True)

    ft_cal_item_102 = models.FloatField(null=True, blank=True)

    ft_cal_item_103 = models.FloatField(null=True, blank=True)

    ft_cal_item_104 = models.FloatField(null=True, blank=True)

    ft_cal_item_105 = models.FloatField(null=True, blank=True)

    ft_cal_item_106 = models.FloatField(null=True, blank=True)

    ft_cal_item_107 = models.FloatField(null=True, blank=True)

    ft_cal_item_108 = models.FloatField(null=True, blank=True)

    ft_cal_item_109 = models.FloatField(null=True, blank=True)

    ft_cal_item_110 = models.FloatField(null=True, blank=True)

    ft_cal_item_111 = models.FloatField(null=True, blank=True)

    ft_cal_item_112 = models.FloatField(null=True, blank=True)

    ft_cal_item_113 = models.FloatField(null=True, blank=True)

    ft_cal_item_114 = models.FloatField(null=True, blank=True)

    ft_cal_item_115 = models.FloatField(null=True, blank=True)

    ft_cal_item_116 = models.FloatField(null=True, blank=True)

    ft_cal_item_117 = models.FloatField(null=True, blank=True)

    ft_cal_item_118 = models.FloatField(null=True, blank=True)

    ft_cal_item_119 = models.FloatField(null=True, blank=True)

    ft_cal_item_120 = models.FloatField(null=True, blank=True)

    ft_cal_item_121 = models.FloatField(null=True, blank=True)

    ft_cal_item_122 = models.FloatField(null=True, blank=True)

    ft_cal_item_123 = models.FloatField(null=True, blank=True)

    ft_cal_item_124 = models.FloatField(null=True, blank=True)

    ft_cal_item_125 = models.FloatField(null=True, blank=True)

    ft_cal_item_126 = models.FloatField(null=True, blank=True)

    ft_cal_item_127 = models.FloatField(null=True, blank=True)

    ft_cal_item_128 = models.FloatField(null=True, blank=True)

    ft_cal_item_129 = models.FloatField(null=True, blank=True)

    ft_cal_item_130 = models.FloatField(null=True, blank=True)

    ft_cal_item_131 = models.FloatField(null=True, blank=True)

    ft_cal_item_132 = models.FloatField(null=True, blank=True)

    ft_cal_item_133 = models.FloatField(null=True, blank=True)

    ft_cal_item_134 = models.FloatField(null=True, blank=True)

    ft_cal_item_135 = models.FloatField(null=True, blank=True)

    ft_cal_item_136 = models.FloatField(null=True, blank=True)

    ft_cal_item_137 = models.FloatField(null=True, blank=True)

    ft_cal_item_138 = models.FloatField(null=True, blank=True)

    ft_cal_item_139 = models.FloatField(null=True, blank=True)

    ft_cal_item_140 = models.FloatField(null=True, blank=True)

    ft_cal_item_141 = models.FloatField(null=True, blank=True)

    ft_cal_item_142 = models.FloatField(null=True, blank=True)

    ft_cal_item_143 = models.FloatField(null=True, blank=True)

    ft_cal_item_144 = models.FloatField(null=True, blank=True)

    ft_cal_item_145 = models.FloatField(null=True, blank=True)

    ft_cal_item_146 = models.FloatField(null=True, blank=True)

    ft_cal_item_147 = models.FloatField(null=True, blank=True)

    ft_cal_item_148 = models.FloatField(null=True, blank=True)

    ft_cal_item_149 = models.FloatField(null=True, blank=True)

    ft_cal_item_150 = models.FloatField(null=True, blank=True)

    ft_cal_item_151 = models.FloatField(null=True, blank=True)

    ft_cal_item_152 = models.FloatField(null=True, blank=True)

    ft_cal_item_153 = models.FloatField(null=True, blank=True)

    ft_cal_item_154 = models.FloatField(null=True, blank=True)

    ft_cal_item_155 = models.FloatField(null=True, blank=True)

    ft_cal_item_156 = models.FloatField(null=True, blank=True)

    ft_cal_item_157 = models.FloatField(null=True, blank=True)

    ft_cal_item_158 = models.FloatField(null=True, blank=True)

    ft_cal_item_159 = models.FloatField(null=True, blank=True)

    ft_cal_item_160 = models.FloatField(null=True, blank=True)

    ft_cal_item_161 = models.FloatField(null=True, blank=True)

    ft_cal_item_162 = models.FloatField(null=True, blank=True)

    ft_cal_item_163 = models.FloatField(null=True, blank=True)

    ft_cal_item_164 = models.FloatField(null=True, blank=True)

    ft_cal_item_165 = models.FloatField(null=True, blank=True)

    ft_cal_item_166 = models.FloatField(null=True, blank=True)

    ft_cal_item_167 = models.FloatField(null=True, blank=True)

    ft_cal_item_168 = models.FloatField(null=True, blank=True)

    ft_cal_item_169 = models.FloatField(null=True, blank=True)

    ft_cal_item_170 = models.FloatField(null=True, blank=True)

    ft_cal_item_171 = models.FloatField(null=True, blank=True)

    ft_cal_item_172 = models.FloatField(null=True, blank=True)

    ft_cal_item_173 = models.FloatField(null=True, blank=True)

    ft_cal_item_174 = models.FloatField(null=True, blank=True)

    ft_cal_item_175 = models.FloatField(null=True, blank=True)

    ft_cal_item_176 = models.FloatField(null=True, blank=True)

    ft_cal_item_177 = models.FloatField(null=True, blank=True)

    ft_cal_item_178 = models.FloatField(null=True, blank=True)

    ft_cal_item_179 = models.FloatField(null=True, blank=True)

    ft_cal_item_180 = models.FloatField(null=True, blank=True)

    ft_cal_item_181 = models.FloatField(null=True, blank=True)

    ft_cal_item_182 = models.FloatField(null=True, blank=True)

    ft_cal_item_183 = models.FloatField(null=True, blank=True)

    ft_cal_item_184 = models.FloatField(null=True, blank=True)

    ft_cal_item_185 = models.FloatField(null=True, blank=True)

    ft_cal_item_186 = models.FloatField(null=True, blank=True)

    ft_cal_item_187 = models.FloatField(null=True, blank=True)

    ft_cal_item_188 = models.FloatField(null=True, blank=True)

    ft_cal_item_189 = models.FloatField(null=True, blank=True)

    ft_cal_item_190 = models.FloatField(null=True, blank=True)

    ft_cal_item_191 = models.FloatField(null=True, blank=True)

    ft_cal_item_192 = models.FloatField(null=True, blank=True)

    ft_cal_item_193 = models.FloatField(null=True, blank=True)

    ft_cal_item_194 = models.FloatField(null=True, blank=True)

    ft_cal_item_195 = models.FloatField(null=True, blank=True)

    ft_cal_item_196 = models.FloatField(null=True, blank=True)

    ft_cal_item_197 = models.FloatField(null=True, blank=True)

    ft_cal_item_198 = models.FloatField(null=True, blank=True)

    ft_cal_item_199 = models.FloatField(null=True, blank=True)

    ft_cal_item_200 = models.FloatField(null=True, blank=True)

    ft_cal_item_201 = models.FloatField(null=True, blank=True)

    ft_cal_item_202 = models.FloatField(null=True, blank=True)

    ft_cal_item_203 = models.FloatField(null=True, blank=True)

    ft_cal_item_204 = models.FloatField(null=True, blank=True)

    ft_cal_item_205 = models.FloatField(null=True, blank=True)

    ft_cal_item_206 = models.FloatField(null=True, blank=True)

    ft_cal_item_207 = models.FloatField(null=True, blank=True)

    ft_cal_item_208 = models.FloatField(null=True, blank=True)

    ft_cal_item_209 = models.FloatField(null=True, blank=True)

    ft_cal_item_210 = models.FloatField(null=True, blank=True)

    ft_cal_item_211 = models.FloatField(null=True, blank=True)

    ft_cal_item_212 = models.FloatField(null=True, blank=True)

    ft_cal_item_213 = models.FloatField(null=True, blank=True)

    ft_cal_item_214 = models.FloatField(null=True, blank=True)

    ft_cal_item_215 = models.FloatField(null=True, blank=True)

    ft_cal_item_216 = models.FloatField(null=True, blank=True)

    ft_cal_item_217 = models.FloatField(null=True, blank=True)

    ft_cal_item_218 = models.FloatField(null=True, blank=True)

    ft_cal_item_219 = models.FloatField(null=True, blank=True)

    ft_cal_item_220 = models.FloatField(null=True, blank=True)

    ft_cal_item_221 = models.FloatField(null=True, blank=True)

    ft_cal_item_222 = models.FloatField(null=True, blank=True)

    ft_cal_item_223 = models.FloatField(null=True, blank=True)

    ft_cal_item_224 = models.FloatField(null=True, blank=True)

    ft_cal_item_225 = models.FloatField(null=True, blank=True)

    ft_cal_item_226 = models.FloatField(null=True, blank=True)

    ft_cal_item_227 = models.FloatField(null=True, blank=True)

    ft_cal_item_228 = models.FloatField(null=True, blank=True)

    ft_cal_item_229 = models.FloatField(null=True, blank=True)

    ft_cal_item_230 = models.FloatField(null=True, blank=True)

    ft_cal_item_231 = models.FloatField(null=True, blank=True)

    ft_cal_item_232 = models.FloatField(null=True, blank=True)

    ft_cal_item_233 = models.FloatField(null=True, blank=True)

    ft_cal_item_234 = models.FloatField(null=True, blank=True)

    ft_cal_item_235 = models.FloatField(null=True, blank=True)

    ft_cal_item_236 = models.FloatField(null=True, blank=True)

    ft_cal_item_237 = models.FloatField(null=True, blank=True)

    ft_cal_item_238 = models.FloatField(null=True, blank=True)

    ft_cal_item_239 = models.FloatField(null=True, blank=True)

    ft_cal_item_240 = models.FloatField(null=True, blank=True)

    ft_cal_item_241 = models.FloatField(null=True, blank=True)

    ft_cal_item_242 = models.FloatField(null=True, blank=True)

    ft_cal_item_243 = models.FloatField(null=True, blank=True)

    ft_cal_item_244 = models.FloatField(null=True, blank=True)

    ft_cal_item_245 = models.FloatField(null=True, blank=True)

    ft_cal_item_246 = models.FloatField(null=True, blank=True)

    ft_cal_item_247 = models.FloatField(null=True, blank=True)

    ft_cal_item_248 = models.FloatField(null=True, blank=True)

    ft_cal_item_249 = models.FloatField(null=True, blank=True)

    ft_cal_item_250 = models.FloatField(null=True, blank=True)

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

