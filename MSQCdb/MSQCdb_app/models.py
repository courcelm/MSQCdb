## Copyright 2012 Mathieu Courcelles
## Mike Tyers's lab / IRIC / Universite de Montreal 

## This file is part of the MSQCdb project
## MSQCdb is free software: you can redistribute it and/or modify
## it under the terms of the GNU Affero General Public License as
## published by the Free Software Foundation, either version 3 of the
## License, or (at your option) any later version.

## MSQCdb is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU Affero General Public License for more details.

## You should have received a copy of the GNU Affero General Public
## License along with MSQCdb. If not, see <http://www.gnu.org/licenses/>.


"""
This is the data model module for the MSQCdb.
"""


# Import Django related libraries
from django.db import models
from django.contrib.auth.models import User
from django.core import urlresolvers
from django.utils.html import escape



    


class Instrument(models.Model):
    """
    This class holds the name of all the MS instrument.
    """
    
    instrument_name = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return str(self.instrument_name)

    class Meta:
        ordering = ['instrument_name']
        



class Sample(models.Model):
    """
    This class stores all the samples that have been processed with the 
    NISTMSQC pipeline and store in the db.
    """
    
    creation_date = models.DateTimeField(auto_now_add=True)
    
    experimentdate = models.DateTimeField("ExperimentDate", null=True, 
                                          blank=True)
    
    raw_file = models.CharField(max_length=1000)
    
    raw_file_fullPath = models.CharField(max_length=1000)
    
    instrument_name = models.ForeignKey(Instrument)

    description = models.TextField('Detailed description', blank=True)
    
    
    def __unicode__(self):
        return str(self.pk)
    

    class Meta:
        ordering = ['-experimentdate']


        

class EventLog(models.Model):
    """
    This class logs events (calibration, maintenance, failure) related to the
    MS instrument.  
    """
    
    created_by = models.ForeignKey(User, null=True, blank=True,
                                   related_name='%(class)s_created_by', 
                                   editable=False)
    
    creation_date = models.DateTimeField(auto_now_add=True)
    
    modification_date = models.DateTimeField('Modified at', auto_now=True)

    datetime = models.DateTimeField()
    
    EVENT_TYPES = (('Calibration', 'Calibration'),
                   ('Failure', 'Failure'),
                   ('Maintenance', 'Maintenance'),
                   ('Note', 'Note'),
                   )
    
    event_type = models.CharField('Event type', max_length=30,
                                     choices=EVENT_TYPES)
    
    instrument_name = models.ForeignKey(Instrument)
    
    name = models.CharField('Name', max_length=200,
                            help_text='Short description of the event')
    
    description = models.TextField('Detailed description (what was replaced,\
                                     how it was fixed)', blank=True)

    def __unicode__(self):
        return '%s: %s' % (self.event_type, self.name)



class Chart(models.Model):
    """
    Chart information for plotting a Highstock chart
    """
    
    title = models.CharField(help_text = 'Title that appears at the top of the\
                                         chart.', max_length=50, unique=True)
    
    yAxisTitle = models.CharField('Y axis title', help_text = 'Title of the y\
                                     axis.', max_length=25)
    
    plotMeanStd = models.BooleanField(u'Plot Mean (\u03BC) / Standard deviation (\u03C3)')
    
    created_by = models.ForeignKey(User, null=True, blank=True,
                                   related_name='%(class)s_created_by', 
                                   editable=False)
    

    def __unicode__(self):
        return str('Chart (' + str(self.pk) + '): ' + self.title)
    
    def get_admin_url(self):
        return urlresolvers.reverse("admin:%s_%s_change" %
        (self._meta.app_label, self._meta.module_name), args=(self.id,))
    
    def get_relative_url(self):
        """
        Define standard relative URL for object access in templates
        """
        return 'chart/%i/' % self.id
    
    def html_url(self):
        return '<a href="%s">%s</a>' % (self.get_admin_url(),
                                        self.__unicode__())




class ChartSeries(models.Model):
    """
    Define the criteria to retrieve a series of data point
    """
    
    chart = models.ForeignKey(Chart)
    
    name  = models.CharField(max_length=25, null=True, blank=True)
    
    instrument_name = models.ForeignKey(Instrument, null=True, blank=True)

    keyword = models.CharField('Sample name keyword', help_text='Sample name\
                                 should contain this word.', max_length=50, 
                                 null=True, blank=True)
    
    table =  models.CharField(max_length=100)
    
    field =  models.CharField(max_length=100)



    class Meta:
        verbose_name_plural = "ChartSeries"



    def __unicode__(self):
        return '<table class="table-tag"><tr>\
                <td><span class="tag">name</span> %s</td>\
                <td><span class="tag">instrument_name</span> %s</td>\
                <td><span class="tag">keyword</span> %s</td>\
                <td><span class="tag">table</span> %s</td>\
                <td><span class="tag">field</span> %s</td>\
                </tr></table>' % (self.name, 
                                                         self.instrument_name,  
                                                         self.keyword, 
                                                         self.table,
                                                         self.field)




class ChartEventFlag(models.Model):
    """
    Define the criteria to retrieve event flagss
    """
    
    chart = models.ForeignKey(Chart)
    
    instrument_name = models.ForeignKey(Instrument, null=True, blank=True)
    
    EVENT_TYPES = (('Calibration', 'Calibration'),
                   ('Failure', 'Failure'),
                   ('Maintenance', 'Maintenance'),
                   ('Note', 'Note'),
                   )
    
    event_type = models.CharField('Event type', max_length=30,
                                     choices=EVENT_TYPES, null=True, 
                                     blank=True)
    
    def __unicode__(self):
        return '<table class="table-tag"><tr>\
                <td><span class="tag">instrument_name</span> %s\
                <td><span class="tag">event_type</span> %s\
                </tr></table>' % (self.instrument_name,
                                  self.event_type)




class Report(models.Model):
    """
    Display a report made of multiple charts.
    """
    
    name = models.CharField(max_length=50, unique=True)
    
    COLUMN_CHOICE = ((1, 1),
                     (2, 2),
                     (3, 3),
                     )
    
    column_num = models.PositiveSmallIntegerField('Number of columns for layout',
                                                  choices=COLUMN_CHOICE)
    
    description = models.TextField('Detailed description of the report',
                                    blank=True)
    
    created_by = models.ForeignKey(User, null=True, blank=True,
                                   related_name='%(class)s_created_by', 
                                   editable=False)    
    
    
    def __unicode__(self):
        return '%s' % (self.name)



    
class ReportChart(models.Model):
    """
    Define the selected chart in the report.
    """
    
    report = models.ForeignKey(Report)
    
    chart = models.ForeignKey(Chart)
    
    #For drag and drop sort of inline
    position = models.PositiveSmallIntegerField("Position")
    
    class Meta:
        ordering = ['position']



    

    
    # Note: the rest of the code has been automaticaly generated by the parser
#       to create the model. Read NISTMSQC paper to have description of all
#       the field or THERMO raw/tune file documentation. 


class MetadataOverview(models.Model):


    class Meta:
        verbose_name = "Meta: Metadata Overview"
        
        ordering = ['experimentdate']


    sample = models.ForeignKey(Sample, related_name='%(class)s_Meta')

    experimentdate = models.DateTimeField("ExperimentDate", null=True, blank=True)

    instrumentmethod = models.CharField("InstrumentMethod", max_length=1000, null=True, blank=True)

    thermo_raw_file = models.CharField("Thermo RAW File", max_length=1000, null=True, blank=True)

    sha1_hash = models.CharField("Sha1 hash", max_length=40, null=True, blank=True)

    instrument_name = models.CharField("Instrument Name", max_length=100, null=True, blank=True)

    instrument_serial_number = models.CharField("Instrument Serial Number", max_length=100, null=True, blank=True)

    instrument_model = models.CharField("Instrument Model", max_length=50, null=True, blank=True)

    comment1 = models.CharField("Comment1", max_length=1000, null=True, blank=True)

    comment2 = models.CharField("Comment2", max_length=1000, null=True, blank=True)

    operator = models.CharField("Operator", max_length=50, null=True, blank=True)

    instrument_software_version = models.CharField("Instrument Software Version", max_length=50, null=True, blank=True)

    instrument_hardware_version = models.CharField("Instrument Hardware Version", max_length=50, null=True, blank=True)






class MetaTuneFileValue(models.Model):


    class Meta:
        verbose_name = "Meta: Tune File Value"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Meta')

    source_type = models.CharField("Source Type", max_length=50, null=True, blank=True)

    capillary_temp_c = models.IntegerField("Capillary Temp (C)", null=True, blank=True)

    apci_vaporizer_temp_c = models.IntegerField("APCI Vaporizer Temp (C)", null=True, blank=True)

    sheath_gas_flow = models.IntegerField("Sheath Gas Flow ()", null=True, blank=True)

    aux_gas_flow = models.IntegerField("Aux Gas Flow ()", null=True, blank=True)

    sweep_gas_flow = models.IntegerField("Sweep Gas Flow ()", null=True, blank=True)

    injection_waveforms = models.IntegerField("Injection Waveforms", null=True, blank=True)

    ion_trap_zoom_agc_target = models.IntegerField("Ion Trap Zoom AGC Target", null=True, blank=True)

    ion_trap_full_agc_target = models.IntegerField("Ion Trap Full AGC Target", null=True, blank=True)

    ion_trap_sim_agc_target = models.IntegerField("Ion Trap SIM AGC Target", null=True, blank=True)

    ion_trap_msn_agc_target = models.IntegerField("Ion Trap MSn AGC Target", null=True, blank=True)

    ftms_injection_waveforms = models.IntegerField("FTMS Injection Waveforms", null=True, blank=True)

    ftms_full_agc_target = models.IntegerField("FTMS Full AGC Target", null=True, blank=True)

    ftms_sim_agc_target = models.IntegerField("FTMS SIM AGC Target", null=True, blank=True)

    ftms_msn_agc_target = models.IntegerField("FTMS MSn AGC Target", null=True, blank=True)

    reagent_ion_source_polarity = models.CharField("Reagent Ion Source Polarity", max_length=50, null=True, blank=True)

    reagent_ion_source_temp_c = models.IntegerField("Reagent Ion Source Temp (C)", null=True, blank=True)

    reagent_ion_source_emission_current_ua = models.IntegerField("Reagent Ion Source Emission Current (uA)", null=True, blank=True)

    reagent_ion_source_electron_energy_v = models.IntegerField("Reagent Ion Source Electron Energy (V)", null=True, blank=True)

    reagent_ion_source_ci_pressure_psi = models.IntegerField("Reagent Ion Source CI Pressure (psi)", null=True, blank=True)

    reagent_vial_1_ion_time = models.IntegerField("Reagent Vial 1 Ion Time", null=True, blank=True)

    reagent_vial_1_agc_target = models.IntegerField("Reagent Vial 1 AGC Target", null=True, blank=True)

    reagent_vial_2_ion_time = models.IntegerField("Reagent Vial 2 Ion Time", null=True, blank=True)

    reagent_vial_2_agc_target = models.IntegerField("Reagent Vial 2 AGC Target", null=True, blank=True)

    supplemental_activation_energy = models.IntegerField("Supplemental Activation Energy", null=True, blank=True)

    faims_total_gas_flow_lmin = models.FloatField("FAIMS Total Gas Flow (L/min)", null=True, blank=True)

    faims_helium_composition_percent = models.IntegerField("FAIMS Helium Composition (%)", null=True, blank=True)

    faims_inner_electrode_temp_c = models.IntegerField("FAIMS Inner Electrode Temp (C)", null=True, blank=True)

    faims_outer_electrode_temp_c = models.IntegerField("FAIMS Outer Electrode Temp (C)", null=True, blank=True)




class MetaPositivePolarity(models.Model):


    class Meta:
        verbose_name = "Meta: Positive Polarity"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Meta')

    source_voltage_kv = models.FloatField("Source Voltage (kV)", null=True, blank=True)

    source_current_ua = models.IntegerField("Source Current (uA)", null=True, blank=True)

    capillary_voltage_v = models.FloatField("Capillary Voltage (V)", null=True, blank=True)

    tube_lens_v = models.IntegerField("Tube Lens (V)", null=True, blank=True)

    skimmer_offset_v = models.IntegerField("Skimmer Offset (V)", null=True, blank=True)

    multipole_rf_amplifier_vpp = models.IntegerField("Multipole RF Amplifier (Vp-p)", null=True, blank=True)

    multipole_00_offset_v = models.FloatField("Multipole 00 Offset (V)", null=True, blank=True)

    lens_0_voltage_v = models.FloatField("Lens 0 Voltage (V)", null=True, blank=True)

    multipole_0_offset_v = models.FloatField("Multipole 0 Offset (V)", null=True, blank=True)

    lens_1_voltage_v = models.FloatField("Lens 1 Voltage (V)", null=True, blank=True)

    gate_lens_offset_v = models.IntegerField("Gate Lens Offset (V)", null=True, blank=True)

    multipole_1_offset_v = models.FloatField("Multipole 1 Offset (V)", null=True, blank=True)

    front_lens_v = models.FloatField("Front Lens (V)", null=True, blank=True)

    ion_trap_zoom_micro_scans = models.IntegerField("Ion Trap Zoom Micro Scans", null=True, blank=True)

    ion_trap_zoom_max_ion_time_ms = models.IntegerField("Ion Trap Zoom Max Ion Time (ms)", null=True, blank=True)

    ion_trap_full_micro_scans = models.IntegerField("Ion Trap Full Micro Scans", null=True, blank=True)

    ion_trap_full_max_ion_time_ms = models.IntegerField("Ion Trap Full Max Ion Time (ms)", null=True, blank=True)

    ion_trap_sim_micro_scans = models.IntegerField("Ion Trap SIM Micro Scans", null=True, blank=True)

    ion_trap_sim_max_ion_time_ms = models.IntegerField("Ion Trap SIM Max Ion Time (ms)", null=True, blank=True)

    ion_trap_msn_micro_scans = models.IntegerField("Ion Trap MSn Micro Scans", null=True, blank=True)

    ion_trap_msn_max_ion_time_ms = models.IntegerField("Ion Trap MSn Max Ion Time (ms)", null=True, blank=True)

    ftms_full_micro_scans = models.IntegerField("FTMS Full Micro Scans", null=True, blank=True)

    ftms_full_max_ion_time_ms = models.IntegerField("FTMS Full Max Ion Time (ms)", null=True, blank=True)

    ftms_sim_micro_scans = models.IntegerField("FTMS SIM Micro Scans", null=True, blank=True)

    ftms_sim_max_ion_time_ms = models.IntegerField("FTMS SIM Max Ion Time (ms)", null=True, blank=True)

    ftms_msn_micro_scans = models.IntegerField("FTMS MSn Micro Scans", null=True, blank=True)

    ftms_msn_max_ion_time_ms = models.IntegerField("FTMS MSn Max Ion Time (ms)", null=True, blank=True)

    reagent_ion_lens_1_v = models.IntegerField("Reagent Ion Lens 1 (V)", null=True, blank=True)

    reagent_ion_gate_lens_v = models.IntegerField("Reagent Ion Gate Lens (V)", null=True, blank=True)

    reagent_ion_lens_2_v = models.IntegerField("Reagent Ion Lens 2 (V)", null=True, blank=True)

    reagent_ion_lens_3_v = models.IntegerField("Reagent Ion Lens 3 (V)", null=True, blank=True)

    reagent_ion_back_lens_offset_v = models.FloatField("Reagent Ion Back Lens Offset (V)", null=True, blank=True)

    reagent_ion_back_multipole_offset_v = models.IntegerField("Reagent Ion Back Multipole Offset (V)", null=True, blank=True)

    faims_obv_v = models.IntegerField("FAIMS OBV (V)", null=True, blank=True)

    faims_dv_v = models.IntegerField("FAIMS DV (V)", null=True, blank=True)

    faims_epv_v = models.IntegerField("FAIMS EPV (V)", null=True, blank=True)

    slens_rf_level_percent = models.FloatField("S-Lens RF Level (%)", null=True, blank=True)
    
    back_lens_reagent_injection_v = models.FloatField("Back Lens Reagent Injection (V)", null=True, blank=True)

    back_section_lpt_reagent_injection_v = models.FloatField("Back Section LPT Reagent Injection (V)", null=True, blank=True)

    center_lens_reagent_injection_v = models.FloatField("Center Lens Reagent Injection (V)", null=True, blank=True)

    front_lens_reagent_injection_v = models.FloatField("Front Lens Reagent Injection (V)", null=True, blank=True)

    center_lens_2_v = models.FloatField("Center Lens 2 (V)", null=True, blank=True)




class MetaNegativePolarity(models.Model):


    class Meta:
        verbose_name = "Meta: Negative Polarity"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Meta')

    source_voltage_kv = models.FloatField("Source Voltage (kV)", null=True, blank=True)

    source_current_ua = models.IntegerField("Source Current (uA)", null=True, blank=True)

    capillary_voltage_v = models.FloatField("Capillary Voltage (V)", null=True, blank=True)

    tube_lens_v = models.IntegerField("Tube Lens (V)", null=True, blank=True)

    skimmer_offset_v = models.IntegerField("Skimmer Offset (V)", null=True, blank=True)

    multipole_rf_amplifier_vpp = models.IntegerField("Multipole RF Amplifier (Vp-p)", null=True, blank=True)

    multipole_00_offset_v = models.FloatField("Multipole 00 Offset (V)", null=True, blank=True)

    lens_0_voltage_v = models.FloatField("Lens 0 Voltage (V)", null=True, blank=True)

    multipole_0_offset_v = models.FloatField("Multipole 0 Offset (V)", null=True, blank=True)

    lens_1_voltage_v = models.FloatField("Lens 1 Voltage (V)", null=True, blank=True)

    gate_lens_offset_v = models.IntegerField("Gate Lens Offset (V)", null=True, blank=True)

    multipole_1_offset_v = models.FloatField("Multipole 1 Offset (V)", null=True, blank=True)

    front_lens_v = models.FloatField("Front Lens (V)", null=True, blank=True)

    ion_trap_zoom_micro_scans = models.IntegerField("Ion Trap Zoom Micro Scans", null=True, blank=True)

    ion_trap_zoom_max_ion_time_ms = models.IntegerField("Ion Trap Zoom Max Ion Time (ms)", null=True, blank=True)

    ion_trap_full_micro_scans = models.IntegerField("Ion Trap Full Micro Scans", null=True, blank=True)

    ion_trap_full_max_ion_time_ms = models.IntegerField("Ion Trap Full Max Ion Time (ms)", null=True, blank=True)

    ion_trap_sim_micro_scans = models.IntegerField("Ion Trap SIM Micro Scans", null=True, blank=True)

    ion_trap_sim_max_ion_time_ms = models.IntegerField("Ion Trap SIM Max Ion Time (ms)", null=True, blank=True)

    ion_trap_msn_micro_scans = models.IntegerField("Ion Trap MSn Micro Scans", null=True, blank=True)

    ion_trap_msn_max_ion_time_ms = models.IntegerField("Ion Trap MSn Max Ion Time (ms)", null=True, blank=True)

    ftms_full_micro_scans = models.IntegerField("FTMS Full Micro Scans", null=True, blank=True)

    ftms_full_max_ion_time_ms = models.IntegerField("FTMS Full Max Ion Time (ms)", null=True, blank=True)

    ftms_sim_micro_scans = models.IntegerField("FTMS SIM Micro Scans", null=True, blank=True)

    ftms_sim_max_ion_time_ms = models.IntegerField("FTMS SIM Max Ion Time (ms)", null=True, blank=True)

    ftms_msn_micro_scans = models.IntegerField("FTMS MSn Micro Scans", null=True, blank=True)

    ftms_msn_max_ion_time_ms = models.IntegerField("FTMS MSn Max Ion Time (ms)", null=True, blank=True)

    reagent_ion_lens_1_v = models.IntegerField("Reagent Ion Lens 1 (V)", null=True, blank=True)

    reagent_ion_gate_lens_v = models.IntegerField("Reagent Ion Gate Lens (V)", null=True, blank=True)

    reagent_ion_lens_2_v = models.IntegerField("Reagent Ion Lens 2 (V)", null=True, blank=True)

    reagent_ion_lens_3_v = models.IntegerField("Reagent Ion Lens 3 (V)", null=True, blank=True)

    reagent_ion_back_lens_offset_v = models.FloatField("Reagent Ion Back Lens Offset (V)", null=True, blank=True)

    reagent_ion_back_multipole_offset_v = models.IntegerField("Reagent Ion Back Multipole Offset (V)", null=True, blank=True)

    faims_obv_v = models.IntegerField("FAIMS OBV (V)", null=True, blank=True)

    faims_dv_v = models.IntegerField("FAIMS DV (V)", null=True, blank=True)

    faims_epv_v = models.IntegerField("FAIMS EPV (V)", null=True, blank=True)
    
    slens_rf_level_percent = models.FloatField("S-Lens RF Level (%)", null=True, blank=True)

    back_lens_reagent_injection_v = models.FloatField("Back Lens Reagent Injection (V)", null=True, blank=True)

    back_section_lpt_reagent_injection_v = models.FloatField("Back Section LPT Reagent Injection (V)", null=True, blank=True)

    center_lens_reagent_injection_v = models.FloatField("Center Lens Reagent Injection (V)", null=True, blank=True)

    front_lens_reagent_injection_v = models.FloatField("Front Lens Reagent Injection (V)", null=True, blank=True)

    center_lens_2_v = models.FloatField("Center Lens 2 (V)", null=True, blank=True)



class MetaAdditionalFtTuneFileValue(models.Model):


    class Meta:
        verbose_name = "Meta: Additional Ft Tune File Value"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Meta')

    ft_tune_item_1 = models.IntegerField("FT Tune Item 1", null=True, blank=True)

    ft_tune_item_2 = models.IntegerField("FT Tune Item 2", null=True, blank=True)

    ft_tune_item_3 = models.IntegerField("FT Tune Item 3", null=True, blank=True)

    ft_tune_item_4 = models.IntegerField("FT Tune Item 4", null=True, blank=True)

    ft_tune_item_5 = models.IntegerField("FT Tune Item 5", null=True, blank=True)

    ft_tune_item_6 = models.IntegerField("FT Tune Item 6", null=True, blank=True)

    ft_tune_item_7 = models.IntegerField("FT Tune Item 7", null=True, blank=True)

    ft_tune_item_8 = models.IntegerField("FT Tune Item 8", null=True, blank=True)

    ft_tune_item_9 = models.IntegerField("FT Tune Item 9", null=True, blank=True)

    ft_tune_item_10 = models.IntegerField("FT Tune Item 10", null=True, blank=True)




class MetaReagentIonSourceTuneFileValue(models.Model):


    class Meta:
        verbose_name = "Meta: Reagent Ion Source Tune File Value"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Meta')

    reagent_ion_source_polarity = models.CharField("Reagent Ion Source Polarity", max_length=50, null=True, blank=True)

    reagent_ion_source_temp_c = models.IntegerField("Reagent Ion Source Temp (C)", null=True, blank=True)

    reagent_ion_source_emission_current_ua = models.IntegerField("Reagent Ion Source Emission Current (uA)", null=True, blank=True)

    reagent_ion_source_electron_energy_v = models.IntegerField("Reagent Ion Source Electron Energy (V)", null=True, blank=True)

    reagent_ion_source_ci_pressure_psi = models.IntegerField("Reagent Ion Source CI Pressure (psi)", null=True, blank=True)

    reagent_vial_1_ion_time = models.IntegerField("Reagent Vial 1 Ion Time", null=True, blank=True)

    reagent_vial_1_agc_target = models.IntegerField("Reagent Vial 1 AGC Target", null=True, blank=True)

    reagent_vial_2_ion_time = models.IntegerField("Reagent Vial 2 Ion Time", null=True, blank=True)

    reagent_vial_2_agc_target = models.IntegerField("Reagent Vial 2 AGC Target", null=True, blank=True)

    supplemental_activation_energy = models.IntegerField("Supplemental Activation Energy", null=True, blank=True)




class MetaCalibrationFileValue(models.Model):


    class Meta:
        verbose_name = "Meta: Calibration File Value"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Meta')

    multiple_rf_frequency = models.FloatField("Multiple RF Frequency", null=True, blank=True)

    main_rf_frequency = models.FloatField("Main RF Frequency", null=True, blank=True)

    qmslope0 = models.FloatField("QMSlope0", null=True, blank=True)

    qmslope1 = models.FloatField("QMSlope1", null=True, blank=True)

    qmslope2 = models.FloatField("QMSlope2", null=True, blank=True)

    qmslope3 = models.FloatField("QMSlope3", null=True, blank=True)

    qmslope4 = models.FloatField("QMSlope4", null=True, blank=True)

    qmint0 = models.FloatField("QMInt0", null=True, blank=True)

    qmint1 = models.FloatField("QMInt1", null=True, blank=True)

    qmint2 = models.FloatField("QMInt2", null=True, blank=True)

    qmint3 = models.FloatField("QMInt3", null=True, blank=True)

    qmint4 = models.FloatField("QMInt4", null=True, blank=True)

    end_section_slope = models.FloatField("End Section Slope", null=True, blank=True)

    end_section_int = models.IntegerField("End Section Int", null=True, blank=True)

    pqd_ce_factor = models.FloatField("PQD CE Factor", null=True, blank=True)

    isow_slope = models.FloatField("IsoW Slope", null=True, blank=True)

    isow_int = models.FloatField("IsoW Int", null=True, blank=True)

    reagent_mp_slope = models.FloatField("Reagent MP Slope", null=True, blank=True)

    reagent_mp_int = models.FloatField("Reagent MP Int", null=True, blank=True)

    tickle_ampdot_slope0 = models.FloatField("Tickle Amp. Slope0", null=True, blank=True)

    tickle_ampdot_int0 = models.FloatField("Tickle Amp. Int0", null=True, blank=True)

    tickle_ampdot_slope1 = models.FloatField("Tickle Amp. Slope1", null=True, blank=True)

    tickle_ampdot_int1 = models.FloatField("Tickle Amp. Int1", null=True, blank=True)

    tickle_ampdot_slope2 = models.FloatField("Tickle Amp. Slope2", null=True, blank=True)

    tickle_ampdot_int2 = models.FloatField("Tickle Amp. Int2", null=True, blank=True)

    tickle_ampdot_slope3 = models.FloatField("Tickle Amp. Slope3", null=True, blank=True)

    tickle_ampdot_int3 = models.FloatField("Tickle Amp. Int3", null=True, blank=True)
    
    multiplier_1_normal_gain = models.FloatField("Multiplier 1 Normal Gain", null=True, blank=True)

    multiplier_1_high_gain = models.FloatField("Multiplier 1 High Gain", null=True, blank=True)

    multiplier_2_normal_gain = models.FloatField("Multiplier 2 Normal Gain", null=True, blank=True)

    multiplier_2_high_gain = models.FloatField("Multiplier 2 High Gain", null=True, blank=True)

    multiplier_1_normal_gain_pos = models.FloatField("Multiplier 1 Normal Gain (pos)", null=True, blank=True)

    multiplier_1_high_gain_pos = models.FloatField("Multiplier 1 High Gain (pos)", null=True, blank=True)

    multiplier_2_normal_gain_pos = models.FloatField("Multiplier 2 Normal Gain (pos)", null=True, blank=True)

    multiplier_2_high_gain_pos = models.FloatField("Multiplier 2 High Gain (pos)", null=True, blank=True)

    multiplier_1_normal_gain_neg = models.FloatField("Multiplier 1 Normal Gain (neg)", null=True, blank=True)

    multiplier_1_high_gain_neg = models.FloatField("Multiplier 1 High Gain (neg)", null=True, blank=True)

    multiplier_2_normal_gain_neg = models.FloatField("Multiplier 2 Normal Gain (neg)", null=True, blank=True)

    multiplier_2_high_gain_neg = models.FloatField("Multiplier 2 High Gain (neg)", null=True, blank=True)

    normal_resdot_eject_slope = models.FloatField("Normal Res. Eject Slope", null=True, blank=True)

    normal_resdot_eject_intercept = models.FloatField("Normal Res. Eject Intercept", null=True, blank=True)

    zoom_resdot_eject_slope = models.FloatField("Zoom Res. Eject Slope", null=True, blank=True)

    zoom_resdot_eject_intercept = models.FloatField("Zoom Res. Eject Intercept", null=True, blank=True)

    turbo_resdot_eject_slope = models.FloatField("Turbo Res. Eject Slope", null=True, blank=True)

    turbo_resdot_eject_intercept = models.IntegerField("Turbo Res. Eject Intercept", null=True, blank=True)

    agc_resdot_eject_slope = models.FloatField("AGC Res. Eject Slope", null=True, blank=True)

    agc_resdot_eject_intercept = models.FloatField("AGC Res. Eject Intercept", null=True, blank=True)

    ultrazoom_resdot_eject_slope = models.FloatField("UltraZoom Res. Eject Slope", null=True, blank=True)

    ultrazoom_resdot_eject_intercept = models.FloatField("UltraZoom Res. Eject Intercept", null=True, blank=True)

    normal_mass_slope = models.FloatField("Normal Mass Slope", null=True, blank=True)

    normal_mass_intercept = models.FloatField("Normal Mass Intercept", null=True, blank=True)

    zoom_mass_slope = models.FloatField("Zoom Mass Slope", null=True, blank=True)

    zoom_mass_intercept = models.FloatField("Zoom Mass Intercept", null=True, blank=True)

    turbo_mass_slope = models.FloatField("Turbo Mass Slope", null=True, blank=True)

    turbo_mass_intercept = models.FloatField("Turbo Mass Intercept", null=True, blank=True)

    agc_mass_slope = models.FloatField("AGC Mass Slope", null=True, blank=True)

    agc_mass_intercept = models.FloatField("AGC Mass Intercept", null=True, blank=True)

    ultrazoom_mass_slope = models.FloatField("UltraZoom Mass Slope", null=True, blank=True)

    ultrazoom_mass_intercept = models.FloatField("UltraZoom Mass Intercept", null=True, blank=True)

    vernier_fine_mass_slope = models.FloatField("Vernier Fine Mass Slope", null=True, blank=True)

    vernier_fine_mass_intercept = models.FloatField("Vernier Fine Mass Intercept", null=True, blank=True)

    vernier_coarse_mass_slope = models.FloatField("Vernier Coarse Mass Slope", null=True, blank=True)

    vernier_coarse_mass_intercept = models.FloatField("Vernier Coarse Mass Intercept", null=True, blank=True)

    capdot_device_min_v = models.FloatField("Cap. Device Min (V)", null=True, blank=True)

    capdot_device_max_v = models.FloatField("Cap.  Device Max (V)", null=True, blank=True)

    tube_lens_device_min_v = models.FloatField("Tube Lens Device Min (V)", null=True, blank=True)

    tube_lens_device_max_v = models.FloatField("Tube Lens  Device Max (V)", null=True, blank=True)

    skimmer_device_min_v = models.FloatField("Skimmer Device Min (V)", null=True, blank=True)

    skimmer_device_max_v = models.FloatField("Skimmer Device Max (V)", null=True, blank=True)

    multipole_00_device_min_v = models.FloatField("Multipole 00 Device Min (V)", null=True, blank=True)

    multipole_00_device_max_v = models.FloatField("Multipole 00 Device Max (V)", null=True, blank=True)

    lens_0_device_min_v = models.FloatField("Lens 0 Device Min (V)", null=True, blank=True)

    lens_0_device_max_v = models.FloatField("Lens 0 Device Max (V)", null=True, blank=True)

    gate_lens_device_min_v = models.FloatField("Gate Lens Device Min (V)", null=True, blank=True)

    gate_lens_device_max_v = models.FloatField("Gate Lens Device Max (V)", null=True, blank=True)

    split_gate_device_min_v = models.FloatField("Split Gate Device Min (V)", null=True, blank=True)

    split_gate_device_max_v = models.FloatField("Split Gate Device Max (V)", null=True, blank=True)

    multipole_0_device_min_v = models.FloatField("Multipole 0 Device Min (V)", null=True, blank=True)

    multipole_0_device_max_v = models.FloatField("Multipole 0 Device Max (V)", null=True, blank=True)

    lens_1_device_min_v = models.FloatField("Lens 1 Device Min (V)", null=True, blank=True)

    lens_1_device_max_v = models.FloatField("Lens 1 Device Max (V)", null=True, blank=True)

    multipole_1_device_min_v = models.FloatField("Multipole 1 Device Min (V)", null=True, blank=True)

    multipole_1_device_max_v = models.FloatField("Multipole 1 Device Max (V)", null=True, blank=True)

    front_lens_device_min_v = models.FloatField("Front Lens Device Min (V)", null=True, blank=True)

    front_lens_device_max_v = models.FloatField("Front Lens Device Max (V)", null=True, blank=True)

    front_section_device_min_v = models.FloatField("Front Section Device Min (V)", null=True, blank=True)

    front_section_device_max_v = models.FloatField("Front Section Device Max (V)", null=True, blank=True)

    center_section_device_min_v = models.FloatField("Center Section Device Min (V)", null=True, blank=True)

    center_section_device_max_v = models.FloatField("Center Section Device Max (V)", null=True, blank=True)

    back_section_device_min_v = models.FloatField("Back Section Device Min (V)", null=True, blank=True)

    back_section_device_max_v = models.FloatField("Back Section Device Max (V)", null=True, blank=True)

    back_lens_device_min_v = models.FloatField("Back Lens Device Min (V)", null=True, blank=True)

    back_lens_device_max_v = models.FloatField("Back Lens Device Max (V)", null=True, blank=True)

    reagent_lens_1_device_min_v = models.FloatField("Reagent Lens 1 Device Min (V)", null=True, blank=True)

    reagent_lens_1_device_max_v = models.FloatField("Reagent Lens 1 Device Max (V)", null=True, blank=True)

    reagent_gate_lens_min_v = models.FloatField("Reagent Gate Lens Min (V)", null=True, blank=True)

    reagent_gate_lens_max_v = models.FloatField("Reagent Gate Lens Max (V)", null=True, blank=True)

    reagent_lens_2_device_min_v = models.FloatField("Reagent Lens 2 Device Min (V)", null=True, blank=True)

    reagent_lens_2_device_max_v = models.FloatField("Reagent Lens 2 Device Max (V)", null=True, blank=True)

    reagent_lens_3_device_min_v = models.FloatField("Reagent Lens 3 Device Min (V)", null=True, blank=True)

    reagent_lens_3_device_max_v = models.FloatField("Reagent Lens 3 Device Max (V)", null=True, blank=True)

    reagent_electron_lens_device_min_v = models.FloatField("Reagent Electron Lens Device Min (V)", null=True, blank=True)

    reagent_electron_lens_device_max_v = models.FloatField("Reagent Electron Lens Device Max (V)", null=True, blank=True)

    center_lens_highlow_transfer_pos_v = models.FloatField("Center Lens High-Low Transfer (pos) (V)", null=True, blank=True)

    back_section_highlow_transfer_pos_v = models.FloatField("Back Section High-Low Transfer (pos) (V)", null=True, blank=True)

    center_lens_highlow_transfer_neg_v = models.FloatField("Center Lens High-Low Transfer (neg) (V)", null=True, blank=True)

    back_section_highlow_transfer_neg_v = models.FloatField("Back Section High-Low Transfer (neg) (V)", null=True, blank=True)

    center_lens_lowhigh_transfer_pos_v = models.FloatField("Center Lens Low-High Transfer (pos) (V)", null=True, blank=True)

    front_section_lowhigh_transfer_pos_v = models.FloatField("Front Section Low-High Transfer (pos) (V)", null=True, blank=True)

    center_lens_lowhigh_transfer_neg_v = models.FloatField("Center Lens Low-High Transfer (neg) (V)", null=True, blank=True)

    front_section_lowhigh_transfer_neg_v = models.FloatField("Front Section Low-High Transfer (neg) (V)", null=True, blank=True)

    scan_phase_0 = models.FloatField("Scan Phase 0", null=True, blank=True)

    scan_phase_1 = models.FloatField("Scan Phase 1", null=True, blank=True)

    scan_phase_2 = models.FloatField("Scan Phase 2", null=True, blank=True)

    scan_phase_3 = models.FloatField("Scan Phase 3", null=True, blank=True)

    scan_phase_4 = models.FloatField("Scan Phase 4", null=True, blank=True)

    scan_phase_5 = models.FloatField("Scan Phase 5", null=True, blank=True)

    scan_phase_6 = models.FloatField("Scan Phase 6", null=True, blank=True)

    scan_phase_7 = models.FloatField("Scan Phase 7", null=True, blank=True)

    scan_phase_8 = models.FloatField("Scan Phase 8", null=True, blank=True)

    scan_phase_9 = models.FloatField("Scan Phase 9", null=True, blank=True)

    scan_phase_10 = models.FloatField("Scan Phase 10", null=True, blank=True)

    scan_phase_11 = models.FloatField("Scan Phase 11", null=True, blank=True)
    
    scan_phase_12 = models.IntegerField("Scan Phase 12", null=True, blank=True)
    
    multiplier_1_res_ej_phase_pos = models.FloatField("Multiplier 1 Res Ej Phase (pos)", null=True, blank=True)

    multiplier_2_res_ej_phase_pos = models.FloatField("Multiplier 2 Res Ej Phase (pos)", null=True, blank=True)

    multiplier_1_res_ej_phase_neg = models.FloatField("Multiplier 1 Res Ej Phase (neg)", null=True, blank=True)

    multiplier_2_res_ej_phase_neg = models.FloatField("Multiplier 2 Res Ej Phase (neg)", null=True, blank=True)

    center_lens_lpt_device_min_v = models.FloatField("Center Lens LPT Device Min (V)", null=True, blank=True)

    center_lens_lpt_device_max_v = models.FloatField("Center Lens LPT Device Max (V)", null=True, blank=True)

    front_section_lpt_device_min_v = models.FloatField("Front Section LPT Device Min (V)", null=True, blank=True)

    front_section_lpt_device_max_v = models.FloatField("Front Section LPT Device Max (V)", null=True, blank=True)

    center_section_lpt_device_min_v = models.FloatField("Center Section LPT Device Min (V)", null=True, blank=True)

    center_section_lpt_device_max_v = models.FloatField("Center Section LPT Device Max (V)", null=True, blank=True)

    back_section_lpt_device_min_v = models.FloatField("Back Section LPT Device Min (V)", null=True, blank=True)

    back_section_lpt_device_max_v = models.FloatField("Back Section LPT Device Max (V)", null=True, blank=True)




