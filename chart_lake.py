import re

years, depths, muds = [], [], []

print("=============================================")
print("      EXTRACTING GEOLOGICAL DATA LOGS        ")
print("=============================================")

with open("lake_history_report.txt", "r") as f:
    for line in f:
        if "Year:" in line:
            year = int(re.search(r"Year:\s*(\d+)", line).group(1))
            depth = float(re.search(r"Depth:\s*([\d\.]+)", line).group(1))
            mud = float(re.search(r"Mud Layer:\s*([\d\.]+)", line).group(1))
            
            years.append(year)
            depths.append(depth)
            muds.append(mud)

print(f"✓ Parsed {len(years)} entries successfully.")
print("\n=============================================")
print("   VISUAL TREND TRENDLINE: SILT ACCUMULATION")
print("=============================================")
print("  Year | Silt Layer Thickness (Scale: 1 '#' = 0.1m)")
print("---------------------------------------------")

for i in range(0, len(years), 10):
    y = years[i]
    m = muds[i]
    bar = "#" * int(m * 10)
    print(f"  {y} | {m:6.4f}m | {bar}")

print(f"  2026 | {muds[-1]:6.4f}m | {'#' * int(muds[-1] * 10)}")
print("---------------------------------------------")
print(" ✓ Analysis Complete: Run 'cat lake_history_report.txt' for text details.")
print("=============================================")
