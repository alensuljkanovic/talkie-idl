"""
This module contains code generator for Talkie IDL.
"""
import os
from jinja2 import Environment
from jinja2.loaders import FileSystemLoader
from talkie.generator import platforms
from talkie.utils import get_root_path, get_templates_path


class TalkieGenerator(object):
    """ Talkie IDL code generator."""
    def __init__(self, interface_def):
        self.interface_def = interface_def

    def _get_environment(self):
        """Loads jinja2 Environment."""
        templates_path = get_templates_path()

        templates = []
        for endpoint in self.interface_def.endpoints:
            templates.append(os.path.join(templates_path, endpoint.lang))

        env = Environment(loader=FileSystemLoader(templates))
        return env

    def _get_platform_data(self, platform):
        """Returns"""
        d = {"name": self.interface_def.name, "functions": []}

        for function in self.interface_def.functions:
            ret_type = platforms.convert_type(platform, function.ret_type)

            func_dict = {"ret_type": ret_type, "name": function.name}

            params_as_str = []
            params = []
            param_names = []
            for param in function.params:
                p_type = platforms.convert_type(platform, param.p_type)
                p_name = param.p_name
                param_names.append(p_name)
                if platforms.is_dynamic(platform):
                    params_as_str.append(p_name)
                else:
                    params_as_str.append("%s %s" % (p_type, p_name))

                params.append({"p_type": p_type, "p_name": p_name})

            params_str = ", ".join(params_as_str)
            func_dict["parameters"] = params_str
            func_dict["params"] = params
            func_dict["param_names"] = ", ".join(param_names)
            func_dict["def_ret_val"] = platforms.get_def_ret_val(platform, function.ret_type)
            d["functions"].append(func_dict)

        return d

    def generate(self):
        """Generates code."""
        env = self._get_environment()

        src_gen_path = os.path.join(get_root_path(), "talkie", "generator",
                                    "src-gen")

        for endpoint in self.interface_def.endpoints:
            platform = endpoint.lang
            d = {
                "endpoint": {
                    "ip": endpoint.ip,
                    "role": endpoint.role,
                    "port": endpoint.port,
                    "lang": endpoint.lang,
                    "name": endpoint.name
                },
                "client": "client",
                "server": "server",
                "interface_name": self.interface_def.name
            }
            d.update(self._get_platform_data(platform))
            file_ext = platforms.get_file_ext(platform)
            number_of_modules = platforms.get_numb_of_modules(platform)

            # Create folder where files for this endpoint will be generated
            folder_path = os.path.join(src_gen_path, endpoint.name)
            try:
                os.mkdir(folder_path)
                try:
                    init_file = platforms.get_init_file(platform) + file_ext
                    init_path = os.path.join(src_gen_path, endpoint.name,
                                             init_file)
                    file = open(init_path, mode="w+",encoding="utf-8")
                    file.write("")
                    file.close()
                except KeyError:
                    # Init file doesn't exist for this platform.
                    pass
                except IOError:
                    raise Exception("Failed to create init file for "
                                    "'{endpoint}'".format(
                        endpoint=endpoint.name))
            except OSError:
                raise Exception("Failed to make directory for '%s'"
                                % endpoint.name)

            #
            # Generate interface file
            #
            interface_template_name = "%s_interface.template" % platform

            interface_name = self.interface_def.name
            if number_of_modules != platforms.MULT_MODULES:
                interface_name += endpoint.name

            module_name = platforms.get_module_name(platform, interface_name)
            file_name = "%s%s" % (module_name, file_ext)
            file_path = os.path.join(folder_path, file_name)
            interface_tm = env.get_template(interface_template_name)
            interface_tm.stream(d=d).dump(file_path)

            if number_of_modules == platforms.MULT_MODULES:
                #
                # Generate stub file
                #
                module_name = platforms.get_module_name(platform,
                                                        endpoint.name +"Stub")
                stub_name = "%s_%s_stub.template" % (platform, endpoint.role)
                file_name = "%s%s" % (module_name, file_ext)
                file_path = os.path.join(folder_path, file_name)
                stub_tm = env.get_template(stub_name)
                stub_tm.stream(d=d).dump(file_path)
                #
                # Generate client/server/peer file
                #
                module_name = platforms.get_module_name(platform,
                                                        endpoint.name)
                if endpoint.role == platforms.ROLE_CLIENT:
                    client_name = "%s_client.template" % platform
                    file_name = "%s%s" % (module_name, file_ext)
                    file_path = os.path.join(folder_path, file_name)
                    client_tm = env.get_template(client_name)
                    client_tm.stream(d=d).dump(file_path)
                elif endpoint.role == platforms.ROLE_SERVER:
                    server_name = "%s_server.template" % platform
                    file_name = "%s%s" % (module_name, file_ext)
                    file_path = os.path.join(folder_path, file_name)
                    server_tm = env.get_template(server_name)
                    server_tm.stream(d=d).dump(file_path)
