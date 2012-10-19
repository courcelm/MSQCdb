from django.db import models
from django.contrib.auth.models import User


class Sample(models.Model):
    
    creation_date = models.DateTimeField(auto_now_add=True)
    
    raw_file = models.CharField(max_length=1000)
    
    instrument_name = models.CharField(max_length=50)

    description = models.TextField( 'Detailed description', blank=True)
    
    
    class Meta:
        unique_together = ('raw_file', 'instrument_name')
        
        


class EventLog(models.Model):
    
    created_by = models.ForeignKey(User, null=True, blank=True, 
                                   related_name='%(class)s_created_by', editable = False)
    
    creation_date = models.DateTimeField(auto_now_add=True)
    
    modification_date = models.DateTimeField('Modified at', auto_now=True)

    datetime = models.DateTimeField()
    
    EVENT_TYPES = (('Calibration', 'Calibration'),
                   ('Failure', 'Failure'),
                   ('Maintenance', 'Maintenance'),
                   )
    
    event_type = models.CharField('Event type', max_length=30, 
                                     choices=EVENT_TYPES )
    
    instrument_name = models.CharField(max_length=50)
    
    name = models.CharField('Name', max_length=200, 
                            help_text='Short description of the event')
    
    description = models.TextField( 'Detailed description (what was replaced, how it was fixed)', blank=True)




class MetadataOverview(models.Model):


    creation_date = models.DateTimeField(auto_now_add=True)

    experimentdate = models.DateTimeField()

    instrumentmethod = models.CharField(max_length=1000, null=True, blank=True)

    thermo_raw_file = models.CharField(max_length=1000)

    sha1_hash = models.CharField(max_length=40, null=True, blank=True)

    instrument_name = models.CharField(max_length=50)

    instrument_serial_number = models.CharField(max_length=50, null=True, blank=True)

    instrument_model = models.CharField(max_length=50, null=True, blank=True)

    comment1 = models.CharField(max_length=1000, null=True, blank=True)

    comment2 = models.CharField(max_length=1000, null=True, blank=True)

    operator = models.CharField(max_length=50, null=True, blank=True)

    instrument_software_version = models.CharField(max_length=10, null=True, blank=True)

    instrument_hardware_version = models.CharField(max_length=10, null=True, blank=True)





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












class SpectrumCount(models.Model):


    class Meta:
        verbose_name = "Spectrum Count"


    ms2_scans = models.IntegerField("MS2 Scans", null=True, blank=True)

    ms1_scans_full = models.IntegerField("MS1 Scans/Full", null=True, blank=True)

    ms1_scans_other = models.IntegerField("MS1 Scans/Other", null=True, blank=True)





class FirstAndLastMs1Rt_Min_(models.Model):


    class Meta:
        verbose_name = "First and Last MS1 RT (min)"


    first_ms1 = models.FloatField("First MS1", null=True, blank=True)

    last_ms1 = models.FloatField("Last MS1", null=True, blank=True)





class TrypticPeptideCount(models.Model):


    class Meta:
        verbose_name = "Tryptic Peptide Count"


    peptides = models.IntegerField("Peptides", null=True, blank=True)

    ions = models.IntegerField("Ions", null=True, blank=True)

    identifications = models.IntegerField("Identifications", null=True, blank=True)

    abundance_pct = models.FloatField("Abundance Pct", null=True, blank=True)

    abundance_1000 = models.FloatField("Abundance/1000", null=True, blank=True)

    ions_peptide = models.FloatField("Ions/Peptide", null=True, blank=True)

    ids_peptide = models.FloatField("IDs/Peptide", null=True, blank=True)





class PeptideCount(models.Model):


    class Meta:
        verbose_name = "Peptide Count"


    peptides = models.IntegerField("Peptides", null=True, blank=True)

    ions = models.IntegerField("Ions", null=True, blank=True)

    identifications = models.IntegerField("Identifications", null=True, blank=True)

    semi_tryp_peps = models.FloatField("Semi/Tryp Peps", null=True, blank=True)

    semi_tryp_cnts = models.FloatField("Semi/Tryp Cnts", null=True, blank=True)

    semi_tryp_abund = models.FloatField("Semi/Tryp Abund", null=True, blank=True)

    miss_tryp_peps = models.FloatField("Miss/Tryp Peps", null=True, blank=True)

    miss_tryp_cnts = models.FloatField("Miss/Tryp Cnts", null=True, blank=True)

    miss_tryp_abund = models.FloatField("Miss/Tryp Abund", null=True, blank=True)

    top_50_ids = models.IntegerField("Top  50 IDs", null=True, blank=True)

    top_100_ids = models.IntegerField("Top 100 IDs", null=True, blank=True)

    top_200_ids = models.IntegerField("Top 200 IDs", null=True, blank=True)

    idpercent_50_top = models.FloatField("Id%  50 Top", null=True, blank=True)

    idpercent_100_top = models.FloatField("Id% 100 Top", null=True, blank=True)

    idpercent_200_top = models.FloatField("Id% 200 Top", null=True, blank=True)

    abpercent_50_top = models.FloatField("Ab% 50 Top", null=True, blank=True)

    abpercent_100_top = models.FloatField("Ab% 100 Top", null=True, blank=True)

    abpercent_200_top = models.FloatField("Ab% 200 Top", null=True, blank=True)

    idsemipercent_50 = models.FloatField("IdSemi%  50", null=True, blank=True)

    idsemipercent_100 = models.FloatField("IdSemi% 100", null=True, blank=True)

    idsemipercent_200 = models.FloatField("IdSemi% 200", null=True, blank=True)

    absemipercent_50 = models.FloatField("AbSemi% 50", null=True, blank=True)

    absemipercent_100 = models.FloatField("AbSemi% 100", null=True, blank=True)

    absemipercent_200 = models.FloatField("AbSemi% 200", null=True, blank=True)

    net_oversample = models.FloatField("Net Oversample", null=True, blank=True)

    ions_peptide = models.FloatField("Ions/Peptide", null=True, blank=True)

    ids_peptide = models.FloatField("IDs/Peptide", null=True, blank=True)





