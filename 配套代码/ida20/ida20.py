import datetime

import ida_kernwin
import idc
import idautils
import idaapi
from ida_kernwin import read_selection


def clear_screen():
    window = idaapi.find_widget('Output window')
    idaapi.activate_widget(window, True)
    idaapi.process_ui_action('msglist:Clear')
    print('-' * 10, datetime.datetime.now(), '-' * 10)


def show_function_item():
    # ea = idc.here()
    # print(hex(ea))

    p0 = idaapi.twinpos_t()
    p1 = idaapi.twinpos_t()
    view = idaapi.get_current_viewer()
    idaapi.read_selection(view, p0, p1)
    place0 = p0.place(view)
    place1 = p1.place(view)
    print(hex(place0.ea), hex(place1.ea))
    # print(place0.ea, place1.ea)
    # ida_kernwin.idaplace_t

    print('o_void:', idc.o_void)
    print('o_reg:', idc.o_reg)
    print('o_mem:', idc.o_mem)

    # read_selection()

    start = idc.read_selection_start()
    end = idc.read_selection_end()
    if start == idc.BADADDR: return
    if end == idc.BADADDR: return

    while start <= end:
        print(hex(start), idc.GetDisasm(start))
        print(idc.print_insn_mnem(start).upper())
        # print(idc.print_operand(start, 0))
        # print(idc.print_operand(start, 1))
        print(idc.get_operand_type(start, 0))
        print(idc.get_operand_value(start, 0))

        print()
        start = idc.next_head(start)


if __name__ == '__main__':
    clear_screen()
    show_function_item()