class MetaCalibrationFileValueResEject(models.Model):


    class Meta:
        verbose_name = "Meta: Calibration File Value ResEject"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Meta')

    resdot_eject_slope_0_0 = models.FloatField("Res. Eject Slope[0][0]", null=True, blank=True)

    resdot_eject_intercept_0_0 = models.FloatField("Res. Eject Intercept[0][0]", null=True, blank=True)

    resdot_eject_slope_0_1 = models.FloatField("Res. Eject Slope[0][1]", null=True, blank=True)

    resdot_eject_intercept_0_1 = models.FloatField("Res. Eject Intercept[0][1]", null=True, blank=True)

    resdot_eject_slope_0_2 = models.FloatField("Res. Eject Slope[0][2]", null=True, blank=True)

    resdot_eject_intercept_0_2 = models.FloatField("Res. Eject Intercept[0][2]", null=True, blank=True)

    resdot_eject_slope_0_3 = models.FloatField("Res. Eject Slope[0][3]", null=True, blank=True)

    resdot_eject_intercept_0_3 = models.FloatField("Res. Eject Intercept[0][3]", null=True, blank=True)

    resdot_eject_slope_0_4 = models.FloatField("Res. Eject Slope[0][4]", null=True, blank=True)

    resdot_eject_intercept_0_4 = models.FloatField("Res. Eject Intercept[0][4]", null=True, blank=True)

    resdot_eject_slope_0_5 = models.FloatField("Res. Eject Slope[0][5]", null=True, blank=True)

    resdot_eject_intercept_0_5 = models.FloatField("Res. Eject Intercept[0][5]", null=True, blank=True)

    resdot_eject_slope_0_6 = models.FloatField("Res. Eject Slope[0][6]", null=True, blank=True)

    resdot_eject_intercept_0_6 = models.FloatField("Res. Eject Intercept[0][6]", null=True, blank=True)

    resdot_eject_slope_0_7 = models.FloatField("Res. Eject Slope[0][7]", null=True, blank=True)

    resdot_eject_intercept_0_7 = models.FloatField("Res. Eject Intercept[0][7]", null=True, blank=True)

    resdot_eject_slope_0_8 = models.FloatField("Res. Eject Slope[0][8]", null=True, blank=True)

    resdot_eject_intercept_0_8 = models.FloatField("Res. Eject Intercept[0][8]", null=True, blank=True)

    resdot_eject_slope_0_9 = models.FloatField("Res. Eject Slope[0][9]", null=True, blank=True)

    resdot_eject_intercept_0_9 = models.FloatField("Res. Eject Intercept[0][9]", null=True, blank=True)

    resdot_eject_slope_0_10 = models.FloatField("Res. Eject Slope[0][10]", null=True, blank=True)

    resdot_eject_intercept_0_10 = models.FloatField("Res. Eject Intercept[0][10]", null=True, blank=True)

    resdot_eject_slope_0_11 = models.FloatField("Res. Eject Slope[0][11]", null=True, blank=True)

    resdot_eject_intercept_0_11 = models.FloatField("Res. Eject Intercept[0][11]", null=True, blank=True)

    resdot_eject_slope_0_12 = models.FloatField("Res. Eject Slope[0][12]", null=True, blank=True)

    resdot_eject_intercept_0_12 = models.FloatField("Res. Eject Intercept[0][12]", null=True, blank=True)

    resdot_eject_slope_0_13 = models.FloatField("Res. Eject Slope[0][13]", null=True, blank=True)

    resdot_eject_intercept_0_13 = models.FloatField("Res. Eject Intercept[0][13]", null=True, blank=True)

    resdot_eject_slope_0_14 = models.FloatField("Res. Eject Slope[0][14]", null=True, blank=True)

    resdot_eject_intercept_0_14 = models.FloatField("Res. Eject Intercept[0][14]", null=True, blank=True)

    resdot_eject_slope_0_15 = models.FloatField("Res. Eject Slope[0][15]", null=True, blank=True)

    resdot_eject_intercept_0_15 = models.FloatField("Res. Eject Intercept[0][15]", null=True, blank=True)

    resdot_eject_slope_0_16 = models.FloatField("Res. Eject Slope[0][16]", null=True, blank=True)

    resdot_eject_intercept_0_16 = models.FloatField("Res. Eject Intercept[0][16]", null=True, blank=True)

    resdot_eject_slope_0_17 = models.FloatField("Res. Eject Slope[0][17]", null=True, blank=True)

    resdot_eject_intercept_0_17 = models.FloatField("Res. Eject Intercept[0][17]", null=True, blank=True)

    resdot_eject_slope_0_18 = models.FloatField("Res. Eject Slope[0][18]", null=True, blank=True)

    resdot_eject_intercept_0_18 = models.FloatField("Res. Eject Intercept[0][18]", null=True, blank=True)

    resdot_eject_slope_0_19 = models.FloatField("Res. Eject Slope[0][19]", null=True, blank=True)

    resdot_eject_intercept_0_19 = models.FloatField("Res. Eject Intercept[0][19]", null=True, blank=True)

    resdot_eject_slope_1_0 = models.FloatField("Res. Eject Slope[1][0]", null=True, blank=True)

    resdot_eject_intercept_1_0 = models.FloatField("Res. Eject Intercept[1][0]", null=True, blank=True)

    resdot_eject_slope_1_1 = models.FloatField("Res. Eject Slope[1][1]", null=True, blank=True)

    resdot_eject_intercept_1_1 = models.FloatField("Res. Eject Intercept[1][1]", null=True, blank=True)

    resdot_eject_slope_1_2 = models.FloatField("Res. Eject Slope[1][2]", null=True, blank=True)

    resdot_eject_intercept_1_2 = models.FloatField("Res. Eject Intercept[1][2]", null=True, blank=True)

    resdot_eject_slope_1_3 = models.FloatField("Res. Eject Slope[1][3]", null=True, blank=True)

    resdot_eject_intercept_1_3 = models.FloatField("Res. Eject Intercept[1][3]", null=True, blank=True)

    resdot_eject_slope_1_4 = models.FloatField("Res. Eject Slope[1][4]", null=True, blank=True)

    resdot_eject_intercept_1_4 = models.FloatField("Res. Eject Intercept[1][4]", null=True, blank=True)

    resdot_eject_slope_1_5 = models.FloatField("Res. Eject Slope[1][5]", null=True, blank=True)

    resdot_eject_intercept_1_5 = models.FloatField("Res. Eject Intercept[1][5]", null=True, blank=True)

    resdot_eject_slope_1_6 = models.FloatField("Res. Eject Slope[1][6]", null=True, blank=True)

    resdot_eject_intercept_1_6 = models.FloatField("Res. Eject Intercept[1][6]", null=True, blank=True)

    resdot_eject_slope_1_7 = models.FloatField("Res. Eject Slope[1][7]", null=True, blank=True)

    resdot_eject_intercept_1_7 = models.FloatField("Res. Eject Intercept[1][7]", null=True, blank=True)

    resdot_eject_slope_1_8 = models.FloatField("Res. Eject Slope[1][8]", null=True, blank=True)

    resdot_eject_intercept_1_8 = models.FloatField("Res. Eject Intercept[1][8]", null=True, blank=True)

    resdot_eject_slope_1_9 = models.FloatField("Res. Eject Slope[1][9]", null=True, blank=True)

    resdot_eject_intercept_1_9 = models.FloatField("Res. Eject Intercept[1][9]", null=True, blank=True)

    resdot_eject_slope_1_10 = models.FloatField("Res. Eject Slope[1][10]", null=True, blank=True)

    resdot_eject_intercept_1_10 = models.FloatField("Res. Eject Intercept[1][10]", null=True, blank=True)

    resdot_eject_slope_1_11 = models.FloatField("Res. Eject Slope[1][11]", null=True, blank=True)

    resdot_eject_intercept_1_11 = models.FloatField("Res. Eject Intercept[1][11]", null=True, blank=True)

    resdot_eject_slope_1_12 = models.FloatField("Res. Eject Slope[1][12]", null=True, blank=True)

    resdot_eject_intercept_1_12 = models.FloatField("Res. Eject Intercept[1][12]", null=True, blank=True)

    resdot_eject_slope_1_13 = models.FloatField("Res. Eject Slope[1][13]", null=True, blank=True)

    resdot_eject_intercept_1_13 = models.FloatField("Res. Eject Intercept[1][13]", null=True, blank=True)

    resdot_eject_slope_1_14 = models.FloatField("Res. Eject Slope[1][14]", null=True, blank=True)

    resdot_eject_intercept_1_14 = models.FloatField("Res. Eject Intercept[1][14]", null=True, blank=True)

    resdot_eject_slope_1_15 = models.FloatField("Res. Eject Slope[1][15]", null=True, blank=True)

    resdot_eject_intercept_1_15 = models.FloatField("Res. Eject Intercept[1][15]", null=True, blank=True)

    resdot_eject_slope_1_16 = models.FloatField("Res. Eject Slope[1][16]", null=True, blank=True)

    resdot_eject_intercept_1_16 = models.FloatField("Res. Eject Intercept[1][16]", null=True, blank=True)

    resdot_eject_slope_1_17 = models.FloatField("Res. Eject Slope[1][17]", null=True, blank=True)

    resdot_eject_intercept_1_17 = models.FloatField("Res. Eject Intercept[1][17]", null=True, blank=True)

    resdot_eject_slope_1_18 = models.FloatField("Res. Eject Slope[1][18]", null=True, blank=True)

    resdot_eject_intercept_1_18 = models.FloatField("Res. Eject Intercept[1][18]", null=True, blank=True)

    resdot_eject_slope_1_19 = models.FloatField("Res. Eject Slope[1][19]", null=True, blank=True)

    resdot_eject_intercept_1_19 = models.FloatField("Res. Eject Intercept[1][19]", null=True, blank=True)

    resdot_eject_slope_2_0 = models.FloatField("Res. Eject Slope[2][0]", null=True, blank=True)

    resdot_eject_intercept_2_0 = models.FloatField("Res. Eject Intercept[2][0]", null=True, blank=True)

    resdot_eject_slope_2_1 = models.FloatField("Res. Eject Slope[2][1]", null=True, blank=True)

    resdot_eject_intercept_2_1 = models.FloatField("Res. Eject Intercept[2][1]", null=True, blank=True)

    resdot_eject_slope_2_2 = models.FloatField("Res. Eject Slope[2][2]", null=True, blank=True)

    resdot_eject_intercept_2_2 = models.FloatField("Res. Eject Intercept[2][2]", null=True, blank=True)

    resdot_eject_slope_2_3 = models.FloatField("Res. Eject Slope[2][3]", null=True, blank=True)

    resdot_eject_intercept_2_3 = models.FloatField("Res. Eject Intercept[2][3]", null=True, blank=True)

    resdot_eject_slope_2_4 = models.FloatField("Res. Eject Slope[2][4]", null=True, blank=True)

    resdot_eject_intercept_2_4 = models.FloatField("Res. Eject Intercept[2][4]", null=True, blank=True)

    resdot_eject_slope_2_5 = models.FloatField("Res. Eject Slope[2][5]", null=True, blank=True)

    resdot_eject_intercept_2_5 = models.FloatField("Res. Eject Intercept[2][5]", null=True, blank=True)

    resdot_eject_slope_2_6 = models.FloatField("Res. Eject Slope[2][6]", null=True, blank=True)

    resdot_eject_intercept_2_6 = models.FloatField("Res. Eject Intercept[2][6]", null=True, blank=True)

    resdot_eject_slope_2_7 = models.FloatField("Res. Eject Slope[2][7]", null=True, blank=True)

    resdot_eject_intercept_2_7 = models.FloatField("Res. Eject Intercept[2][7]", null=True, blank=True)

    resdot_eject_slope_2_8 = models.FloatField("Res. Eject Slope[2][8]", null=True, blank=True)

    resdot_eject_intercept_2_8 = models.FloatField("Res. Eject Intercept[2][8]", null=True, blank=True)

    resdot_eject_slope_2_9 = models.FloatField("Res. Eject Slope[2][9]", null=True, blank=True)

    resdot_eject_intercept_2_9 = models.FloatField("Res. Eject Intercept[2][9]", null=True, blank=True)

    resdot_eject_slope_2_10 = models.FloatField("Res. Eject Slope[2][10]", null=True, blank=True)

    resdot_eject_intercept_2_10 = models.FloatField("Res. Eject Intercept[2][10]", null=True, blank=True)

    resdot_eject_slope_2_11 = models.FloatField("Res. Eject Slope[2][11]", null=True, blank=True)

    resdot_eject_intercept_2_11 = models.FloatField("Res. Eject Intercept[2][11]", null=True, blank=True)

    resdot_eject_slope_2_12 = models.FloatField("Res. Eject Slope[2][12]", null=True, blank=True)

    resdot_eject_intercept_2_12 = models.FloatField("Res. Eject Intercept[2][12]", null=True, blank=True)

    resdot_eject_slope_2_13 = models.FloatField("Res. Eject Slope[2][13]", null=True, blank=True)

    resdot_eject_intercept_2_13 = models.FloatField("Res. Eject Intercept[2][13]", null=True, blank=True)

    resdot_eject_slope_2_14 = models.FloatField("Res. Eject Slope[2][14]", null=True, blank=True)

    resdot_eject_intercept_2_14 = models.FloatField("Res. Eject Intercept[2][14]", null=True, blank=True)

    resdot_eject_slope_2_15 = models.FloatField("Res. Eject Slope[2][15]", null=True, blank=True)

    resdot_eject_intercept_2_15 = models.FloatField("Res. Eject Intercept[2][15]", null=True, blank=True)

    resdot_eject_slope_2_16 = models.FloatField("Res. Eject Slope[2][16]", null=True, blank=True)

    resdot_eject_intercept_2_16 = models.FloatField("Res. Eject Intercept[2][16]", null=True, blank=True)

    resdot_eject_slope_2_17 = models.FloatField("Res. Eject Slope[2][17]", null=True, blank=True)

    resdot_eject_intercept_2_17 = models.FloatField("Res. Eject Intercept[2][17]", null=True, blank=True)

    resdot_eject_slope_2_18 = models.FloatField("Res. Eject Slope[2][18]", null=True, blank=True)

    resdot_eject_intercept_2_18 = models.FloatField("Res. Eject Intercept[2][18]", null=True, blank=True)

    resdot_eject_slope_2_19 = models.FloatField("Res. Eject Slope[2][19]", null=True, blank=True)

    resdot_eject_intercept_2_19 = models.FloatField("Res. Eject Intercept[2][19]", null=True, blank=True)

    resdot_eject_slope_3_0 = models.FloatField("Res. Eject Slope[3][0]", null=True, blank=True)

    resdot_eject_intercept_3_0 = models.FloatField("Res. Eject Intercept[3][0]", null=True, blank=True)

    resdot_eject_slope_3_1 = models.FloatField("Res. Eject Slope[3][1]", null=True, blank=True)

    resdot_eject_intercept_3_1 = models.FloatField("Res. Eject Intercept[3][1]", null=True, blank=True)

    resdot_eject_slope_3_2 = models.FloatField("Res. Eject Slope[3][2]", null=True, blank=True)

    resdot_eject_intercept_3_2 = models.FloatField("Res. Eject Intercept[3][2]", null=True, blank=True)

    resdot_eject_slope_3_3 = models.FloatField("Res. Eject Slope[3][3]", null=True, blank=True)

    resdot_eject_intercept_3_3 = models.FloatField("Res. Eject Intercept[3][3]", null=True, blank=True)

    resdot_eject_slope_3_4 = models.FloatField("Res. Eject Slope[3][4]", null=True, blank=True)

    resdot_eject_intercept_3_4 = models.FloatField("Res. Eject Intercept[3][4]", null=True, blank=True)

    resdot_eject_slope_3_5 = models.FloatField("Res. Eject Slope[3][5]", null=True, blank=True)

    resdot_eject_intercept_3_5 = models.FloatField("Res. Eject Intercept[3][5]", null=True, blank=True)

    resdot_eject_slope_3_6 = models.FloatField("Res. Eject Slope[3][6]", null=True, blank=True)

    resdot_eject_intercept_3_6 = models.FloatField("Res. Eject Intercept[3][6]", null=True, blank=True)

    resdot_eject_slope_3_7 = models.FloatField("Res. Eject Slope[3][7]", null=True, blank=True)

    resdot_eject_intercept_3_7 = models.FloatField("Res. Eject Intercept[3][7]", null=True, blank=True)

    resdot_eject_slope_3_8 = models.FloatField("Res. Eject Slope[3][8]", null=True, blank=True)

    resdot_eject_intercept_3_8 = models.FloatField("Res. Eject Intercept[3][8]", null=True, blank=True)

    resdot_eject_slope_3_9 = models.FloatField("Res. Eject Slope[3][9]", null=True, blank=True)

    resdot_eject_intercept_3_9 = models.FloatField("Res. Eject Intercept[3][9]", null=True, blank=True)

    resdot_eject_slope_3_10 = models.FloatField("Res. Eject Slope[3][10]", null=True, blank=True)

    resdot_eject_intercept_3_10 = models.FloatField("Res. Eject Intercept[3][10]", null=True, blank=True)

    resdot_eject_slope_3_11 = models.FloatField("Res. Eject Slope[3][11]", null=True, blank=True)

    resdot_eject_intercept_3_11 = models.FloatField("Res. Eject Intercept[3][11]", null=True, blank=True)

    resdot_eject_slope_3_12 = models.FloatField("Res. Eject Slope[3][12]", null=True, blank=True)

    resdot_eject_intercept_3_12 = models.FloatField("Res. Eject Intercept[3][12]", null=True, blank=True)

    resdot_eject_slope_3_13 = models.FloatField("Res. Eject Slope[3][13]", null=True, blank=True)

    resdot_eject_intercept_3_13 = models.FloatField("Res. Eject Intercept[3][13]", null=True, blank=True)

    resdot_eject_slope_3_14 = models.FloatField("Res. Eject Slope[3][14]", null=True, blank=True)

    resdot_eject_intercept_3_14 = models.FloatField("Res. Eject Intercept[3][14]", null=True, blank=True)

    resdot_eject_slope_3_15 = models.FloatField("Res. Eject Slope[3][15]", null=True, blank=True)

    resdot_eject_intercept_3_15 = models.FloatField("Res. Eject Intercept[3][15]", null=True, blank=True)

    resdot_eject_slope_3_16 = models.FloatField("Res. Eject Slope[3][16]", null=True, blank=True)

    resdot_eject_intercept_3_16 = models.FloatField("Res. Eject Intercept[3][16]", null=True, blank=True)

    resdot_eject_slope_3_17 = models.FloatField("Res. Eject Slope[3][17]", null=True, blank=True)

    resdot_eject_intercept_3_17 = models.FloatField("Res. Eject Intercept[3][17]", null=True, blank=True)

    resdot_eject_slope_3_18 = models.FloatField("Res. Eject Slope[3][18]", null=True, blank=True)

    resdot_eject_intercept_3_18 = models.FloatField("Res. Eject Intercept[3][18]", null=True, blank=True)

    resdot_eject_slope_3_19 = models.FloatField("Res. Eject Slope[3][19]", null=True, blank=True)

    resdot_eject_intercept_3_19 = models.FloatField("Res. Eject Intercept[3][19]", null=True, blank=True)

    resdot_eject_slope_4_0 = models.FloatField("Res. Eject Slope[4][0]", null=True, blank=True)

    resdot_eject_intercept_4_0 = models.FloatField("Res. Eject Intercept[4][0]", null=True, blank=True)

    resdot_eject_slope_4_1 = models.FloatField("Res. Eject Slope[4][1]", null=True, blank=True)

    resdot_eject_intercept_4_1 = models.FloatField("Res. Eject Intercept[4][1]", null=True, blank=True)

    resdot_eject_slope_4_2 = models.FloatField("Res. Eject Slope[4][2]", null=True, blank=True)

    resdot_eject_intercept_4_2 = models.FloatField("Res. Eject Intercept[4][2]", null=True, blank=True)

    resdot_eject_slope_4_3 = models.FloatField("Res. Eject Slope[4][3]", null=True, blank=True)

    resdot_eject_intercept_4_3 = models.FloatField("Res. Eject Intercept[4][3]", null=True, blank=True)

    resdot_eject_slope_4_4 = models.FloatField("Res. Eject Slope[4][4]", null=True, blank=True)

    resdot_eject_intercept_4_4 = models.FloatField("Res. Eject Intercept[4][4]", null=True, blank=True)

    resdot_eject_slope_4_5 = models.FloatField("Res. Eject Slope[4][5]", null=True, blank=True)

    resdot_eject_intercept_4_5 = models.FloatField("Res. Eject Intercept[4][5]", null=True, blank=True)

    resdot_eject_slope_4_6 = models.FloatField("Res. Eject Slope[4][6]", null=True, blank=True)

    resdot_eject_intercept_4_6 = models.FloatField("Res. Eject Intercept[4][6]", null=True, blank=True)

    resdot_eject_slope_4_7 = models.FloatField("Res. Eject Slope[4][7]", null=True, blank=True)

    resdot_eject_intercept_4_7 = models.FloatField("Res. Eject Intercept[4][7]", null=True, blank=True)

    resdot_eject_slope_4_8 = models.FloatField("Res. Eject Slope[4][8]", null=True, blank=True)

    resdot_eject_intercept_4_8 = models.FloatField("Res. Eject Intercept[4][8]", null=True, blank=True)

    resdot_eject_slope_4_9 = models.FloatField("Res. Eject Slope[4][9]", null=True, blank=True)

    resdot_eject_intercept_4_9 = models.FloatField("Res. Eject Intercept[4][9]", null=True, blank=True)

    resdot_eject_slope_4_10 = models.FloatField("Res. Eject Slope[4][10]", null=True, blank=True)

    resdot_eject_intercept_4_10 = models.FloatField("Res. Eject Intercept[4][10]", null=True, blank=True)

    resdot_eject_slope_4_11 = models.FloatField("Res. Eject Slope[4][11]", null=True, blank=True)

    resdot_eject_intercept_4_11 = models.FloatField("Res. Eject Intercept[4][11]", null=True, blank=True)

    resdot_eject_slope_4_12 = models.FloatField("Res. Eject Slope[4][12]", null=True, blank=True)

    resdot_eject_intercept_4_12 = models.FloatField("Res. Eject Intercept[4][12]", null=True, blank=True)

    resdot_eject_slope_4_13 = models.FloatField("Res. Eject Slope[4][13]", null=True, blank=True)

    resdot_eject_intercept_4_13 = models.FloatField("Res. Eject Intercept[4][13]", null=True, blank=True)

    resdot_eject_slope_4_14 = models.FloatField("Res. Eject Slope[4][14]", null=True, blank=True)

    resdot_eject_intercept_4_14 = models.FloatField("Res. Eject Intercept[4][14]", null=True, blank=True)

    resdot_eject_slope_4_15 = models.FloatField("Res. Eject Slope[4][15]", null=True, blank=True)

    resdot_eject_intercept_4_15 = models.FloatField("Res. Eject Intercept[4][15]", null=True, blank=True)

    resdot_eject_slope_4_16 = models.FloatField("Res. Eject Slope[4][16]", null=True, blank=True)

    resdot_eject_intercept_4_16 = models.FloatField("Res. Eject Intercept[4][16]", null=True, blank=True)

    resdot_eject_slope_4_17 = models.FloatField("Res. Eject Slope[4][17]", null=True, blank=True)

    resdot_eject_intercept_4_17 = models.FloatField("Res. Eject Intercept[4][17]", null=True, blank=True)

    resdot_eject_slope_4_18 = models.FloatField("Res. Eject Slope[4][18]", null=True, blank=True)

    resdot_eject_intercept_4_18 = models.FloatField("Res. Eject Intercept[4][18]", null=True, blank=True)

    resdot_eject_slope_4_19 = models.FloatField("Res. Eject Slope[4][19]", null=True, blank=True)

    resdot_eject_intercept_4_19 = models.FloatField("Res. Eject Intercept[4][19]", null=True, blank=True)

    resdot_eject_slope_5_0 = models.FloatField("Res. Eject Slope[5][0]", null=True, blank=True)

    resdot_eject_intercept_5_0 = models.FloatField("Res. Eject Intercept[5][0]", null=True, blank=True)

    resdot_eject_slope_5_1 = models.FloatField("Res. Eject Slope[5][1]", null=True, blank=True)

    resdot_eject_intercept_5_1 = models.FloatField("Res. Eject Intercept[5][1]", null=True, blank=True)

    resdot_eject_slope_5_2 = models.FloatField("Res. Eject Slope[5][2]", null=True, blank=True)

    resdot_eject_intercept_5_2 = models.FloatField("Res. Eject Intercept[5][2]", null=True, blank=True)

    resdot_eject_slope_5_3 = models.FloatField("Res. Eject Slope[5][3]", null=True, blank=True)

    resdot_eject_intercept_5_3 = models.FloatField("Res. Eject Intercept[5][3]", null=True, blank=True)

    resdot_eject_slope_5_4 = models.FloatField("Res. Eject Slope[5][4]", null=True, blank=True)

    resdot_eject_intercept_5_4 = models.FloatField("Res. Eject Intercept[5][4]", null=True, blank=True)

    resdot_eject_slope_5_5 = models.FloatField("Res. Eject Slope[5][5]", null=True, blank=True)

    resdot_eject_intercept_5_5 = models.FloatField("Res. Eject Intercept[5][5]", null=True, blank=True)

    resdot_eject_slope_5_6 = models.FloatField("Res. Eject Slope[5][6]", null=True, blank=True)

    resdot_eject_intercept_5_6 = models.FloatField("Res. Eject Intercept[5][6]", null=True, blank=True)

    resdot_eject_slope_5_7 = models.FloatField("Res. Eject Slope[5][7]", null=True, blank=True)

    resdot_eject_intercept_5_7 = models.FloatField("Res. Eject Intercept[5][7]", null=True, blank=True)

    resdot_eject_slope_5_8 = models.FloatField("Res. Eject Slope[5][8]", null=True, blank=True)

    resdot_eject_intercept_5_8 = models.FloatField("Res. Eject Intercept[5][8]", null=True, blank=True)

    resdot_eject_slope_5_9 = models.FloatField("Res. Eject Slope[5][9]", null=True, blank=True)

    resdot_eject_intercept_5_9 = models.FloatField("Res. Eject Intercept[5][9]", null=True, blank=True)

    resdot_eject_slope_5_10 = models.FloatField("Res. Eject Slope[5][10]", null=True, blank=True)

    resdot_eject_intercept_5_10 = models.FloatField("Res. Eject Intercept[5][10]", null=True, blank=True)

    resdot_eject_slope_5_11 = models.FloatField("Res. Eject Slope[5][11]", null=True, blank=True)

    resdot_eject_intercept_5_11 = models.FloatField("Res. Eject Intercept[5][11]", null=True, blank=True)

    resdot_eject_slope_5_12 = models.FloatField("Res. Eject Slope[5][12]", null=True, blank=True)

    resdot_eject_intercept_5_12 = models.FloatField("Res. Eject Intercept[5][12]", null=True, blank=True)

    resdot_eject_slope_5_13 = models.FloatField("Res. Eject Slope[5][13]", null=True, blank=True)

    resdot_eject_intercept_5_13 = models.FloatField("Res. Eject Intercept[5][13]", null=True, blank=True)

    resdot_eject_slope_5_14 = models.FloatField("Res. Eject Slope[5][14]", null=True, blank=True)

    resdot_eject_intercept_5_14 = models.FloatField("Res. Eject Intercept[5][14]", null=True, blank=True)

    resdot_eject_slope_5_15 = models.FloatField("Res. Eject Slope[5][15]", null=True, blank=True)

    resdot_eject_intercept_5_15 = models.FloatField("Res. Eject Intercept[5][15]", null=True, blank=True)

    resdot_eject_slope_5_16 = models.FloatField("Res. Eject Slope[5][16]", null=True, blank=True)

    resdot_eject_intercept_5_16 = models.FloatField("Res. Eject Intercept[5][16]", null=True, blank=True)

    resdot_eject_slope_5_17 = models.FloatField("Res. Eject Slope[5][17]", null=True, blank=True)

    resdot_eject_intercept_5_17 = models.FloatField("Res. Eject Intercept[5][17]", null=True, blank=True)

    resdot_eject_slope_5_18 = models.FloatField("Res. Eject Slope[5][18]", null=True, blank=True)

    resdot_eject_intercept_5_18 = models.FloatField("Res. Eject Intercept[5][18]", null=True, blank=True)

    resdot_eject_slope_5_19 = models.FloatField("Res. Eject Slope[5][19]", null=True, blank=True)

    resdot_eject_intercept_5_19 = models.FloatField("Res. Eject Intercept[5][19]", null=True, blank=True)

    resdot_eject_slope_6_0 = models.FloatField("Res. Eject Slope[6][0]", null=True, blank=True)

    resdot_eject_intercept_6_0 = models.FloatField("Res. Eject Intercept[6][0]", null=True, blank=True)

    resdot_eject_slope_6_1 = models.FloatField("Res. Eject Slope[6][1]", null=True, blank=True)

    resdot_eject_intercept_6_1 = models.FloatField("Res. Eject Intercept[6][1]", null=True, blank=True)

    resdot_eject_slope_6_2 = models.FloatField("Res. Eject Slope[6][2]", null=True, blank=True)

    resdot_eject_intercept_6_2 = models.FloatField("Res. Eject Intercept[6][2]", null=True, blank=True)

    resdot_eject_slope_6_3 = models.FloatField("Res. Eject Slope[6][3]", null=True, blank=True)

    resdot_eject_intercept_6_3 = models.FloatField("Res. Eject Intercept[6][3]", null=True, blank=True)

    resdot_eject_slope_6_4 = models.FloatField("Res. Eject Slope[6][4]", null=True, blank=True)

    resdot_eject_intercept_6_4 = models.FloatField("Res. Eject Intercept[6][4]", null=True, blank=True)

    resdot_eject_slope_6_5 = models.FloatField("Res. Eject Slope[6][5]", null=True, blank=True)

    resdot_eject_intercept_6_5 = models.FloatField("Res. Eject Intercept[6][5]", null=True, blank=True)

    resdot_eject_slope_6_6 = models.FloatField("Res. Eject Slope[6][6]", null=True, blank=True)

    resdot_eject_intercept_6_6 = models.FloatField("Res. Eject Intercept[6][6]", null=True, blank=True)

    resdot_eject_slope_6_7 = models.FloatField("Res. Eject Slope[6][7]", null=True, blank=True)

    resdot_eject_intercept_6_7 = models.FloatField("Res. Eject Intercept[6][7]", null=True, blank=True)

    resdot_eject_slope_6_8 = models.FloatField("Res. Eject Slope[6][8]", null=True, blank=True)

    resdot_eject_intercept_6_8 = models.FloatField("Res. Eject Intercept[6][8]", null=True, blank=True)

    resdot_eject_slope_6_9 = models.FloatField("Res. Eject Slope[6][9]", null=True, blank=True)

    resdot_eject_intercept_6_9 = models.FloatField("Res. Eject Intercept[6][9]", null=True, blank=True)

    resdot_eject_slope_6_10 = models.FloatField("Res. Eject Slope[6][10]", null=True, blank=True)

    resdot_eject_intercept_6_10 = models.FloatField("Res. Eject Intercept[6][10]", null=True, blank=True)

    resdot_eject_slope_6_11 = models.FloatField("Res. Eject Slope[6][11]", null=True, blank=True)

    resdot_eject_intercept_6_11 = models.FloatField("Res. Eject Intercept[6][11]", null=True, blank=True)

    resdot_eject_slope_6_12 = models.FloatField("Res. Eject Slope[6][12]", null=True, blank=True)

    resdot_eject_intercept_6_12 = models.FloatField("Res. Eject Intercept[6][12]", null=True, blank=True)

    resdot_eject_slope_6_13 = models.FloatField("Res. Eject Slope[6][13]", null=True, blank=True)

    resdot_eject_intercept_6_13 = models.FloatField("Res. Eject Intercept[6][13]", null=True, blank=True)

    resdot_eject_slope_6_14 = models.FloatField("Res. Eject Slope[6][14]", null=True, blank=True)

    resdot_eject_intercept_6_14 = models.FloatField("Res. Eject Intercept[6][14]", null=True, blank=True)

    resdot_eject_slope_6_15 = models.FloatField("Res. Eject Slope[6][15]", null=True, blank=True)

    resdot_eject_intercept_6_15 = models.FloatField("Res. Eject Intercept[6][15]", null=True, blank=True)

    resdot_eject_slope_6_16 = models.FloatField("Res. Eject Slope[6][16]", null=True, blank=True)

    resdot_eject_intercept_6_16 = models.FloatField("Res. Eject Intercept[6][16]", null=True, blank=True)

    resdot_eject_slope_6_17 = models.FloatField("Res. Eject Slope[6][17]", null=True, blank=True)

    resdot_eject_intercept_6_17 = models.FloatField("Res. Eject Intercept[6][17]", null=True, blank=True)

    resdot_eject_slope_6_18 = models.FloatField("Res. Eject Slope[6][18]", null=True, blank=True)

    resdot_eject_intercept_6_18 = models.FloatField("Res. Eject Intercept[6][18]", null=True, blank=True)

    resdot_eject_slope_6_19 = models.FloatField("Res. Eject Slope[6][19]", null=True, blank=True)

    resdot_eject_intercept_6_19 = models.FloatField("Res. Eject Intercept[6][19]", null=True, blank=True)

    resdot_eject_slope_7_0 = models.FloatField("Res. Eject Slope[7][0]", null=True, blank=True)

    resdot_eject_intercept_7_0 = models.FloatField("Res. Eject Intercept[7][0]", null=True, blank=True)

    resdot_eject_slope_7_1 = models.FloatField("Res. Eject Slope[7][1]", null=True, blank=True)

    resdot_eject_intercept_7_1 = models.FloatField("Res. Eject Intercept[7][1]", null=True, blank=True)

    resdot_eject_slope_7_2 = models.FloatField("Res. Eject Slope[7][2]", null=True, blank=True)

    resdot_eject_intercept_7_2 = models.FloatField("Res. Eject Intercept[7][2]", null=True, blank=True)

    resdot_eject_slope_7_3 = models.FloatField("Res. Eject Slope[7][3]", null=True, blank=True)

    resdot_eject_intercept_7_3 = models.FloatField("Res. Eject Intercept[7][3]", null=True, blank=True)

    resdot_eject_slope_7_4 = models.FloatField("Res. Eject Slope[7][4]", null=True, blank=True)

    resdot_eject_intercept_7_4 = models.FloatField("Res. Eject Intercept[7][4]", null=True, blank=True)

    resdot_eject_slope_7_5 = models.FloatField("Res. Eject Slope[7][5]", null=True, blank=True)

    resdot_eject_intercept_7_5 = models.FloatField("Res. Eject Intercept[7][5]", null=True, blank=True)

    resdot_eject_slope_7_6 = models.FloatField("Res. Eject Slope[7][6]", null=True, blank=True)

    resdot_eject_intercept_7_6 = models.FloatField("Res. Eject Intercept[7][6]", null=True, blank=True)

    resdot_eject_slope_7_7 = models.FloatField("Res. Eject Slope[7][7]", null=True, blank=True)

    resdot_eject_intercept_7_7 = models.FloatField("Res. Eject Intercept[7][7]", null=True, blank=True)

    resdot_eject_slope_7_8 = models.FloatField("Res. Eject Slope[7][8]", null=True, blank=True)

    resdot_eject_intercept_7_8 = models.FloatField("Res. Eject Intercept[7][8]", null=True, blank=True)

    resdot_eject_slope_7_9 = models.FloatField("Res. Eject Slope[7][9]", null=True, blank=True)

    resdot_eject_intercept_7_9 = models.FloatField("Res. Eject Intercept[7][9]", null=True, blank=True)

    resdot_eject_slope_7_10 = models.FloatField("Res. Eject Slope[7][10]", null=True, blank=True)

    resdot_eject_intercept_7_10 = models.FloatField("Res. Eject Intercept[7][10]", null=True, blank=True)

    resdot_eject_slope_7_11 = models.FloatField("Res. Eject Slope[7][11]", null=True, blank=True)

    resdot_eject_intercept_7_11 = models.FloatField("Res. Eject Intercept[7][11]", null=True, blank=True)

    resdot_eject_slope_7_12 = models.FloatField("Res. Eject Slope[7][12]", null=True, blank=True)

    resdot_eject_intercept_7_12 = models.FloatField("Res. Eject Intercept[7][12]", null=True, blank=True)

    resdot_eject_slope_7_13 = models.FloatField("Res. Eject Slope[7][13]", null=True, blank=True)

    resdot_eject_intercept_7_13 = models.FloatField("Res. Eject Intercept[7][13]", null=True, blank=True)

    resdot_eject_slope_7_14 = models.FloatField("Res. Eject Slope[7][14]", null=True, blank=True)

    resdot_eject_intercept_7_14 = models.FloatField("Res. Eject Intercept[7][14]", null=True, blank=True)

    resdot_eject_slope_7_15 = models.FloatField("Res. Eject Slope[7][15]", null=True, blank=True)

    resdot_eject_intercept_7_15 = models.FloatField("Res. Eject Intercept[7][15]", null=True, blank=True)

    resdot_eject_slope_7_16 = models.FloatField("Res. Eject Slope[7][16]", null=True, blank=True)

    resdot_eject_intercept_7_16 = models.FloatField("Res. Eject Intercept[7][16]", null=True, blank=True)

    resdot_eject_slope_7_17 = models.FloatField("Res. Eject Slope[7][17]", null=True, blank=True)

    resdot_eject_intercept_7_17 = models.FloatField("Res. Eject Intercept[7][17]", null=True, blank=True)

    resdot_eject_slope_7_18 = models.FloatField("Res. Eject Slope[7][18]", null=True, blank=True)

    resdot_eject_intercept_7_18 = models.FloatField("Res. Eject Intercept[7][18]", null=True, blank=True)

    resdot_eject_slope_7_19 = models.FloatField("Res. Eject Slope[7][19]", null=True, blank=True)

    resdot_eject_intercept_7_19 = models.FloatField("Res. Eject Intercept[7][19]", null=True, blank=True)

    resdot_eject_slope_8_0 = models.FloatField("Res. Eject Slope[8][0]", null=True, blank=True)

    resdot_eject_intercept_8_0 = models.FloatField("Res. Eject Intercept[8][0]", null=True, blank=True)

    resdot_eject_slope_8_1 = models.FloatField("Res. Eject Slope[8][1]", null=True, blank=True)

    resdot_eject_intercept_8_1 = models.FloatField("Res. Eject Intercept[8][1]", null=True, blank=True)

    resdot_eject_slope_8_2 = models.FloatField("Res. Eject Slope[8][2]", null=True, blank=True)

    resdot_eject_intercept_8_2 = models.FloatField("Res. Eject Intercept[8][2]", null=True, blank=True)

    resdot_eject_slope_8_3 = models.FloatField("Res. Eject Slope[8][3]", null=True, blank=True)

    resdot_eject_intercept_8_3 = models.FloatField("Res. Eject Intercept[8][3]", null=True, blank=True)

    resdot_eject_slope_8_4 = models.FloatField("Res. Eject Slope[8][4]", null=True, blank=True)

    resdot_eject_intercept_8_4 = models.FloatField("Res. Eject Intercept[8][4]", null=True, blank=True)

    resdot_eject_slope_8_5 = models.FloatField("Res. Eject Slope[8][5]", null=True, blank=True)

    resdot_eject_intercept_8_5 = models.FloatField("Res. Eject Intercept[8][5]", null=True, blank=True)

    resdot_eject_slope_8_6 = models.FloatField("Res. Eject Slope[8][6]", null=True, blank=True)

    resdot_eject_intercept_8_6 = models.FloatField("Res. Eject Intercept[8][6]", null=True, blank=True)

    resdot_eject_slope_8_7 = models.FloatField("Res. Eject Slope[8][7]", null=True, blank=True)

    resdot_eject_intercept_8_7 = models.FloatField("Res. Eject Intercept[8][7]", null=True, blank=True)

    resdot_eject_slope_8_8 = models.FloatField("Res. Eject Slope[8][8]", null=True, blank=True)

    resdot_eject_intercept_8_8 = models.FloatField("Res. Eject Intercept[8][8]", null=True, blank=True)

    resdot_eject_slope_8_9 = models.FloatField("Res. Eject Slope[8][9]", null=True, blank=True)

    resdot_eject_intercept_8_9 = models.FloatField("Res. Eject Intercept[8][9]", null=True, blank=True)

    resdot_eject_slope_8_10 = models.FloatField("Res. Eject Slope[8][10]", null=True, blank=True)

    resdot_eject_intercept_8_10 = models.FloatField("Res. Eject Intercept[8][10]", null=True, blank=True)

    resdot_eject_slope_8_11 = models.FloatField("Res. Eject Slope[8][11]", null=True, blank=True)

    resdot_eject_intercept_8_11 = models.FloatField("Res. Eject Intercept[8][11]", null=True, blank=True)

    resdot_eject_slope_8_12 = models.FloatField("Res. Eject Slope[8][12]", null=True, blank=True)

    resdot_eject_intercept_8_12 = models.FloatField("Res. Eject Intercept[8][12]", null=True, blank=True)

    resdot_eject_slope_8_13 = models.FloatField("Res. Eject Slope[8][13]", null=True, blank=True)

    resdot_eject_intercept_8_13 = models.FloatField("Res. Eject Intercept[8][13]", null=True, blank=True)

    resdot_eject_slope_8_14 = models.FloatField("Res. Eject Slope[8][14]", null=True, blank=True)

    resdot_eject_intercept_8_14 = models.FloatField("Res. Eject Intercept[8][14]", null=True, blank=True)

    resdot_eject_slope_8_15 = models.FloatField("Res. Eject Slope[8][15]", null=True, blank=True)

    resdot_eject_intercept_8_15 = models.FloatField("Res. Eject Intercept[8][15]", null=True, blank=True)

    resdot_eject_slope_8_16 = models.FloatField("Res. Eject Slope[8][16]", null=True, blank=True)

    resdot_eject_intercept_8_16 = models.FloatField("Res. Eject Intercept[8][16]", null=True, blank=True)

    resdot_eject_slope_8_17 = models.FloatField("Res. Eject Slope[8][17]", null=True, blank=True)

    resdot_eject_intercept_8_17 = models.FloatField("Res. Eject Intercept[8][17]", null=True, blank=True)

    resdot_eject_slope_8_18 = models.FloatField("Res. Eject Slope[8][18]", null=True, blank=True)

    resdot_eject_intercept_8_18 = models.FloatField("Res. Eject Intercept[8][18]", null=True, blank=True)

    resdot_eject_slope_8_19 = models.FloatField("Res. Eject Slope[8][19]", null=True, blank=True)

    resdot_eject_intercept_8_19 = models.FloatField("Res. Eject Intercept[8][19]", null=True, blank=True)

    resdot_eject_slope_9_0 = models.FloatField("Res. Eject Slope[9][0]", null=True, blank=True)

    resdot_eject_intercept_9_0 = models.FloatField("Res. Eject Intercept[9][0]", null=True, blank=True)

    resdot_eject_slope_9_1 = models.FloatField("Res. Eject Slope[9][1]", null=True, blank=True)

    resdot_eject_intercept_9_1 = models.FloatField("Res. Eject Intercept[9][1]", null=True, blank=True)

    resdot_eject_slope_9_2 = models.FloatField("Res. Eject Slope[9][2]", null=True, blank=True)

    resdot_eject_intercept_9_2 = models.FloatField("Res. Eject Intercept[9][2]", null=True, blank=True)

    resdot_eject_slope_9_3 = models.FloatField("Res. Eject Slope[9][3]", null=True, blank=True)

    resdot_eject_intercept_9_3 = models.FloatField("Res. Eject Intercept[9][3]", null=True, blank=True)

    resdot_eject_slope_9_4 = models.FloatField("Res. Eject Slope[9][4]", null=True, blank=True)

    resdot_eject_intercept_9_4 = models.FloatField("Res. Eject Intercept[9][4]", null=True, blank=True)

    resdot_eject_slope_9_5 = models.FloatField("Res. Eject Slope[9][5]", null=True, blank=True)

    resdot_eject_intercept_9_5 = models.FloatField("Res. Eject Intercept[9][5]", null=True, blank=True)

    resdot_eject_slope_9_6 = models.FloatField("Res. Eject Slope[9][6]", null=True, blank=True)

    resdot_eject_intercept_9_6 = models.FloatField("Res. Eject Intercept[9][6]", null=True, blank=True)

    resdot_eject_slope_9_7 = models.FloatField("Res. Eject Slope[9][7]", null=True, blank=True)

    resdot_eject_intercept_9_7 = models.FloatField("Res. Eject Intercept[9][7]", null=True, blank=True)

    resdot_eject_slope_9_8 = models.FloatField("Res. Eject Slope[9][8]", null=True, blank=True)

    resdot_eject_intercept_9_8 = models.FloatField("Res. Eject Intercept[9][8]", null=True, blank=True)

    resdot_eject_slope_9_9 = models.FloatField("Res. Eject Slope[9][9]", null=True, blank=True)

    resdot_eject_intercept_9_9 = models.FloatField("Res. Eject Intercept[9][9]", null=True, blank=True)

    resdot_eject_slope_9_10 = models.FloatField("Res. Eject Slope[9][10]", null=True, blank=True)

    resdot_eject_intercept_9_10 = models.FloatField("Res. Eject Intercept[9][10]", null=True, blank=True)

    resdot_eject_slope_9_11 = models.FloatField("Res. Eject Slope[9][11]", null=True, blank=True)

    resdot_eject_intercept_9_11 = models.FloatField("Res. Eject Intercept[9][11]", null=True, blank=True)

    resdot_eject_slope_9_12 = models.FloatField("Res. Eject Slope[9][12]", null=True, blank=True)

    resdot_eject_intercept_9_12 = models.FloatField("Res. Eject Intercept[9][12]", null=True, blank=True)

    resdot_eject_slope_9_13 = models.FloatField("Res. Eject Slope[9][13]", null=True, blank=True)

    resdot_eject_intercept_9_13 = models.FloatField("Res. Eject Intercept[9][13]", null=True, blank=True)

    resdot_eject_slope_9_14 = models.FloatField("Res. Eject Slope[9][14]", null=True, blank=True)

    resdot_eject_intercept_9_14 = models.FloatField("Res. Eject Intercept[9][14]", null=True, blank=True)

    resdot_eject_slope_9_15 = models.FloatField("Res. Eject Slope[9][15]", null=True, blank=True)

    resdot_eject_intercept_9_15 = models.FloatField("Res. Eject Intercept[9][15]", null=True, blank=True)

    resdot_eject_slope_9_16 = models.FloatField("Res. Eject Slope[9][16]", null=True, blank=True)

    resdot_eject_intercept_9_16 = models.FloatField("Res. Eject Intercept[9][16]", null=True, blank=True)

    resdot_eject_slope_9_17 = models.FloatField("Res. Eject Slope[9][17]", null=True, blank=True)

    resdot_eject_intercept_9_17 = models.FloatField("Res. Eject Intercept[9][17]", null=True, blank=True)

    resdot_eject_slope_9_18 = models.FloatField("Res. Eject Slope[9][18]", null=True, blank=True)

    resdot_eject_intercept_9_18 = models.FloatField("Res. Eject Intercept[9][18]", null=True, blank=True)

    resdot_eject_slope_9_19 = models.FloatField("Res. Eject Slope[9][19]", null=True, blank=True)

    resdot_eject_intercept_9_19 = models.FloatField("Res. Eject Intercept[9][19]", null=True, blank=True)

    resdot_eject_slope_10_0 = models.FloatField("Res. Eject Slope[10][0]", null=True, blank=True)

    resdot_eject_intercept_10_0 = models.FloatField("Res. Eject Intercept[10][0]", null=True, blank=True)

    resdot_eject_slope_10_1 = models.FloatField("Res. Eject Slope[10][1]", null=True, blank=True)

    resdot_eject_intercept_10_1 = models.FloatField("Res. Eject Intercept[10][1]", null=True, blank=True)

    resdot_eject_slope_10_2 = models.FloatField("Res. Eject Slope[10][2]", null=True, blank=True)

    resdot_eject_intercept_10_2 = models.FloatField("Res. Eject Intercept[10][2]", null=True, blank=True)

    resdot_eject_slope_10_3 = models.FloatField("Res. Eject Slope[10][3]", null=True, blank=True)

    resdot_eject_intercept_10_3 = models.FloatField("Res. Eject Intercept[10][3]", null=True, blank=True)

    resdot_eject_slope_10_4 = models.FloatField("Res. Eject Slope[10][4]", null=True, blank=True)

    resdot_eject_intercept_10_4 = models.FloatField("Res. Eject Intercept[10][4]", null=True, blank=True)

    resdot_eject_slope_10_5 = models.FloatField("Res. Eject Slope[10][5]", null=True, blank=True)

    resdot_eject_intercept_10_5 = models.FloatField("Res. Eject Intercept[10][5]", null=True, blank=True)

    resdot_eject_slope_10_6 = models.FloatField("Res. Eject Slope[10][6]", null=True, blank=True)

    resdot_eject_intercept_10_6 = models.FloatField("Res. Eject Intercept[10][6]", null=True, blank=True)

    resdot_eject_slope_10_7 = models.FloatField("Res. Eject Slope[10][7]", null=True, blank=True)

    resdot_eject_intercept_10_7 = models.FloatField("Res. Eject Intercept[10][7]", null=True, blank=True)

    resdot_eject_slope_10_8 = models.FloatField("Res. Eject Slope[10][8]", null=True, blank=True)

    resdot_eject_intercept_10_8 = models.FloatField("Res. Eject Intercept[10][8]", null=True, blank=True)

    resdot_eject_slope_10_9 = models.FloatField("Res. Eject Slope[10][9]", null=True, blank=True)

    resdot_eject_intercept_10_9 = models.FloatField("Res. Eject Intercept[10][9]", null=True, blank=True)

    resdot_eject_slope_10_10 = models.FloatField("Res. Eject Slope[10][10]", null=True, blank=True)

    resdot_eject_intercept_10_10 = models.FloatField("Res. Eject Intercept[10][10]", null=True, blank=True)

    resdot_eject_slope_10_11 = models.FloatField("Res. Eject Slope[10][11]", null=True, blank=True)

    resdot_eject_intercept_10_11 = models.FloatField("Res. Eject Intercept[10][11]", null=True, blank=True)

    resdot_eject_slope_10_12 = models.FloatField("Res. Eject Slope[10][12]", null=True, blank=True)

    resdot_eject_intercept_10_12 = models.FloatField("Res. Eject Intercept[10][12]", null=True, blank=True)

    resdot_eject_slope_10_13 = models.FloatField("Res. Eject Slope[10][13]", null=True, blank=True)

    resdot_eject_intercept_10_13 = models.FloatField("Res. Eject Intercept[10][13]", null=True, blank=True)

    resdot_eject_slope_10_14 = models.FloatField("Res. Eject Slope[10][14]", null=True, blank=True)

    resdot_eject_intercept_10_14 = models.FloatField("Res. Eject Intercept[10][14]", null=True, blank=True)

    resdot_eject_slope_10_15 = models.FloatField("Res. Eject Slope[10][15]", null=True, blank=True)

    resdot_eject_intercept_10_15 = models.FloatField("Res. Eject Intercept[10][15]", null=True, blank=True)

    resdot_eject_slope_10_16 = models.FloatField("Res. Eject Slope[10][16]", null=True, blank=True)

    resdot_eject_intercept_10_16 = models.FloatField("Res. Eject Intercept[10][16]", null=True, blank=True)

    resdot_eject_slope_10_17 = models.FloatField("Res. Eject Slope[10][17]", null=True, blank=True)

    resdot_eject_intercept_10_17 = models.FloatField("Res. Eject Intercept[10][17]", null=True, blank=True)

    resdot_eject_slope_10_18 = models.FloatField("Res. Eject Slope[10][18]", null=True, blank=True)

    resdot_eject_intercept_10_18 = models.FloatField("Res. Eject Intercept[10][18]", null=True, blank=True)

    resdot_eject_slope_10_19 = models.FloatField("Res. Eject Slope[10][19]", null=True, blank=True)

    resdot_eject_intercept_10_19 = models.FloatField("Res. Eject Intercept[10][19]", null=True, blank=True)

    resdot_eject_slope_11_0 = models.FloatField("Res. Eject Slope[11][0]", null=True, blank=True)

    resdot_eject_intercept_11_0 = models.FloatField("Res. Eject Intercept[11][0]", null=True, blank=True)

    resdot_eject_slope_11_1 = models.FloatField("Res. Eject Slope[11][1]", null=True, blank=True)

    resdot_eject_intercept_11_1 = models.FloatField("Res. Eject Intercept[11][1]", null=True, blank=True)

    resdot_eject_slope_11_2 = models.FloatField("Res. Eject Slope[11][2]", null=True, blank=True)

    resdot_eject_intercept_11_2 = models.FloatField("Res. Eject Intercept[11][2]", null=True, blank=True)

    resdot_eject_slope_11_3 = models.FloatField("Res. Eject Slope[11][3]", null=True, blank=True)

    resdot_eject_intercept_11_3 = models.FloatField("Res. Eject Intercept[11][3]", null=True, blank=True)

    resdot_eject_slope_11_4 = models.FloatField("Res. Eject Slope[11][4]", null=True, blank=True)

    resdot_eject_intercept_11_4 = models.FloatField("Res. Eject Intercept[11][4]", null=True, blank=True)

    resdot_eject_slope_11_5 = models.FloatField("Res. Eject Slope[11][5]", null=True, blank=True)

    resdot_eject_intercept_11_5 = models.FloatField("Res. Eject Intercept[11][5]", null=True, blank=True)

    resdot_eject_slope_11_6 = models.FloatField("Res. Eject Slope[11][6]", null=True, blank=True)

    resdot_eject_intercept_11_6 = models.FloatField("Res. Eject Intercept[11][6]", null=True, blank=True)

    resdot_eject_slope_11_7 = models.FloatField("Res. Eject Slope[11][7]", null=True, blank=True)

    resdot_eject_intercept_11_7 = models.FloatField("Res. Eject Intercept[11][7]", null=True, blank=True)

    resdot_eject_slope_11_8 = models.FloatField("Res. Eject Slope[11][8]", null=True, blank=True)

    resdot_eject_intercept_11_8 = models.FloatField("Res. Eject Intercept[11][8]", null=True, blank=True)

    resdot_eject_slope_11_9 = models.FloatField("Res. Eject Slope[11][9]", null=True, blank=True)

    resdot_eject_intercept_11_9 = models.FloatField("Res. Eject Intercept[11][9]", null=True, blank=True)

    resdot_eject_slope_11_10 = models.FloatField("Res. Eject Slope[11][10]", null=True, blank=True)

    resdot_eject_intercept_11_10 = models.FloatField("Res. Eject Intercept[11][10]", null=True, blank=True)

    resdot_eject_slope_11_11 = models.FloatField("Res. Eject Slope[11][11]", null=True, blank=True)

    resdot_eject_intercept_11_11 = models.FloatField("Res. Eject Intercept[11][11]", null=True, blank=True)

    resdot_eject_slope_11_12 = models.FloatField("Res. Eject Slope[11][12]", null=True, blank=True)

    resdot_eject_intercept_11_12 = models.FloatField("Res. Eject Intercept[11][12]", null=True, blank=True)

    resdot_eject_slope_11_13 = models.FloatField("Res. Eject Slope[11][13]", null=True, blank=True)

    resdot_eject_intercept_11_13 = models.FloatField("Res. Eject Intercept[11][13]", null=True, blank=True)

    resdot_eject_slope_11_14 = models.FloatField("Res. Eject Slope[11][14]", null=True, blank=True)

    resdot_eject_intercept_11_14 = models.FloatField("Res. Eject Intercept[11][14]", null=True, blank=True)

    resdot_eject_slope_11_15 = models.FloatField("Res. Eject Slope[11][15]", null=True, blank=True)

    resdot_eject_intercept_11_15 = models.FloatField("Res. Eject Intercept[11][15]", null=True, blank=True)

    resdot_eject_slope_11_16 = models.FloatField("Res. Eject Slope[11][16]", null=True, blank=True)

    resdot_eject_intercept_11_16 = models.FloatField("Res. Eject Intercept[11][16]", null=True, blank=True)

    resdot_eject_slope_11_17 = models.FloatField("Res. Eject Slope[11][17]", null=True, blank=True)

    resdot_eject_intercept_11_17 = models.FloatField("Res. Eject Intercept[11][17]", null=True, blank=True)

    resdot_eject_slope_11_18 = models.FloatField("Res. Eject Slope[11][18]", null=True, blank=True)

    resdot_eject_intercept_11_18 = models.FloatField("Res. Eject Intercept[11][18]", null=True, blank=True)

    resdot_eject_slope_11_19 = models.FloatField("Res. Eject Slope[11][19]", null=True, blank=True)

    resdot_eject_intercept_11_19 = models.FloatField("Res. Eject Intercept[11][19]", null=True, blank=True)

    resdot_eject_slope_12_0 = models.FloatField("Res. Eject Slope[12][0]", null=True, blank=True)

    resdot_eject_intercept_12_0 = models.FloatField("Res. Eject Intercept[12][0]", null=True, blank=True)

    resdot_eject_slope_12_1 = models.FloatField("Res. Eject Slope[12][1]", null=True, blank=True)

    resdot_eject_intercept_12_1 = models.FloatField("Res. Eject Intercept[12][1]", null=True, blank=True)

    resdot_eject_slope_12_2 = models.FloatField("Res. Eject Slope[12][2]", null=True, blank=True)

    resdot_eject_intercept_12_2 = models.FloatField("Res. Eject Intercept[12][2]", null=True, blank=True)

    resdot_eject_slope_12_3 = models.FloatField("Res. Eject Slope[12][3]", null=True, blank=True)

    resdot_eject_intercept_12_3 = models.FloatField("Res. Eject Intercept[12][3]", null=True, blank=True)

    resdot_eject_slope_12_4 = models.FloatField("Res. Eject Slope[12][4]", null=True, blank=True)

    resdot_eject_intercept_12_4 = models.FloatField("Res. Eject Intercept[12][4]", null=True, blank=True)

    resdot_eject_slope_12_5 = models.FloatField("Res. Eject Slope[12][5]", null=True, blank=True)

    resdot_eject_intercept_12_5 = models.FloatField("Res. Eject Intercept[12][5]", null=True, blank=True)

    resdot_eject_slope_12_6 = models.FloatField("Res. Eject Slope[12][6]", null=True, blank=True)

    resdot_eject_intercept_12_6 = models.FloatField("Res. Eject Intercept[12][6]", null=True, blank=True)

    resdot_eject_slope_12_7 = models.FloatField("Res. Eject Slope[12][7]", null=True, blank=True)

    resdot_eject_intercept_12_7 = models.FloatField("Res. Eject Intercept[12][7]", null=True, blank=True)

    resdot_eject_slope_12_8 = models.FloatField("Res. Eject Slope[12][8]", null=True, blank=True)

    resdot_eject_intercept_12_8 = models.FloatField("Res. Eject Intercept[12][8]", null=True, blank=True)

    resdot_eject_slope_12_9 = models.FloatField("Res. Eject Slope[12][9]", null=True, blank=True)

    resdot_eject_intercept_12_9 = models.FloatField("Res. Eject Intercept[12][9]", null=True, blank=True)

    resdot_eject_slope_12_10 = models.FloatField("Res. Eject Slope[12][10]", null=True, blank=True)

    resdot_eject_intercept_12_10 = models.FloatField("Res. Eject Intercept[12][10]", null=True, blank=True)

    resdot_eject_slope_12_11 = models.FloatField("Res. Eject Slope[12][11]", null=True, blank=True)

    resdot_eject_intercept_12_11 = models.FloatField("Res. Eject Intercept[12][11]", null=True, blank=True)

    resdot_eject_slope_12_12 = models.FloatField("Res. Eject Slope[12][12]", null=True, blank=True)

    resdot_eject_intercept_12_12 = models.FloatField("Res. Eject Intercept[12][12]", null=True, blank=True)

    resdot_eject_slope_12_13 = models.FloatField("Res. Eject Slope[12][13]", null=True, blank=True)

    resdot_eject_intercept_12_13 = models.FloatField("Res. Eject Intercept[12][13]", null=True, blank=True)

    resdot_eject_slope_12_14 = models.FloatField("Res. Eject Slope[12][14]", null=True, blank=True)

    resdot_eject_intercept_12_14 = models.FloatField("Res. Eject Intercept[12][14]", null=True, blank=True)

    resdot_eject_slope_12_15 = models.FloatField("Res. Eject Slope[12][15]", null=True, blank=True)

    resdot_eject_intercept_12_15 = models.FloatField("Res. Eject Intercept[12][15]", null=True, blank=True)

    resdot_eject_slope_12_16 = models.FloatField("Res. Eject Slope[12][16]", null=True, blank=True)

    resdot_eject_intercept_12_16 = models.FloatField("Res. Eject Intercept[12][16]", null=True, blank=True)

    resdot_eject_slope_12_17 = models.FloatField("Res. Eject Slope[12][17]", null=True, blank=True)

    resdot_eject_intercept_12_17 = models.FloatField("Res. Eject Intercept[12][17]", null=True, blank=True)

    resdot_eject_slope_12_18 = models.FloatField("Res. Eject Slope[12][18]", null=True, blank=True)

    resdot_eject_intercept_12_18 = models.FloatField("Res. Eject Intercept[12][18]", null=True, blank=True)

    resdot_eject_slope_12_19 = models.FloatField("Res. Eject Slope[12][19]", null=True, blank=True)

    resdot_eject_intercept_12_19 = models.FloatField("Res. Eject Intercept[12][19]", null=True, blank=True)





