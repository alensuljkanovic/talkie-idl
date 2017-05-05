package tf_inheritance version=0.1

typedef HardwareSettings[
    str hw_product_name
    str hw_revision
    i32 configuration_id
]

typedef PrettyHardwareSettings : HardwareSettings[
    float timestamp
]

interface schematic_api[

    def get_hw_settings(list<HardwareSettings> *hw_settings)

]
