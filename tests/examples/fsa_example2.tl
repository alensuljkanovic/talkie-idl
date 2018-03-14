package compile_api version=0.1

typedef Node [
    str name
    list<Node> children
]

typedef AST [
    list<Node> nodes
]

interface compile_api[

    def parse(str input, AST *ast)
    def analyze_tree(AST ast)
    def optimize_tree(AST ast, AST *optimized_ast)
    def allocate_registers()
    def generate(AST ast)
    def compile(AST ast, str *code)


    /* following events are automatically added:
    parse_called, parse_ok & parse_failed (from parse function)
    analyze_tree_called, analyze_tree_ok & analyze_tree_failed, etc. */


    fsa [
        start START

        state START:
            on parse_called goto PARSING

        state PARSING:
            (parse)  // can be ommited?
            on analyze_tree_called goto ANALYSING
            on parse_failed_called goto START

        state ANALYSING:
            (analyze_tree)
            on optimize_tree_called goto OPTIMISING

        state OPTIMISING:
            (optimize_tree)
            on compile_called goto COMPILING

        state COMPILING:
            (allocate_registers, generate, compile)
            on compile_ok goto START
            on compile_failed goto START

    ]
]