class MetaCalibrationFileValueMass(models.Model):


    class Meta:
        verbose_name = "Meta: Calibration File Value Mass"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Meta')

    mass_slope_0_0 = models.FloatField("Mass Slope[0][0]", null=True, blank=True)

    mass_intercept_0_0 = models.FloatField("Mass Intercept[0][0]", null=True, blank=True)

    mass_slope_0_1 = models.FloatField("Mass Slope[0][1]", null=True, blank=True)

    mass_intercept_0_1 = models.FloatField("Mass Intercept[0][1]", null=True, blank=True)

    mass_slope_0_2 = models.FloatField("Mass Slope[0][2]", null=True, blank=True)

    mass_intercept_0_2 = models.FloatField("Mass Intercept[0][2]", null=True, blank=True)

    mass_slope_0_3 = models.FloatField("Mass Slope[0][3]", null=True, blank=True)

    mass_intercept_0_3 = models.FloatField("Mass Intercept[0][3]", null=True, blank=True)

    mass_slope_0_4 = models.FloatField("Mass Slope[0][4]", null=True, blank=True)

    mass_intercept_0_4 = models.FloatField("Mass Intercept[0][4]", null=True, blank=True)

    mass_slope_0_5 = models.FloatField("Mass Slope[0][5]", null=True, blank=True)

    mass_intercept_0_5 = models.FloatField("Mass Intercept[0][5]", null=True, blank=True)

    mass_slope_0_6 = models.FloatField("Mass Slope[0][6]", null=True, blank=True)

    mass_intercept_0_6 = models.FloatField("Mass Intercept[0][6]", null=True, blank=True)

    mass_slope_0_7 = models.FloatField("Mass Slope[0][7]", null=True, blank=True)

    mass_intercept_0_7 = models.FloatField("Mass Intercept[0][7]", null=True, blank=True)

    mass_slope_0_8 = models.FloatField("Mass Slope[0][8]", null=True, blank=True)

    mass_intercept_0_8 = models.FloatField("Mass Intercept[0][8]", null=True, blank=True)

    mass_slope_0_9 = models.FloatField("Mass Slope[0][9]", null=True, blank=True)

    mass_intercept_0_9 = models.FloatField("Mass Intercept[0][9]", null=True, blank=True)

    mass_slope_0_10 = models.FloatField("Mass Slope[0][10]", null=True, blank=True)

    mass_intercept_0_10 = models.FloatField("Mass Intercept[0][10]", null=True, blank=True)

    mass_slope_0_11 = models.FloatField("Mass Slope[0][11]", null=True, blank=True)

    mass_intercept_0_11 = models.FloatField("Mass Intercept[0][11]", null=True, blank=True)

    mass_slope_0_12 = models.FloatField("Mass Slope[0][12]", null=True, blank=True)

    mass_intercept_0_12 = models.FloatField("Mass Intercept[0][12]", null=True, blank=True)

    mass_slope_0_13 = models.FloatField("Mass Slope[0][13]", null=True, blank=True)

    mass_intercept_0_13 = models.FloatField("Mass Intercept[0][13]", null=True, blank=True)

    mass_slope_0_14 = models.FloatField("Mass Slope[0][14]", null=True, blank=True)

    mass_intercept_0_14 = models.FloatField("Mass Intercept[0][14]", null=True, blank=True)

    mass_slope_0_15 = models.FloatField("Mass Slope[0][15]", null=True, blank=True)

    mass_intercept_0_15 = models.FloatField("Mass Intercept[0][15]", null=True, blank=True)

    mass_slope_0_16 = models.FloatField("Mass Slope[0][16]", null=True, blank=True)

    mass_intercept_0_16 = models.FloatField("Mass Intercept[0][16]", null=True, blank=True)

    mass_slope_0_17 = models.FloatField("Mass Slope[0][17]", null=True, blank=True)

    mass_intercept_0_17 = models.FloatField("Mass Intercept[0][17]", null=True, blank=True)

    mass_slope_0_18 = models.FloatField("Mass Slope[0][18]", null=True, blank=True)

    mass_intercept_0_18 = models.FloatField("Mass Intercept[0][18]", null=True, blank=True)

    mass_slope_0_19 = models.FloatField("Mass Slope[0][19]", null=True, blank=True)

    mass_intercept_0_19 = models.FloatField("Mass Intercept[0][19]", null=True, blank=True)

    mass_slope_1_0 = models.FloatField("Mass Slope[1][0]", null=True, blank=True)

    mass_intercept_1_0 = models.FloatField("Mass Intercept[1][0]", null=True, blank=True)

    mass_slope_1_1 = models.FloatField("Mass Slope[1][1]", null=True, blank=True)

    mass_intercept_1_1 = models.FloatField("Mass Intercept[1][1]", null=True, blank=True)

    mass_slope_1_2 = models.FloatField("Mass Slope[1][2]", null=True, blank=True)

    mass_intercept_1_2 = models.FloatField("Mass Intercept[1][2]", null=True, blank=True)

    mass_slope_1_3 = models.FloatField("Mass Slope[1][3]", null=True, blank=True)

    mass_intercept_1_3 = models.FloatField("Mass Intercept[1][3]", null=True, blank=True)

    mass_slope_1_4 = models.FloatField("Mass Slope[1][4]", null=True, blank=True)

    mass_intercept_1_4 = models.FloatField("Mass Intercept[1][4]", null=True, blank=True)

    mass_slope_1_5 = models.FloatField("Mass Slope[1][5]", null=True, blank=True)

    mass_intercept_1_5 = models.FloatField("Mass Intercept[1][5]", null=True, blank=True)

    mass_slope_1_6 = models.FloatField("Mass Slope[1][6]", null=True, blank=True)

    mass_intercept_1_6 = models.FloatField("Mass Intercept[1][6]", null=True, blank=True)

    mass_slope_1_7 = models.FloatField("Mass Slope[1][7]", null=True, blank=True)

    mass_intercept_1_7 = models.FloatField("Mass Intercept[1][7]", null=True, blank=True)

    mass_slope_1_8 = models.FloatField("Mass Slope[1][8]", null=True, blank=True)

    mass_intercept_1_8 = models.FloatField("Mass Intercept[1][8]", null=True, blank=True)

    mass_slope_1_9 = models.FloatField("Mass Slope[1][9]", null=True, blank=True)

    mass_intercept_1_9 = models.FloatField("Mass Intercept[1][9]", null=True, blank=True)

    mass_slope_1_10 = models.FloatField("Mass Slope[1][10]", null=True, blank=True)

    mass_intercept_1_10 = models.FloatField("Mass Intercept[1][10]", null=True, blank=True)

    mass_slope_1_11 = models.FloatField("Mass Slope[1][11]", null=True, blank=True)

    mass_intercept_1_11 = models.FloatField("Mass Intercept[1][11]", null=True, blank=True)

    mass_slope_1_12 = models.FloatField("Mass Slope[1][12]", null=True, blank=True)

    mass_intercept_1_12 = models.FloatField("Mass Intercept[1][12]", null=True, blank=True)

    mass_slope_1_13 = models.FloatField("Mass Slope[1][13]", null=True, blank=True)

    mass_intercept_1_13 = models.FloatField("Mass Intercept[1][13]", null=True, blank=True)

    mass_slope_1_14 = models.FloatField("Mass Slope[1][14]", null=True, blank=True)

    mass_intercept_1_14 = models.FloatField("Mass Intercept[1][14]", null=True, blank=True)

    mass_slope_1_15 = models.FloatField("Mass Slope[1][15]", null=True, blank=True)

    mass_intercept_1_15 = models.FloatField("Mass Intercept[1][15]", null=True, blank=True)

    mass_slope_1_16 = models.FloatField("Mass Slope[1][16]", null=True, blank=True)

    mass_intercept_1_16 = models.FloatField("Mass Intercept[1][16]", null=True, blank=True)

    mass_slope_1_17 = models.FloatField("Mass Slope[1][17]", null=True, blank=True)

    mass_intercept_1_17 = models.FloatField("Mass Intercept[1][17]", null=True, blank=True)

    mass_slope_1_18 = models.FloatField("Mass Slope[1][18]", null=True, blank=True)

    mass_intercept_1_18 = models.FloatField("Mass Intercept[1][18]", null=True, blank=True)

    mass_slope_1_19 = models.FloatField("Mass Slope[1][19]", null=True, blank=True)

    mass_intercept_1_19 = models.FloatField("Mass Intercept[1][19]", null=True, blank=True)

    mass_slope_2_0 = models.FloatField("Mass Slope[2][0]", null=True, blank=True)

    mass_intercept_2_0 = models.FloatField("Mass Intercept[2][0]", null=True, blank=True)

    mass_slope_2_1 = models.FloatField("Mass Slope[2][1]", null=True, blank=True)

    mass_intercept_2_1 = models.FloatField("Mass Intercept[2][1]", null=True, blank=True)

    mass_slope_2_2 = models.FloatField("Mass Slope[2][2]", null=True, blank=True)

    mass_intercept_2_2 = models.FloatField("Mass Intercept[2][2]", null=True, blank=True)

    mass_slope_2_3 = models.FloatField("Mass Slope[2][3]", null=True, blank=True)

    mass_intercept_2_3 = models.FloatField("Mass Intercept[2][3]", null=True, blank=True)

    mass_slope_2_4 = models.FloatField("Mass Slope[2][4]", null=True, blank=True)

    mass_intercept_2_4 = models.FloatField("Mass Intercept[2][4]", null=True, blank=True)

    mass_slope_2_5 = models.FloatField("Mass Slope[2][5]", null=True, blank=True)

    mass_intercept_2_5 = models.FloatField("Mass Intercept[2][5]", null=True, blank=True)

    mass_slope_2_6 = models.FloatField("Mass Slope[2][6]", null=True, blank=True)

    mass_intercept_2_6 = models.FloatField("Mass Intercept[2][6]", null=True, blank=True)

    mass_slope_2_7 = models.FloatField("Mass Slope[2][7]", null=True, blank=True)

    mass_intercept_2_7 = models.FloatField("Mass Intercept[2][7]", null=True, blank=True)

    mass_slope_2_8 = models.FloatField("Mass Slope[2][8]", null=True, blank=True)

    mass_intercept_2_8 = models.FloatField("Mass Intercept[2][8]", null=True, blank=True)

    mass_slope_2_9 = models.FloatField("Mass Slope[2][9]", null=True, blank=True)

    mass_intercept_2_9 = models.FloatField("Mass Intercept[2][9]", null=True, blank=True)

    mass_slope_2_10 = models.FloatField("Mass Slope[2][10]", null=True, blank=True)

    mass_intercept_2_10 = models.FloatField("Mass Intercept[2][10]", null=True, blank=True)

    mass_slope_2_11 = models.FloatField("Mass Slope[2][11]", null=True, blank=True)

    mass_intercept_2_11 = models.FloatField("Mass Intercept[2][11]", null=True, blank=True)

    mass_slope_2_12 = models.FloatField("Mass Slope[2][12]", null=True, blank=True)

    mass_intercept_2_12 = models.FloatField("Mass Intercept[2][12]", null=True, blank=True)

    mass_slope_2_13 = models.FloatField("Mass Slope[2][13]", null=True, blank=True)

    mass_intercept_2_13 = models.FloatField("Mass Intercept[2][13]", null=True, blank=True)

    mass_slope_2_14 = models.FloatField("Mass Slope[2][14]", null=True, blank=True)

    mass_intercept_2_14 = models.FloatField("Mass Intercept[2][14]", null=True, blank=True)

    mass_slope_2_15 = models.FloatField("Mass Slope[2][15]", null=True, blank=True)

    mass_intercept_2_15 = models.FloatField("Mass Intercept[2][15]", null=True, blank=True)

    mass_slope_2_16 = models.FloatField("Mass Slope[2][16]", null=True, blank=True)

    mass_intercept_2_16 = models.FloatField("Mass Intercept[2][16]", null=True, blank=True)

    mass_slope_2_17 = models.FloatField("Mass Slope[2][17]", null=True, blank=True)

    mass_intercept_2_17 = models.FloatField("Mass Intercept[2][17]", null=True, blank=True)

    mass_slope_2_18 = models.FloatField("Mass Slope[2][18]", null=True, blank=True)

    mass_intercept_2_18 = models.FloatField("Mass Intercept[2][18]", null=True, blank=True)

    mass_slope_2_19 = models.FloatField("Mass Slope[2][19]", null=True, blank=True)

    mass_intercept_2_19 = models.FloatField("Mass Intercept[2][19]", null=True, blank=True)

    mass_slope_3_0 = models.FloatField("Mass Slope[3][0]", null=True, blank=True)

    mass_intercept_3_0 = models.FloatField("Mass Intercept[3][0]", null=True, blank=True)

    mass_slope_3_1 = models.FloatField("Mass Slope[3][1]", null=True, blank=True)

    mass_intercept_3_1 = models.FloatField("Mass Intercept[3][1]", null=True, blank=True)

    mass_slope_3_2 = models.FloatField("Mass Slope[3][2]", null=True, blank=True)

    mass_intercept_3_2 = models.FloatField("Mass Intercept[3][2]", null=True, blank=True)

    mass_slope_3_3 = models.FloatField("Mass Slope[3][3]", null=True, blank=True)

    mass_intercept_3_3 = models.FloatField("Mass Intercept[3][3]", null=True, blank=True)

    mass_slope_3_4 = models.FloatField("Mass Slope[3][4]", null=True, blank=True)

    mass_intercept_3_4 = models.FloatField("Mass Intercept[3][4]", null=True, blank=True)

    mass_slope_3_5 = models.FloatField("Mass Slope[3][5]", null=True, blank=True)

    mass_intercept_3_5 = models.FloatField("Mass Intercept[3][5]", null=True, blank=True)

    mass_slope_3_6 = models.FloatField("Mass Slope[3][6]", null=True, blank=True)

    mass_intercept_3_6 = models.FloatField("Mass Intercept[3][6]", null=True, blank=True)

    mass_slope_3_7 = models.FloatField("Mass Slope[3][7]", null=True, blank=True)

    mass_intercept_3_7 = models.FloatField("Mass Intercept[3][7]", null=True, blank=True)

    mass_slope_3_8 = models.FloatField("Mass Slope[3][8]", null=True, blank=True)

    mass_intercept_3_8 = models.FloatField("Mass Intercept[3][8]", null=True, blank=True)

    mass_slope_3_9 = models.FloatField("Mass Slope[3][9]", null=True, blank=True)

    mass_intercept_3_9 = models.FloatField("Mass Intercept[3][9]", null=True, blank=True)

    mass_slope_3_10 = models.FloatField("Mass Slope[3][10]", null=True, blank=True)

    mass_intercept_3_10 = models.FloatField("Mass Intercept[3][10]", null=True, blank=True)

    mass_slope_3_11 = models.FloatField("Mass Slope[3][11]", null=True, blank=True)

    mass_intercept_3_11 = models.FloatField("Mass Intercept[3][11]", null=True, blank=True)

    mass_slope_3_12 = models.FloatField("Mass Slope[3][12]", null=True, blank=True)

    mass_intercept_3_12 = models.FloatField("Mass Intercept[3][12]", null=True, blank=True)

    mass_slope_3_13 = models.FloatField("Mass Slope[3][13]", null=True, blank=True)

    mass_intercept_3_13 = models.FloatField("Mass Intercept[3][13]", null=True, blank=True)

    mass_slope_3_14 = models.FloatField("Mass Slope[3][14]", null=True, blank=True)

    mass_intercept_3_14 = models.FloatField("Mass Intercept[3][14]", null=True, blank=True)

    mass_slope_3_15 = models.FloatField("Mass Slope[3][15]", null=True, blank=True)

    mass_intercept_3_15 = models.FloatField("Mass Intercept[3][15]", null=True, blank=True)

    mass_slope_3_16 = models.FloatField("Mass Slope[3][16]", null=True, blank=True)

    mass_intercept_3_16 = models.FloatField("Mass Intercept[3][16]", null=True, blank=True)

    mass_slope_3_17 = models.FloatField("Mass Slope[3][17]", null=True, blank=True)

    mass_intercept_3_17 = models.FloatField("Mass Intercept[3][17]", null=True, blank=True)

    mass_slope_3_18 = models.FloatField("Mass Slope[3][18]", null=True, blank=True)

    mass_intercept_3_18 = models.FloatField("Mass Intercept[3][18]", null=True, blank=True)

    mass_slope_3_19 = models.FloatField("Mass Slope[3][19]", null=True, blank=True)

    mass_intercept_3_19 = models.FloatField("Mass Intercept[3][19]", null=True, blank=True)

    mass_slope_4_0 = models.FloatField("Mass Slope[4][0]", null=True, blank=True)

    mass_intercept_4_0 = models.FloatField("Mass Intercept[4][0]", null=True, blank=True)

    mass_slope_4_1 = models.FloatField("Mass Slope[4][1]", null=True, blank=True)

    mass_intercept_4_1 = models.FloatField("Mass Intercept[4][1]", null=True, blank=True)

    mass_slope_4_2 = models.FloatField("Mass Slope[4][2]", null=True, blank=True)

    mass_intercept_4_2 = models.FloatField("Mass Intercept[4][2]", null=True, blank=True)

    mass_slope_4_3 = models.FloatField("Mass Slope[4][3]", null=True, blank=True)

    mass_intercept_4_3 = models.FloatField("Mass Intercept[4][3]", null=True, blank=True)

    mass_slope_4_4 = models.FloatField("Mass Slope[4][4]", null=True, blank=True)

    mass_intercept_4_4 = models.FloatField("Mass Intercept[4][4]", null=True, blank=True)

    mass_slope_4_5 = models.FloatField("Mass Slope[4][5]", null=True, blank=True)

    mass_intercept_4_5 = models.FloatField("Mass Intercept[4][5]", null=True, blank=True)

    mass_slope_4_6 = models.FloatField("Mass Slope[4][6]", null=True, blank=True)

    mass_intercept_4_6 = models.FloatField("Mass Intercept[4][6]", null=True, blank=True)

    mass_slope_4_7 = models.FloatField("Mass Slope[4][7]", null=True, blank=True)

    mass_intercept_4_7 = models.FloatField("Mass Intercept[4][7]", null=True, blank=True)

    mass_slope_4_8 = models.FloatField("Mass Slope[4][8]", null=True, blank=True)

    mass_intercept_4_8 = models.FloatField("Mass Intercept[4][8]", null=True, blank=True)

    mass_slope_4_9 = models.FloatField("Mass Slope[4][9]", null=True, blank=True)

    mass_intercept_4_9 = models.FloatField("Mass Intercept[4][9]", null=True, blank=True)

    mass_slope_4_10 = models.FloatField("Mass Slope[4][10]", null=True, blank=True)

    mass_intercept_4_10 = models.FloatField("Mass Intercept[4][10]", null=True, blank=True)

    mass_slope_4_11 = models.FloatField("Mass Slope[4][11]", null=True, blank=True)

    mass_intercept_4_11 = models.FloatField("Mass Intercept[4][11]", null=True, blank=True)

    mass_slope_4_12 = models.FloatField("Mass Slope[4][12]", null=True, blank=True)

    mass_intercept_4_12 = models.FloatField("Mass Intercept[4][12]", null=True, blank=True)

    mass_slope_4_13 = models.FloatField("Mass Slope[4][13]", null=True, blank=True)

    mass_intercept_4_13 = models.FloatField("Mass Intercept[4][13]", null=True, blank=True)

    mass_slope_4_14 = models.FloatField("Mass Slope[4][14]", null=True, blank=True)

    mass_intercept_4_14 = models.FloatField("Mass Intercept[4][14]", null=True, blank=True)

    mass_slope_4_15 = models.FloatField("Mass Slope[4][15]", null=True, blank=True)

    mass_intercept_4_15 = models.FloatField("Mass Intercept[4][15]", null=True, blank=True)

    mass_slope_4_16 = models.FloatField("Mass Slope[4][16]", null=True, blank=True)

    mass_intercept_4_16 = models.FloatField("Mass Intercept[4][16]", null=True, blank=True)

    mass_slope_4_17 = models.FloatField("Mass Slope[4][17]", null=True, blank=True)

    mass_intercept_4_17 = models.FloatField("Mass Intercept[4][17]", null=True, blank=True)

    mass_slope_4_18 = models.FloatField("Mass Slope[4][18]", null=True, blank=True)

    mass_intercept_4_18 = models.FloatField("Mass Intercept[4][18]", null=True, blank=True)

    mass_slope_4_19 = models.FloatField("Mass Slope[4][19]", null=True, blank=True)

    mass_intercept_4_19 = models.FloatField("Mass Intercept[4][19]", null=True, blank=True)

    mass_slope_5_0 = models.FloatField("Mass Slope[5][0]", null=True, blank=True)

    mass_intercept_5_0 = models.FloatField("Mass Intercept[5][0]", null=True, blank=True)

    mass_slope_5_1 = models.FloatField("Mass Slope[5][1]", null=True, blank=True)

    mass_intercept_5_1 = models.FloatField("Mass Intercept[5][1]", null=True, blank=True)

    mass_slope_5_2 = models.FloatField("Mass Slope[5][2]", null=True, blank=True)

    mass_intercept_5_2 = models.FloatField("Mass Intercept[5][2]", null=True, blank=True)

    mass_slope_5_3 = models.FloatField("Mass Slope[5][3]", null=True, blank=True)

    mass_intercept_5_3 = models.FloatField("Mass Intercept[5][3]", null=True, blank=True)

    mass_slope_5_4 = models.FloatField("Mass Slope[5][4]", null=True, blank=True)

    mass_intercept_5_4 = models.FloatField("Mass Intercept[5][4]", null=True, blank=True)

    mass_slope_5_5 = models.FloatField("Mass Slope[5][5]", null=True, blank=True)

    mass_intercept_5_5 = models.FloatField("Mass Intercept[5][5]", null=True, blank=True)

    mass_slope_5_6 = models.FloatField("Mass Slope[5][6]", null=True, blank=True)

    mass_intercept_5_6 = models.FloatField("Mass Intercept[5][6]", null=True, blank=True)

    mass_slope_5_7 = models.FloatField("Mass Slope[5][7]", null=True, blank=True)

    mass_intercept_5_7 = models.FloatField("Mass Intercept[5][7]", null=True, blank=True)

    mass_slope_5_8 = models.FloatField("Mass Slope[5][8]", null=True, blank=True)

    mass_intercept_5_8 = models.FloatField("Mass Intercept[5][8]", null=True, blank=True)

    mass_slope_5_9 = models.FloatField("Mass Slope[5][9]", null=True, blank=True)

    mass_intercept_5_9 = models.FloatField("Mass Intercept[5][9]", null=True, blank=True)

    mass_slope_5_10 = models.FloatField("Mass Slope[5][10]", null=True, blank=True)

    mass_intercept_5_10 = models.FloatField("Mass Intercept[5][10]", null=True, blank=True)

    mass_slope_5_11 = models.FloatField("Mass Slope[5][11]", null=True, blank=True)

    mass_intercept_5_11 = models.FloatField("Mass Intercept[5][11]", null=True, blank=True)

    mass_slope_5_12 = models.FloatField("Mass Slope[5][12]", null=True, blank=True)

    mass_intercept_5_12 = models.FloatField("Mass Intercept[5][12]", null=True, blank=True)

    mass_slope_5_13 = models.FloatField("Mass Slope[5][13]", null=True, blank=True)

    mass_intercept_5_13 = models.FloatField("Mass Intercept[5][13]", null=True, blank=True)

    mass_slope_5_14 = models.FloatField("Mass Slope[5][14]", null=True, blank=True)

    mass_intercept_5_14 = models.FloatField("Mass Intercept[5][14]", null=True, blank=True)

    mass_slope_5_15 = models.FloatField("Mass Slope[5][15]", null=True, blank=True)

    mass_intercept_5_15 = models.FloatField("Mass Intercept[5][15]", null=True, blank=True)

    mass_slope_5_16 = models.FloatField("Mass Slope[5][16]", null=True, blank=True)

    mass_intercept_5_16 = models.FloatField("Mass Intercept[5][16]", null=True, blank=True)

    mass_slope_5_17 = models.FloatField("Mass Slope[5][17]", null=True, blank=True)

    mass_intercept_5_17 = models.FloatField("Mass Intercept[5][17]", null=True, blank=True)

    mass_slope_5_18 = models.FloatField("Mass Slope[5][18]", null=True, blank=True)

    mass_intercept_5_18 = models.FloatField("Mass Intercept[5][18]", null=True, blank=True)

    mass_slope_5_19 = models.FloatField("Mass Slope[5][19]", null=True, blank=True)

    mass_intercept_5_19 = models.FloatField("Mass Intercept[5][19]", null=True, blank=True)

    mass_slope_6_0 = models.FloatField("Mass Slope[6][0]", null=True, blank=True)

    mass_intercept_6_0 = models.FloatField("Mass Intercept[6][0]", null=True, blank=True)

    mass_slope_6_1 = models.FloatField("Mass Slope[6][1]", null=True, blank=True)

    mass_intercept_6_1 = models.FloatField("Mass Intercept[6][1]", null=True, blank=True)

    mass_slope_6_2 = models.FloatField("Mass Slope[6][2]", null=True, blank=True)

    mass_intercept_6_2 = models.FloatField("Mass Intercept[6][2]", null=True, blank=True)

    mass_slope_6_3 = models.FloatField("Mass Slope[6][3]", null=True, blank=True)

    mass_intercept_6_3 = models.FloatField("Mass Intercept[6][3]", null=True, blank=True)

    mass_slope_6_4 = models.FloatField("Mass Slope[6][4]", null=True, blank=True)

    mass_intercept_6_4 = models.FloatField("Mass Intercept[6][4]", null=True, blank=True)

    mass_slope_6_5 = models.FloatField("Mass Slope[6][5]", null=True, blank=True)

    mass_intercept_6_5 = models.FloatField("Mass Intercept[6][5]", null=True, blank=True)

    mass_slope_6_6 = models.FloatField("Mass Slope[6][6]", null=True, blank=True)

    mass_intercept_6_6 = models.FloatField("Mass Intercept[6][6]", null=True, blank=True)

    mass_slope_6_7 = models.FloatField("Mass Slope[6][7]", null=True, blank=True)

    mass_intercept_6_7 = models.FloatField("Mass Intercept[6][7]", null=True, blank=True)

    mass_slope_6_8 = models.FloatField("Mass Slope[6][8]", null=True, blank=True)

    mass_intercept_6_8 = models.FloatField("Mass Intercept[6][8]", null=True, blank=True)

    mass_slope_6_9 = models.FloatField("Mass Slope[6][9]", null=True, blank=True)

    mass_intercept_6_9 = models.FloatField("Mass Intercept[6][9]", null=True, blank=True)

    mass_slope_6_10 = models.FloatField("Mass Slope[6][10]", null=True, blank=True)

    mass_intercept_6_10 = models.FloatField("Mass Intercept[6][10]", null=True, blank=True)

    mass_slope_6_11 = models.FloatField("Mass Slope[6][11]", null=True, blank=True)

    mass_intercept_6_11 = models.FloatField("Mass Intercept[6][11]", null=True, blank=True)

    mass_slope_6_12 = models.FloatField("Mass Slope[6][12]", null=True, blank=True)

    mass_intercept_6_12 = models.FloatField("Mass Intercept[6][12]", null=True, blank=True)

    mass_slope_6_13 = models.FloatField("Mass Slope[6][13]", null=True, blank=True)

    mass_intercept_6_13 = models.FloatField("Mass Intercept[6][13]", null=True, blank=True)

    mass_slope_6_14 = models.FloatField("Mass Slope[6][14]", null=True, blank=True)

    mass_intercept_6_14 = models.FloatField("Mass Intercept[6][14]", null=True, blank=True)

    mass_slope_6_15 = models.FloatField("Mass Slope[6][15]", null=True, blank=True)

    mass_intercept_6_15 = models.FloatField("Mass Intercept[6][15]", null=True, blank=True)

    mass_slope_6_16 = models.FloatField("Mass Slope[6][16]", null=True, blank=True)

    mass_intercept_6_16 = models.FloatField("Mass Intercept[6][16]", null=True, blank=True)

    mass_slope_6_17 = models.FloatField("Mass Slope[6][17]", null=True, blank=True)

    mass_intercept_6_17 = models.FloatField("Mass Intercept[6][17]", null=True, blank=True)

    mass_slope_6_18 = models.FloatField("Mass Slope[6][18]", null=True, blank=True)

    mass_intercept_6_18 = models.FloatField("Mass Intercept[6][18]", null=True, blank=True)

    mass_slope_6_19 = models.FloatField("Mass Slope[6][19]", null=True, blank=True)

    mass_intercept_6_19 = models.FloatField("Mass Intercept[6][19]", null=True, blank=True)

    mass_slope_7_0 = models.FloatField("Mass Slope[7][0]", null=True, blank=True)

    mass_intercept_7_0 = models.FloatField("Mass Intercept[7][0]", null=True, blank=True)

    mass_slope_7_1 = models.FloatField("Mass Slope[7][1]", null=True, blank=True)

    mass_intercept_7_1 = models.FloatField("Mass Intercept[7][1]", null=True, blank=True)

    mass_slope_7_2 = models.FloatField("Mass Slope[7][2]", null=True, blank=True)

    mass_intercept_7_2 = models.FloatField("Mass Intercept[7][2]", null=True, blank=True)

    mass_slope_7_3 = models.FloatField("Mass Slope[7][3]", null=True, blank=True)

    mass_intercept_7_3 = models.FloatField("Mass Intercept[7][3]", null=True, blank=True)

    mass_slope_7_4 = models.FloatField("Mass Slope[7][4]", null=True, blank=True)

    mass_intercept_7_4 = models.FloatField("Mass Intercept[7][4]", null=True, blank=True)

    mass_slope_7_5 = models.FloatField("Mass Slope[7][5]", null=True, blank=True)

    mass_intercept_7_5 = models.FloatField("Mass Intercept[7][5]", null=True, blank=True)

    mass_slope_7_6 = models.FloatField("Mass Slope[7][6]", null=True, blank=True)

    mass_intercept_7_6 = models.FloatField("Mass Intercept[7][6]", null=True, blank=True)

    mass_slope_7_7 = models.FloatField("Mass Slope[7][7]", null=True, blank=True)

    mass_intercept_7_7 = models.FloatField("Mass Intercept[7][7]", null=True, blank=True)

    mass_slope_7_8 = models.FloatField("Mass Slope[7][8]", null=True, blank=True)

    mass_intercept_7_8 = models.FloatField("Mass Intercept[7][8]", null=True, blank=True)

    mass_slope_7_9 = models.FloatField("Mass Slope[7][9]", null=True, blank=True)

    mass_intercept_7_9 = models.FloatField("Mass Intercept[7][9]", null=True, blank=True)

    mass_slope_7_10 = models.FloatField("Mass Slope[7][10]", null=True, blank=True)

    mass_intercept_7_10 = models.FloatField("Mass Intercept[7][10]", null=True, blank=True)

    mass_slope_7_11 = models.FloatField("Mass Slope[7][11]", null=True, blank=True)

    mass_intercept_7_11 = models.FloatField("Mass Intercept[7][11]", null=True, blank=True)

    mass_slope_7_12 = models.FloatField("Mass Slope[7][12]", null=True, blank=True)

    mass_intercept_7_12 = models.FloatField("Mass Intercept[7][12]", null=True, blank=True)

    mass_slope_7_13 = models.FloatField("Mass Slope[7][13]", null=True, blank=True)

    mass_intercept_7_13 = models.FloatField("Mass Intercept[7][13]", null=True, blank=True)

    mass_slope_7_14 = models.FloatField("Mass Slope[7][14]", null=True, blank=True)

    mass_intercept_7_14 = models.FloatField("Mass Intercept[7][14]", null=True, blank=True)

    mass_slope_7_15 = models.FloatField("Mass Slope[7][15]", null=True, blank=True)

    mass_intercept_7_15 = models.FloatField("Mass Intercept[7][15]", null=True, blank=True)

    mass_slope_7_16 = models.FloatField("Mass Slope[7][16]", null=True, blank=True)

    mass_intercept_7_16 = models.FloatField("Mass Intercept[7][16]", null=True, blank=True)

    mass_slope_7_17 = models.FloatField("Mass Slope[7][17]", null=True, blank=True)

    mass_intercept_7_17 = models.FloatField("Mass Intercept[7][17]", null=True, blank=True)

    mass_slope_7_18 = models.FloatField("Mass Slope[7][18]", null=True, blank=True)

    mass_intercept_7_18 = models.FloatField("Mass Intercept[7][18]", null=True, blank=True)

    mass_slope_7_19 = models.FloatField("Mass Slope[7][19]", null=True, blank=True)

    mass_intercept_7_19 = models.FloatField("Mass Intercept[7][19]", null=True, blank=True)

    mass_slope_8_0 = models.FloatField("Mass Slope[8][0]", null=True, blank=True)

    mass_intercept_8_0 = models.FloatField("Mass Intercept[8][0]", null=True, blank=True)

    mass_slope_8_1 = models.FloatField("Mass Slope[8][1]", null=True, blank=True)

    mass_intercept_8_1 = models.FloatField("Mass Intercept[8][1]", null=True, blank=True)

    mass_slope_8_2 = models.FloatField("Mass Slope[8][2]", null=True, blank=True)

    mass_intercept_8_2 = models.FloatField("Mass Intercept[8][2]", null=True, blank=True)

    mass_slope_8_3 = models.FloatField("Mass Slope[8][3]", null=True, blank=True)

    mass_intercept_8_3 = models.FloatField("Mass Intercept[8][3]", null=True, blank=True)

    mass_slope_8_4 = models.FloatField("Mass Slope[8][4]", null=True, blank=True)

    mass_intercept_8_4 = models.FloatField("Mass Intercept[8][4]", null=True, blank=True)

    mass_slope_8_5 = models.FloatField("Mass Slope[8][5]", null=True, blank=True)

    mass_intercept_8_5 = models.FloatField("Mass Intercept[8][5]", null=True, blank=True)

    mass_slope_8_6 = models.FloatField("Mass Slope[8][6]", null=True, blank=True)

    mass_intercept_8_6 = models.FloatField("Mass Intercept[8][6]", null=True, blank=True)

    mass_slope_8_7 = models.FloatField("Mass Slope[8][7]", null=True, blank=True)

    mass_intercept_8_7 = models.FloatField("Mass Intercept[8][7]", null=True, blank=True)

    mass_slope_8_8 = models.FloatField("Mass Slope[8][8]", null=True, blank=True)

    mass_intercept_8_8 = models.FloatField("Mass Intercept[8][8]", null=True, blank=True)

    mass_slope_8_9 = models.FloatField("Mass Slope[8][9]", null=True, blank=True)

    mass_intercept_8_9 = models.FloatField("Mass Intercept[8][9]", null=True, blank=True)

    mass_slope_8_10 = models.FloatField("Mass Slope[8][10]", null=True, blank=True)

    mass_intercept_8_10 = models.FloatField("Mass Intercept[8][10]", null=True, blank=True)

    mass_slope_8_11 = models.FloatField("Mass Slope[8][11]", null=True, blank=True)

    mass_intercept_8_11 = models.FloatField("Mass Intercept[8][11]", null=True, blank=True)

    mass_slope_8_12 = models.FloatField("Mass Slope[8][12]", null=True, blank=True)

    mass_intercept_8_12 = models.FloatField("Mass Intercept[8][12]", null=True, blank=True)

    mass_slope_8_13 = models.FloatField("Mass Slope[8][13]", null=True, blank=True)

    mass_intercept_8_13 = models.FloatField("Mass Intercept[8][13]", null=True, blank=True)

    mass_slope_8_14 = models.FloatField("Mass Slope[8][14]", null=True, blank=True)

    mass_intercept_8_14 = models.FloatField("Mass Intercept[8][14]", null=True, blank=True)

    mass_slope_8_15 = models.FloatField("Mass Slope[8][15]", null=True, blank=True)

    mass_intercept_8_15 = models.FloatField("Mass Intercept[8][15]", null=True, blank=True)

    mass_slope_8_16 = models.FloatField("Mass Slope[8][16]", null=True, blank=True)

    mass_intercept_8_16 = models.FloatField("Mass Intercept[8][16]", null=True, blank=True)

    mass_slope_8_17 = models.FloatField("Mass Slope[8][17]", null=True, blank=True)

    mass_intercept_8_17 = models.FloatField("Mass Intercept[8][17]", null=True, blank=True)

    mass_slope_8_18 = models.FloatField("Mass Slope[8][18]", null=True, blank=True)

    mass_intercept_8_18 = models.FloatField("Mass Intercept[8][18]", null=True, blank=True)

    mass_slope_8_19 = models.FloatField("Mass Slope[8][19]", null=True, blank=True)

    mass_intercept_8_19 = models.FloatField("Mass Intercept[8][19]", null=True, blank=True)

    mass_slope_9_0 = models.FloatField("Mass Slope[9][0]", null=True, blank=True)

    mass_intercept_9_0 = models.FloatField("Mass Intercept[9][0]", null=True, blank=True)

    mass_slope_9_1 = models.FloatField("Mass Slope[9][1]", null=True, blank=True)

    mass_intercept_9_1 = models.FloatField("Mass Intercept[9][1]", null=True, blank=True)

    mass_slope_9_2 = models.FloatField("Mass Slope[9][2]", null=True, blank=True)

    mass_intercept_9_2 = models.FloatField("Mass Intercept[9][2]", null=True, blank=True)

    mass_slope_9_3 = models.FloatField("Mass Slope[9][3]", null=True, blank=True)

    mass_intercept_9_3 = models.FloatField("Mass Intercept[9][3]", null=True, blank=True)

    mass_slope_9_4 = models.FloatField("Mass Slope[9][4]", null=True, blank=True)

    mass_intercept_9_4 = models.FloatField("Mass Intercept[9][4]", null=True, blank=True)

    mass_slope_9_5 = models.FloatField("Mass Slope[9][5]", null=True, blank=True)

    mass_intercept_9_5 = models.FloatField("Mass Intercept[9][5]", null=True, blank=True)

    mass_slope_9_6 = models.FloatField("Mass Slope[9][6]", null=True, blank=True)

    mass_intercept_9_6 = models.FloatField("Mass Intercept[9][6]", null=True, blank=True)

    mass_slope_9_7 = models.FloatField("Mass Slope[9][7]", null=True, blank=True)

    mass_intercept_9_7 = models.FloatField("Mass Intercept[9][7]", null=True, blank=True)

    mass_slope_9_8 = models.FloatField("Mass Slope[9][8]", null=True, blank=True)

    mass_intercept_9_8 = models.FloatField("Mass Intercept[9][8]", null=True, blank=True)

    mass_slope_9_9 = models.FloatField("Mass Slope[9][9]", null=True, blank=True)

    mass_intercept_9_9 = models.FloatField("Mass Intercept[9][9]", null=True, blank=True)

    mass_slope_9_10 = models.FloatField("Mass Slope[9][10]", null=True, blank=True)

    mass_intercept_9_10 = models.FloatField("Mass Intercept[9][10]", null=True, blank=True)

    mass_slope_9_11 = models.FloatField("Mass Slope[9][11]", null=True, blank=True)

    mass_intercept_9_11 = models.FloatField("Mass Intercept[9][11]", null=True, blank=True)

    mass_slope_9_12 = models.FloatField("Mass Slope[9][12]", null=True, blank=True)

    mass_intercept_9_12 = models.FloatField("Mass Intercept[9][12]", null=True, blank=True)

    mass_slope_9_13 = models.FloatField("Mass Slope[9][13]", null=True, blank=True)

    mass_intercept_9_13 = models.FloatField("Mass Intercept[9][13]", null=True, blank=True)

    mass_slope_9_14 = models.FloatField("Mass Slope[9][14]", null=True, blank=True)

    mass_intercept_9_14 = models.FloatField("Mass Intercept[9][14]", null=True, blank=True)

    mass_slope_9_15 = models.FloatField("Mass Slope[9][15]", null=True, blank=True)

    mass_intercept_9_15 = models.FloatField("Mass Intercept[9][15]", null=True, blank=True)

    mass_slope_9_16 = models.FloatField("Mass Slope[9][16]", null=True, blank=True)

    mass_intercept_9_16 = models.FloatField("Mass Intercept[9][16]", null=True, blank=True)

    mass_slope_9_17 = models.FloatField("Mass Slope[9][17]", null=True, blank=True)

    mass_intercept_9_17 = models.FloatField("Mass Intercept[9][17]", null=True, blank=True)

    mass_slope_9_18 = models.FloatField("Mass Slope[9][18]", null=True, blank=True)

    mass_intercept_9_18 = models.FloatField("Mass Intercept[9][18]", null=True, blank=True)

    mass_slope_9_19 = models.FloatField("Mass Slope[9][19]", null=True, blank=True)

    mass_intercept_9_19 = models.FloatField("Mass Intercept[9][19]", null=True, blank=True)

    mass_slope_10_0 = models.FloatField("Mass Slope[10][0]", null=True, blank=True)

    mass_intercept_10_0 = models.FloatField("Mass Intercept[10][0]", null=True, blank=True)

    mass_slope_10_1 = models.FloatField("Mass Slope[10][1]", null=True, blank=True)

    mass_intercept_10_1 = models.FloatField("Mass Intercept[10][1]", null=True, blank=True)

    mass_slope_10_2 = models.FloatField("Mass Slope[10][2]", null=True, blank=True)

    mass_intercept_10_2 = models.FloatField("Mass Intercept[10][2]", null=True, blank=True)

    mass_slope_10_3 = models.FloatField("Mass Slope[10][3]", null=True, blank=True)

    mass_intercept_10_3 = models.FloatField("Mass Intercept[10][3]", null=True, blank=True)

    mass_slope_10_4 = models.FloatField("Mass Slope[10][4]", null=True, blank=True)

    mass_intercept_10_4 = models.FloatField("Mass Intercept[10][4]", null=True, blank=True)

    mass_slope_10_5 = models.FloatField("Mass Slope[10][5]", null=True, blank=True)

    mass_intercept_10_5 = models.FloatField("Mass Intercept[10][5]", null=True, blank=True)

    mass_slope_10_6 = models.FloatField("Mass Slope[10][6]", null=True, blank=True)

    mass_intercept_10_6 = models.FloatField("Mass Intercept[10][6]", null=True, blank=True)

    mass_slope_10_7 = models.FloatField("Mass Slope[10][7]", null=True, blank=True)

    mass_intercept_10_7 = models.FloatField("Mass Intercept[10][7]", null=True, blank=True)

    mass_slope_10_8 = models.FloatField("Mass Slope[10][8]", null=True, blank=True)

    mass_intercept_10_8 = models.FloatField("Mass Intercept[10][8]", null=True, blank=True)

    mass_slope_10_9 = models.FloatField("Mass Slope[10][9]", null=True, blank=True)

    mass_intercept_10_9 = models.FloatField("Mass Intercept[10][9]", null=True, blank=True)

    mass_slope_10_10 = models.FloatField("Mass Slope[10][10]", null=True, blank=True)

    mass_intercept_10_10 = models.FloatField("Mass Intercept[10][10]", null=True, blank=True)

    mass_slope_10_11 = models.FloatField("Mass Slope[10][11]", null=True, blank=True)

    mass_intercept_10_11 = models.FloatField("Mass Intercept[10][11]", null=True, blank=True)

    mass_slope_10_12 = models.FloatField("Mass Slope[10][12]", null=True, blank=True)

    mass_intercept_10_12 = models.FloatField("Mass Intercept[10][12]", null=True, blank=True)

    mass_slope_10_13 = models.FloatField("Mass Slope[10][13]", null=True, blank=True)

    mass_intercept_10_13 = models.FloatField("Mass Intercept[10][13]", null=True, blank=True)

    mass_slope_10_14 = models.FloatField("Mass Slope[10][14]", null=True, blank=True)

    mass_intercept_10_14 = models.FloatField("Mass Intercept[10][14]", null=True, blank=True)

    mass_slope_10_15 = models.FloatField("Mass Slope[10][15]", null=True, blank=True)

    mass_intercept_10_15 = models.FloatField("Mass Intercept[10][15]", null=True, blank=True)

    mass_slope_10_16 = models.FloatField("Mass Slope[10][16]", null=True, blank=True)

    mass_intercept_10_16 = models.FloatField("Mass Intercept[10][16]", null=True, blank=True)

    mass_slope_10_17 = models.FloatField("Mass Slope[10][17]", null=True, blank=True)

    mass_intercept_10_17 = models.FloatField("Mass Intercept[10][17]", null=True, blank=True)

    mass_slope_10_18 = models.FloatField("Mass Slope[10][18]", null=True, blank=True)

    mass_intercept_10_18 = models.FloatField("Mass Intercept[10][18]", null=True, blank=True)

    mass_slope_10_19 = models.FloatField("Mass Slope[10][19]", null=True, blank=True)

    mass_intercept_10_19 = models.FloatField("Mass Intercept[10][19]", null=True, blank=True)

    mass_slope_11_0 = models.FloatField("Mass Slope[11][0]", null=True, blank=True)

    mass_intercept_11_0 = models.FloatField("Mass Intercept[11][0]", null=True, blank=True)

    mass_slope_11_1 = models.FloatField("Mass Slope[11][1]", null=True, blank=True)

    mass_intercept_11_1 = models.FloatField("Mass Intercept[11][1]", null=True, blank=True)

    mass_slope_11_2 = models.FloatField("Mass Slope[11][2]", null=True, blank=True)

    mass_intercept_11_2 = models.FloatField("Mass Intercept[11][2]", null=True, blank=True)

    mass_slope_11_3 = models.FloatField("Mass Slope[11][3]", null=True, blank=True)

    mass_intercept_11_3 = models.FloatField("Mass Intercept[11][3]", null=True, blank=True)

    mass_slope_11_4 = models.FloatField("Mass Slope[11][4]", null=True, blank=True)

    mass_intercept_11_4 = models.FloatField("Mass Intercept[11][4]", null=True, blank=True)

    mass_slope_11_5 = models.FloatField("Mass Slope[11][5]", null=True, blank=True)

    mass_intercept_11_5 = models.FloatField("Mass Intercept[11][5]", null=True, blank=True)

    mass_slope_11_6 = models.FloatField("Mass Slope[11][6]", null=True, blank=True)

    mass_intercept_11_6 = models.FloatField("Mass Intercept[11][6]", null=True, blank=True)

    mass_slope_11_7 = models.FloatField("Mass Slope[11][7]", null=True, blank=True)

    mass_intercept_11_7 = models.FloatField("Mass Intercept[11][7]", null=True, blank=True)

    mass_slope_11_8 = models.FloatField("Mass Slope[11][8]", null=True, blank=True)

    mass_intercept_11_8 = models.FloatField("Mass Intercept[11][8]", null=True, blank=True)

    mass_slope_11_9 = models.FloatField("Mass Slope[11][9]", null=True, blank=True)

    mass_intercept_11_9 = models.FloatField("Mass Intercept[11][9]", null=True, blank=True)

    mass_slope_11_10 = models.FloatField("Mass Slope[11][10]", null=True, blank=True)

    mass_intercept_11_10 = models.FloatField("Mass Intercept[11][10]", null=True, blank=True)

    mass_slope_11_11 = models.FloatField("Mass Slope[11][11]", null=True, blank=True)

    mass_intercept_11_11 = models.FloatField("Mass Intercept[11][11]", null=True, blank=True)

    mass_slope_11_12 = models.FloatField("Mass Slope[11][12]", null=True, blank=True)

    mass_intercept_11_12 = models.FloatField("Mass Intercept[11][12]", null=True, blank=True)

    mass_slope_11_13 = models.FloatField("Mass Slope[11][13]", null=True, blank=True)

    mass_intercept_11_13 = models.FloatField("Mass Intercept[11][13]", null=True, blank=True)

    mass_slope_11_14 = models.FloatField("Mass Slope[11][14]", null=True, blank=True)

    mass_intercept_11_14 = models.FloatField("Mass Intercept[11][14]", null=True, blank=True)

    mass_slope_11_15 = models.FloatField("Mass Slope[11][15]", null=True, blank=True)

    mass_intercept_11_15 = models.FloatField("Mass Intercept[11][15]", null=True, blank=True)

    mass_slope_11_16 = models.FloatField("Mass Slope[11][16]", null=True, blank=True)

    mass_intercept_11_16 = models.FloatField("Mass Intercept[11][16]", null=True, blank=True)

    mass_slope_11_17 = models.FloatField("Mass Slope[11][17]", null=True, blank=True)

    mass_intercept_11_17 = models.FloatField("Mass Intercept[11][17]", null=True, blank=True)

    mass_slope_11_18 = models.FloatField("Mass Slope[11][18]", null=True, blank=True)

    mass_intercept_11_18 = models.FloatField("Mass Intercept[11][18]", null=True, blank=True)

    mass_slope_11_19 = models.FloatField("Mass Slope[11][19]", null=True, blank=True)

    mass_intercept_11_19 = models.FloatField("Mass Intercept[11][19]", null=True, blank=True)

    mass_slope_12_0 = models.FloatField("Mass Slope[12][0]", null=True, blank=True)

    mass_intercept_12_0 = models.FloatField("Mass Intercept[12][0]", null=True, blank=True)

    mass_slope_12_1 = models.FloatField("Mass Slope[12][1]", null=True, blank=True)

    mass_intercept_12_1 = models.FloatField("Mass Intercept[12][1]", null=True, blank=True)

    mass_slope_12_2 = models.FloatField("Mass Slope[12][2]", null=True, blank=True)

    mass_intercept_12_2 = models.FloatField("Mass Intercept[12][2]", null=True, blank=True)

    mass_slope_12_3 = models.FloatField("Mass Slope[12][3]", null=True, blank=True)

    mass_intercept_12_3 = models.FloatField("Mass Intercept[12][3]", null=True, blank=True)

    mass_slope_12_4 = models.FloatField("Mass Slope[12][4]", null=True, blank=True)

    mass_intercept_12_4 = models.FloatField("Mass Intercept[12][4]", null=True, blank=True)

    mass_slope_12_5 = models.FloatField("Mass Slope[12][5]", null=True, blank=True)

    mass_intercept_12_5 = models.FloatField("Mass Intercept[12][5]", null=True, blank=True)

    mass_slope_12_6 = models.FloatField("Mass Slope[12][6]", null=True, blank=True)

    mass_intercept_12_6 = models.FloatField("Mass Intercept[12][6]", null=True, blank=True)

    mass_slope_12_7 = models.FloatField("Mass Slope[12][7]", null=True, blank=True)

    mass_intercept_12_7 = models.FloatField("Mass Intercept[12][7]", null=True, blank=True)

    mass_slope_12_8 = models.FloatField("Mass Slope[12][8]", null=True, blank=True)

    mass_intercept_12_8 = models.FloatField("Mass Intercept[12][8]", null=True, blank=True)

    mass_slope_12_9 = models.FloatField("Mass Slope[12][9]", null=True, blank=True)

    mass_intercept_12_9 = models.FloatField("Mass Intercept[12][9]", null=True, blank=True)

    mass_slope_12_10 = models.FloatField("Mass Slope[12][10]", null=True, blank=True)

    mass_intercept_12_10 = models.FloatField("Mass Intercept[12][10]", null=True, blank=True)

    mass_slope_12_11 = models.FloatField("Mass Slope[12][11]", null=True, blank=True)

    mass_intercept_12_11 = models.FloatField("Mass Intercept[12][11]", null=True, blank=True)

    mass_slope_12_12 = models.FloatField("Mass Slope[12][12]", null=True, blank=True)

    mass_intercept_12_12 = models.FloatField("Mass Intercept[12][12]", null=True, blank=True)

    mass_slope_12_13 = models.FloatField("Mass Slope[12][13]", null=True, blank=True)

    mass_intercept_12_13 = models.FloatField("Mass Intercept[12][13]", null=True, blank=True)

    mass_slope_12_14 = models.FloatField("Mass Slope[12][14]", null=True, blank=True)

    mass_intercept_12_14 = models.FloatField("Mass Intercept[12][14]", null=True, blank=True)

    mass_slope_12_15 = models.FloatField("Mass Slope[12][15]", null=True, blank=True)

    mass_intercept_12_15 = models.FloatField("Mass Intercept[12][15]", null=True, blank=True)

    mass_slope_12_16 = models.FloatField("Mass Slope[12][16]", null=True, blank=True)

    mass_intercept_12_16 = models.FloatField("Mass Intercept[12][16]", null=True, blank=True)

    mass_slope_12_17 = models.FloatField("Mass Slope[12][17]", null=True, blank=True)

    mass_intercept_12_17 = models.FloatField("Mass Intercept[12][17]", null=True, blank=True)

    mass_slope_12_18 = models.FloatField("Mass Slope[12][18]", null=True, blank=True)

    mass_intercept_12_18 = models.FloatField("Mass Intercept[12][18]", null=True, blank=True)

    mass_slope_12_19 = models.FloatField("Mass Slope[12][19]", null=True, blank=True)

    mass_intercept_12_19 = models.FloatField("Mass Intercept[12][19]", null=True, blank=True)