class DifferentProtein(models.Model):


    class Meta:
        verbose_name = "Different Protein"


    n1_or_more_peps = models.IntegerField("1 or more Peps", null=True, blank=True)

    gt1_peptides = models.IntegerField(">1 Peptides", null=True, blank=True)





class MiddlePeptideRetentionTimePeriod_Min_(models.Model):


    class Meta:
        verbose_name = "Middle Peptide Retention Time Period (min)"


    half_period = models.FloatField("Half Period", null=True, blank=True)

    start_time = models.FloatField("Start Time", null=True, blank=True)

    mid_time = models.FloatField("Mid Time", null=True, blank=True)

    qratio_time = models.FloatField("Qratio Time", null=True, blank=True)

    ms2_scans = models.IntegerField("MS2 scans", null=True, blank=True)

    ms1_scans = models.IntegerField("MS1 Scans", null=True, blank=True)

    pep_id_rate = models.FloatField("Pep ID Rate", null=True, blank=True)

    id_rate = models.FloatField("ID Rate", null=True, blank=True)

    id_efficiency = models.FloatField("ID Efficiency", null=True, blank=True)





class Ms1DuringMiddle_AndEarly_PeptideRetentionPeriod(models.Model):


    class Meta:
        verbose_name = "MS1 During Middle (and Early) Peptide Retention Period"


    s_n_median = models.FloatField("S/N Median", null=True, blank=True)

    tic_median_1000 = models.IntegerField("TIC Median/1000", null=True, blank=True)

    npeaks_median = models.IntegerField("Npeaks Median", null=True, blank=True)

    scantoscan = models.FloatField("Scan-to-Scan", null=True, blank=True)

    s2s3q_med = models.FloatField("S2S-3Q/Med", null=True, blank=True)

    s2s1qrt_med = models.FloatField("S2S-1Qrt/Med", null=True, blank=True)

    s2s2qrt_med = models.FloatField("S2S-2Qrt/Med", null=True, blank=True)

    s2s3qrt_med = models.FloatField("S2S-3Qrt/Med", null=True, blank=True)

    s2s4qrt_med = models.FloatField("S2S-4Qrt/Med", null=True, blank=True)

    esi_off_time = models.FloatField("ESI Off Time", null=True, blank=True)

    max_ms1_jump = models.FloatField("Max MS1 Jump", null=True, blank=True)

    max_ms1_fall = models.FloatField("Max MS1 Fall", null=True, blank=True)

    ms1_jumps_gt10x = models.IntegerField("MS1 Jumps >10x", null=True, blank=True)

    ms1_falls_lt1x = models.IntegerField("MS1 Falls <.1x", null=True, blank=True)

    esi_off_lowrt = models.FloatField("ESI Off LowRT", null=True, blank=True)

    max_jump_lowrt = models.FloatField("Max Jump LowRT", null=True, blank=True)

    max_fall_lowrt = models.FloatField("Max Fall LowRT", null=True, blank=True)

    ms1_lowrt_gt10x = models.IntegerField("MS1 LowRT >10x", null=True, blank=True)

    ms1_lowrt_lt1x = models.IntegerField("MS1 LowRT <.1x", null=True, blank=True)

    esi_off_hirt = models.FloatField("ESI Off HiRT", null=True, blank=True)

    max_jump_hirt = models.FloatField("Max Jump HiRT", null=True, blank=True)

    max_fall_hirt = models.FloatField("Max Fall HiRT", null=True, blank=True)

    ms1_hirt_gt10x = models.IntegerField("MS1 HiRT >10x", null=True, blank=True)

    ms1_hirt_lt1x = models.IntegerField("MS1 HiRT <.1x", null=True, blank=True)





class Ms1TotalIonCurrentForDifferentRtPeriod(models.Model):


    class Meta:
        verbose_name = "MS1 Total Ion Current For Different RT Period"


    n1st_quart_id = models.FloatField("1st Quart ID", null=True, blank=True)

    middle_id = models.FloatField("Middle ID", null=True, blank=True)

    last_id_quart = models.FloatField("Last ID Quart", null=True, blank=True)

    to_end_of_run = models.FloatField("To End of Run", null=True, blank=True)





class TotalIonCurrentForIdsAtPeakMaxima(models.Model):


    class Meta:
        verbose_name = "Total Ion Current For IDs at Peak Maxima"


    med_tic_id_1000 = models.FloatField("Med TIC ID/1000", null=True, blank=True)

    interq_tic = models.FloatField("InterQ TIC", null=True, blank=True)

    mid_interq_tic = models.FloatField("Mid InterQ TIC", null=True, blank=True)





class PrecursorMZForId(models.Model):


    class Meta:
        verbose_name = "Precursor m/z for ID"


    median = models.FloatField("Median", null=True, blank=True)

    half_width = models.FloatField("Half Width", null=True, blank=True)

    quart_ratio = models.FloatField("Quart Ratio", null=True, blank=True)

    precursor_min = models.FloatField("Precursor Min", null=True, blank=True)

    precursor_max = models.FloatField("Precursor Max", null=True, blank=True)

    med_at_q1_tic = models.FloatField("Med @ Q1 TIC", null=True, blank=True)

    med_at_q2_tic = models.FloatField("Med @ Q2 TIC", null=True, blank=True)

    med_at_q3_tic = models.FloatField("Med @ Q3 TIC", null=True, blank=True)

    med_at_q4_tic = models.FloatField("Med @ Q4 TIC", null=True, blank=True)

    med_at_q1_rt = models.FloatField("Med @ Q1 RT", null=True, blank=True)

    med_at_q2_rt = models.FloatField("Med @ Q2 RT", null=True, blank=True)

    med_at_q3_rt = models.FloatField("Med @ Q3 RT", null=True, blank=True)

    med_at_q4_rt = models.FloatField("Med @ Q4 RT", null=True, blank=True)

    med_at_q1_rt_plus2 = models.FloatField("Med @ Q1 RT/+2", null=True, blank=True)

    med_at_q2_rt_plus2 = models.FloatField("Med @ Q2 RT/+2", null=True, blank=True)

    med_at_q3_rt_plus2 = models.FloatField("Med @ Q3 RT/+2", null=True, blank=True)

    med_at_q4_rt_plus2 = models.FloatField("Med @ Q4 RT/+2", null=True, blank=True)

    med_charge_plus1 = models.FloatField("Med Charge +1", null=True, blank=True)

    med_charge_plus2 = models.FloatField("Med Charge +2", null=True, blank=True)

    med_charge_plus3 = models.FloatField("Med Charge +3", null=True, blank=True)

    med_charge_plus4 = models.FloatField("Med Charge +4", null=True, blank=True)





