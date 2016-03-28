import csv


class sizing(object):
    """
    {
        "h&m" : {
            "s" : (30, 32),
            "m" : (32, 34)
        },
        "uniqlo" : {
            "s" : (30, 32),
            "m" : (32, 34)
        }
    }
    """
    sizing_dict = {}
    with open("../model/sizing.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if len(row) < 4:
                continue

            # row = [brand_name, size, low_bound, upper_bound]
            if row[0] in sizing_dict:
                sizing_dict[row[0]][row[1]] = (int(row[2]), int(row[3]))
            else:
                sizing_dict[row[0]] = {row[1]: (int(row[2]), int(row[3]))}