class MetaCalibrationFileValueFtCal(models.Model):


    class Meta:
        verbose_name = "Meta: Calibration File Value FtCal"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Meta')

    ft_caldot_item_1 = models.FloatField("FT Cal. Item 1", null=True, blank=True)

    ft_caldot_item_2 = models.FloatField("FT Cal. Item 2", null=True, blank=True)

    ft_caldot_item_3 = models.FloatField("FT Cal. Item 3", null=True, blank=True)

    ft_caldot_item_4 = models.FloatField("FT Cal. Item 4", null=True, blank=True)

    ft_caldot_item_5 = models.FloatField("FT Cal. Item 5", null=True, blank=True)

    ft_caldot_item_6 = models.FloatField("FT Cal. Item 6", null=True, blank=True)

    ft_caldot_item_7 = models.FloatField("FT Cal. Item 7", null=True, blank=True)

    ft_caldot_item_8 = models.FloatField("FT Cal. Item 8", null=True, blank=True)

    ft_caldot_item_9 = models.FloatField("FT Cal. Item 9", null=True, blank=True)

    ft_caldot_item_10 = models.FloatField("FT Cal. Item 10", null=True, blank=True)

    ft_caldot_item_11 = models.FloatField("FT Cal. Item 11", null=True, blank=True)

    ft_caldot_item_12 = models.FloatField("FT Cal. Item 12", null=True, blank=True)

    ft_caldot_item_13 = models.FloatField("FT Cal. Item 13", null=True, blank=True)

    ft_caldot_item_14 = models.FloatField("FT Cal. Item 14", null=True, blank=True)

    ft_caldot_item_15 = models.FloatField("FT Cal. Item 15", null=True, blank=True)

    ft_caldot_item_16 = models.FloatField("FT Cal. Item 16", null=True, blank=True)

    ft_caldot_item_17 = models.FloatField("FT Cal. Item 17", null=True, blank=True)

    ft_caldot_item_18 = models.FloatField("FT Cal. Item 18", null=True, blank=True)

    ft_caldot_item_19 = models.FloatField("FT Cal. Item 19", null=True, blank=True)

    ft_caldot_item_20 = models.FloatField("FT Cal. Item 20", null=True, blank=True)

    ft_caldot_item_21 = models.FloatField("FT Cal. Item 21", null=True, blank=True)

    ft_caldot_item_22 = models.FloatField("FT Cal. Item 22", null=True, blank=True)

    ft_caldot_item_23 = models.FloatField("FT Cal. Item 23", null=True, blank=True)

    ft_caldot_item_24 = models.FloatField("FT Cal. Item 24", null=True, blank=True)

    ft_caldot_item_25 = models.FloatField("FT Cal. Item 25", null=True, blank=True)

    ft_caldot_item_26 = models.FloatField("FT Cal. Item 26", null=True, blank=True)

    ft_caldot_item_27 = models.FloatField("FT Cal. Item 27", null=True, blank=True)

    ft_caldot_item_28 = models.FloatField("FT Cal. Item 28", null=True, blank=True)

    ft_caldot_item_29 = models.FloatField("FT Cal. Item 29", null=True, blank=True)

    ft_caldot_item_30 = models.FloatField("FT Cal. Item 30", null=True, blank=True)

    ft_caldot_item_31 = models.FloatField("FT Cal. Item 31", null=True, blank=True)

    ft_caldot_item_32 = models.FloatField("FT Cal. Item 32", null=True, blank=True)

    ft_caldot_item_33 = models.FloatField("FT Cal. Item 33", null=True, blank=True)

    ft_caldot_item_34 = models.FloatField("FT Cal. Item 34", null=True, blank=True)

    ft_caldot_item_35 = models.FloatField("FT Cal. Item 35", null=True, blank=True)

    ft_caldot_item_36 = models.FloatField("FT Cal. Item 36", null=True, blank=True)

    ft_caldot_item_37 = models.FloatField("FT Cal. Item 37", null=True, blank=True)

    ft_caldot_item_38 = models.FloatField("FT Cal. Item 38", null=True, blank=True)

    ft_caldot_item_39 = models.FloatField("FT Cal. Item 39", null=True, blank=True)

    ft_caldot_item_40 = models.FloatField("FT Cal. Item 40", null=True, blank=True)

    ft_caldot_item_41 = models.FloatField("FT Cal. Item 41", null=True, blank=True)

    ft_caldot_item_42 = models.FloatField("FT Cal. Item 42", null=True, blank=True)

    ft_caldot_item_43 = models.FloatField("FT Cal. Item 43", null=True, blank=True)

    ft_caldot_item_44 = models.FloatField("FT Cal. Item 44", null=True, blank=True)

    ft_caldot_item_45 = models.FloatField("FT Cal. Item 45", null=True, blank=True)

    ft_caldot_item_46 = models.FloatField("FT Cal. Item 46", null=True, blank=True)

    ft_caldot_item_47 = models.FloatField("FT Cal. Item 47", null=True, blank=True)

    ft_caldot_item_48 = models.FloatField("FT Cal. Item 48", null=True, blank=True)

    ft_caldot_item_49 = models.FloatField("FT Cal. Item 49", null=True, blank=True)

    ft_caldot_item_50 = models.FloatField("FT Cal. Item 50", null=True, blank=True)

    ft_caldot_item_51 = models.FloatField("FT Cal. Item 51", null=True, blank=True)

    ft_caldot_item_52 = models.FloatField("FT Cal. Item 52", null=True, blank=True)

    ft_caldot_item_53 = models.FloatField("FT Cal. Item 53", null=True, blank=True)

    ft_caldot_item_54 = models.FloatField("FT Cal. Item 54", null=True, blank=True)

    ft_caldot_item_55 = models.FloatField("FT Cal. Item 55", null=True, blank=True)

    ft_caldot_item_56 = models.FloatField("FT Cal. Item 56", null=True, blank=True)

    ft_caldot_item_57 = models.FloatField("FT Cal. Item 57", null=True, blank=True)

    ft_caldot_item_58 = models.FloatField("FT Cal. Item 58", null=True, blank=True)

    ft_caldot_item_59 = models.FloatField("FT Cal. Item 59", null=True, blank=True)

    ft_caldot_item_60 = models.FloatField("FT Cal. Item 60", null=True, blank=True)

    ft_caldot_item_61 = models.FloatField("FT Cal. Item 61", null=True, blank=True)

    ft_caldot_item_62 = models.FloatField("FT Cal. Item 62", null=True, blank=True)

    ft_caldot_item_63 = models.FloatField("FT Cal. Item 63", null=True, blank=True)

    ft_caldot_item_64 = models.FloatField("FT Cal. Item 64", null=True, blank=True)

    ft_caldot_item_65 = models.FloatField("FT Cal. Item 65", null=True, blank=True)

    ft_caldot_item_66 = models.FloatField("FT Cal. Item 66", null=True, blank=True)

    ft_caldot_item_67 = models.FloatField("FT Cal. Item 67", null=True, blank=True)

    ft_caldot_item_68 = models.FloatField("FT Cal. Item 68", null=True, blank=True)

    ft_caldot_item_69 = models.FloatField("FT Cal. Item 69", null=True, blank=True)

    ft_caldot_item_70 = models.FloatField("FT Cal. Item 70", null=True, blank=True)

    ft_caldot_item_71 = models.FloatField("FT Cal. Item 71", null=True, blank=True)

    ft_caldot_item_72 = models.FloatField("FT Cal. Item 72", null=True, blank=True)

    ft_caldot_item_73 = models.FloatField("FT Cal. Item 73", null=True, blank=True)

    ft_caldot_item_74 = models.FloatField("FT Cal. Item 74", null=True, blank=True)

    ft_caldot_item_75 = models.FloatField("FT Cal. Item 75", null=True, blank=True)

    ft_caldot_item_76 = models.FloatField("FT Cal. Item 76", null=True, blank=True)

    ft_caldot_item_77 = models.FloatField("FT Cal. Item 77", null=True, blank=True)

    ft_caldot_item_78 = models.FloatField("FT Cal. Item 78", null=True, blank=True)

    ft_caldot_item_79 = models.FloatField("FT Cal. Item 79", null=True, blank=True)

    ft_caldot_item_80 = models.FloatField("FT Cal. Item 80", null=True, blank=True)

    ft_caldot_item_81 = models.FloatField("FT Cal. Item 81", null=True, blank=True)

    ft_caldot_item_82 = models.FloatField("FT Cal. Item 82", null=True, blank=True)

    ft_caldot_item_83 = models.FloatField("FT Cal. Item 83", null=True, blank=True)

    ft_caldot_item_84 = models.FloatField("FT Cal. Item 84", null=True, blank=True)

    ft_caldot_item_85 = models.FloatField("FT Cal. Item 85", null=True, blank=True)

    ft_caldot_item_86 = models.FloatField("FT Cal. Item 86", null=True, blank=True)

    ft_caldot_item_87 = models.FloatField("FT Cal. Item 87", null=True, blank=True)

    ft_caldot_item_88 = models.FloatField("FT Cal. Item 88", null=True, blank=True)

    ft_caldot_item_89 = models.FloatField("FT Cal. Item 89", null=True, blank=True)

    ft_caldot_item_90 = models.FloatField("FT Cal. Item 90", null=True, blank=True)

    ft_caldot_item_91 = models.FloatField("FT Cal. Item 91", null=True, blank=True)

    ft_caldot_item_92 = models.FloatField("FT Cal. Item 92", null=True, blank=True)

    ft_caldot_item_93 = models.FloatField("FT Cal. Item 93", null=True, blank=True)

    ft_caldot_item_94 = models.FloatField("FT Cal. Item 94", null=True, blank=True)

    ft_caldot_item_95 = models.FloatField("FT Cal. Item 95", null=True, blank=True)

    ft_caldot_item_96 = models.FloatField("FT Cal. Item 96", null=True, blank=True)

    ft_caldot_item_97 = models.FloatField("FT Cal. Item 97", null=True, blank=True)

    ft_caldot_item_98 = models.FloatField("FT Cal. Item 98", null=True, blank=True)

    ft_caldot_item_99 = models.FloatField("FT Cal. Item 99", null=True, blank=True)

    ft_caldot_item_100 = models.FloatField("FT Cal. Item 100", null=True, blank=True)

    ft_caldot_item_101 = models.FloatField("FT Cal. Item 101", null=True, blank=True)

    ft_caldot_item_102 = models.FloatField("FT Cal. Item 102", null=True, blank=True)

    ft_caldot_item_103 = models.FloatField("FT Cal. Item 103", null=True, blank=True)

    ft_caldot_item_104 = models.FloatField("FT Cal. Item 104", null=True, blank=True)

    ft_caldot_item_105 = models.FloatField("FT Cal. Item 105", null=True, blank=True)

    ft_caldot_item_106 = models.FloatField("FT Cal. Item 106", null=True, blank=True)

    ft_caldot_item_107 = models.FloatField("FT Cal. Item 107", null=True, blank=True)

    ft_caldot_item_108 = models.FloatField("FT Cal. Item 108", null=True, blank=True)

    ft_caldot_item_109 = models.FloatField("FT Cal. Item 109", null=True, blank=True)

    ft_caldot_item_110 = models.FloatField("FT Cal. Item 110", null=True, blank=True)

    ft_caldot_item_111 = models.FloatField("FT Cal. Item 111", null=True, blank=True)

    ft_caldot_item_112 = models.FloatField("FT Cal. Item 112", null=True, blank=True)

    ft_caldot_item_113 = models.FloatField("FT Cal. Item 113", null=True, blank=True)

    ft_caldot_item_114 = models.FloatField("FT Cal. Item 114", null=True, blank=True)

    ft_caldot_item_115 = models.FloatField("FT Cal. Item 115", null=True, blank=True)

    ft_caldot_item_116 = models.FloatField("FT Cal. Item 116", null=True, blank=True)

    ft_caldot_item_117 = models.FloatField("FT Cal. Item 117", null=True, blank=True)

    ft_caldot_item_118 = models.FloatField("FT Cal. Item 118", null=True, blank=True)

    ft_caldot_item_119 = models.FloatField("FT Cal. Item 119", null=True, blank=True)

    ft_caldot_item_120 = models.FloatField("FT Cal. Item 120", null=True, blank=True)

    ft_caldot_item_121 = models.FloatField("FT Cal. Item 121", null=True, blank=True)

    ft_caldot_item_122 = models.FloatField("FT Cal. Item 122", null=True, blank=True)

    ft_caldot_item_123 = models.FloatField("FT Cal. Item 123", null=True, blank=True)

    ft_caldot_item_124 = models.FloatField("FT Cal. Item 124", null=True, blank=True)

    ft_caldot_item_125 = models.FloatField("FT Cal. Item 125", null=True, blank=True)

    ft_caldot_item_126 = models.FloatField("FT Cal. Item 126", null=True, blank=True)

    ft_caldot_item_127 = models.FloatField("FT Cal. Item 127", null=True, blank=True)

    ft_caldot_item_128 = models.FloatField("FT Cal. Item 128", null=True, blank=True)

    ft_caldot_item_129 = models.FloatField("FT Cal. Item 129", null=True, blank=True)

    ft_caldot_item_130 = models.FloatField("FT Cal. Item 130", null=True, blank=True)

    ft_caldot_item_131 = models.FloatField("FT Cal. Item 131", null=True, blank=True)

    ft_caldot_item_132 = models.FloatField("FT Cal. Item 132", null=True, blank=True)

    ft_caldot_item_133 = models.FloatField("FT Cal. Item 133", null=True, blank=True)

    ft_caldot_item_134 = models.FloatField("FT Cal. Item 134", null=True, blank=True)

    ft_caldot_item_135 = models.FloatField("FT Cal. Item 135", null=True, blank=True)

    ft_caldot_item_136 = models.FloatField("FT Cal. Item 136", null=True, blank=True)

    ft_caldot_item_137 = models.FloatField("FT Cal. Item 137", null=True, blank=True)

    ft_caldot_item_138 = models.FloatField("FT Cal. Item 138", null=True, blank=True)

    ft_caldot_item_139 = models.FloatField("FT Cal. Item 139", null=True, blank=True)

    ft_caldot_item_140 = models.FloatField("FT Cal. Item 140", null=True, blank=True)

    ft_caldot_item_141 = models.FloatField("FT Cal. Item 141", null=True, blank=True)

    ft_caldot_item_142 = models.FloatField("FT Cal. Item 142", null=True, blank=True)

    ft_caldot_item_143 = models.FloatField("FT Cal. Item 143", null=True, blank=True)

    ft_caldot_item_144 = models.FloatField("FT Cal. Item 144", null=True, blank=True)

    ft_caldot_item_145 = models.FloatField("FT Cal. Item 145", null=True, blank=True)

    ft_caldot_item_146 = models.FloatField("FT Cal. Item 146", null=True, blank=True)

    ft_caldot_item_147 = models.FloatField("FT Cal. Item 147", null=True, blank=True)

    ft_caldot_item_148 = models.FloatField("FT Cal. Item 148", null=True, blank=True)

    ft_caldot_item_149 = models.FloatField("FT Cal. Item 149", null=True, blank=True)

    ft_caldot_item_150 = models.FloatField("FT Cal. Item 150", null=True, blank=True)

    ft_caldot_item_151 = models.FloatField("FT Cal. Item 151", null=True, blank=True)

    ft_caldot_item_152 = models.FloatField("FT Cal. Item 152", null=True, blank=True)

    ft_caldot_item_153 = models.FloatField("FT Cal. Item 153", null=True, blank=True)

    ft_caldot_item_154 = models.FloatField("FT Cal. Item 154", null=True, blank=True)

    ft_caldot_item_155 = models.FloatField("FT Cal. Item 155", null=True, blank=True)

    ft_caldot_item_156 = models.FloatField("FT Cal. Item 156", null=True, blank=True)

    ft_caldot_item_157 = models.FloatField("FT Cal. Item 157", null=True, blank=True)

    ft_caldot_item_158 = models.FloatField("FT Cal. Item 158", null=True, blank=True)

    ft_caldot_item_159 = models.FloatField("FT Cal. Item 159", null=True, blank=True)

    ft_caldot_item_160 = models.FloatField("FT Cal. Item 160", null=True, blank=True)

    ft_caldot_item_161 = models.FloatField("FT Cal. Item 161", null=True, blank=True)

    ft_caldot_item_162 = models.FloatField("FT Cal. Item 162", null=True, blank=True)

    ft_caldot_item_163 = models.FloatField("FT Cal. Item 163", null=True, blank=True)

    ft_caldot_item_164 = models.FloatField("FT Cal. Item 164", null=True, blank=True)

    ft_caldot_item_165 = models.FloatField("FT Cal. Item 165", null=True, blank=True)

    ft_caldot_item_166 = models.FloatField("FT Cal. Item 166", null=True, blank=True)

    ft_caldot_item_167 = models.FloatField("FT Cal. Item 167", null=True, blank=True)

    ft_caldot_item_168 = models.FloatField("FT Cal. Item 168", null=True, blank=True)

    ft_caldot_item_169 = models.FloatField("FT Cal. Item 169", null=True, blank=True)

    ft_caldot_item_170 = models.FloatField("FT Cal. Item 170", null=True, blank=True)

    ft_caldot_item_171 = models.FloatField("FT Cal. Item 171", null=True, blank=True)

    ft_caldot_item_172 = models.FloatField("FT Cal. Item 172", null=True, blank=True)

    ft_caldot_item_173 = models.FloatField("FT Cal. Item 173", null=True, blank=True)

    ft_caldot_item_174 = models.FloatField("FT Cal. Item 174", null=True, blank=True)

    ft_caldot_item_175 = models.FloatField("FT Cal. Item 175", null=True, blank=True)

    ft_caldot_item_176 = models.FloatField("FT Cal. Item 176", null=True, blank=True)

    ft_caldot_item_177 = models.FloatField("FT Cal. Item 177", null=True, blank=True)

    ft_caldot_item_178 = models.FloatField("FT Cal. Item 178", null=True, blank=True)

    ft_caldot_item_179 = models.FloatField("FT Cal. Item 179", null=True, blank=True)

    ft_caldot_item_180 = models.FloatField("FT Cal. Item 180", null=True, blank=True)

    ft_caldot_item_181 = models.FloatField("FT Cal. Item 181", null=True, blank=True)

    ft_caldot_item_182 = models.FloatField("FT Cal. Item 182", null=True, blank=True)

    ft_caldot_item_183 = models.FloatField("FT Cal. Item 183", null=True, blank=True)

    ft_caldot_item_184 = models.FloatField("FT Cal. Item 184", null=True, blank=True)

    ft_caldot_item_185 = models.FloatField("FT Cal. Item 185", null=True, blank=True)

    ft_caldot_item_186 = models.FloatField("FT Cal. Item 186", null=True, blank=True)

    ft_caldot_item_187 = models.FloatField("FT Cal. Item 187", null=True, blank=True)

    ft_caldot_item_188 = models.FloatField("FT Cal. Item 188", null=True, blank=True)

    ft_caldot_item_189 = models.FloatField("FT Cal. Item 189", null=True, blank=True)

    ft_caldot_item_190 = models.FloatField("FT Cal. Item 190", null=True, blank=True)

    ft_caldot_item_191 = models.FloatField("FT Cal. Item 191", null=True, blank=True)

    ft_caldot_item_192 = models.FloatField("FT Cal. Item 192", null=True, blank=True)

    ft_caldot_item_193 = models.FloatField("FT Cal. Item 193", null=True, blank=True)

    ft_caldot_item_194 = models.FloatField("FT Cal. Item 194", null=True, blank=True)

    ft_caldot_item_195 = models.FloatField("FT Cal. Item 195", null=True, blank=True)

    ft_caldot_item_196 = models.FloatField("FT Cal. Item 196", null=True, blank=True)

    ft_caldot_item_197 = models.FloatField("FT Cal. Item 197", null=True, blank=True)

    ft_caldot_item_198 = models.FloatField("FT Cal. Item 198", null=True, blank=True)

    ft_caldot_item_199 = models.FloatField("FT Cal. Item 199", null=True, blank=True)

    ft_caldot_item_200 = models.FloatField("FT Cal. Item 200", null=True, blank=True)

    ft_caldot_item_201 = models.FloatField("FT Cal. Item 201", null=True, blank=True)

    ft_caldot_item_202 = models.FloatField("FT Cal. Item 202", null=True, blank=True)

    ft_caldot_item_203 = models.FloatField("FT Cal. Item 203", null=True, blank=True)

    ft_caldot_item_204 = models.FloatField("FT Cal. Item 204", null=True, blank=True)

    ft_caldot_item_205 = models.FloatField("FT Cal. Item 205", null=True, blank=True)

    ft_caldot_item_206 = models.FloatField("FT Cal. Item 206", null=True, blank=True)

    ft_caldot_item_207 = models.FloatField("FT Cal. Item 207", null=True, blank=True)

    ft_caldot_item_208 = models.FloatField("FT Cal. Item 208", null=True, blank=True)

    ft_caldot_item_209 = models.FloatField("FT Cal. Item 209", null=True, blank=True)

    ft_caldot_item_210 = models.FloatField("FT Cal. Item 210", null=True, blank=True)

    ft_caldot_item_211 = models.FloatField("FT Cal. Item 211", null=True, blank=True)

    ft_caldot_item_212 = models.FloatField("FT Cal. Item 212", null=True, blank=True)

    ft_caldot_item_213 = models.FloatField("FT Cal. Item 213", null=True, blank=True)

    ft_caldot_item_214 = models.FloatField("FT Cal. Item 214", null=True, blank=True)

    ft_caldot_item_215 = models.FloatField("FT Cal. Item 215", null=True, blank=True)

    ft_caldot_item_216 = models.FloatField("FT Cal. Item 216", null=True, blank=True)

    ft_caldot_item_217 = models.FloatField("FT Cal. Item 217", null=True, blank=True)

    ft_caldot_item_218 = models.FloatField("FT Cal. Item 218", null=True, blank=True)

    ft_caldot_item_219 = models.FloatField("FT Cal. Item 219", null=True, blank=True)

    ft_caldot_item_220 = models.FloatField("FT Cal. Item 220", null=True, blank=True)

    ft_caldot_item_221 = models.FloatField("FT Cal. Item 221", null=True, blank=True)

    ft_caldot_item_222 = models.FloatField("FT Cal. Item 222", null=True, blank=True)

    ft_caldot_item_223 = models.FloatField("FT Cal. Item 223", null=True, blank=True)

    ft_caldot_item_224 = models.FloatField("FT Cal. Item 224", null=True, blank=True)

    ft_caldot_item_225 = models.FloatField("FT Cal. Item 225", null=True, blank=True)

    ft_caldot_item_226 = models.FloatField("FT Cal. Item 226", null=True, blank=True)

    ft_caldot_item_227 = models.FloatField("FT Cal. Item 227", null=True, blank=True)

    ft_caldot_item_228 = models.FloatField("FT Cal. Item 228", null=True, blank=True)

    ft_caldot_item_229 = models.FloatField("FT Cal. Item 229", null=True, blank=True)

    ft_caldot_item_230 = models.FloatField("FT Cal. Item 230", null=True, blank=True)

    ft_caldot_item_231 = models.FloatField("FT Cal. Item 231", null=True, blank=True)

    ft_caldot_item_232 = models.FloatField("FT Cal. Item 232", null=True, blank=True)

    ft_caldot_item_233 = models.FloatField("FT Cal. Item 233", null=True, blank=True)

    ft_caldot_item_234 = models.FloatField("FT Cal. Item 234", null=True, blank=True)

    ft_caldot_item_235 = models.FloatField("FT Cal. Item 235", null=True, blank=True)

    ft_caldot_item_236 = models.FloatField("FT Cal. Item 236", null=True, blank=True)

    ft_caldot_item_237 = models.FloatField("FT Cal. Item 237", null=True, blank=True)

    ft_caldot_item_238 = models.FloatField("FT Cal. Item 238", null=True, blank=True)

    ft_caldot_item_239 = models.FloatField("FT Cal. Item 239", null=True, blank=True)

    ft_caldot_item_240 = models.FloatField("FT Cal. Item 240", null=True, blank=True)

    ft_caldot_item_241 = models.FloatField("FT Cal. Item 241", null=True, blank=True)

    ft_caldot_item_242 = models.FloatField("FT Cal. Item 242", null=True, blank=True)

    ft_caldot_item_243 = models.FloatField("FT Cal. Item 243", null=True, blank=True)

    ft_caldot_item_244 = models.FloatField("FT Cal. Item 244", null=True, blank=True)

    ft_caldot_item_245 = models.FloatField("FT Cal. Item 245", null=True, blank=True)

    ft_caldot_item_246 = models.FloatField("FT Cal. Item 246", null=True, blank=True)

    ft_caldot_item_247 = models.FloatField("FT Cal. Item 247", null=True, blank=True)

    ft_caldot_item_248 = models.FloatField("FT Cal. Item 248", null=True, blank=True)

    ft_caldot_item_249 = models.FloatField("FT Cal. Item 249", null=True, blank=True)

    ft_caldot_item_250 = models.FloatField("FT Cal. Item 250", null=True, blank=True)

    ft_caldot_item_251 = models.FloatField("FT Cal. Item 251", null=True, blank=True)

    ft_caldot_item_252 = models.FloatField("FT Cal. Item 252", null=True, blank=True)

    ft_caldot_item_253 = models.FloatField("FT Cal. Item 253", null=True, blank=True)

    ft_caldot_item_254 = models.FloatField("FT Cal. Item 254", null=True, blank=True)

    ft_caldot_item_255 = models.FloatField("FT Cal. Item 255", null=True, blank=True)

    ft_caldot_item_256 = models.FloatField("FT Cal. Item 256", null=True, blank=True)

    ft_caldot_item_257 = models.FloatField("FT Cal. Item 257", null=True, blank=True)

    ft_caldot_item_258 = models.FloatField("FT Cal. Item 258", null=True, blank=True)

    ft_caldot_item_259 = models.FloatField("FT Cal. Item 259", null=True, blank=True)

    ft_caldot_item_260 = models.FloatField("FT Cal. Item 260", null=True, blank=True)

    ft_caldot_item_261 = models.FloatField("FT Cal. Item 261", null=True, blank=True)

    ft_caldot_item_262 = models.FloatField("FT Cal. Item 262", null=True, blank=True)

    ft_caldot_item_263 = models.FloatField("FT Cal. Item 263", null=True, blank=True)

    ft_caldot_item_264 = models.FloatField("FT Cal. Item 264", null=True, blank=True)

    ft_caldot_item_265 = models.FloatField("FT Cal. Item 265", null=True, blank=True)

    ft_caldot_item_266 = models.FloatField("FT Cal. Item 266", null=True, blank=True)

    ft_caldot_item_267 = models.FloatField("FT Cal. Item 267", null=True, blank=True)

    ft_caldot_item_268 = models.FloatField("FT Cal. Item 268", null=True, blank=True)

    ft_caldot_item_269 = models.FloatField("FT Cal. Item 269", null=True, blank=True)

    ft_caldot_item_270 = models.FloatField("FT Cal. Item 270", null=True, blank=True)

    ft_caldot_item_271 = models.FloatField("FT Cal. Item 271", null=True, blank=True)

    ft_caldot_item_272 = models.FloatField("FT Cal. Item 272", null=True, blank=True)

    ft_caldot_item_273 = models.FloatField("FT Cal. Item 273", null=True, blank=True)

    ft_caldot_item_274 = models.FloatField("FT Cal. Item 274", null=True, blank=True)

    ft_caldot_item_275 = models.FloatField("FT Cal. Item 275", null=True, blank=True)

    ft_caldot_item_276 = models.FloatField("FT Cal. Item 276", null=True, blank=True)

    ft_caldot_item_277 = models.FloatField("FT Cal. Item 277", null=True, blank=True)

    ft_caldot_item_278 = models.FloatField("FT Cal. Item 278", null=True, blank=True)

    ft_caldot_item_279 = models.FloatField("FT Cal. Item 279", null=True, blank=True)

    ft_caldot_item_280 = models.FloatField("FT Cal. Item 280", null=True, blank=True)

    ft_caldot_item_281 = models.FloatField("FT Cal. Item 281", null=True, blank=True)

    ft_caldot_item_282 = models.FloatField("FT Cal. Item 282", null=True, blank=True)

    ft_caldot_item_283 = models.FloatField("FT Cal. Item 283", null=True, blank=True)

    ft_caldot_item_284 = models.FloatField("FT Cal. Item 284", null=True, blank=True)

    ft_caldot_item_285 = models.FloatField("FT Cal. Item 285", null=True, blank=True)

    ft_caldot_item_286 = models.FloatField("FT Cal. Item 286", null=True, blank=True)

    ft_caldot_item_287 = models.FloatField("FT Cal. Item 287", null=True, blank=True)

    ft_caldot_item_288 = models.FloatField("FT Cal. Item 288", null=True, blank=True)

    ft_caldot_item_289 = models.FloatField("FT Cal. Item 289", null=True, blank=True)

    ft_caldot_item_290 = models.FloatField("FT Cal. Item 290", null=True, blank=True)

    ft_caldot_item_291 = models.FloatField("FT Cal. Item 291", null=True, blank=True)

    ft_caldot_item_292 = models.FloatField("FT Cal. Item 292", null=True, blank=True)

    ft_caldot_item_293 = models.FloatField("FT Cal. Item 293", null=True, blank=True)

    ft_caldot_item_294 = models.FloatField("FT Cal. Item 294", null=True, blank=True)

    ft_caldot_item_295 = models.FloatField("FT Cal. Item 295", null=True, blank=True)

    ft_caldot_item_296 = models.FloatField("FT Cal. Item 296", null=True, blank=True)

    ft_caldot_item_297 = models.FloatField("FT Cal. Item 297", null=True, blank=True)

    ft_caldot_item_298 = models.FloatField("FT Cal. Item 298", null=True, blank=True)

    ft_caldot_item_299 = models.FloatField("FT Cal. Item 299", null=True, blank=True)

    ft_caldot_item_300 = models.FloatField("FT Cal. Item 300", null=True, blank=True)

    ft_caldot_item_301 = models.FloatField("FT Cal. Item 301", null=True, blank=True)

    ft_caldot_item_302 = models.FloatField("FT Cal. Item 302", null=True, blank=True)

    ft_caldot_item_303 = models.FloatField("FT Cal. Item 303", null=True, blank=True)

    ft_caldot_item_304 = models.FloatField("FT Cal. Item 304", null=True, blank=True)

    ft_caldot_item_305 = models.FloatField("FT Cal. Item 305", null=True, blank=True)

    ft_caldot_item_306 = models.FloatField("FT Cal. Item 306", null=True, blank=True)

    ft_caldot_item_307 = models.FloatField("FT Cal. Item 307", null=True, blank=True)

    ft_caldot_item_308 = models.FloatField("FT Cal. Item 308", null=True, blank=True)

    ft_caldot_item_309 = models.FloatField("FT Cal. Item 309", null=True, blank=True)

    ft_caldot_item_310 = models.FloatField("FT Cal. Item 310", null=True, blank=True)

    ft_caldot_item_311 = models.FloatField("FT Cal. Item 311", null=True, blank=True)

    ft_caldot_item_312 = models.FloatField("FT Cal. Item 312", null=True, blank=True)

    ft_caldot_item_313 = models.FloatField("FT Cal. Item 313", null=True, blank=True)

    ft_caldot_item_314 = models.FloatField("FT Cal. Item 314", null=True, blank=True)

    ft_caldot_item_315 = models.FloatField("FT Cal. Item 315", null=True, blank=True)

    ft_caldot_item_316 = models.FloatField("FT Cal. Item 316", null=True, blank=True)

    ft_caldot_item_317 = models.FloatField("FT Cal. Item 317", null=True, blank=True)

    ft_caldot_item_318 = models.FloatField("FT Cal. Item 318", null=True, blank=True)

    ft_caldot_item_319 = models.FloatField("FT Cal. Item 319", null=True, blank=True)

    ft_caldot_item_320 = models.FloatField("FT Cal. Item 320", null=True, blank=True)

    ft_caldot_item_321 = models.FloatField("FT Cal. Item 321", null=True, blank=True)

    ft_caldot_item_322 = models.FloatField("FT Cal. Item 322", null=True, blank=True)

    ft_caldot_item_323 = models.FloatField("FT Cal. Item 323", null=True, blank=True)

    ft_caldot_item_324 = models.FloatField("FT Cal. Item 324", null=True, blank=True)

    ft_caldot_item_325 = models.FloatField("FT Cal. Item 325", null=True, blank=True)

    ft_caldot_item_326 = models.FloatField("FT Cal. Item 326", null=True, blank=True)

    ft_caldot_item_327 = models.FloatField("FT Cal. Item 327", null=True, blank=True)

    ft_caldot_item_328 = models.FloatField("FT Cal. Item 328", null=True, blank=True)

    ft_caldot_item_329 = models.FloatField("FT Cal. Item 329", null=True, blank=True)

    ft_caldot_item_330 = models.FloatField("FT Cal. Item 330", null=True, blank=True)

    ft_caldot_item_331 = models.FloatField("FT Cal. Item 331", null=True, blank=True)

    ft_caldot_item_332 = models.FloatField("FT Cal. Item 332", null=True, blank=True)

    ft_caldot_item_333 = models.FloatField("FT Cal. Item 333", null=True, blank=True)

    ft_caldot_item_334 = models.FloatField("FT Cal. Item 334", null=True, blank=True)

    ft_caldot_item_335 = models.FloatField("FT Cal. Item 335", null=True, blank=True)

    ft_caldot_item_336 = models.FloatField("FT Cal. Item 336", null=True, blank=True)

    ft_caldot_item_337 = models.FloatField("FT Cal. Item 337", null=True, blank=True)

    ft_caldot_item_338 = models.FloatField("FT Cal. Item 338", null=True, blank=True)

    ft_caldot_item_339 = models.FloatField("FT Cal. Item 339", null=True, blank=True)

    ft_caldot_item_340 = models.FloatField("FT Cal. Item 340", null=True, blank=True)

    ft_caldot_item_341 = models.FloatField("FT Cal. Item 341", null=True, blank=True)

    ft_caldot_item_342 = models.FloatField("FT Cal. Item 342", null=True, blank=True)

    ft_caldot_item_343 = models.FloatField("FT Cal. Item 343", null=True, blank=True)

    ft_caldot_item_344 = models.FloatField("FT Cal. Item 344", null=True, blank=True)

    ft_caldot_item_345 = models.FloatField("FT Cal. Item 345", null=True, blank=True)

    ft_caldot_item_346 = models.FloatField("FT Cal. Item 346", null=True, blank=True)

    ft_caldot_item_347 = models.FloatField("FT Cal. Item 347", null=True, blank=True)

    ft_caldot_item_348 = models.FloatField("FT Cal. Item 348", null=True, blank=True)

    ft_caldot_item_349 = models.FloatField("FT Cal. Item 349", null=True, blank=True)

    ft_caldot_item_350 = models.FloatField("FT Cal. Item 350", null=True, blank=True)

    ft_caldot_item_351 = models.FloatField("FT Cal. Item 351", null=True, blank=True)

    ft_caldot_item_352 = models.FloatField("FT Cal. Item 352", null=True, blank=True)

    ft_caldot_item_353 = models.FloatField("FT Cal. Item 353", null=True, blank=True)

    ft_caldot_item_354 = models.FloatField("FT Cal. Item 354", null=True, blank=True)

    ft_caldot_item_355 = models.FloatField("FT Cal. Item 355", null=True, blank=True)

    ft_caldot_item_356 = models.FloatField("FT Cal. Item 356", null=True, blank=True)

    ft_caldot_item_357 = models.FloatField("FT Cal. Item 357", null=True, blank=True)

    ft_caldot_item_358 = models.FloatField("FT Cal. Item 358", null=True, blank=True)

    ft_caldot_item_359 = models.FloatField("FT Cal. Item 359", null=True, blank=True)

    ft_caldot_item_360 = models.FloatField("FT Cal. Item 360", null=True, blank=True)

    ft_caldot_item_361 = models.FloatField("FT Cal. Item 361", null=True, blank=True)

    ft_caldot_item_362 = models.FloatField("FT Cal. Item 362", null=True, blank=True)

    ft_caldot_item_363 = models.FloatField("FT Cal. Item 363", null=True, blank=True)

    ft_caldot_item_364 = models.FloatField("FT Cal. Item 364", null=True, blank=True)

    ft_caldot_item_365 = models.FloatField("FT Cal. Item 365", null=True, blank=True)

    ft_caldot_item_366 = models.FloatField("FT Cal. Item 366", null=True, blank=True)

    ft_caldot_item_367 = models.FloatField("FT Cal. Item 367", null=True, blank=True)

    ft_caldot_item_368 = models.FloatField("FT Cal. Item 368", null=True, blank=True)

    ft_caldot_item_369 = models.FloatField("FT Cal. Item 369", null=True, blank=True)

    ft_caldot_item_370 = models.FloatField("FT Cal. Item 370", null=True, blank=True)

    ft_caldot_item_371 = models.FloatField("FT Cal. Item 371", null=True, blank=True)

    ft_caldot_item_372 = models.FloatField("FT Cal. Item 372", null=True, blank=True)

    ft_caldot_item_373 = models.FloatField("FT Cal. Item 373", null=True, blank=True)

    ft_caldot_item_374 = models.FloatField("FT Cal. Item 374", null=True, blank=True)

    ft_caldot_item_375 = models.FloatField("FT Cal. Item 375", null=True, blank=True)

    ft_caldot_item_376 = models.FloatField("FT Cal. Item 376", null=True, blank=True)

    ft_caldot_item_377 = models.FloatField("FT Cal. Item 377", null=True, blank=True)

    ft_caldot_item_378 = models.FloatField("FT Cal. Item 378", null=True, blank=True)

    ft_caldot_item_379 = models.FloatField("FT Cal. Item 379", null=True, blank=True)

    ft_caldot_item_380 = models.FloatField("FT Cal. Item 380", null=True, blank=True)

    ft_caldot_item_381 = models.FloatField("FT Cal. Item 381", null=True, blank=True)

    ft_caldot_item_382 = models.FloatField("FT Cal. Item 382", null=True, blank=True)

    ft_caldot_item_383 = models.FloatField("FT Cal. Item 383", null=True, blank=True)

    ft_caldot_item_384 = models.FloatField("FT Cal. Item 384", null=True, blank=True)

    ft_caldot_item_385 = models.FloatField("FT Cal. Item 385", null=True, blank=True)

    ft_caldot_item_386 = models.FloatField("FT Cal. Item 386", null=True, blank=True)

    ft_caldot_item_387 = models.FloatField("FT Cal. Item 387", null=True, blank=True)

    ft_caldot_item_388 = models.FloatField("FT Cal. Item 388", null=True, blank=True)

    ft_caldot_item_389 = models.FloatField("FT Cal. Item 389", null=True, blank=True)

    ft_caldot_item_390 = models.FloatField("FT Cal. Item 390", null=True, blank=True)

    ft_caldot_item_391 = models.FloatField("FT Cal. Item 391", null=True, blank=True)

    ft_caldot_item_392 = models.FloatField("FT Cal. Item 392", null=True, blank=True)

    ft_caldot_item_393 = models.FloatField("FT Cal. Item 393", null=True, blank=True)

    ft_caldot_item_394 = models.FloatField("FT Cal. Item 394", null=True, blank=True)

    ft_caldot_item_395 = models.FloatField("FT Cal. Item 395", null=True, blank=True)

    ft_caldot_item_396 = models.FloatField("FT Cal. Item 396", null=True, blank=True)

    ft_caldot_item_397 = models.FloatField("FT Cal. Item 397", null=True, blank=True)

    ft_caldot_item_398 = models.FloatField("FT Cal. Item 398", null=True, blank=True)

    ft_caldot_item_399 = models.FloatField("FT Cal. Item 399", null=True, blank=True)

    ft_caldot_item_400 = models.FloatField("FT Cal. Item 400", null=True, blank=True)

    ft_caldot_item_401 = models.FloatField("FT Cal. Item 401", null=True, blank=True)

    ft_caldot_item_402 = models.FloatField("FT Cal. Item 402", null=True, blank=True)

    ft_caldot_item_403 = models.FloatField("FT Cal. Item 403", null=True, blank=True)

    ft_caldot_item_404 = models.FloatField("FT Cal. Item 404", null=True, blank=True)

    ft_caldot_item_405 = models.FloatField("FT Cal. Item 405", null=True, blank=True)

    ft_caldot_item_406 = models.FloatField("FT Cal. Item 406", null=True, blank=True)

    ft_caldot_item_407 = models.FloatField("FT Cal. Item 407", null=True, blank=True)

    ft_caldot_item_408 = models.FloatField("FT Cal. Item 408", null=True, blank=True)

    ft_caldot_item_409 = models.FloatField("FT Cal. Item 409", null=True, blank=True)

    ft_caldot_item_410 = models.FloatField("FT Cal. Item 410", null=True, blank=True)

    ft_caldot_item_411 = models.FloatField("FT Cal. Item 411", null=True, blank=True)

    ft_caldot_item_412 = models.FloatField("FT Cal. Item 412", null=True, blank=True)

    ft_caldot_item_413 = models.FloatField("FT Cal. Item 413", null=True, blank=True)

    ft_caldot_item_414 = models.FloatField("FT Cal. Item 414", null=True, blank=True)

    ft_caldot_item_415 = models.FloatField("FT Cal. Item 415", null=True, blank=True)

    ft_caldot_item_416 = models.FloatField("FT Cal. Item 416", null=True, blank=True)

    ft_caldot_item_417 = models.FloatField("FT Cal. Item 417", null=True, blank=True)

    ft_caldot_item_418 = models.FloatField("FT Cal. Item 418", null=True, blank=True)

    ft_caldot_item_419 = models.FloatField("FT Cal. Item 419", null=True, blank=True)

    ft_caldot_item_420 = models.FloatField("FT Cal. Item 420", null=True, blank=True)

    ft_caldot_item_421 = models.FloatField("FT Cal. Item 421", null=True, blank=True)

    ft_caldot_item_422 = models.FloatField("FT Cal. Item 422", null=True, blank=True)

    ft_caldot_item_423 = models.FloatField("FT Cal. Item 423", null=True, blank=True)

    ft_caldot_item_424 = models.FloatField("FT Cal. Item 424", null=True, blank=True)

    ft_caldot_item_425 = models.FloatField("FT Cal. Item 425", null=True, blank=True)

    ft_caldot_item_426 = models.FloatField("FT Cal. Item 426", null=True, blank=True)

    ft_caldot_item_427 = models.FloatField("FT Cal. Item 427", null=True, blank=True)

    ft_caldot_item_428 = models.FloatField("FT Cal. Item 428", null=True, blank=True)

    ft_caldot_item_429 = models.FloatField("FT Cal. Item 429", null=True, blank=True)

    ft_caldot_item_430 = models.FloatField("FT Cal. Item 430", null=True, blank=True)

    ft_caldot_item_431 = models.FloatField("FT Cal. Item 431", null=True, blank=True)

    ft_caldot_item_432 = models.FloatField("FT Cal. Item 432", null=True, blank=True)

    ft_caldot_item_433 = models.FloatField("FT Cal. Item 433", null=True, blank=True)

    ft_caldot_item_434 = models.FloatField("FT Cal. Item 434", null=True, blank=True)

    ft_caldot_item_435 = models.FloatField("FT Cal. Item 435", null=True, blank=True)

    ft_caldot_item_436 = models.FloatField("FT Cal. Item 436", null=True, blank=True)

    ft_caldot_item_437 = models.FloatField("FT Cal. Item 437", null=True, blank=True)

    ft_caldot_item_438 = models.FloatField("FT Cal. Item 438", null=True, blank=True)

    ft_caldot_item_439 = models.FloatField("FT Cal. Item 439", null=True, blank=True)

    ft_caldot_item_440 = models.FloatField("FT Cal. Item 440", null=True, blank=True)

    ft_caldot_item_441 = models.FloatField("FT Cal. Item 441", null=True, blank=True)

    ft_caldot_item_442 = models.FloatField("FT Cal. Item 442", null=True, blank=True)

    ft_caldot_item_443 = models.FloatField("FT Cal. Item 443", null=True, blank=True)

    ft_caldot_item_444 = models.FloatField("FT Cal. Item 444", null=True, blank=True)

    ft_caldot_item_445 = models.FloatField("FT Cal. Item 445", null=True, blank=True)

    ft_caldot_item_446 = models.FloatField("FT Cal. Item 446", null=True, blank=True)

    ft_caldot_item_447 = models.FloatField("FT Cal. Item 447", null=True, blank=True)

    ft_caldot_item_448 = models.FloatField("FT Cal. Item 448", null=True, blank=True)

    ft_caldot_item_449 = models.FloatField("FT Cal. Item 449", null=True, blank=True)

    ft_caldot_item_450 = models.FloatField("FT Cal. Item 450", null=True, blank=True)

    ft_caldot_item_451 = models.FloatField("FT Cal. Item 451", null=True, blank=True)

    ft_caldot_item_452 = models.FloatField("FT Cal. Item 452", null=True, blank=True)

    ft_caldot_item_453 = models.FloatField("FT Cal. Item 453", null=True, blank=True)

    ft_caldot_item_454 = models.FloatField("FT Cal. Item 454", null=True, blank=True)

    ft_caldot_item_455 = models.FloatField("FT Cal. Item 455", null=True, blank=True)

    ft_caldot_item_456 = models.FloatField("FT Cal. Item 456", null=True, blank=True)

    ft_caldot_item_457 = models.FloatField("FT Cal. Item 457", null=True, blank=True)

    ft_caldot_item_458 = models.FloatField("FT Cal. Item 458", null=True, blank=True)

    ft_caldot_item_459 = models.FloatField("FT Cal. Item 459", null=True, blank=True)

    ft_caldot_item_460 = models.FloatField("FT Cal. Item 460", null=True, blank=True)

    ft_caldot_item_461 = models.FloatField("FT Cal. Item 461", null=True, blank=True)

    ft_caldot_item_462 = models.FloatField("FT Cal. Item 462", null=True, blank=True)

    ft_caldot_item_463 = models.FloatField("FT Cal. Item 463", null=True, blank=True)

    ft_caldot_item_464 = models.FloatField("FT Cal. Item 464", null=True, blank=True)

    ft_caldot_item_465 = models.FloatField("FT Cal. Item 465", null=True, blank=True)

    ft_caldot_item_466 = models.FloatField("FT Cal. Item 466", null=True, blank=True)

    ft_caldot_item_467 = models.FloatField("FT Cal. Item 467", null=True, blank=True)

    ft_caldot_item_468 = models.FloatField("FT Cal. Item 468", null=True, blank=True)

    ft_caldot_item_469 = models.FloatField("FT Cal. Item 469", null=True, blank=True)

    ft_caldot_item_470 = models.FloatField("FT Cal. Item 470", null=True, blank=True)

    ft_caldot_item_471 = models.FloatField("FT Cal. Item 471", null=True, blank=True)

    ft_caldot_item_472 = models.FloatField("FT Cal. Item 472", null=True, blank=True)

    ft_caldot_item_473 = models.FloatField("FT Cal. Item 473", null=True, blank=True)

    ft_caldot_item_474 = models.FloatField("FT Cal. Item 474", null=True, blank=True)

    ft_caldot_item_475 = models.FloatField("FT Cal. Item 475", null=True, blank=True)

    ft_caldot_item_476 = models.FloatField("FT Cal. Item 476", null=True, blank=True)

    ft_caldot_item_477 = models.FloatField("FT Cal. Item 477", null=True, blank=True)

    ft_caldot_item_478 = models.FloatField("FT Cal. Item 478", null=True, blank=True)

    ft_caldot_item_479 = models.FloatField("FT Cal. Item 479", null=True, blank=True)

    ft_caldot_item_480 = models.FloatField("FT Cal. Item 480", null=True, blank=True)

    ft_caldot_item_481 = models.FloatField("FT Cal. Item 481", null=True, blank=True)

    ft_caldot_item_482 = models.FloatField("FT Cal. Item 482", null=True, blank=True)

    ft_caldot_item_483 = models.FloatField("FT Cal. Item 483", null=True, blank=True)

    ft_caldot_item_484 = models.FloatField("FT Cal. Item 484", null=True, blank=True)

    ft_caldot_item_485 = models.FloatField("FT Cal. Item 485", null=True, blank=True)

    ft_caldot_item_486 = models.FloatField("FT Cal. Item 486", null=True, blank=True)

    ft_caldot_item_487 = models.FloatField("FT Cal. Item 487", null=True, blank=True)

    ft_caldot_item_488 = models.FloatField("FT Cal. Item 488", null=True, blank=True)

    ft_caldot_item_489 = models.FloatField("FT Cal. Item 489", null=True, blank=True)

    ft_caldot_item_490 = models.FloatField("FT Cal. Item 490", null=True, blank=True)

    ft_caldot_item_491 = models.FloatField("FT Cal. Item 491", null=True, blank=True)

    ft_caldot_item_492 = models.FloatField("FT Cal. Item 492", null=True, blank=True)

    ft_caldot_item_493 = models.FloatField("FT Cal. Item 493", null=True, blank=True)

    ft_caldot_item_494 = models.FloatField("FT Cal. Item 494", null=True, blank=True)

    ft_caldot_item_495 = models.FloatField("FT Cal. Item 495", null=True, blank=True)

    ft_caldot_item_496 = models.FloatField("FT Cal. Item 496", null=True, blank=True)

    ft_caldot_item_497 = models.FloatField("FT Cal. Item 497", null=True, blank=True)

    ft_caldot_item_498 = models.FloatField("FT Cal. Item 498", null=True, blank=True)

    ft_caldot_item_499 = models.FloatField("FT Cal. Item 499", null=True, blank=True)

    ft_caldot_item_500 = models.FloatField("FT Cal. Item 500", null=True, blank=True)




