package typhoon_api version=0.1

typedef HardwareSettings[
    str hw_product_name
    str hw_revision
    i32 configuration_id
]

interface schematic_api[

    def get_hw_settings(list<HardwareSettings> *hw_settings)
    def get_settings(dict<i64, set<HardwareSettings>> *settings)
]

interface hil_api [
    def start_capture(list<i32> cp_settings, list<list<i32>> tr_settings, list<list<list<i32>>> ch_settings,
                      str file_name, str execute_at=None, i32 timeout=None,
                      list **data_buffer)

    def read_analog_signals(list<dict> **signals)
    def read_analog_signals(list<dict<i32, str>> **signals)
]
