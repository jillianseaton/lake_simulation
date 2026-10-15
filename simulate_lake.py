import random
import re

print("=============================================")
print("  ADVANCED LAKE ROAD DECISION ENGINE (v2.0) ")
print("=============================================")

try:
    depth = float(input("Enter initial 1901 Lake Depth (meters): "))
    mud_rate_mm = float(input("Enter baseline Annual Mud Accumulation (mm/year): "))
    era1_fac = float(input("Era 1 Activity Factor (1901-1945) [0.5 - 2.5]: "))
    era2_fac = float(input("Era 2 Activity Factor (1946-1990) [1.0 - 3.0]: "))
    era3_fac = float(input("Era 3 Activity Factor (1991-2026) [1.0 - 5.0]: "))
except ValueError:
    print("Invalid input. Reverting to default metrics.")
    depth, mud_rate_mm, era1_fac, era2_fac, era3_fac = 25.0, 8.0, 1.0, 2.0, 2.5

mud_rate_m = mud_rate_mm / 1000.0
total_mud_m = 0.0
random.seed()

with open("lake_history_report.txt", "w") as f:
    f.write("=============================================\n")
    f.write("  UPGRADED ADVANCED ENGINEERING SIMULATION\n")
    f.write("=============================================\n")
    
    for year in range(1901, 2027):
        if year <= 1945:
            era = "Early Industrial"
            current_erosion = mud_rate_m * era1_fac
        elif year <= 1990:
            era = "Infrastructure Expansion"
            current_erosion = mud_rate_m * era2_fac
        else:
            era = "Modern Eco-Management"
            current_erosion = mud_rate_m * era3_fac
            
        disaster_log = ""
        if random.random() < 0.015:
            disaster_type = random.choice(["SEVERE MUDSLIDE", "DAM BREACH RUNOFF", "FLASH FLOOD EROSION"])
            spike_magnitude = random.uniform(0.15, 0.45)
            current_erosion += spike_magnitude
            disaster_log = f" [! DISASTER: {disaster_type} (+{spike_magnitude*1000:.1f}mm)]"

        total_mud_m += current_erosion
        depth -= current_erosion
        if depth < 0: depth = 0

        if total_mud_m < 0.5:
            capacity_tons = 40.0
            status = "STABLE BEARING BRACKET"
        elif total_mud_m < 1.5:
            capacity_tons = 24.0
            status = "CAUTION: MINOR SETTLEMENT RISK"
        elif total_mud_m < 2.5:
            capacity_tons = 12.0
            status = "WARNING: STRUCTURAL MITIGATION REQUIRED"
        else:
            capacity_tons = 3.5
            status = "CRITICAL: SOIL LIQUEFACTION / ROAD CLOSURE RISK"

        log_line = f"Year: {year} | Era: {era:<24} | Depth: {depth:7.4f}m | Mud Layer: {total_mud_m:6.4f}m | Load Limit: {capacity_tons:4.1f} Tons -> {status}{disaster_log}\n"
        f.write(log_line)
        
        if year % 20 == 0 or year == 1901 or year == 2026 or "DISASTER" in disaster_log:
            print(f" -> {log_line.strip()}")

print("\n✓ Simulation Complete! Data compiled in: lake_history_report.txt")
