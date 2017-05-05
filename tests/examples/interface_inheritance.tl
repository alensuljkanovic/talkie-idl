package interface_inheritance version=0.1

typedef HardwareSettings[
    str hw_product_name
    str hw_revision
    i32 configuration_id
]

interface getters[
    def get_hw_settings(HardwareSettings *hw_settings)
]

interface setters [
    def set_hw_settings(HardwareSettings hw_settings)
    def set_hw_settings(str hw_product_name, str hw_revision, i32 configuration_id)
]

interface getters_and_setters : getters, setters [
    def compile()
]