class MetaTuneData(models.Model):


    class Meta:
        verbose_name = "Meta:  Tune Data"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Meta')

    spray_voltage_plus = models.IntegerField("Spray Voltage (+)", null=True, blank=True)

    spray_voltage = models.IntegerField("Spray Voltage (-)", null=True, blank=True)

    capillary_temperature_plus_or_plus = models.IntegerField("Capillary Temperature (+ or +-)", null=True, blank=True)

    capillary_temperature = models.IntegerField("Capillary Temperature (-)", null=True, blank=True)

    sheath_gas_plus_or_plus = models.IntegerField("Sheath Gas (+ or +-)", null=True, blank=True)

    sheath_gas = models.IntegerField("Sheath Gas (-)", null=True, blank=True)

    aux_gas_plus_or_plus = models.IntegerField("Aux Gas (+ or +-)", null=True, blank=True)

    aux_gas = models.IntegerField("Aux Gas (-)", null=True, blank=True)

    spare_gas_plus_or_plus = models.IntegerField("Spare Gas (+ or +-)", null=True, blank=True)

    spare_gas = models.IntegerField("Spare Gas (-)", null=True, blank=True)

    max_spray_current_plus = models.IntegerField("Max Spray Current (+)", null=True, blank=True)

    max_spray_current = models.IntegerField("Max Spray Current (-)", null=True, blank=True)

    probe_heater_tempdot_plus_or_plus = models.IntegerField("Probe Heater Temp. (+ or +-)", null=True, blank=True)

    probe_heater_tempdot = models.IntegerField("Probe Heater Temp. (-)", null=True, blank=True)

    slens_rf_level = models.IntegerField("S-Lens RF Level", null=True, blank=True)

    ion_source = models.CharField("Ion Source", max_length=50, null=True, blank=True)





