import wingdbstub
import idc
import idautils

wingdbstub.Ensure()
print('Test From Wing Pro 8')
for seg in idautils.Segments():
    name = idc.get_segm_name(seg)
    start = idc.get_segm_start(seg)
    end = idc.get_segm_end(seg)
    print(name,start,end)
