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


def show_segments():
    for seg in idautils.Segments():
        segm_name = idc.get_segm_name(seg)
        segm_start = idc.get_segm_start(seg)
        segm_end = idc.get_segm_end(seg)
        print(segm_name, '0x%X' % segm_start, '0x%X' % segm_end, (segm_end - segm_start))


if __name__ == '__main__':
    clear_screen()
    show_segments()
