def find_paragraph(data,x,y):
    final_array = []

    while data != []:
        item = data.pop(0)
        final_array.append(item)
        copy_data = data.copy()

        while copy_data != []:
            copy_item = copy_data.pop(0)
            y_diff = copy_item[3] - final_array[-1][3]
            x_diff = copy_item[1] - final_array[-1][1]
            ok = data

            if y_diff < y and x_diff > (x * -1)  and x_diff < x:
                final_array[-1][0] = min([copy_item[0], final_array[-1][0]])
                final_array[-1][1] = max([copy_item[1], final_array[-1][1]])
                final_array[-1][2] = min([copy_item[2], final_array[-1][2]])
                final_array[-1][3] = max([copy_item[3], final_array[-1][3]])

                data.remove(copy_item)
    print(final_array)
    return final_array