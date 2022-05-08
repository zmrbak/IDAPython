import datetime

import idc
import idautils
import idaapi


def clear_screen():
    window = idaapi.find_widget('Output window')
    idaapi.activate_widget(window, True)
    idaapi.process_ui_action('msglist:Clear')
    print('-' * 10, datetime.datetime.now(), '-' * 10)


def function_statistics():
    count_sub = 0
    count_unknown = 0
    count_named = 0
    for func in idautils.Functions():
        func_name = idc.get_func_name(func)
        if func_name.startswith('sub_'):
            count_sub += 1
            continue
        if func_name.startswith('unknown_'):
            count_unknown += 1
            continue
        count_named += 1

    print('functions start with "sub_"', count_sub)
    print('functions start with "unknown_"', count_unknown)
    print('functions named', count_named)


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    clear_screen()
    function_statistics()