class NumberOfIonsVsCharge(models.Model):


    class Meta:
        verbose_name = "Number of Ions vs Charge"


    charge_plus1 = models.IntegerField("Charge +1", null=True, blank=True)

    charge_plus2 = models.IntegerField("Charge +2", null=True, blank=True)

    charge_plus3 = models.IntegerField("Charge +3", null=True, blank=True)

    charge_plus4 = models.IntegerField("Charge +4", null=True, blank=True)

    charge_plus5 = models.IntegerField("Charge +5", null=True, blank=True)

    plus2_at_q1_rt = models.IntegerField("+2 @ Q1 RT", null=True, blank=True)

    plus2_at_q2_rt = models.IntegerField("+2 @ Q2 RT", null=True, blank=True)

    plus2_at_q3_rt = models.IntegerField("+2 @ Q3 RT", null=True, blank=True)

    plus2_at_q4_rt = models.IntegerField("+2 @ Q4 RT", null=True, blank=True)

    plus1_plus2_at_q1_rt = models.FloatField("+1/+2 @ Q1 RT", null=True, blank=True)

    plus1_plus2_at_q2_rt = models.FloatField("+1/+2 @ Q2 RT", null=True, blank=True)

    plus1_plus2_at_q3_rt = models.FloatField("+1/+2 @ Q3 RT", null=True, blank=True)

    plus1_plus2_at_q4_rt = models.FloatField("+1/+2 @ Q4 RT", null=True, blank=True)

    plus3_plus2_at_q1_rt = models.FloatField("+3/+2 @ Q1 RT", null=True, blank=True)

    plus3_plus2_at_q2_rt = models.FloatField("+3/+2 @ Q2 RT", null=True, blank=True)

    plus3_plus2_at_q3_rt = models.FloatField("+3/+2 @ Q3 RT", null=True, blank=True)

    plus3_plus2_at_q4_rt = models.FloatField("+3/+2 @ Q4 RT", null=True, blank=True)





class AveragesVsRtForIdedPeptide(models.Model):


    class Meta:
        verbose_name = "Averages vs RT for IDed Peptide"


    length_q1 = models.FloatField("Length Q1", null=True, blank=True)

    length_q4 = models.FloatField("Length Q4", null=True, blank=True)

    charge_q1 = models.FloatField("Charge Q1", null=True, blank=True)

    charge_q4 = models.FloatField("Charge Q4", null=True, blank=True)





class PrecursorMZ_PeptideIonMZ_plus2ChargeOnlyRejectgt0(models.Model):


    class Meta:
        verbose_name = "Precursor m/z - Peptide Ion m/z (+2 Charge Only, Reject >0.45 m/z)"


    spectra = models.IntegerField("Spectra", null=True, blank=True)

    median = models.FloatField("Median", null=True, blank=True)

    mean_absolute = models.FloatField("Mean Absolute", null=True, blank=True)

    ppm_median = models.FloatField("ppm Median", null=True, blank=True)

    ppm_interq = models.FloatField("ppm InterQ", null=True, blank=True)





class IonIdsByChargeState_RelativeToplus2_(models.Model):


    class Meta:
        verbose_name = "Ion IDs by Charge State (Relative to +2)"


    plus2_ion_count = models.IntegerField("+2 Ion Count", null=True, blank=True)

    charge_plus1 = models.FloatField("Charge +1", null=True, blank=True)

    charge_plus2 = models.FloatField("Charge +2", null=True, blank=True)

    charge_plus3 = models.FloatField("Charge +3", null=True, blank=True)

    charge_plus4 = models.FloatField("Charge +4", null=True, blank=True)





class AveragePeptideLengthsForDifferentChargeState(models.Model):


    class Meta:
        verbose_name = "Average Peptide Lengths for Different Charge State"


    charge_plus1 = models.FloatField("Charge +1", null=True, blank=True)

    charge_plus2 = models.FloatField("Charge +2", null=True, blank=True)

    charge_plus3 = models.FloatField("Charge +3", null=True, blank=True)

    charge_plus4 = models.FloatField("Charge +4", null=True, blank=True)





class AveragePeptideLengthsForCharge2ForDifferentNumber(models.Model):


    class Meta:
        verbose_name = "Average Peptide Lengths For Charge 2 for Different Numbers of Mobile Proton"


    naa_cheq2_mpeq1 = models.FloatField("NAA,Ch=2,MP=1", null=True, blank=True)

    naa_cheq2_mpeq0 = models.FloatField("NAA,Ch=2,MP=0", null=True, blank=True)

    naa_cheq2_mpeq1 = models.FloatField("NAA,Ch=2,MP=1", null=True, blank=True)

    naa_cheq2_mpeq2 = models.FloatField("NAA,Ch=2,MP=2", null=True, blank=True)





class NumbersOfIonIdsAtDifferentChargesWith1MobileProton(models.Model):


    class Meta:
        verbose_name = "Numbers of Ion Ids at Different Charges with 1 Mobile Proton"


    cheq1_mpeq1 = models.IntegerField("Ch=1 MP=1", null=True, blank=True)

    cheq2_mpeq1 = models.IntegerField("Ch=2 MP=1", null=True, blank=True)

    cheq3_mpeq1 = models.IntegerField("Ch=3 MP=1", null=True, blank=True)

    cheq4_mpeq1 = models.IntegerField("Ch=4 MP=1", null=True, blank=True)





