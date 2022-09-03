import csv


def InNoiDungFile_CSV(filename):
    with open(filename, encoding="utf-8", newline='') as f:
        reader = csv.DictReader(f)
        data = list(reader)

    template = """                                                              DANH SÁCH CÁC TỈNH THÀNH PHỐ 
                                        CÓ BIÊN GIỚI VỚI 2 NƯỚC HOẶC VỪA CÓ BIÊN GIỚI VỚI 1 NƯỚC, VỪA CÓ GIÁP BIỂN"""
    print(template)

    template1 = "|{:<3}|{:<23}|{:<20}|{:<8}|{:<10}|{:<20}|{:<20}|{:<25} |{:<16}|"
    template2 = "|{:<3}|{:<23}{:<20}{:<8}{:<10}{:<20}{:<20}|{:<25}|{:<16}|"
    # print(['TT'] + list(data[0].keys()))
    print(template2.format('TT', '\ufeffTên khu vực', ' |Tên Tỉnh-Thành phố', '  |Dân số', '  |Diện tích',
          ' |Có biên giới với TQ', ' |Có biên giới với Lào', 'Có biên giới với Campuchia', 'Có giáp với biển'))
    dem = 0
    tong_dt = 0
    tong_ds = 0
    lst_name = []
    keyword = 'Có'

    for kv in data:
        ten_kv = kv['\ufeffTên khu vực']
        ten_tp = kv['Tên Tỉnh-Thành phố']
        ds = kv['Dân số']
        dt = kv['Diện tích']
        co_bg_vs_tq = kv['Có biên giới với TQ']
        co_bg_vs_lao = kv['Có biên giới với Lào']
        co_bg_vs_campuchia = kv['Có biên giới với Campuchia']
        co_giap_bien = kv['Có giáp với biển']

        if (co_bg_vs_tq == co_bg_vs_lao and co_bg_vs_lao == keyword) or \
            (co_bg_vs_lao == co_bg_vs_campuchia and co_bg_vs_campuchia == keyword) or \
                (co_bg_vs_campuchia == co_bg_vs_tq and co_bg_vs_tq == keyword) or \
                (co_giap_bien == keyword and any(x == keyword for x in (co_bg_vs_tq, co_bg_vs_lao, co_bg_vs_campuchia))):
            dem += 1
            info = (dem, ten_kv, ten_tp, ds, dt, co_bg_vs_tq,
                    co_bg_vs_lao, co_bg_vs_campuchia, co_giap_bien)
            print(template1.format(*info))
            tong_dt += eval(dt)
            tong_ds += eval(ds)
            lst_name.append(kv)

    print(
        f"\t\t\t\tTổng cộng gồm {dem} Tỉnh-Thành phố, với tổng diện tích là {tong_dt:.1f} và tổng dân số là {tong_ds}")

    return lst_name


def GhiFile_CSV(listname, filename="ketqua.csv"):
    with open(filename, encoding="utf-8", newline='', mode='w') as fw:
        headers = list(listname[0].keys())

        writer = csv.DictWriter(fw, fieldnames=headers)

        writer.writeheader()
        for row in listname:
            writer.writerow(row)


if __name__ == "__main__":
    try:
        lstname = InNoiDungFile_CSV("Data_DiaLyVietNam.csv")
        GhiFile_CSV(lstname)
    except Exception:
        print("Da xay ra loi, vui long thu lai!")
