package fsa_example version=0.1

typedef ItemHandle[
    str item_type
    str fqn
]

interface schematic_api[

    def load(str file_path, ItemHandle *model)
    def create_component(str type_name, ItemHandle parent, str name, ItemHandle *created)
    def compile()
    def close_model()

    fsa [
        start START

        state START:
            on load goto MODEL_OPENED


        state MODEL_OPENED:
            on compile or create_component goto MODEL_OPENED
            on close_model goto START

    ]
]