class PercentOfIdsAtDifferentChargesAndMobileProtonsRel(models.Model):


    class Meta:
        verbose_name = "Percent of IDs at Different Charges and Mobile Protons Relative to IDs with 1 Mobile Proton"


    cheq1_mpeq1 = models.FloatField("Ch=1 MP=1", null=True, blank=True)

    cheq1_mpeq0 = models.FloatField("Ch=1 MP=0", null=True, blank=True)

    cheq1_mpeq1 = models.FloatField("Ch=1 MP=1", null=True, blank=True)

    cheq2_mpeq1 = models.FloatField("Ch=2 MP=1", null=True, blank=True)

    cheq2_mpeq0 = models.FloatField("Ch=2 MP=0", null=True, blank=True)

    cheq2_mpeq1 = models.FloatField("Ch=2 MP=1", null=True, blank=True)

    cheq3_mpeq1 = models.FloatField("Ch=3 MP=1", null=True, blank=True)

    cheq3_mpeq0 = models.FloatField("Ch=3 MP=0", null=True, blank=True)

    cheq3_mpeq1 = models.FloatField("Ch=3 MP=1", null=True, blank=True)





class IntensitiesVsDifferentMobileProton(models.Model):


    class Meta:
        verbose_name = "Intensities vs Different Mobile Proton"


    ions_mpeq1 = models.IntegerField("Ions, MP=1", null=True, blank=True)

    ions_mpeq0 = models.IntegerField("Ions, MP=0", null=True, blank=True)

    ions_mpeq1 = models.IntegerField("Ions, MP=1", null=True, blank=True)

    ions_mpeq2 = models.IntegerField("Ions, MP=2", null=True, blank=True)

    inten_mpeq1 = models.FloatField("Inten, MP=1", null=True, blank=True)

    inten_mpeq0 = models.FloatField("Inten, MP=0", null=True, blank=True)

    inten_mpeq1 = models.FloatField("Inten, MP=1", null=True, blank=True)

    inten_mpeq2 = models.FloatField("Inten, MP=2", null=True, blank=True)





class PrecursorMZ_MonoisotopeExactMZ(models.Model):


    class Meta:
        verbose_name = "Precursor m/z - Monoisotope Exact m/z"


    more_than_100 = models.IntegerField("More Than 100", null=True, blank=True)

    betw_1000500 = models.IntegerField("Betw 100.0-50.0", null=True, blank=True)

    betw_500250 = models.IntegerField("Betw 50.0-25.0", null=True, blank=True)

    betw_250125 = models.IntegerField("Betw 25.0-12.5", null=True, blank=True)

    betw_12563 = models.IntegerField("Betw 12.5-6.3", null=True, blank=True)

    betw_6331 = models.IntegerField("Betw 6.3-3.1", null=True, blank=True)

    betw_3116 = models.IntegerField("Betw 3.1-1.6", null=True, blank=True)

    betw_1608 = models.IntegerField("Betw 1.6-0.8", null=True, blank=True)

    top_half = models.IntegerField("Top Half", null=True, blank=True)

    next_half_2 = models.IntegerField("Next Half (2)", null=True, blank=True)

    next_half_3 = models.IntegerField("Next Half (3)", null=True, blank=True)

    next_half_4 = models.IntegerField("Next Half (4)", null=True, blank=True)

    next_half_5 = models.IntegerField("Next Half (5)", null=True, blank=True)

    next_half_6 = models.IntegerField("Next Half (6)", null=True, blank=True)

    next_half_7 = models.IntegerField("Next Half (7)", null=True, blank=True)

    next_half_8 = models.IntegerField("Next Half (8)", null=True, blank=True)





class Ms2IdSpectra(models.Model):


    class Meta:
        verbose_name = "MS2 ID Spectra"


    npeaks_median = models.IntegerField("NPeaks Median", null=True, blank=True)

    npeaks_interq = models.FloatField("NPeaks InterQ", null=True, blank=True)

    s_n_median = models.FloatField("S/N Median", null=True, blank=True)

    s_n_interq = models.FloatField("S/N InterQ", null=True, blank=True)

    id_score_median = models.FloatField("ID Score Median", null=True, blank=True)

    id_score_interq = models.FloatField("ID Score InterQ", null=True, blank=True)

    idsc_med_q1msmx = models.FloatField("IDSc Med Q1Msmx", null=True, blank=True)





class Ms1IdMax(models.Model):


    class Meta:
        verbose_name = "MS1 ID Max"


    median = models.FloatField("Median", null=True, blank=True)

    half_width = models.FloatField("Half Width", null=True, blank=True)

    quart_ratio = models.FloatField("Quart Ratio", null=True, blank=True)

    median_midrt = models.FloatField("Median MidRT", null=True, blank=True)

    n75_25_midrt = models.FloatField("75/25 MidRT", null=True, blank=True)

    n95_5_midrt = models.FloatField("95/5 MidRT", null=True, blank=True)

    n75_25_pctile = models.FloatField("75/25 Pctile", null=True, blank=True)

    n95_5_pctile = models.FloatField("95/5 Pctile", null=True, blank=True)





class FractionOfMs2IdentifiedAtDifferentMs1MaxQuartile(models.Model):


    class Meta:
        verbose_name = "Fraction of MS2 Identified at Different MS1max Quartile"


    id_fract_q1 = models.FloatField("ID Fract Q1", null=True, blank=True)

    id_fract_q2 = models.FloatField("ID fract Q2", null=True, blank=True)

    id_fract_q3 = models.FloatField("ID Fract Q3", null=True, blank=True)

    id_fract_q4 = models.FloatField("ID Fract Q4", null=True, blank=True)