class MetaCalibrationData(models.Model):


    class Meta:
        verbose_name = "Meta:  Calibration Data"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Meta')

    mass_caldot_plus_age_d = models.FloatField("Mass Cal. (+) age (d)", null=True, blank=True)

    mass_caldot_age_d = models.FloatField("Mass Cal. (-) age (d)", null=True, blank=True)

    isolation_caldot_plus_age_d = models.FloatField("Isolation Cal. (+) age (d)", null=True, blank=True)

    isolation_caldot_age_d = models.FloatField("Isolation Cal. (-) age (d)", null=True, blank=True)

    amplifier_gain = models.IntegerField("Amplifier Gain", null=True, blank=True)

    mass_calibration_parameter_0 = models.IntegerField("Mass Calibration Parameter (0)", null=True, blank=True)

    mass_calibration_parameter_1 = models.IntegerField("Mass Calibration Parameter (1)", null=True, blank=True)

    mass_calibration_parameter_2 = models.FloatField("Mass Calibration Parameter (2)", null=True, blank=True)

    mass_calibration_parameter_3 = models.FloatField("Mass Calibration Parameter (3)", null=True, blank=True)

    mass_calibration_parameter_4 = models.FloatField("Mass Calibration Parameter (4)", null=True, blank=True)

    mass_calibration_parameter_5 = models.FloatField("Mass Calibration Parameter (5)", null=True, blank=True)

    mass_calibration_parameter_6 = models.FloatField("Mass Calibration Parameter (6)", null=True, blank=True)

    mass_calibration_parameter_7 = models.FloatField("Mass Calibration Parameter (7)", null=True, blank=True)

    mass_calibration_parameter_8 = models.FloatField("Mass Calibration Parameter (8)", null=True, blank=True)

    mass_calibration_parameter_9 = models.FloatField("Mass Calibration Parameter (9)", null=True, blank=True)

    mass_calibration_parameter_10 = models.FloatField("Mass Calibration Parameter (10)", null=True, blank=True)

    mass_calibration_parameter_11 = models.IntegerField("Mass Calibration Parameter (11)", null=True, blank=True)

    mass_calibration_parameter_12 = models.FloatField("Mass Calibration Parameter (12)", null=True, blank=True)

    mass_calibration_parameter_13 = models.IntegerField("Mass Calibration Parameter (13)", null=True, blank=True)

    mass_calibration_parameter_14 = models.FloatField("Mass Calibration Parameter (14)", null=True, blank=True)

    mass_calibration_parameter_15 = models.FloatField("Mass Calibration Parameter (15)", null=True, blank=True)

    mass_calibration_parameter_16 = models.FloatField("Mass Calibration Parameter (16)", null=True, blank=True)

    mass_calibration_parameter_17 = models.FloatField("Mass Calibration Parameter (17)", null=True, blank=True)

    mass_calibration_parameter_18 = models.FloatField("Mass Calibration Parameter (18)", null=True, blank=True)

    mass_calibration_parameter_19 = models.FloatField("Mass Calibration Parameter (19)", null=True, blank=True)

    mass_calibration_parameter_20 = models.FloatField("Mass Calibration Parameter (20)", null=True, blank=True)

    mass_calibration_parameter_21 = models.FloatField("Mass Calibration Parameter (21)", null=True, blank=True)

    mass_calibration_parameter_22 = models.IntegerField("Mass Calibration Parameter (22)", null=True, blank=True)

    mass_calibration_parameter_23 = models.IntegerField("Mass Calibration Parameter (23)", null=True, blank=True)

    mass_calibration_parameter_24 = models.IntegerField("Mass Calibration Parameter (24)", null=True, blank=True)

    mass_calibration_parameter_25 = models.IntegerField("Mass Calibration Parameter (25)", null=True, blank=True)

    mass_calibration_parameter_26 = models.IntegerField("Mass Calibration Parameter (26)", null=True, blank=True)

    mass_calibration_parameter_27 = models.IntegerField("Mass Calibration Parameter (27)", null=True, blank=True)

    mass_calibration_parameter_28 = models.IntegerField("Mass Calibration Parameter (28)", null=True, blank=True)

    mass_calibration_parameter_29 = models.IntegerField("Mass Calibration Parameter (29)", null=True, blank=True)

    mass_calibration_parameter_30 = models.IntegerField("Mass Calibration Parameter (30)", null=True, blank=True)

    mass_calibration_parameter_31 = models.IntegerField("Mass Calibration Parameter (31)", null=True, blank=True)

    mass_calibration_parameter_32 = models.IntegerField("Mass Calibration Parameter (32)", null=True, blank=True)

    mass_calibration_parameter_33 = models.IntegerField("Mass Calibration Parameter (33)", null=True, blank=True)

    mass_calibration_parameter_34 = models.FloatField("Mass Calibration Parameter (34)", null=True, blank=True)

    mass_calibration_parameter_35 = models.FloatField("Mass Calibration Parameter (35)", null=True, blank=True)

    mass_calibration_parameter_36 = models.FloatField("Mass Calibration Parameter (36)", null=True, blank=True)

    mass_calibration_parameter_37 = models.IntegerField("Mass Calibration Parameter (37)", null=True, blank=True)

    mass_calibration_parameter_38 = models.IntegerField("Mass Calibration Parameter (38)", null=True, blank=True)

    mass_calibration_parameter_39 = models.FloatField("Mass Calibration Parameter (39)", null=True, blank=True)

    mass_calibration_parameter_40 = models.IntegerField("Mass Calibration Parameter (40)", null=True, blank=True)

    mass_calibration_parameter_41 = models.FloatField("Mass Calibration Parameter (41)", null=True, blank=True)

    mass_calibration_parameter_42 = models.FloatField("Mass Calibration Parameter (42)", null=True, blank=True)

    mass_calibration_parameter_43 = models.FloatField("Mass Calibration Parameter (43)", null=True, blank=True)

    mass_calibration_parameter_44 = models.FloatField("Mass Calibration Parameter (44)", null=True, blank=True)

    mass_calibration_parameter_45 = models.FloatField("Mass Calibration Parameter (45)", null=True, blank=True)

    mass_calibration_parameter_46 = models.FloatField("Mass Calibration Parameter (46)", null=True, blank=True)

    mass_calibration_parameter_47 = models.FloatField("Mass Calibration Parameter (47)", null=True, blank=True)

    mass_calibration_parameter_48 = models.FloatField("Mass Calibration Parameter (48)", null=True, blank=True)

    mass_calibration_parameter_49 = models.FloatField("Mass Calibration Parameter (49)", null=True, blank=True)

    mass_calibration_parameter_50 = models.FloatField("Mass Calibration Parameter (50)", null=True, blank=True)

    mass_calibration_parameter_51 = models.FloatField("Mass Calibration Parameter (51)", null=True, blank=True)

    mass_calibration_parameter_52 = models.FloatField("Mass Calibration Parameter (52)", null=True, blank=True)

    mass_calibration_parameter_53 = models.IntegerField("Mass Calibration Parameter (53)", null=True, blank=True)

    mass_calibration_parameter_54 = models.IntegerField("Mass Calibration Parameter (54)", null=True, blank=True)

    mass_calibration_parameter_55 = models.IntegerField("Mass Calibration Parameter (55)", null=True, blank=True)

    mass_calibration_parameter_56 = models.FloatField("Mass Calibration Parameter (56)", null=True, blank=True)

    mass_calibration_parameter_57 = models.FloatField("Mass Calibration Parameter (57)", null=True, blank=True)

    mass_calibration_parameter_58 = models.FloatField("Mass Calibration Parameter (58)", null=True, blank=True)

    mass_calibration_parameter_59 = models.IntegerField("Mass Calibration Parameter (59)", null=True, blank=True)

    mass_calibration_parameter_60 = models.IntegerField("Mass Calibration Parameter (60)", null=True, blank=True)

    mass_calibration_parameter_61 = models.FloatField("Mass Calibration Parameter (61)", null=True, blank=True)

    mass_calibration_parameter_62 = models.IntegerField("Mass Calibration Parameter (62)", null=True, blank=True)

    mass_calibration_parameter_63 = models.FloatField("Mass Calibration Parameter (63)", null=True, blank=True)

    mass_calibration_parameter_64 = models.FloatField("Mass Calibration Parameter (64)", null=True, blank=True)

    mass_calibration_parameter_65 = models.FloatField("Mass Calibration Parameter (65)", null=True, blank=True)

    mass_calibration_parameter_66 = models.FloatField("Mass Calibration Parameter (66)", null=True, blank=True)

    mass_calibration_parameter_67 = models.FloatField("Mass Calibration Parameter (67)", null=True, blank=True)

    mass_calibration_parameter_68 = models.FloatField("Mass Calibration Parameter (68)", null=True, blank=True)

    mass_calibration_parameter_69 = models.FloatField("Mass Calibration Parameter (69)", null=True, blank=True)

    mass_calibration_parameter_70 = models.FloatField("Mass Calibration Parameter (70)", null=True, blank=True)

    mass_calibration_parameter_71 = models.FloatField("Mass Calibration Parameter (71)", null=True, blank=True)

    mass_calibration_parameter_72 = models.FloatField("Mass Calibration Parameter (72)", null=True, blank=True)

    mass_calibration_parameter_73 = models.FloatField("Mass Calibration Parameter (73)", null=True, blank=True)

    mass_calibration_parameter_74 = models.FloatField("Mass Calibration Parameter (74)", null=True, blank=True)

    mass_calibration_parameter_75 = models.FloatField("Mass Calibration Parameter (75)", null=True, blank=True)

    mass_calibration_parameter_76 = models.FloatField("Mass Calibration Parameter (76)", null=True, blank=True)

    mass_calibration_parameter_77 = models.FloatField("Mass Calibration Parameter (77)", null=True, blank=True)

    mass_calibration_parameter_78 = models.FloatField("Mass Calibration Parameter (78)", null=True, blank=True)

    mass_calibration_parameter_79 = models.IntegerField("Mass Calibration Parameter (79)", null=True, blank=True)

    mass_calibration_parameter_80 = models.IntegerField("Mass Calibration Parameter (80)", null=True, blank=True)

    mass_calibration_parameter_81 = models.IntegerField("Mass Calibration Parameter (81)", null=True, blank=True)

    mass_calibration_parameter_82 = models.IntegerField("Mass Calibration Parameter (82)", null=True, blank=True)

    mass_calibration_parameter_83 = models.IntegerField("Mass Calibration Parameter (83)", null=True, blank=True)

    mass_calibration_parameter_84 = models.IntegerField("Mass Calibration Parameter (84)", null=True, blank=True)

    mass_calibration_parameter_85 = models.IntegerField("Mass Calibration Parameter (85)", null=True, blank=True)

    mass_calibration_parameter_86 = models.IntegerField("Mass Calibration Parameter (86)", null=True, blank=True)

    mass_calibration_parameter_87 = models.IntegerField("Mass Calibration Parameter (87)", null=True, blank=True)

    mass_calibration_parameter_88 = models.IntegerField("Mass Calibration Parameter (88)", null=True, blank=True)

    mass_calibration_parameter_89 = models.IntegerField("Mass Calibration Parameter (89)", null=True, blank=True)

    mass_calibration_parameter_90 = models.IntegerField("Mass Calibration Parameter (90)", null=True, blank=True)

    mass_calibration_parameter_91 = models.IntegerField("Mass Calibration Parameter (91)", null=True, blank=True)

    mass_calibration_parameter_92 = models.IntegerField("Mass Calibration Parameter (92)", null=True, blank=True)

    mass_calibration_parameter_93 = models.IntegerField("Mass Calibration Parameter (93)", null=True, blank=True)

    mass_calibration_parameter_94 = models.IntegerField("Mass Calibration Parameter (94)", null=True, blank=True)

    mass_calibration_parameter_95 = models.IntegerField("Mass Calibration Parameter (95)", null=True, blank=True)

    mass_calibration_parameter_96 = models.IntegerField("Mass Calibration Parameter (96)", null=True, blank=True)

    mass_calibration_parameter_97 = models.IntegerField("Mass Calibration Parameter (97)", null=True, blank=True)

    mass_calibration_parameter_98 = models.IntegerField("Mass Calibration Parameter (98)", null=True, blank=True)

    mass_calibration_parameter_99 = models.IntegerField("Mass Calibration Parameter (99)", null=True, blank=True)

    mass_calibration_parameter_100 = models.IntegerField("Mass Calibration Parameter (100)", null=True, blank=True)

    mass_calibration_parameter_101 = models.IntegerField("Mass Calibration Parameter (101)", null=True, blank=True)

    mass_calibration_parameter_102 = models.IntegerField("Mass Calibration Parameter (102)", null=True, blank=True)

    mass_calibration_parameter_103 = models.IntegerField("Mass Calibration Parameter (103)", null=True, blank=True)

    mass_calibration_parameter_104 = models.IntegerField("Mass Calibration Parameter (104)", null=True, blank=True)

    mass_calibration_parameter_105 = models.IntegerField("Mass Calibration Parameter (105)", null=True, blank=True)

    mass_calibration_parameter_106 = models.IntegerField("Mass Calibration Parameter (106)", null=True, blank=True)

    mass_calibration_parameter_107 = models.IntegerField("Mass Calibration Parameter (107)", null=True, blank=True)

    mass_calibration_parameter_108 = models.IntegerField("Mass Calibration Parameter (108)", null=True, blank=True)

    mass_calibration_parameter_109 = models.IntegerField("Mass Calibration Parameter (109)", null=True, blank=True)

    mass_calibration_parameter_110 = models.IntegerField("Mass Calibration Parameter (110)", null=True, blank=True)

    mass_calibration_parameter_111 = models.IntegerField("Mass Calibration Parameter (111)", null=True, blank=True)

    mass_calibration_parameter_112 = models.IntegerField("Mass Calibration Parameter (112)", null=True, blank=True)

    mass_calibration_parameter_113 = models.IntegerField("Mass Calibration Parameter (113)", null=True, blank=True)

    mass_calibration_parameter_114 = models.IntegerField("Mass Calibration Parameter (114)", null=True, blank=True)

    mass_calibration_parameter_115 = models.IntegerField("Mass Calibration Parameter (115)", null=True, blank=True)

    mass_calibration_parameter_116 = models.IntegerField("Mass Calibration Parameter (116)", null=True, blank=True)

    mass_calibration_parameter_117 = models.IntegerField("Mass Calibration Parameter (117)", null=True, blank=True)

    mass_calibration_parameter_118 = models.IntegerField("Mass Calibration Parameter (118)", null=True, blank=True)

    mass_calibration_parameter_119 = models.IntegerField("Mass Calibration Parameter (119)", null=True, blank=True)

    ctcd_scale_plus = models.FloatField("CTCD Scale (+)", null=True, blank=True)

    ctcd_scale = models.FloatField("CTCD Scale (-)", null=True, blank=True)

    ctcd_para_plus = models.FloatField("CTCD Para (+)", null=True, blank=True)

    ctcd_para = models.FloatField("CTCD Para (-)", null=True, blank=True)

    detect_delay = models.FloatField("Detect Delay", null=True, blank=True)

    relais_delay = models.IntegerField("Relais Delay", null=True, blank=True)

    resdotdepdot_delay = models.IntegerField("Res.-Dep. Delay", null=True, blank=True)

    quad_dc_plus0 = models.FloatField("Quad DC (+,0)", null=True, blank=True)

    quad_dc_plus1 = models.FloatField("Quad DC (+,1)", null=True, blank=True)

    quad_dc_0 = models.FloatField("Quad DC (-,0)", null=True, blank=True)

    quad_dc_1 = models.FloatField("Quad DC (-,1)", null=True, blank=True)

    quad_otk_plus0 = models.FloatField("Quad OTK (+,0)", null=True, blank=True)

    quad_otk_plus1 = models.FloatField("Quad OTK (+,1)", null=True, blank=True)

    quad_otk_0 = models.FloatField("Quad OTK (-,0)", null=True, blank=True)

    quad_otk_1 = models.FloatField("Quad OTK (-,1)", null=True, blank=True)

    quad_para_a = models.IntegerField("Quad Para A", null=True, blank=True)

    quad_para_b = models.IntegerField("Quad Para B", null=True, blank=True)

    quad_para_c = models.IntegerField("Quad Para C", null=True, blank=True)

    clt_gnd_voltage_plus = models.FloatField("CLT GND Voltage (+)", null=True, blank=True)

    clt_gnd_voltage = models.FloatField("CLT GND Voltage (-)", null=True, blank=True)

    clt_offset_voltage_plus = models.IntegerField("CLT Offset Voltage (+)", null=True, blank=True)

    clt_offset_voltage = models.IntegerField("CLT Offset Voltage (-)", null=True, blank=True)

    clt_push_voltage_plus = models.IntegerField("CLT Push Voltage (+)", null=True, blank=True)

    clt_push_voltage = models.IntegerField("CLT Push Voltage (-)", null=True, blank=True)

    clt_pull_voltage_plus = models.IntegerField("CLT Pull Voltage (+)", null=True, blank=True)

    clt_pull_voltage = models.IntegerField("CLT Pull Voltage (-)", null=True, blank=True)

    lens_6_voltage_plus = models.IntegerField("Lens 6 Voltage (+)", null=True, blank=True)

    lens_6_voltage = models.IntegerField("Lens 6 Voltage (-)", null=True, blank=True)

    zlens_3_voltage_plus = models.IntegerField("Z-Lens 3 Voltage (+)", null=True, blank=True)

    zlens_3_voltage = models.IntegerField("Z-Lens 3 Voltage (-)", null=True, blank=True)

    deinject_voltage_plus = models.IntegerField("De-Inject Voltage (+)", null=True, blank=True)

    deinject_voltage = models.IntegerField("De-Inject Voltage (-)", null=True, blank=True)

    demeasure_voltage_plus = models.IntegerField("De-Measure Voltage (+)", null=True, blank=True)

    demeasure_voltage = models.IntegerField("De-Measure Voltage (-)", null=True, blank=True)

    ceinject_voltage_plus = models.IntegerField("CE-Inject Voltage (+)", null=True, blank=True)

    ceinject_voltage = models.IntegerField("CE-Inject Voltage (-)", null=True, blank=True)





