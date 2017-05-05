package typhoon_api version=0.1


interface hil_api [

    def load_model(str file="", bool offlineMode=True, bool vhil_device=False, bool *status)
    def load_settings_file(str file="", bool *status)
    def save_settings_file(str filePath, bool *status)
    def update_sources(list<str> sources, float executeAt=None, bool *status)
    def prepare_source_arbitrary_waveform(str name, str file = "", bool *status)
    def prepare_source_constant_value(str name, float value = 0, bool *status)

    def prepare_source_sine_waveform(str name, float rms=None,
                                     float frequency=None, float phase=None,
                                     list harmonics=None,
                                     list harmonics_pu=None,
                                     bool *status)

    def set_source_scaling(str name, float scaling, float executeAt=None)

    def set_pv_input_file(str name, str file, float illumination=0.0,
                          float temperature = 0.0, bool *status)

    def set_pv_amb_params(str name, float illumination=None,
                          float temperature=None, float executeAt=None,
                          list *result)

    def set_analog_output(i64 channel, str name=None, float scaling=None,
                          float offset = None, i64 device=0, bool *status)

    def set_analog_output_signal(i64 channel, str name, i64 device=0,
                                 bool *status)

    def set_analog_output_scaling(i64 channel, float scaling=0.0, i64 device=0,
                                  bool *status)

    def set_analog_output_offset(i64 channel, float offset=0.0, i64 device=0,
                                 bool *status)

    def set_digital_output(i64 channel, str name=None, bool invert=None,
                           bool swControl=None, i64 value = None, i64 device=0,
                           bool *status)

    def set_digital_output_signal(i64 channel, str name, i64 device=0,
                                  bool *status)

    def set_digital_output_inverting(i64 channel, bool invert=False, i64 device=0,
                                     bool *status)

    def set_digital_output_sw_control(i64 channel, bool swControl=False, i64 device=0,
                                      bool *status)
    
    def set_digital_output_software_value(i64 channel, i64 value=0, i64 device=0,
                                          bool *status)

    def set_contactor(str name, bool swControl=None, bool swState=None,
                      float executeAt=None, bool *status)

    def set_contactor_control_mode(str name, bool swControl=False, float executeAt=None,
                                   bool *status)
         
    def set_contactor_state(str name, bool swState=False, float executeAt=None,
                            bool *status)

    def set_machine_constant_torque(str name = "", float value=0.0, float executeAt=None,
                                    bool *status)
    def set_machine_linear_torque(str name = "", float value=0.0, float executeAt=None,
                                  bool *status)
    def set_machine_square_torque(str name = "", float value=0.0, float executeAt=None,
                                  bool *status)

    def set_machine_load_source(str name = "", bool software=True,
                                bool *status)

    def set_machine_external_torque_type(str name = "", bool frictional=True,
                                         bool *status)

    def set_machine_constant_torque_type(str name = "", bool frictional=True,
                                         bool *status)

    def set_machine_load_type(str name = "", bool torque=True, bool *status)

    def set_machine_speed(str name = "", float speed=0.0, float executeAt=None,
                          bool *status)

    def set_machine_initial_angle(str name = "", float angle=0.0, bool *status)
    def set_machine_initial_speed(str name = "", float speed=0.0, bool *status)
    def set_machine_inc_encoder_offset(str name = "", float offset=0.0, bool *status)
    def set_machine_sin_encoder_offset(str name = "", float offset=0.0, bool *status)

    def set_pe_switching_block_control_mode(str blockName="", str switchName="",
                                            bool swControl=True, float executeAt=None,
                                            bool *status)

    def set_pe_switching_block_software_value(str blockName="", str switchName="",
                                              i64 value=0, float executeAt=None,
                                              bool *status)

    def set_initial_battery_soc(str batteryName, float initialValue, bool *status)
    def set_scada_input_value(str scadaInputName, float value, bool *status)

    def set_cp_input_value(str cpCategory, str cpGroup, str cpInputName, float value, bool *status)
    def set_text_mode(str mode)
    def set_debug_level(i64 level = 0)

    def start_capture(list cpSettings, list trSettings, list chSettings, list **dataBuffer, str fileName="",  float executeAt=None, float timeout=None)

    def start_simulation(bool *status)
    def stop_simulation(bool *status)
    def capture_in_progress(bool *status)
    def timeout_occurred(bool *status)

    def read_pv_iv_curve(str name, float voltage, list *results)
    def read_analog_signal(str name = "", float *value)
    def read_analog_signals(list signals, list *values)
    def read_digital_signal(str name = "", i64 device=None, i64 *value)
    def read_digital_signals(list signals, list *results)
    def read_digital_input(i64 pinNum=1, i64 device = 0, i64 *value)

    def wait_sec(i64 sec)
    def wait_msec(i64 msec)
    def wait_on_user() 
    def end_script_by_user()

    def reset_flag_status(str flag, i64 device=0, bool *status)
    def get_cp_output_value(str cpCategory, str cpGroup, str cpOutputName, float *value)
    def get_scada_output_value(str scadaOutputName, float *value)
    def get_battery_soc(str batteryName, float *value)
    def get_pv_mpp(str name, list *results)

    def get_sim_step(i64 device=0, float *value)
    def get_sim_time(i64 device=0, float *value)
    def get_hw_info(list *hw_info)

    def get_flag_status(str flag, i64 device=0, bool *status)
    def get_sources(list *sources)
    def get_pvs(list *pvs)
    def get_analog_signals(list *signals)
    def get_digital_signals(list *signals)
    def get_contactors(list *contractors)
    def get_machines(list *machines)
    def get_pe_switching_blocks(list *blocks)

    def get_source_settings(str name, dict *settings)
    def get_pv_panel_settings(str name, dict *settings)
    def get_machine_settings(str name, dict *settings)
    def get_pe_switching_block_settings(str blockName="", str switchName="",
                                        dict *settings)
    def get_contactor_settings(str name, dict *settings)
    def get_analog_output_settings(i64 channel, i64 device=0, dict *settings)
    def get_digital_output_settings(i64 channel, i64 device=0, dict *settings)
    def get_cp_input_settings(str cpCategory, str cpGroup, str cpInputName, dict *settings)
    def get_scada_input_settings(str scadaInputName, dict *settings)

    def get_hil_serial_number(list *serialNumbers)
    def available_sources(bool *status)
    def available_pvs(bool *status)
    def available_analog_signals(bool *status)
    def available_digital_signals(bool *status)
    def available_contactors(bool *status)
    def available_machines(bool *status)
    def available_pe_switching_blocks(bool *status)
]