class Ms1IdAbundAtMs2Acquisition(models.Model):


    class Meta:
        verbose_name = "MS1 ID Abund at MS2 Acquisition"


    median = models.FloatField("Median", null=True, blank=True)

    half_width = models.FloatField("Half Width", null=True, blank=True)

    n75_25_pctile = models.FloatField("75/25 Pctile", null=True, blank=True)

    n95_5_pctile = models.FloatField("95/5 Pctile", null=True, blank=True)





class Ms2IdAbundReported(models.Model):


    class Meta:
        verbose_name = "MS2 ID Abund Reported"


    median = models.IntegerField("Median", null=True, blank=True)

    half_width = models.IntegerField("Half Width", null=True, blank=True)

    n75_25_pctile = models.FloatField("75/25 Pctile", null=True, blank=True)

    n95_5_pctile = models.FloatField("95/5 Pctile", null=True, blank=True)





class PeakWidthAtHalfHeightForId(models.Model):


    class Meta:
        verbose_name = "Peak Width at Half Height for ID"


    median_value = models.FloatField("Median Value", null=True, blank=True)

    med_top_quart = models.FloatField("Med Top Quart", null=True, blank=True)

    med_top_16th = models.FloatField("Med Top 16th", null=True, blank=True)

    med_top_100 = models.FloatField("Med Top 100", null=True, blank=True)

    median_disper = models.FloatField("Median Disper", null=True, blank=True)

    med_quart_disp = models.FloatField("Med Quart Disp", null=True, blank=True)

    med_16th_disp = models.FloatField("Med 16th Disp", null=True, blank=True)

    med_100_disp = models.FloatField("Med 100 Disp", null=True, blank=True)

    n3quart_value = models.FloatField("3Quart Value", null=True, blank=True)

    n9dec_value = models.FloatField("9Dec Value", null=True, blank=True)

    ms1_interscan_s = models.FloatField("MS1 Interscan/s", null=True, blank=True)

    ms1_scan_fwhm = models.FloatField("MS1 Scan/FWHM", null=True, blank=True)

    ids_used = models.IntegerField("IDs Used", null=True, blank=True)





class PeakWidthsAtHalfMaxOverRtDecilesForId(models.Model):


    class Meta:
        verbose_name = "Peak Widths at Half Max over RT deciles for ID"


    first_decile = models.FloatField("First Decile", null=True, blank=True)

    median_value = models.FloatField("Median Value", null=True, blank=True)

    last_decile = models.FloatField("Last Decile", null=True, blank=True)





class NearbyResamplingOfIds_OversamplingDetail(models.Model):


    class Meta:
        verbose_name = "Nearby Resampling of IDs - Oversampling Detail"


    repeated_ids = models.IntegerField("Repeated IDs", null=True, blank=True)

    med_rt_diff_s = models.FloatField("Med RT Diff/s", null=True, blank=True)

    n1q_rt_diff_s = models.FloatField("1Q RT Diff/s", null=True, blank=True)

    n1dec_rt_diff_s = models.FloatField("1Dec RT Diff/s", null=True, blank=True)

    median_dm_z = models.FloatField("Median dm/z", null=True, blank=True)

    quart_dm_z = models.FloatField("Quart dm/z", null=True, blank=True)





class WideRtDifferencesForIds_gt4Min_(models.Model):


    class Meta:
        verbose_name = "Wide RT Differences for IDs (> 4 min)"


    peptides = models.IntegerField("Peptides", null=True, blank=True)

    spectra = models.IntegerField("Spectra", null=True, blank=True)





class FractionOfRepeatPeptideIdsWithDivergentRt_RtVsRt_(models.Model):


    class Meta:
        verbose_name = "Fraction of Repeat Peptide IDs with Divergent RT (RT vs RT-best ID) - Chromatographic 'Bleed'"


    _4_min = models.FloatField("- 4 min", null=True, blank=True)

    plus_4_min = models.FloatField("+ 4 min", null=True, blank=True)





class EarlyAndLateRtOversampling_SpectrumIdsUniquePepti(models.Model):


    class Meta:
        verbose_name = "Early and Late RT Oversampling (Spectrum IDs/Unique Peptide IDs) - Chromatographic: Flow Through/Bleed"


    first_decile = models.FloatField("First Decile", null=True, blank=True)

    last_decile = models.FloatField("Last Decile", null=True, blank=True)





class PeptideIonIdsBygt3Spectra_Hi_Vs1_3Spectra_Lo_Extr(models.Model):


    class Meta:
        verbose_name = "Peptide Ion IDs by > 3 Spectra (Hi) vs  1-3 Spectra (Lo) - Extreme Oversampling"


    pep_ions_hi = models.IntegerField("Pep Ions (Hi)", null=True, blank=True)

    ratio_hi_lo = models.FloatField("Ratio Hi/Lo", null=True, blank=True)

    spec_cnts_hi = models.IntegerField("Spec Cnts (Hi)", null=True, blank=True)

    ratio_hi_lo = models.FloatField("Ratio Hi/Lo", null=True, blank=True)

    spec_pep_hi = models.FloatField("Spec/Pep (Hi)", null=True, blank=True)

    spec_cnt_excess = models.FloatField("Spec Cnt Excess", null=True, blank=True)





class RatiosOfPeptideIonsIdedByDifferentNumbersOfSpectr(models.Model):


    class Meta:
        verbose_name = "Ratios of Peptide Ions IDed by Different Numbers of Spectra - Oversampling Measure"


    once_twice = models.FloatField("Once/Twice", null=True, blank=True)

    twice_thrice = models.FloatField("Twice/Thrice", null=True, blank=True)





class SingleSpectrumPeptideIonIdentifications_Oversampl(models.Model):


    class Meta:
        verbose_name = "Single Spectrum Peptide Ion Identifications - Oversampling Measure"


    peptide_ions = models.IntegerField("Peptide Ions", null=True, blank=True)

    fract_gt1_ions = models.FloatField("Fract >1 Ions", null=True, blank=True)

    n1_vs_gt1_pepion = models.FloatField("1 vs >1 PepIon", null=True, blank=True)

    n1_vs_gt1_spec = models.FloatField("1 vs >1 Spec", null=True, blank=True)





