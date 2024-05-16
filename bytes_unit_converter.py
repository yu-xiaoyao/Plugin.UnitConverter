import math

bytes_units = ["bit", "Bytes", "KB", "MB", "GB", "TB", "PB", "EB"]


# https://www.toolhelper.cn/Digit/UnitConvert?tab=byte
# https://33tool.com/byte/
def detect_units(input_value: str):
    str_len = len(input_value)
    if input_value.endswith("/bit"):
        input_val = input_value[:str_len - 4]
        detect_idx = 0
    elif input_value.endswith("/bytes") or input_value.endswith("/byte") or input_value.endswith("/B"):
        input_val = input_value[:str_len - 6]
        detect_idx = 1
    elif input_value.endswith("/KB"):
        input_val = input_value[:str_len - 3]
        detect_idx = 2
    elif input_value.endswith("/MB"):
        input_val = input_value[:str_len - 3]
        detect_idx = 3
    elif input_value.endswith("/GB"):
        input_val = input_value[:str_len - 3]
        detect_idx = 4
    elif input_value.endswith("/TB"):
        input_val = input_value[:str_len - 3]
        detect_idx = 5
    elif input_value.endswith("/PB"):
        input_val = input_value[:str_len - 3]
        detect_idx = 6
    elif input_value.endswith("/EB"):
        input_val = input_value[:str_len - 3]
        detect_idx = 7
    elif input_value.isdigit():
        input_val = input_value
        detect_idx = 1
    else:
        input_val = input_value
        detect_idx = -1
    return detect_idx, input_val


def print_unit(result_list, units):
    for item in result_list:
        num = item['num']
        unit_str = units[item['unit']]
        print(num, unit_str)


def byte_unit_converter(input_value, input_idx, units, size=1024.0):
    u_size = len(units)
    bytes_num = int(input_value)
    input_idx_i = input_idx
    bytes_num_i = bytes_num

    print('input value:', bytes_num)
    print('input isdigit:', input_value.isdigit())
    print('input index:', input_idx)
    print('current unit: ', units[input_idx])

    # bit handle
    result_list = []
    if input_idx_i == 0:
        input_idx = 1
        bytes_num = bytes_num_i / 8
        result_list.append({
            'num': bytes_num,
            'unit': 1
        })

    # >
    scale_index = 1
    for index in range(input_idx + 1, u_size):
        cur_scale = int(math.pow(size, scale_index))
        scale_index += 1
        convert_result = bytes_num / cur_scale
        # result_list.append({
        #     'num': convert_result,
        #     'unit': index
        # })
        if convert_result <= 1:
            break

    # <
    scale_index = 1
    for index in range(input_idx_i, 0, -1):
        if index == 0:
            pass
        else:
            cur_scale = int(math.pow(size, scale_index))
            scale_index += 1
            convert_result = bytes_num * cur_scale
            result_list.append({
                'num': convert_result,
                'unit': index - 1
            })

    print_unit(result_list, units)
    # <

    # for i in range(len(units)):
    #     if (input_value / size) < 1:
    #         return "%.2f%s" % (input_value, units[i])
    #     input_value = input_value / size


if __name__ == '__main__':
    idx, content = detect_units('102410241024/MB')
    if idx >= 0:
        byte_unit_converter(content, idx, bytes_units)
