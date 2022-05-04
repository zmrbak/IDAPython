import idc
import idautils


def main():
    print('This is From PyCharm')
    print("This is from PyCharm tool")
    for seg in idautils.Segments():
        name = idc.get_segm_name(seg)
        start = idc.get_segm_start(seg)
        end = idc.get_segm_end(seg)
        print(name, start, end)


if __name__ == '__main__':
    main()