class Ms1MaxMs1SampledAbundanceRatioIds_InefficientSamp(models.Model):


    class Meta:
        verbose_name = "MS1max/MS1sampled Abundance Ratio IDs - Inefficient Sampling"


    median_all_ids = models.FloatField("Median All IDs", null=True, blank=True)

    n3q_all_ids = models.FloatField("3Q All IDs", null=True, blank=True)

    n9dec_all_ids = models.FloatField("9Dec All IDs", null=True, blank=True)

    med_top_100 = models.FloatField("Med Top 100", null=True, blank=True)

    med_top_dec = models.FloatField("Med Top Dec", null=True, blank=True)

    med_top_quart = models.FloatField("Med Top Quart", null=True, blank=True)

    med_bottom_1_2 = models.FloatField("Med Bottom 1/2", null=True, blank=True)





class Rt_Ms1Max_Rt_Ms2_ForIds_Sec_(models.Model):


    class Meta:
        verbose_name = "RT(MS1max)-RT(MS2) for IDs (sec)"


    med_diff_abs = models.IntegerField("Med Diff Abs", null=True, blank=True)

    median_diff = models.IntegerField("Median Diff", null=True, blank=True)

    first_quart = models.IntegerField("First Quart", null=True, blank=True)

    third_quart = models.IntegerField("Third Quart", null=True, blank=True)





class IonInjectionTimesForIds_Ms_(models.Model):


    class Meta:
        verbose_name = "Ion Injection Times for IDs (ms)"


    ms1_median = models.IntegerField("MS1 Median", null=True, blank=True)

    ms1_maximum = models.IntegerField("MS1 Maximum", null=True, blank=True)

    ms2_median = models.FloatField("MS2 Median", null=True, blank=True)

    ms2_maximun = models.FloatField("MS2 Maximun", null=True, blank=True)

    ms2_fract_max = models.FloatField("MS2 Fract Max", null=True, blank=True)





class TopIonAbundanceMeasure(models.Model):


    class Meta:
        verbose_name = "Top Ion Abundance Measure"


    top_10percent_abund = models.IntegerField("Top 10% Abund", null=True, blank=True)

    top_25percent_abund = models.IntegerField("Top 25% Abund", null=True, blank=True)

    top_50percent_abund = models.IntegerField("Top 50% Abund", null=True, blank=True)

    fractab_top = models.FloatField("Fractab Top", null=True, blank=True)

    fractab_top_10 = models.FloatField("Fractab Top 10", null=True, blank=True)

    fractab_top_100 = models.FloatField("Fractab Top 100", null=True, blank=True)





class IsotopicAbundanceVariation(models.Model):


    class Meta:
        verbose_name = "Isotopic Abundance Variation"


    number_of_ions = models.IntegerField("Number of Ions", null=True, blank=True)

    median_dev = models.FloatField("Median Dev", null=True, blank=True)

    interquart = models.FloatField("Interquart", null=True, blank=True)





class IonPeakClusterCountDistribution(models.Model):


    class Meta:
        verbose_name = "Ion 'Peak Cluster' Count Distribution"


    total_found = models.IntegerField("Total Found", null=True, blank=True)

    id_fraction = models.FloatField("ID Fraction", null=True, blank=True)

    noid_fraction = models.FloatField("noID Fraction", null=True, blank=True)

    nosamp_fraction = models.FloatField("noSamp Fraction", null=True, blank=True)





class IonClusterAbundanceDistribution(models.Model):


    class Meta:
        verbose_name = "Ion Cluster Abundance Distribution"


    id_fraction = models.FloatField("ID Fraction", null=True, blank=True)

    noid_fraction = models.FloatField("noID Fraction", null=True, blank=True)

    nosamp_fraction = models.FloatField("noSamp Fraction", null=True, blank=True)

    noid_med_rel = models.FloatField("noID Med Rel", null=True, blank=True)

    unsamp_med_rel = models.FloatField("Unsamp Med Rel", null=True, blank=True)





class AbundanceDistributionTotal(models.Model):


    class Meta:
        verbose_name = "Abundance Distribution: Total"


    total_fraction = models.FloatField("Total Fraction", null=True, blank=True)

    peptides = models.FloatField("Peptides", null=True, blank=True)

    samplednoid = models.FloatField("Sampled-NoID", null=True, blank=True)

    not_sampled_percent = models.FloatField("Not Sampled %", null=True, blank=True)

    noise = models.FloatField("Noise", null=True, blank=True)





class AbundanceDistribution1RtQuartile(models.Model):


    class Meta:
        verbose_name = "Abundance Distribution: 1 RT Quartile"


    rt_segment_end = models.FloatField("RT Segment End", null=True, blank=True)

    total_fraction = models.FloatField("Total Fraction", null=True, blank=True)

    peptides = models.FloatField("Peptides", null=True, blank=True)

    samplednoid = models.FloatField("Sampled-NoID", null=True, blank=True)

    not_sampled_percent = models.FloatField("Not Sampled %", null=True, blank=True)

    noise = models.FloatField("Noise", null=True, blank=True)





class AbundanceDistribution2RtQuartile(models.Model):


    class Meta:
        verbose_name = "Abundance Distribution: 2 RT Quartile"


    rt_segment_end = models.FloatField("RT Segment End", null=True, blank=True)

    total_fraction = models.FloatField("Total Fraction", null=True, blank=True)

    peptides = models.FloatField("Peptides", null=True, blank=True)

    samplednoid = models.FloatField("Sampled-NoID", null=True, blank=True)

    not_sampled_percent = models.FloatField("Not Sampled %", null=True, blank=True)

    noise = models.FloatField("Noise", null=True, blank=True)





