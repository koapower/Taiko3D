import csv

def osu_to_csv(osu_file, csv_file):
    with open(osu_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # 找到 [HitObjects] 段落
    hitobjects_start = None
    for i, line in enumerate(lines):
        if line.strip() == "[HitObjects]":
            hitobjects_start = i + 1
            break

    if hitobjects_start is None:
        print("找不到 [HitObjects] 段落")
        return

    hitobjects = lines[hitobjects_start:]

    # 解析 hitobjects
    parsed = []
    for idx, line in enumerate(hitobjects):
        line = line.strip()
        if not line:
            continue
        parts = line.split(",")
        if len(parts) < 5:
            continue  # 無效行

        osu_x = int(parts[0])
        osu_y = int(parts[1])
        hit_time = int(parts[2])
        param1 = int(parts[3])
        hitsound = int(parts[4])
        param3 = parts[5] if len(parts) > 5 else ""

        parsed.append([idx, osu_x, osu_y, hit_time, param1, hitsound, param3])

    # 寫出 CSV
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["RowIndex", "OsuX", "OsuY", "HitTime", "Param1", "HitSound", "Param3"])
        writer.writerows(parsed)

    print(f"轉換完成: {csv_file}")


# 使用範例
osuFileName = "Rick Astley - Never Gonna Give You Up (Besai Remix) (Koalazy) [testt]"
csvFileName = "testmap"
osu_to_csv(f"{osuFileName}.osu", f"{csvFileName}.csv")
