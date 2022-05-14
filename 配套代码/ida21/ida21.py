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
    # idautils.Strings()
    s = idautils.Strings()
    s.setup(strtypes=[idc.STRTYPE_C, idc.STRTYPE_C16])
    for i in s:
        if str(i).find('.db') >= 0:
            # print("%x: len=%d type=%d -> '%s'" % (i.ea, i.length, i.strtype, str(i)))
            print(hex(i.ea), str(i))


if __name__ == '__main__':
    clear_screen()
    show_action()
