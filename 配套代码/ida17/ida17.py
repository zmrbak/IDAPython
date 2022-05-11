import datetime

import idc
import idautils
import idaapi
from ida_segment import segment_t


def clear_screen():
    window = idaapi.find_widget('Output window')
    idaapi.activate_widget(window, True)
    idaapi.process_ui_action('msglist:Clear')
    print('-' * 10, datetime.datetime.now(), '-' * 10)


def show_functions():
    for func in idautils.Functions():
        func_name = idc.get_func_name(func)
        func_end = idc.get_func_attr(func, idc.FUNCATTR_END)
        func_flags = idc.get_func_attr(func, idc.FUNCATTR_FLAGS)
        # idc.get_func_flags(func)
        if func_flags & idc.FUNC_LIB:
            # if func_end - func == 5: continue
            # if func_end - func == 6: continue
            print(hex(func), func_name, hex(func_end), func_end - func, func_flags)
    idc.choose_func('please select a function')


if __name__ == '__main__':
    clear_screen()
    show_functions()