class AbundanceDistribution3RtQuartile(models.Model):


    class Meta:
        verbose_name = "Abundance Distribution: 3 RT Quartile"


    rt_segment_end = models.FloatField("RT Segment End", null=True, blank=True)

    total_fraction = models.FloatField("Total Fraction", null=True, blank=True)

    peptides = models.FloatField("Peptides", null=True, blank=True)

    samplednoid = models.FloatField("Sampled-NoID", null=True, blank=True)

    not_sampled_percent = models.FloatField("Not Sampled %", null=True, blank=True)

    noise = models.FloatField("Noise", null=True, blank=True)





class AbundanceDistribution4RtQuartile(models.Model):


    class Meta:
        verbose_name = "Abundance Distribution: 4 RT Quartile"


    rt_segment_end = models.FloatField("RT Segment End", null=True, blank=True)

    total_fraction = models.FloatField("Total Fraction", null=True, blank=True)

    peptides = models.FloatField("Peptides", null=True, blank=True)

    samplednoid = models.FloatField("Sampled-NoID", null=True, blank=True)

    not_sampled_percent = models.FloatField("Not Sampled %", null=True, blank=True)

    noise = models.FloatField("Noise", null=True, blank=True)





class AbundanceDistributionLastSegment(models.Model):


    class Meta:
        verbose_name = "Abundance Distribution: Last Segment"


    rt_segment_end = models.FloatField("RT Segment End", null=True, blank=True)

    total_fraction = models.FloatField("Total Fraction", null=True, blank=True)

    peptides = models.FloatField("Peptides", null=True, blank=True)

    samplednoid = models.FloatField("Sampled-NoID", null=True, blank=True)

    not_sampled_percent = models.FloatField("Not Sampled %", null=True, blank=True)

    noise = models.FloatField("Noise", null=True, blank=True)





class MZMediansForClustersAtRtQuartiles_AllCharges_(models.Model):


    class Meta:
        verbose_name = "m/z Medians for Clusters at RT Quartiles (all charges)"


    first_quart = models.FloatField("First Quart", null=True, blank=True)

    second_quart = models.FloatField("Second Quart", null=True, blank=True)

    third_quart = models.FloatField("Third Quart", null=True, blank=True)

    fourth_quart = models.FloatField("Fourth Quart", null=True, blank=True)





class MZMediansForClustersAtRtQuartiles_plus2Only_(models.Model):


    class Meta:
        verbose_name = "m/z Medians for Clusters at RT Quartiles (+2 only)"


    first_quart = models.FloatField("First Quart", null=True, blank=True)

    second_quart = models.FloatField("Second Quart", null=True, blank=True)

    third_quart = models.FloatField("Third Quart", null=True, blank=True)

    fourth_quart = models.FloatField("Fourth Quart", null=True, blank=True)





class MZMediansForClustersAtDifferentCharge(models.Model):


    class Meta:
        verbose_name = "m/z Medians for Clusters at Different Charge"


    charge_plus1 = models.FloatField("Charge +1", null=True, blank=True)

    charge_plus2 = models.FloatField("Charge +2", null=True, blank=True)

    charge_plus3 = models.FloatField("Charge +3", null=True, blank=True)

    no_charge = models.FloatField("No Charge", null=True, blank=True)





class NumbersOfClustersOfDifferentCharge(models.Model):


    class Meta:
        verbose_name = "Numbers of Clusters of Different Charge"


    charge_plus2 = models.IntegerField("Charge +2", null=True, blank=True)

    no_charge_plus2 = models.FloatField("No Charge/+2", null=True, blank=True)

    charge_plus1_plus2 = models.FloatField("Charge +1/+2", null=True, blank=True)

    charge_plus3_plus2 = models.FloatField("Charge +3/+2", null=True, blank=True)





class NumbersOfClustersAtplus1plus2ChargesAtRtQuartile(models.Model):


    class Meta:
        verbose_name = "Numbers of Clusters at +1/+2 Charges at RT Quartile"


    plus2_clusters = models.IntegerField("+2 Clusters", null=True, blank=True)

    rt_quart_1 = models.FloatField("RT Quart 1", null=True, blank=True)

    rt_quart_2 = models.FloatField("RT Quart 2", null=True, blank=True)

    rt_quart_3 = models.FloatField("RT Quart 3", null=True, blank=True)

    rt_quart_4 = models.FloatField("RT Quart 4", null=True, blank=True)





class NumbersOfClustersAtplus3plus2ChargesAtRtQuartile(models.Model):


    class Meta:
        verbose_name = "Numbers of Clusters at +3/+2 Charges at RT Quartile"


    plus2_clusters = models.IntegerField("+2 Clusters", null=True, blank=True)

    rt_quart_1 = models.FloatField("RT Quart 1", null=True, blank=True)

    rt_quart_2 = models.FloatField("RT Quart 2", null=True, blank=True)

    rt_quart_3 = models.FloatField("RT Quart 3", null=True, blank=True)

    rt_quart_4 = models.FloatField("RT Quart 4", null=True, blank=True)





class FractOfClusterAbundanceAt50And90OfAllAbundance(models.Model):


    class Meta:
        verbose_name = "Fract of Cluster Abundance at 50% and 90% of All Abundance"


    n50percent_ions = models.IntegerField("50% Ions", null=True, blank=True)

    n50percent_id = models.FloatField("50% ID", null=True, blank=True)

    n50percent_noidsamp = models.FloatField("50% noIDSamp", null=True, blank=True)

    n50percent_noidnosamp = models.FloatField("50% noIDnoSamp", null=True, blank=True)

    n90percent_ions = models.IntegerField("90% Ions", null=True, blank=True)

    n90percent_id = models.FloatField("90% ID", null=True, blank=True)

    n90percent_noidsamp = models.FloatField("90% noIDSamp", null=True, blank=True)

    n90percent_noidnosamp = models.FloatField("90% noIDnoSamp", null=True, blank=True)