class MetaConfigurationData(models.Model):


    class Meta:
        verbose_name = "Meta:  Configuration Data"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Meta')

    preamp_protect_mode = models.IntegerField("Preamp Protect Mode", null=True, blank=True)

    tmp_sweep_mode = models.IntegerField("TMP Sweep Mode", null=True, blank=True)

    temp_sensor_mode = models.IntegerField("Temp Sensor Mode", null=True, blank=True)





class ReportSpectrumCount(models.Model):


    class Meta:
        verbose_name = "Report: Spectrum Count"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    ms2_scans = models.IntegerField("MS2 Scans", null=True, blank=True)

    ms1_scansfull = models.IntegerField("MS1 Scans/Full", null=True, blank=True)

    ms1_scansother = models.IntegerField("MS1 Scans/Other", null=True, blank=True)





class ReportFirstAndLastMs1Rt_Min(models.Model):


    class Meta:
        verbose_name = "Report: First And Last Ms1 Rt (Min)"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    first_ms1 = models.FloatField("First MS1", null=True, blank=True)

    last_ms1 = models.FloatField("Last MS1", null=True, blank=True)





class ReportTrypticPeptideCount(models.Model):


    class Meta:
        verbose_name = "Report: Tryptic Peptide Count"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    peptides = models.IntegerField("Peptides", null=True, blank=True)

    ions = models.IntegerField("Ions", null=True, blank=True)

    identifications = models.IntegerField("Identifications", null=True, blank=True)

    abundance_pct = models.FloatField("Abundance Pct", null=True, blank=True)

    abundance1000 = models.FloatField("Abundance/1000", null=True, blank=True)

    ionspeptide = models.FloatField("Ions/Peptide", null=True, blank=True)

    idspeptide = models.FloatField("IDs/Peptide", null=True, blank=True)





class ReportPeptideCount(models.Model):


    class Meta:
        verbose_name = "Report: Peptide Count"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    peptides = models.IntegerField("Peptides", null=True, blank=True)

    ions = models.IntegerField("Ions", null=True, blank=True)

    identifications = models.IntegerField("Identifications", null=True, blank=True)

    semitryp_peps = models.FloatField("Semi/Tryp Peps", null=True, blank=True)

    semitryp_cnts = models.FloatField("Semi/Tryp Cnts", null=True, blank=True)

    semitryp_abund = models.FloatField("Semi/Tryp Abund", null=True, blank=True)

    misstryp_peps = models.FloatField("Miss/Tryp Peps", null=True, blank=True)

    misstryp_cnts = models.FloatField("Miss/Tryp Cnts", null=True, blank=True)

    misstryp_abund = models.FloatField("Miss/Tryp Abund", null=True, blank=True)

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

    ionspeptide = models.FloatField("Ions/Peptide", null=True, blank=True)

    idspeptide = models.FloatField("IDs/Peptide", null=True, blank=True)

    itraq_ids = models.IntegerField("iTRAQ IDs", null=True, blank=True)




class ReportDifferentProtein(models.Model):


    class Meta:
        verbose_name = "Report: Different Protein"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    n1_or_more_peps = models.IntegerField("1 or more Peps", null=True, blank=True)

    gt1_peptides = models.IntegerField(">1 Peptides", null=True, blank=True)





class ReportMiddlePeptideRetentionTimePeriod_Min(models.Model):


    class Meta:
        verbose_name = "Report: Middle Peptide Retention Time Period (Min)"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    half_period = models.FloatField("Half Period", null=True, blank=True)

    start_time = models.FloatField("Start Time", null=True, blank=True)

    mid_time = models.FloatField("Mid Time", null=True, blank=True)

    qratio_time = models.FloatField("Qratio Time", null=True, blank=True)

    ms2_scans = models.IntegerField("MS2 scans", null=True, blank=True)

    ms1_scans = models.IntegerField("MS1 Scans", null=True, blank=True)

    pep_id_rate = models.FloatField("Pep ID Rate", null=True, blank=True)

    id_rate = models.FloatField("ID Rate", null=True, blank=True)

    id_efficiency = models.FloatField("ID Efficiency", null=True, blank=True)





class ReportMs1DuringMiddle_AndEarly_PeptideRetentionPer(models.Model):


    class Meta:
        verbose_name = "Report: Ms1 During Middle (And Early) Peptide Retention Period"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    sn_median = models.FloatField("S/N Median", null=True, blank=True)

    tic_median1000 = models.IntegerField("TIC Median/1000", null=True, blank=True)
    
    tic_medi10000 = models.IntegerField("TIC Medi/10000", null=True, blank=True)

    npeaks_median = models.IntegerField("Npeaks Median", null=True, blank=True)

    scantoscan = models.FloatField("Scan-to-Scan", null=True, blank=True)

    s2s3qmed = models.FloatField("S2S-3Q/Med", null=True, blank=True)

    s2s1qrtmed = models.FloatField("S2S-1Qrt/Med", null=True, blank=True)

    s2s2qrtmed = models.FloatField("S2S-2Qrt/Med", null=True, blank=True)

    s2s3qrtmed = models.FloatField("S2S-3Qrt/Med", null=True, blank=True)

    s2s4qrtmed = models.FloatField("S2S-4Qrt/Med", null=True, blank=True)
    
    s2s_max = models.FloatField("S2S max", null=True, blank=True)

    s2s_max_rt = models.IntegerField("S2S max RT", null=True, blank=True)

    s2s_rt_ranges = models.IntegerField("S2S RT range/s", null=True, blank=True)

    s2s_2nd = models.FloatField("S2S 2nd", null=True, blank=True)

    s2s_2nd_rt = models.FloatField("S2S 2nd RT", null=True, blank=True)

    s2s_3rd = models.FloatField("S2S 3rd", null=True, blank=True)

    s2s_3rd_rt = models.FloatField("S2S 3rd RT", null=True, blank=True)


    esi_off_time = models.FloatField("ESI Off Time", null=True, blank=True)

    max_ms1_jump = models.FloatField("Max MS1 Jump", null=True, blank=True)

    max_ms1_fall = models.FloatField("Max MS1 Fall", null=True, blank=True)

    ms1_jumps_gt10x = models.IntegerField("MS1 Jumps >10x", null=True, blank=True)

    ms1_falls_ltdot1x = models.IntegerField("MS1 Falls <.1x", null=True, blank=True)

    esi_off_lowrt = models.FloatField("ESI Off LowRT", null=True, blank=True)

    max_jump_lowrt = models.FloatField("Max Jump LowRT", null=True, blank=True)

    max_fall_lowrt = models.FloatField("Max Fall LowRT", null=True, blank=True)

    ms1_lowrt_gt10x = models.IntegerField("MS1 LowRT >10x", null=True, blank=True)

    ms1_lowrt_ltdot1x = models.IntegerField("MS1 LowRT <.1x", null=True, blank=True)

    esi_off_hirt = models.FloatField("ESI Off HiRT", null=True, blank=True)

    max_jump_hirt = models.FloatField("Max Jump HiRT", null=True, blank=True)

    max_fall_hirt = models.FloatField("Max Fall HiRT", null=True, blank=True)

    ms1_hirt_gt10x = models.IntegerField("MS1 HiRT >10x", null=True, blank=True)

    ms1_hirt_ltdot1x = models.IntegerField("MS1 HiRT <.1x", null=True, blank=True)




class ReportMs1TotalIonCurrentForDifferentRtPeriod(models.Model):


    class Meta:
        verbose_name = "Report: Ms1 Total Ion Current For Different Rt Period"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    n1st_quart_id = models.FloatField("1st Quart ID", null=True, blank=True)

    middle_id = models.FloatField("Middle ID", null=True, blank=True)

    last_id_quart = models.FloatField("Last ID Quart", null=True, blank=True)

    to_end_of_run = models.FloatField("To End of Run", null=True, blank=True)





class ReportTotalIonCurrentForIdsAtPeakMaxima(models.Model):


    class Meta:
        verbose_name = "Report: Total Ion Current For Ids At Peak Maxima"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    med_tic_id1000 = models.FloatField("Med TIC ID/1000", null=True, blank=True)

    interq_tic = models.FloatField("InterQ TIC", null=True, blank=True)

    mid_interq_tic = models.FloatField("Mid InterQ TIC", null=True, blank=True)





class ReportPrecursorMZForId(models.Model):


    class Meta:
        verbose_name = "Report: Precursor M/Z For Id"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

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

    med_at_q1_rtplus2 = models.FloatField("Med @ Q1 RT/+2", null=True, blank=True)

    med_at_q2_rtplus2 = models.FloatField("Med @ Q2 RT/+2", null=True, blank=True)

    med_at_q3_rtplus2 = models.FloatField("Med @ Q3 RT/+2", null=True, blank=True)

    med_at_q4_rtplus2 = models.FloatField("Med @ Q4 RT/+2", null=True, blank=True)

    med_charge_plus1 = models.FloatField("Med Charge +1", null=True, blank=True)

    med_charge_plus2 = models.FloatField("Med Charge +2", null=True, blank=True)

    med_charge_plus3 = models.FloatField("Med Charge +3", null=True, blank=True)

    med_charge_plus4 = models.FloatField("Med Charge +4", null=True, blank=True)





class ReportNumberOfIonsVsCharge(models.Model):


    class Meta:
        verbose_name = "Report: Number Of Ions Vs Charge"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    charge_plus1 = models.IntegerField("Charge +1", null=True, blank=True)

    charge_plus2 = models.IntegerField("Charge +2", null=True, blank=True)

    charge_plus3 = models.IntegerField("Charge +3", null=True, blank=True)

    charge_plus4 = models.IntegerField("Charge +4", null=True, blank=True)

    charge_plus5 = models.IntegerField("Charge +5", null=True, blank=True)

    plus2_at_q1_rt = models.IntegerField("+2 @ Q1 RT", null=True, blank=True)

    plus2_at_q2_rt = models.IntegerField("+2 @ Q2 RT", null=True, blank=True)

    plus2_at_q3_rt = models.IntegerField("+2 @ Q3 RT", null=True, blank=True)

    plus2_at_q4_rt = models.IntegerField("+2 @ Q4 RT", null=True, blank=True)

    plus1plus2_at_q1_rt = models.FloatField("+1/+2 @ Q1 RT", null=True, blank=True)

    plus1plus2_at_q2_rt = models.FloatField("+1/+2 @ Q2 RT", null=True, blank=True)

    plus1plus2_at_q3_rt = models.FloatField("+1/+2 @ Q3 RT", null=True, blank=True)

    plus1plus2_at_q4_rt = models.FloatField("+1/+2 @ Q4 RT", null=True, blank=True)

    plus3plus2_at_q1_rt = models.FloatField("+3/+2 @ Q1 RT", null=True, blank=True)

    plus3plus2_at_q2_rt = models.FloatField("+3/+2 @ Q2 RT", null=True, blank=True)

    plus3plus2_at_q3_rt = models.FloatField("+3/+2 @ Q3 RT", null=True, blank=True)

    plus3plus2_at_q4_rt = models.FloatField("+3/+2 @ Q4 RT", null=True, blank=True)





