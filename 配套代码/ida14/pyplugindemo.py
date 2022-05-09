import sys
from datetime import datetime

import ida_idaapi
import idaapi
import idautils
import idc


def PLUGIN_ENTRY():
    """
    Required plugin entry point for IDAPython plugins.
    """
    return PyPluginDemo()


def clear_screen():
    window = idaapi.find_widget('Output window')
    idaapi.activate_widget(window, True)
    idaapi.process_ui_action('msglist:Clear')
    print('-' * 10, datetime.now(), '-' * 10)


class PyPluginDemo(ida_idaapi.plugin_t):
    """
    The IDA Patching plugin stub.
    """
    # ida_idaapi.PLUGIN_HIDE |
    flags = ida_idaapi.PLUGIN_PROC | ida_idaapi.PLUGIN_UNL
    comment = "A plugin of PyPluginDemo"
    help = "A help of PyPluginDemo"
    wanted_name = "PyPluginDemo"
    wanted_hotkey = "alt+9"

    # --------------------------------------------------------------------------
    # IDA Plugin Overloads
    # --------------------------------------------------------------------------

    def __init__(self):
        self.count_sub = 0
        self.count_unknown = 0
        self.count_named = 0

    def init(self):
        clear_screen()
        print('*' * 10, 'PyPluginDemo init...', self.wanted_name)
        return ida_idaapi.PLUGIN_KEEP

    def run(self, arg):
        print('*' * 10, 'PyPluginDemo run...', self.wanted_name)
        self.function_statistics()

    def term(self):
        print('*' * 10, 'PyPluginDemo term...', self.wanted_name)

    def function_statistics(self):
        for func in idautils.Functions():
            func_name = idc.get_func_name(func)
            if func_name.startswith('sub_'):
                self.count_sub += 1
                continue
            if func_name.startswith('unknown_'):
                self.count_unknown += 1
                continue
            self.count_named += 1

        print('functions start with "sub_"', self.count_sub)
        print('functions start with "unknown_"', self.count_unknown)
        print('functions named', self.count_named)
