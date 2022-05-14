import datetime

import idaapi
import idautils
import idc


def clear_screen():
    window = idaapi.find_widget('Output window')
    idaapi.activate_widget(window, True)
    idaapi.process_ui_action('msglist:Clear')
    print('-' * 10, datetime.datetime.now(), '-' * 10)


def show_action():
    # ea = idc.here()
    # print(hex(ea), idaapi.get_ea_name(ea))

    name_value = idaapi.get_name_value(idc.BADADDR, 'WriteFile')
    print(name_value[0], hex(name_value[1]))

    index = 0
    for name_tuple in idautils.Names():
        index += 1
        if index > 50: return
        # ?__scrt_uninitialize_thread_safe_statics@@YAXXZ
        # print(hex(name_tuple[0]), name_tuple[1])

        # __scrt_uninitialize_thread_safe_statics(void)
        # print(hex(name_tuple[0]), idaapi.get_short_name(name_tuple[0], 0))

        # void __cdecl __scrt_uninitialize_thread_safe_statics(void)
        # print(hex(name_tuple[0]), idaapi.get_long_name(name_tuple[0], 0))

        # (10004580__scrt_uninitialize_thread_safe_statics(void)
        # print(hex(name_tuple[0]), idaapi.get_colored_short_name(name_tuple[0], 0))

        # (10004580void __cdecl __scrt_uninitialize_thread_safe_statics(void)
        # print(hex(name_tuple[0]), idaapi.get_colored_long_name(name_tuple[0], 0))

        # void __cdecl __scrt_uninitialize_thread_safe_statics(void)
        # print(hex(name_tuple[0]), idaapi.get_demangled_name(name_tuple[0], 0, 0))

        # __scrt_uninitialize_thread_safe_statics(void)
        # print(hex(name_tuple[0]), idaapi.get_nice_colored_name(name_tuple[0], 0))

    # name_ea = idc.get_name_ea(idc.BADADDR, 'WriteFile')
    # name_ea = idc.get_name_ea_simple('WriteFile')
    # print(hex(name_ea), idc.get_name(name_ea))


if __name__ == '__main__':
    clear_screen()
    show_action()
