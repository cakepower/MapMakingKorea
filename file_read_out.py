def menu():
    return input("===F)ile H)elp Q)uit ===")

def draw_pytagcloud(data_array):
    #data_array=["롯데리아','롯데리아', "CU"]
    from pytagcloud import create_tag_image, make_tags
    from collections import Counter

    words_count = Counter(data_array)
    counts = words_count.most_common(100)

    tags = make_tags(counts, maxsize=120)
    create_tag_image(tags, "cloud_large.png", size=(900, 600), fontname="Nanum Gothic Bold")


def draw_pytagcloud2(data_array):
    #data_array=["롯데리아','롯데리아', "CU"]
    from pytagcloud import create_tag_image, make_tags
    from collections import Counter

    words_count = Counter(data_array)
    counts = words_count.most_common(100)

    tags = make_tags(counts, maxsize=120)
    create_tag_image(tags, "cloud_large2.png", size=(900, 600), fontname="Nanum Gothic Bold")


def draw_pytagcloud3(data_array):
    #data_array=["롯데리아','롯데리아', "CU"]
    from pytagcloud import create_tag_image, make_tags
    from collections import Counter

    words_count = Counter(data_array)
    counts = words_count.most_common(100)

    tags = make_tags(counts, maxsize=120)
    create_tag_image(tags, "cloud_large3.png", size=(900, 600), fontname="Nanum Gothic Bold")


def csv_file_open3():
    filename = input("input csv filename")
    import os, csv
    x = os.path.splitext(filename)
    outputfilename = x[0] + "_out" + x[1]
    f = open(filename, "r")
    f2 = open(outputfilename, "w")

    titles_array = []
    csv_reader = csv.reader(f)
    for oneline in csv_reader:
        title_key = oneline[1]
        titles_array.append(title_key)
        pass

    f.close()
    f2.close()
    draw_pytagcloud3(titles_array)


def csv_file_open2():
    filename = input("input csv filename")
    import os, csv
    x = os.path.splitext(filename)
    outputfilename = x[0] + "_out" + x[1]
    f = open(filename, "r")
    f2 = open(outputfilename, "w")

    csv_reader = csv.reader(f)

    cnt = 0
    titles_array =[]
    titles_dic = {}
    lotte_count = 0

    while True:
        oneline = f.readline()
        if oneline == "":
            break
        cols = oneline.split(",")
        title_key = cols[1]
        titles_array.append(title_key)

                
        if title_key not in titles_dic:
            titles_dic[title_key] = 1
        else:
            titles_dic[title_key] = titles_dic[title_key] + 1

        if cols[1].find("롯데리아") >= 0:
            # lotte_count += 1
            f2.write(oneline)

    f.close()
    f2.close()

    report = open("result.txt", "w")
    for title in titles_dic:
        report.write(title + ":")
        report.write(str(titles_dic[title]))
        report.write("\n")
    report.close()

    draw_pytagcloud2(titles_array)

csv_file_open3()