class Top10NoidIon(models.Model):


    class Meta:
        verbose_name = "Top 10 NoID Ion"


    noid_1_rank = models.IntegerField("NoID 1 Rank", null=True, blank=True)

    noid_1_relab = models.FloatField("NoID 1 RelAb", null=True, blank=True)

    noid_1_rt = models.FloatField("NoID 1 RT", null=True, blank=True)

    noid_1_m_z = models.FloatField("NoID 1 m/z", null=True, blank=True)

    noid_2_rank = models.IntegerField("NoID 2 Rank", null=True, blank=True)

    noid_2_relab = models.FloatField("NoID 2 RelAb", null=True, blank=True)

    noid_2_rt = models.FloatField("NoID 2 RT", null=True, blank=True)

    noid_2_m_z = models.FloatField("NoID 2 m/z", null=True, blank=True)

    noid_3_rank = models.IntegerField("NoID 3 Rank", null=True, blank=True)

    noid_3_relab = models.FloatField("NoID 3 RelAb", null=True, blank=True)

    noid_3_rt = models.FloatField("NoID 3 RT", null=True, blank=True)

    noid_3_m_z = models.FloatField("NoID 3 m/z", null=True, blank=True)

    noid_4_rank = models.IntegerField("NoID 4 Rank", null=True, blank=True)

    noid_4_relab = models.FloatField("NoID 4 RelAb", null=True, blank=True)

    noid_4_rt = models.FloatField("NoID 4 RT", null=True, blank=True)

    noid_4_m_z = models.FloatField("NoID 4 m/z", null=True, blank=True)

    noid_5_rank = models.IntegerField("NoID 5 Rank", null=True, blank=True)

    noid_5_relab = models.FloatField("NoID 5 RelAb", null=True, blank=True)

    noid_5_rt = models.FloatField("NoID 5 RT", null=True, blank=True)

    noid_5_m_z = models.FloatField("NoID 5 m/z", null=True, blank=True)

    noid_6_rank = models.IntegerField("NoID 6 Rank", null=True, blank=True)

    noid_6_relab = models.FloatField("NoID 6 RelAb", null=True, blank=True)

    noid_6_rt = models.FloatField("NoID 6 RT", null=True, blank=True)

    noid_6_m_z = models.FloatField("NoID 6 m/z", null=True, blank=True)

    noid_7_rank = models.IntegerField("NoID 7 Rank", null=True, blank=True)

    noid_7_relab = models.FloatField("NoID 7 RelAb", null=True, blank=True)

    noid_7_rt = models.FloatField("NoID 7 RT", null=True, blank=True)

    noid_7_m_z = models.FloatField("NoID 7 m/z", null=True, blank=True)

    noid_8_rank = models.IntegerField("NoID 8 Rank", null=True, blank=True)

    noid_8_relab = models.FloatField("NoID 8 RelAb", null=True, blank=True)

    noid_8_rt = models.FloatField("NoID 8 RT", null=True, blank=True)

    noid_8_m_z = models.FloatField("NoID 8 m/z", null=True, blank=True)

    noid_9_rank = models.IntegerField("NoID 9 Rank", null=True, blank=True)

    noid_9_relab = models.FloatField("NoID 9 RelAb", null=True, blank=True)

    noid_9_rt = models.FloatField("NoID 9 RT", null=True, blank=True)

    noid_9_m_z = models.FloatField("NoID 9 m/z", null=True, blank=True)

    noid_10_rank = models.IntegerField("NoID 10 Rank", null=True, blank=True)

    noid_10_relab = models.FloatField("NoID 10 RelAb", null=True, blank=True)

    noid_10_rt = models.FloatField("NoID 10 RT", null=True, blank=True)

    noid_10_m_z = models.FloatField("NoID 10 m/z", null=True, blank=True)





class NewMetric(models.Model):


    class Meta:
        verbose_name = "New Metric"


    peak_wid_alt = models.FloatField("Peak Wid Alt", null=True, blank=True)

    unexpect_int = models.IntegerField("Unexpect Int", null=True, blank=True)





class OtherIonClusterStatistic(models.Model):


    class Meta:
        verbose_name = "Other Ion Cluster Statistic"


    rt_begin = models.FloatField("RT Begin", null=True, blank=True)

    rt_end = models.FloatField("RT End", null=True, blank=True)

    idpep_not_found = models.IntegerField("IDPep Not Found", null=True, blank=True)

    ids_too_early = models.IntegerField("IDs too Early", null=True, blank=True)

    ids_too_late = models.IntegerField("IDs too Late", null=True, blank=True)

    ids_no_abund = models.IntegerField("IDs no Abund", null=True, blank=True)

    noids_no_abund = models.IntegerField("noIDs no Abund", null=True, blank=True)

    nids_found = models.IntegerField("nIDs Found", null=True, blank=True)

    missed_rt = models.FloatField("Missed RT", null=True, blank=True)

    missed_clust = models.FloatField("Missed Clust", null=True, blank=True)

    low_qpercent_lteq61 = models.FloatField("Low Q% <=61", null=True, blank=True)

    qual_percent_0_0 = models.FloatField("Qual % 0:0", null=True, blank=True)

    qual_percent_10_19 = models.FloatField("Qual % 10:19", null=True, blank=True)

    qual_percent_20_29 = models.FloatField("Qual % 20:29", null=True, blank=True)

    qual_percent_30_39 = models.FloatField("Qual % 30:39", null=True, blank=True)

    qual_percent_40_49 = models.FloatField("Qual % 40:49", null=True, blank=True)

    qual_percent_50_59 = models.FloatField("Qual % 50:59", null=True, blank=True)

    qual_percent_60_69 = models.FloatField("Qual % 60:69", null=True, blank=True)

    qual_percent_70_79 = models.FloatField("Qual % 70:79", null=True, blank=True)

    qual_percent_80_89 = models.FloatField("Qual % 80:89", null=True, blank=True)

    qual_percent_90_99 = models.FloatField("Qual % 90:99", null=True, blank=True)

    qual_percent_100_100 = models.FloatField("Qual % 100:100", null=True, blank=True)