class ReportAveragesVsRtForIdedPeptide(models.Model):


    class Meta:
        verbose_name = "Report: Averages Vs Rt For Ided Peptide"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    length_q1 = models.FloatField("Length Q1", null=True, blank=True)

    length_q4 = models.FloatField("Length Q4", null=True, blank=True)

    charge_q1 = models.FloatField("Charge Q1", null=True, blank=True)

    charge_q4 = models.FloatField("Charge Q4", null=True, blank=True)





class ReportPrecursorMZPeptideIonMZ_Plus2ChargeOnlyRejec(models.Model):


    class Meta:
        verbose_name = "Report: Precursor M/Z - Peptide Ion M/Z (+2 Charge Only, Reject >0.45 M/Z)"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    spectra = models.IntegerField("Spectra", null=True, blank=True)

    median = models.FloatField("Median", null=True, blank=True)

    mean_absolute = models.FloatField("Mean Absolute", null=True, blank=True)

    ppm_median = models.FloatField("ppm Median", null=True, blank=True)

    ppm_interq = models.FloatField("ppm InterQ", null=True, blank=True)





class ReportIonIdsByChargeState_RelativeToPlus2(models.Model):


    class Meta:
        verbose_name = "Report: Ion Ids By Charge State (Relative To +2)"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    plus2_ion_count = models.IntegerField("+2 Ion Count", null=True, blank=True)

    charge_plus1 = models.FloatField("Charge +1", null=True, blank=True)

    charge_plus2 = models.FloatField("Charge +2", null=True, blank=True)

    charge_plus3 = models.FloatField("Charge +3", null=True, blank=True)

    charge_plus4 = models.FloatField("Charge +4", null=True, blank=True)





class ReportAveragePeptideLengthsForDifferentChargeState(models.Model):


    class Meta:
        verbose_name = "Report: Average Peptide Lengths For Different Charge State"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    charge_plus1 = models.FloatField("Charge +1", null=True, blank=True)

    charge_plus2 = models.FloatField("Charge +2", null=True, blank=True)

    charge_plus3 = models.FloatField("Charge +3", null=True, blank=True)

    charge_plus4 = models.FloatField("Charge +4", null=True, blank=True)





class ReportAveragePeptideLengthsForCharge2ForDifferentN(models.Model):


    class Meta:
        verbose_name = "Report: Average Peptide Lengths For Charge 2 For Different Numbers Of Mobile Proton"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    naacheq2mpeq1 = models.FloatField("NAA,Ch=2,MP=-1", null=True, blank=True)

    naacheq2mpeq0 = models.FloatField("NAA,Ch=2,MP=0", null=True, blank=True)

    naacheq2mpeq1 = models.FloatField("NAA,Ch=2,MP=1", null=True, blank=True)

    naacheq2mpeq2 = models.FloatField("NAA,Ch=2,MP=2", null=True, blank=True)





class ReportNumbersOfIonIdsAtDifferentChargesWith1Mobile(models.Model):


    class Meta:
        verbose_name = "Report: Numbers Of Ion Ids At Different Charges With 1 Mobile Proton"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    cheq1_mpeq1 = models.IntegerField("Ch=1 MP=1", null=True, blank=True)

    cheq2_mpeq1 = models.IntegerField("Ch=2 MP=1", null=True, blank=True)

    cheq3_mpeq1 = models.IntegerField("Ch=3 MP=1", null=True, blank=True)

    cheq4_mpeq1 = models.IntegerField("Ch=4 MP=1", null=True, blank=True)





class ReportPercentOfIdsAtDifferentChargesAndMobileProto(models.Model):


    class Meta:
        verbose_name = "Report: Percent Of Ids At Different Charges And Mobile Protons Relative To Ids With 1 Mobile Proton"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    cheq1_mpeq1 = models.FloatField("Ch=1 MP=-1", null=True, blank=True)

    cheq1_mpeq0 = models.FloatField("Ch=1 MP=0", null=True, blank=True)

    cheq1_mpeq1 = models.FloatField("Ch=1 MP=1", null=True, blank=True)

    cheq2_mpeq1 = models.FloatField("Ch=2 MP=-1", null=True, blank=True)

    cheq2_mpeq0 = models.FloatField("Ch=2 MP=0", null=True, blank=True)

    cheq2_mpeq1 = models.FloatField("Ch=2 MP=1", null=True, blank=True)

    cheq3_mpeq1 = models.FloatField("Ch=3 MP=-1", null=True, blank=True)

    cheq3_mpeq0 = models.FloatField("Ch=3 MP=0", null=True, blank=True)

    cheq3_mpeq1 = models.FloatField("Ch=3 MP=1", null=True, blank=True)





class ReportIntensitiesVsDifferentMobileProton(models.Model):


    class Meta:
        verbose_name = "Report: Intensities Vs Different Mobile Proton"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    ions_mpeq1 = models.IntegerField("Ions, MP=-1", null=True, blank=True)

    ions_mpeq0 = models.IntegerField("Ions, MP=0", null=True, blank=True)

    ions_mpeq1 = models.IntegerField("Ions, MP=1", null=True, blank=True)

    ions_mpeq2 = models.IntegerField("Ions, MP=2", null=True, blank=True)

    inten_mpeq1 = models.FloatField("Inten, MP=-1", null=True, blank=True)

    inten_mpeq0 = models.FloatField("Inten, MP=0", null=True, blank=True)

    inten_mpeq1 = models.FloatField("Inten, MP=1", null=True, blank=True)

    inten_mpeq2 = models.FloatField("Inten, MP=2", null=True, blank=True)





class ReportPrecursorMZMonoisotopeExactMZ(models.Model):


    class Meta:
        verbose_name = "Report: Precursor M/Z - Monoisotope Exact M/Z"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    more_than_100 = models.IntegerField("More Than 100", null=True, blank=True)

    betw_100dot050dot0 = models.IntegerField("Betw 100.0-50.0", null=True, blank=True)

    betw_50dot025dot0 = models.IntegerField("Betw 50.0-25.0", null=True, blank=True)

    betw_25dot012dot5 = models.IntegerField("Betw 25.0-12.5", null=True, blank=True)

    betw_12dot56dot3 = models.IntegerField("Betw 12.5-6.3", null=True, blank=True)

    betw_6dot33dot1 = models.IntegerField("Betw 6.3-3.1", null=True, blank=True)

    betw_3dot11dot6 = models.IntegerField("Betw 3.1-1.6", null=True, blank=True)

    betw_1dot60dot8 = models.IntegerField("Betw 1.6-0.8", null=True, blank=True)

    top_half = models.IntegerField("Top Half", null=True, blank=True)

    next_half_2 = models.IntegerField("Next Half (2)", null=True, blank=True)

    next_half_3 = models.IntegerField("Next Half (3)", null=True, blank=True)

    next_half_4 = models.IntegerField("Next Half (4)", null=True, blank=True)

    next_half_5 = models.IntegerField("Next Half (5)", null=True, blank=True)

    next_half_6 = models.IntegerField("Next Half (6)", null=True, blank=True)

    next_half_7 = models.IntegerField("Next Half (7)", null=True, blank=True)

    next_half_8 = models.IntegerField("Next Half (8)", null=True, blank=True)





class ReportMs2IdSpectra(models.Model):


    class Meta:
        verbose_name = "Report: Ms2 Id Spectra"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    npeaks_median = models.IntegerField("NPeaks Median", null=True, blank=True)

    npeaks_interq = models.FloatField("NPeaks InterQ", null=True, blank=True)

    sn_median = models.FloatField("S/N Median", null=True, blank=True)

    sn_interq = models.FloatField("S/N InterQ", null=True, blank=True)

    id_score_median = models.FloatField("ID Score Median", null=True, blank=True)

    id_score_interq = models.FloatField("ID Score InterQ", null=True, blank=True)

    idsc_med_q1msmx = models.FloatField("IDSc Med Q1Msmx", null=True, blank=True)





class ReportMs1IdMax(models.Model):


    class Meta:
        verbose_name = "Report: Ms1 Id Max"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    median = models.FloatField("Median", null=True, blank=True)

    half_width = models.FloatField("Half Width", null=True, blank=True)

    quart_ratio = models.FloatField("Quart Ratio", null=True, blank=True)

    median_midrt = models.FloatField("Median MidRT", null=True, blank=True)

    n7525_midrt = models.FloatField("75/25 MidRT", null=True, blank=True)

    n955_midrt = models.FloatField("95/5 MidRT", null=True, blank=True)

    n7525_pctile = models.FloatField("75/25 Pctile", null=True, blank=True)

    n955_pctile = models.FloatField("95/5 Pctile", null=True, blank=True)





class ReportFractionOfMs2IdentifiedAtDifferentMs1MaxQuar(models.Model):


    class Meta:
        verbose_name = "Report: Fraction Of Ms2 Identified At Different Ms1Max Quartile"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    id_fract_q1 = models.FloatField("ID Fract Q1", null=True, blank=True)

    id_fract_q2 = models.FloatField("ID fract Q2", null=True, blank=True)

    id_fract_q3 = models.FloatField("ID Fract Q3", null=True, blank=True)

    id_fract_q4 = models.FloatField("ID Fract Q4", null=True, blank=True)





class ReportMs1IdAbundAtMs2Acquisition(models.Model):


    class Meta:
        verbose_name = "Report: Ms1 Id Abund At Ms2 Acquisition"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    median = models.FloatField("Median", null=True, blank=True)

    half_width = models.FloatField("Half Width", null=True, blank=True)

    n7525_pctile = models.FloatField("75/25 Pctile", null=True, blank=True)

    n955_pctile = models.FloatField("95/5 Pctile", null=True, blank=True)





class ReportMs2IdAbundReported(models.Model):


    class Meta:
        verbose_name = "Report: Ms2 Id Abund Reported"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    median = models.FloatField("Median", null=True, blank=True)

    half_width = models.FloatField("Half Width", null=True, blank=True)

    n7525_pctile = models.FloatField("75/25 Pctile", null=True, blank=True)

    n955_pctile = models.FloatField("95/5 Pctile", null=True, blank=True)





class ReportPeakWidthAtHalfHeightForId(models.Model):


    class Meta:
        verbose_name = "Report: Peak Width At Half Height For Id"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

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

    ms1_interscans = models.FloatField("MS1 Interscan/s", null=True, blank=True)

    ms1_scanfwhm = models.FloatField("MS1 Scan/FWHM", null=True, blank=True)

    ids_used = models.IntegerField("IDs Used", null=True, blank=True)





class ReportPeakWidthsAtHalfMaxOverRtDecilesForId(models.Model):


    class Meta:
        verbose_name = "Report: Peak Widths At Half Max Over Rt Deciles For Id"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    first_decile = models.FloatField("First Decile", null=True, blank=True)

    median_value = models.FloatField("Median Value", null=True, blank=True)

    last_decile = models.FloatField("Last Decile", null=True, blank=True)





class ReportNearbyResamplingOfIdsOversamplingDetail(models.Model):


    class Meta:
        verbose_name = "Report: Nearby Resampling Of Ids - Oversampling Detail"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    repeated_ids = models.IntegerField("Repeated IDs", null=True, blank=True)

    med_rt_diffs = models.FloatField("Med RT Diff/s", null=True, blank=True)

    n1q_rt_diffs = models.FloatField("1Q RT Diff/s", null=True, blank=True)

    n1dec_rt_diffs = models.FloatField("1Dec RT Diff/s", null=True, blank=True)

    median_dmz = models.FloatField("Median dm/z", null=True, blank=True)

    quart_dmz = models.FloatField("Quart dm/z", null=True, blank=True)





class ReportWideRtDifferencesForIds_Gt4Min(models.Model):


    class Meta:
        verbose_name = "Report: Wide Rt Differences For Ids (> 4 Min)"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    peptides = models.IntegerField("Peptides", null=True, blank=True)

    spectra = models.IntegerField("Spectra", null=True, blank=True)





class ReportFractionOfRepeatPeptideIdsWithDivergentRt_Rt(models.Model):


    class Meta:
        verbose_name = "Report: Fraction Of Repeat Peptide Ids With Divergent Rt (Rt Vs Rt-Best Id) - Chromatographic 'Bleed'"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    _4_min = models.FloatField("- 4 min", null=True, blank=True)

    plus_4_min = models.FloatField("+ 4 min", null=True, blank=True)





class ReportEarlyAndLateRtOversampling_SpectrumIdsUnique(models.Model):


    class Meta:
        verbose_name = "Report: Early And Late Rt Oversampling (Spectrum Ids/Unique Peptide Ids) - Chromatographic: Flow Through/Bleed"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    first_decile = models.FloatField("First Decile", null=True, blank=True)

    last_decile = models.FloatField("Last Decile", null=True, blank=True)





class ReportPeptideIonIdsByGt3Spectra_Hi_Vs13Spectra_Lo_(models.Model):


    class Meta:
        verbose_name = "Report: Peptide Ion Ids By > 3 Spectra (Hi) Vs  1-3 Spectra (Lo) - Extreme Oversampling"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    pep_ions_hi = models.IntegerField("Pep Ions (Hi)", null=True, blank=True)

    ratio_hilo = models.FloatField("Ratio Hi/Lo", null=True, blank=True)

    spec_cnts_hi = models.IntegerField("Spec Cnts (Hi)", null=True, blank=True)

    ratio_hilo = models.FloatField("Ratio Hi/Lo", null=True, blank=True)

    specpep_hi = models.FloatField("Spec/Pep (Hi)", null=True, blank=True)

    spec_cnt_excess = models.FloatField("Spec Cnt Excess", null=True, blank=True)





class ReportRatiosOfPeptideIonsIdedByDifferentNumbersOfS(models.Model):


    class Meta:
        verbose_name = "Report: Ratios Of Peptide Ions Ided By Different Numbers Of Spectra - Oversampling Measure"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    oncetwice = models.FloatField("Once/Twice", null=True, blank=True)

    twicethrice = models.FloatField("Twice/Thrice", null=True, blank=True)





class ReportSingleSpectrumPeptideIonIdentificationsOvers(models.Model):


    class Meta:
        verbose_name = "Report: Single Spectrum Peptide Ion Identifications - Oversampling Measure"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    peptide_ions = models.IntegerField("Peptide Ions", null=True, blank=True)

    fract_gt1_ions = models.FloatField("Fract >1 Ions", null=True, blank=True)

    n1_vs_gt1_pepion = models.FloatField("1 vs >1 PepIon", null=True, blank=True)

    n1_vs_gt1_spec = models.FloatField("1 vs >1 Spec", null=True, blank=True)





class ReportMs1MaxMs1SampledAbundanceRatioIdsInefficient(models.Model):


    class Meta:
        verbose_name = "Report: Ms1Max/Ms1Sampled Abundance Ratio Ids - Inefficient Sampling"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    median_all_ids = models.FloatField("Median All IDs", null=True, blank=True)

    n3q_all_ids = models.FloatField("3Q All IDs", null=True, blank=True)

    n9dec_all_ids = models.FloatField("9Dec All IDs", null=True, blank=True)

    med_top_100 = models.FloatField("Med Top 100", null=True, blank=True)

    med_top_dec = models.FloatField("Med Top Dec", null=True, blank=True)

    med_top_quart = models.FloatField("Med Top Quart", null=True, blank=True)

    med_bottom_12 = models.FloatField("Med Bottom 1/2", null=True, blank=True)





class ReportRt_Ms1Max_Rt_Ms2_ForIds_Sec(models.Model):


    class Meta:
        verbose_name = "Report: Rt(Ms1Max)-Rt(Ms2) For Ids (Sec)"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    med_diff_abs = models.IntegerField("Med Diff Abs", null=True, blank=True)

    median_diff = models.IntegerField("Median Diff", null=True, blank=True)

    first_quart = models.IntegerField("First Quart", null=True, blank=True)

    third_quart = models.IntegerField("Third Quart", null=True, blank=True)





class ReportIonInjectionTimesForIds_Ms(models.Model):


    class Meta:
        verbose_name = "Report: Ion Injection Times For Ids (Ms)"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    ms1_median = models.IntegerField("MS1 Median", null=True, blank=True)

    ms1_maximum = models.IntegerField("MS1 Maximum", null=True, blank=True)

    ms2_median = models.FloatField("MS2 Median", null=True, blank=True)

    ms2_maximun = models.FloatField("MS2 Maximun", null=True, blank=True)

    ms2_fract_max = models.FloatField("MS2 Fract Max", null=True, blank=True)





class ReportTopIonAbundanceMeasure(models.Model):


    class Meta:
        verbose_name = "Report: Top Ion Abundance Measure"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    top_10percent_abund = models.IntegerField("Top 10% Abund", null=True, blank=True)

    top_25percent_abund = models.IntegerField("Top 25% Abund", null=True, blank=True)

    top_50percent_abund = models.IntegerField("Top 50% Abund", null=True, blank=True)

    fractab_top = models.FloatField("Fractab Top", null=True, blank=True)

    fractab_top_10 = models.FloatField("Fractab Top 10", null=True, blank=True)

    fractab_top_100 = models.FloatField("Fractab Top 100", null=True, blank=True)





class ReportIsotopicAbundanceVariation(models.Model):


    class Meta:
        verbose_name = "Report: Isotopic Abundance Variation"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    number_of_ions = models.IntegerField("Number of Ions", null=True, blank=True)

    median_dev = models.FloatField("Median Dev", null=True, blank=True)

    interquart = models.FloatField("Interquart", null=True, blank=True)





class ReportIonPeakClusterCountDistribution(models.Model):


    class Meta:
        verbose_name = "Report: Ion 'Peak Cluster' Count Distribution"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    total_found = models.IntegerField("Total Found", null=True, blank=True)

    id_fraction = models.FloatField("ID Fraction", null=True, blank=True)

    noid_fraction = models.FloatField("noID Fraction", null=True, blank=True)

    nosamp_fraction = models.FloatField("noSamp Fraction", null=True, blank=True)





class ReportIonClusterAbundanceDistribution(models.Model):


    class Meta:
        verbose_name = "Report: Ion Cluster Abundance Distribution"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    id_fraction = models.FloatField("ID Fraction", null=True, blank=True)

    noid_fraction = models.FloatField("noID Fraction", null=True, blank=True)

    nosamp_fraction = models.FloatField("noSamp Fraction", null=True, blank=True)

    noid_med_rel = models.FloatField("noID Med Rel", null=True, blank=True)

    unsamp_med_rel = models.FloatField("Unsamp Med Rel", null=True, blank=True)





class ReportAbundanceDistributionTotal(models.Model):


    class Meta:
        verbose_name = "Report: Abundance Distribution: Total"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    total_fraction = models.FloatField("Total Fraction", null=True, blank=True)

    peptides = models.FloatField("Peptides", null=True, blank=True)

    samplednoid = models.FloatField("Sampled-NoID", null=True, blank=True)

    not_sampled_percent = models.FloatField("Not Sampled %", null=True, blank=True)

    noise = models.FloatField("Noise", null=True, blank=True)





class ReportAbundanceDistribution1RtQuartile(models.Model):


    class Meta:
        verbose_name = "Report: Abundance Distribution: 1 Rt Quartile"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    rt_segment_end = models.FloatField("RT Segment End", null=True, blank=True)

    total_fraction = models.FloatField("Total Fraction", null=True, blank=True)

    peptides = models.FloatField("Peptides", null=True, blank=True)

    samplednoid = models.FloatField("Sampled-NoID", null=True, blank=True)

    not_sampled_percent = models.FloatField("Not Sampled %", null=True, blank=True)

    noise = models.FloatField("Noise", null=True, blank=True)





class ReportAbundanceDistribution2RtQuartile(models.Model):


    class Meta:
        verbose_name = "Report: Abundance Distribution: 2 Rt Quartile"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    rt_segment_end = models.FloatField("RT Segment End", null=True, blank=True)

    total_fraction = models.FloatField("Total Fraction", null=True, blank=True)

    peptides = models.FloatField("Peptides", null=True, blank=True)

    samplednoid = models.FloatField("Sampled-NoID", null=True, blank=True)

    not_sampled_percent = models.FloatField("Not Sampled %", null=True, blank=True)

    noise = models.FloatField("Noise", null=True, blank=True)





class ReportAbundanceDistribution3RtQuartile(models.Model):


    class Meta:
        verbose_name = "Report: Abundance Distribution: 3 Rt Quartile"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    rt_segment_end = models.FloatField("RT Segment End", null=True, blank=True)

    total_fraction = models.FloatField("Total Fraction", null=True, blank=True)

    peptides = models.FloatField("Peptides", null=True, blank=True)

    samplednoid = models.FloatField("Sampled-NoID", null=True, blank=True)

    not_sampled_percent = models.FloatField("Not Sampled %", null=True, blank=True)

    noise = models.FloatField("Noise", null=True, blank=True)





class ReportAbundanceDistribution4RtQuartile(models.Model):


    class Meta:
        verbose_name = "Report: Abundance Distribution: 4 Rt Quartile"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    rt_segment_end = models.FloatField("RT Segment End", null=True, blank=True)

    total_fraction = models.FloatField("Total Fraction", null=True, blank=True)

    peptides = models.FloatField("Peptides", null=True, blank=True)

    samplednoid = models.FloatField("Sampled-NoID", null=True, blank=True)

    not_sampled_percent = models.FloatField("Not Sampled %", null=True, blank=True)

    noise = models.FloatField("Noise", null=True, blank=True)





class ReportAbundanceDistributionLastSegment(models.Model):


    class Meta:
        verbose_name = "Report: Abundance Distribution: Last Segment"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    rt_segment_end = models.FloatField("RT Segment End", null=True, blank=True)

    total_fraction = models.FloatField("Total Fraction", null=True, blank=True)

    peptides = models.FloatField("Peptides", null=True, blank=True)

    samplednoid = models.FloatField("Sampled-NoID", null=True, blank=True)

    not_sampled_percent = models.FloatField("Not Sampled %", null=True, blank=True)

    noise = models.FloatField("Noise", null=True, blank=True)





class ReportMZMediansForClustersAtRtQuartiles_AllCharges(models.Model):


    class Meta:
        verbose_name = "Report: M/Z Medians For Clusters At Rt Quartiles (All Charges)"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    first_quart = models.FloatField("First Quart", null=True, blank=True)

    second_quart = models.FloatField("Second Quart", null=True, blank=True)

    third_quart = models.FloatField("Third Quart", null=True, blank=True)

    fourth_quart = models.FloatField("Fourth Quart", null=True, blank=True)





class ReportMZMediansForClustersAtRtQuartiles_Plus2Only(models.Model):


    class Meta:
        verbose_name = "Report: M/Z Medians For Clusters At Rt Quartiles (+2 Only)"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    first_quart = models.FloatField("First Quart", null=True, blank=True)

    second_quart = models.FloatField("Second Quart", null=True, blank=True)

    third_quart = models.FloatField("Third Quart", null=True, blank=True)

    fourth_quart = models.FloatField("Fourth Quart", null=True, blank=True)





class ReportMZMediansForClustersAtDifferentCharge(models.Model):


    class Meta:
        verbose_name = "Report: M/Z Medians For Clusters At Different Charge"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    charge_plus1 = models.FloatField("Charge +1", null=True, blank=True)

    charge_plus2 = models.FloatField("Charge +2", null=True, blank=True)

    charge_plus3 = models.FloatField("Charge +3", null=True, blank=True)

    no_charge = models.FloatField("No Charge", null=True, blank=True)





class ReportNumbersOfClustersOfDifferentCharge(models.Model):


    class Meta:
        verbose_name = "Report: Numbers Of Clusters Of Different Charge"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    charge_plus2 = models.IntegerField("Charge +2", null=True, blank=True)

    no_chargeplus2 = models.FloatField("No Charge/+2", null=True, blank=True)

    charge_plus1plus2 = models.FloatField("Charge +1/+2", null=True, blank=True)

    charge_plus3plus2 = models.FloatField("Charge +3/+2", null=True, blank=True)





class ReportNumbersOfClustersAtPlus1Plus2ChargesAtRtQuar(models.Model):


    class Meta:
        verbose_name = "Report: Numbers Of Clusters At +1/+2 Charges At Rt Quartile"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    plus2_clusters = models.IntegerField("+2 Clusters", null=True, blank=True)

    rt_quart_1 = models.FloatField("RT Quart 1", null=True, blank=True)

    rt_quart_2 = models.FloatField("RT Quart 2", null=True, blank=True)

    rt_quart_3 = models.FloatField("RT Quart 3", null=True, blank=True)

    rt_quart_4 = models.FloatField("RT Quart 4", null=True, blank=True)





class ReportNumbersOfClustersAtPlus3Plus2ChargesAtRtQuar(models.Model):


    class Meta:
        verbose_name = "Report: Numbers Of Clusters At +3/+2 Charges At Rt Quartile"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    plus2_clusters = models.IntegerField("+2 Clusters", null=True, blank=True)

    rt_quart_1 = models.FloatField("RT Quart 1", null=True, blank=True)

    rt_quart_2 = models.FloatField("RT Quart 2", null=True, blank=True)

    rt_quart_3 = models.FloatField("RT Quart 3", null=True, blank=True)

    rt_quart_4 = models.FloatField("RT Quart 4", null=True, blank=True)





class ReportFractOfClusterAbundanceAt50PercentAnd90Perce(models.Model):


    class Meta:
        verbose_name = "Report: Fract Of Cluster Abundance At 50% And 90% Of All Abundance"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    n50percent_ions = models.IntegerField("50% Ions", null=True, blank=True)

    n50percent_id = models.FloatField("50% ID", null=True, blank=True)

    n50percent_noidsamp = models.FloatField("50% noIDSamp", null=True, blank=True)

    n50percent_noidnosamp = models.FloatField("50% noIDnoSamp", null=True, blank=True)

    n90percent_ions = models.IntegerField("90% Ions", null=True, blank=True)

    n90percent_id = models.FloatField("90% ID", null=True, blank=True)

    n90percent_noidsamp = models.FloatField("90% noIDSamp", null=True, blank=True)

    n90percent_noidnosamp = models.FloatField("90% noIDnoSamp", null=True, blank=True)





class ReportTop10NoidIon(models.Model):


    class Meta:
        verbose_name = "Report: Top 10 Noid Ion"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    noid_1_rank = models.IntegerField("NoID 1 Rank", null=True, blank=True)

    noid_1_relab = models.FloatField("NoID 1 RelAb", null=True, blank=True)

    noid_1_rt = models.FloatField("NoID 1 RT", null=True, blank=True)

    noid_1_mz = models.FloatField("NoID 1 m/z", null=True, blank=True)

    noid_2_rank = models.IntegerField("NoID 2 Rank", null=True, blank=True)

    noid_2_relab = models.FloatField("NoID 2 RelAb", null=True, blank=True)

    noid_2_rt = models.FloatField("NoID 2 RT", null=True, blank=True)

    noid_2_mz = models.FloatField("NoID 2 m/z", null=True, blank=True)

    noid_3_rank = models.IntegerField("NoID 3 Rank", null=True, blank=True)

    noid_3_relab = models.FloatField("NoID 3 RelAb", null=True, blank=True)

    noid_3_rt = models.FloatField("NoID 3 RT", null=True, blank=True)

    noid_3_mz = models.FloatField("NoID 3 m/z", null=True, blank=True)

    noid_4_rank = models.IntegerField("NoID 4 Rank", null=True, blank=True)

    noid_4_relab = models.FloatField("NoID 4 RelAb", null=True, blank=True)

    noid_4_rt = models.FloatField("NoID 4 RT", null=True, blank=True)

    noid_4_mz = models.FloatField("NoID 4 m/z", null=True, blank=True)

    noid_5_rank = models.IntegerField("NoID 5 Rank", null=True, blank=True)

    noid_5_relab = models.FloatField("NoID 5 RelAb", null=True, blank=True)

    noid_5_rt = models.FloatField("NoID 5 RT", null=True, blank=True)

    noid_5_mz = models.FloatField("NoID 5 m/z", null=True, blank=True)

    noid_6_rank = models.IntegerField("NoID 6 Rank", null=True, blank=True)

    noid_6_relab = models.FloatField("NoID 6 RelAb", null=True, blank=True)

    noid_6_rt = models.FloatField("NoID 6 RT", null=True, blank=True)

    noid_6_mz = models.FloatField("NoID 6 m/z", null=True, blank=True)

    noid_7_rank = models.IntegerField("NoID 7 Rank", null=True, blank=True)

    noid_7_relab = models.FloatField("NoID 7 RelAb", null=True, blank=True)

    noid_7_rt = models.FloatField("NoID 7 RT", null=True, blank=True)

    noid_7_mz = models.FloatField("NoID 7 m/z", null=True, blank=True)

    noid_8_rank = models.IntegerField("NoID 8 Rank", null=True, blank=True)

    noid_8_relab = models.FloatField("NoID 8 RelAb", null=True, blank=True)

    noid_8_rt = models.FloatField("NoID 8 RT", null=True, blank=True)

    noid_8_mz = models.FloatField("NoID 8 m/z", null=True, blank=True)

    noid_9_rank = models.IntegerField("NoID 9 Rank", null=True, blank=True)

    noid_9_relab = models.FloatField("NoID 9 RelAb", null=True, blank=True)

    noid_9_rt = models.FloatField("NoID 9 RT", null=True, blank=True)

    noid_9_mz = models.FloatField("NoID 9 m/z", null=True, blank=True)

    noid_10_rank = models.IntegerField("NoID 10 Rank", null=True, blank=True)

    noid_10_relab = models.FloatField("NoID 10 RelAb", null=True, blank=True)

    noid_10_rt = models.FloatField("NoID 10 RT", null=True, blank=True)

    noid_10_mz = models.FloatField("NoID 10 m/z", null=True, blank=True)





class ReportNewMetric(models.Model):


    class Meta:
        verbose_name = "Report: New Metric"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    peak_wid_alt = models.FloatField("Peak Wid Alt", null=True, blank=True)

    unexpect_int = models.IntegerField("Unexpect Int", null=True, blank=True)





class ReportOtherIonClusterStatistic(models.Model):


    class Meta:
        verbose_name = "Report: Other Ion Cluster Statistic"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

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

    qual_percent_00 = models.FloatField("Qual % 0:0", null=True, blank=True)

    qual_percent_1019 = models.FloatField("Qual % 10:19", null=True, blank=True)

    qual_percent_2029 = models.FloatField("Qual % 20:29", null=True, blank=True)

    qual_percent_3039 = models.FloatField("Qual % 30:39", null=True, blank=True)

    qual_percent_4049 = models.FloatField("Qual % 40:49", null=True, blank=True)

    qual_percent_5059 = models.FloatField("Qual % 50:59", null=True, blank=True)

    qual_percent_6069 = models.FloatField("Qual % 60:69", null=True, blank=True)

    qual_percent_7079 = models.FloatField("Qual % 70:79", null=True, blank=True)

    qual_percent_8089 = models.FloatField("Qual % 80:89", null=True, blank=True)

    qual_percent_9099 = models.FloatField("Qual % 90:99", null=True, blank=True)

    qual_percent_100100 = models.FloatField("Qual % 100:100", null=True, blank=True)
    
    


class ReportHcdMetric(models.Model):


    class Meta:
        verbose_name = "Report: Hcd Metric"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

    nb_spectra = models.IntegerField("# Spectra", null=True, blank=True)

    ceparentplus2 = models.FloatField("CE/Parent:+2", null=True, blank=True)

    ceparentplus3 = models.FloatField("CE/Parent:+3", null=True, blank=True)

    fragpre_plus2_l10 = models.FloatField("Frag/Pre +2 L10", null=True, blank=True)

    fragpre_plus3_l10 = models.FloatField("Frag/Pre +3 L10", null=True, blank=True)

    fragpre_plus2_iq = models.FloatField("Frag/Pre +2 IQ", null=True, blank=True)

    fragpre_plus3_iq = models.FloatField("Frag/Pre +3 IQ", null=True, blank=True)

    fragpre_plus2_m0 = models.FloatField("Frag/Pre +2 m0", null=True, blank=True)

    fragpre_plus2_m1 = models.FloatField("Frag/Pre +2 m1", null=True, blank=True)




class ReportPeakWidthForMiddleHalfOfSignalForId(models.Model):


    class Meta:
        verbose_name = "Report: Peak Width For Middle Half Of Signal For Id"


    sample = models.ForeignKey(Sample, related_name='%(class)s_Report')

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

    ms1_interscans = models.FloatField("MS1 Interscan/s", null=True, blank=True)

    ms1_scanfwhm = models.FloatField("MS1 Scan/FWHM", null=True, blank=True)

    ids_used = models.IntegerField("IDs Used", null=True, blank=True)

    
    
class Reservation(models.Model):
    """
    Stores instrument reservation and scheduling.
    """

    created_by = models.ForeignKey(User, null=True, blank=True,
                                   related_name='%(class)s_created_by', 
                                   editable=False)
    
    creation_date = models.DateTimeField(auto_now_add=True)
    
    modification_date = models.DateTimeField('Modified at', auto_now=True)
    
    instrument = models.ForeignKey(Instrument)
    
    time_needed = models.FloatField('Time_needed (days)')
    
    sample_count = models.IntegerField(blank=True, null=True)
    
    comment = models.TextField(help_text='Chromatography, deadline, assistance required, \
                                project details, etc.',
                               blank=True, null=True)
    
    
    prefered_start_date = models.DateField('Prefered start date', 
                                               blank=True, null=True)
    
    scheduled_start_date = models.DateField('Scheduled start date', 
                                                blank=True, null=True)
    
    scheduled_end_date = models.DateField('Scheduled end date', 
                                              blank=True, null=True)
