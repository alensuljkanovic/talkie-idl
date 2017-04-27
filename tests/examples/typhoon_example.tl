package typhoon_api version=0.1

typedef HardwareSettings[
    str hw_product_name
    str hw_revision
    i32 configuration_id
]

interface schematic_api[

    def get_hw_settings(HardwareSettings *hw_settings)
    def set_hw_settings(HardwareSettings hw_settings)
    def set_hw_settings(str hw_product_name, str hw_revision, i32 configuration_id)
    def compile()
]

interface hil_api [
    def start_capture(list cp_setting, list tr_settings, list ch_settings,
                      str file_name, str execute_at=None, i32 timeout=None,
                      list **data_buffer)

    def read_analog_signals(list **signals)
]
