import datetime
import idc
import idautils
import idaapi


def clear_screen():
    window = idaapi.find_widget('Output window')
    idaapi.activate_widget(window, True)
    idaapi.process_ui_action('msglist:Clear')
    print('-' * 10, datetime.datetime.now(), '-' * 10)


def show_function_item():
    ea = idc.here()
    print(hex(ea))

    next_head = idc.next_head(ea)
    next_addr = idc.next_addr(ea)
    print(hex(next_head), hex(next_addr))

    # idaapi.get_item
    # address_list = idautils.FuncItems(ea)
    # print(len(list(items)))

    # for address in address_list:
    #     dis_assembly = idc.GetDisasm(address)
    #     item_head = idc.get_item_head(address)
    #     item_end = idc.get_item_end(address)
    #     item_size = idc.get_item_size(address)
    #     print(hex(address), dis_assembly)
    #     print(hex(item_head), hex(item_end), item_size)


if __name__ == '__main__':
    clear_screen()
    show_function_item()
