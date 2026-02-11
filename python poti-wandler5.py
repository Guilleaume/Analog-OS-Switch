# Guitar Load & Treble Bleed Calculator (v1.2p Series)

This repository contains tools and documentation for the **v1.2p Guitar Wiring Kernel**, specifically designed for high-performance Single-Coil environments.

## 🎸 The Project
The v1.2p series focuses on a **dual-boot wiring standard**:
- **Normal Mode:** 50s wiring (Push-pot pressed).
- **Modern Mode:** Modern wiring (Push-pot pulled).
- **Optional:** Toggleable Treble-Bleed circuit.

### Featured Instruments
- **ST0001 (LPB):** The original development platform for the v1.2p kernel. Features series-switched Neck and Bridge pickups.
- **ST0002 (Seafoam Green):** Second production unit of the v1.2p series.
- **Gax 70 "Yato" v1.0:** The experimental precursor.

## 🖥️ The Python Tool: `poti-wandler5.py`
To achieve an authentic humbucker response when switching to **Series-Mode**, the system must correct the parallel load from **125k back to 250k**. This prevents "choking" the high-end.

This script calculates:
1. **Parallel Load Correction:** Finds the exact resistor needed (based on the E24 series) to hit your target impedance.
2. **Treble Bleed Combination Finder:** Validates Capacitor (C) and Resistor (R) values for various styles (Fralin, Fender, Vintage).

## 🛠 Installation & Usage
1. Ensure you have Python 3.x installed.
2. Run the script:
   ```bash
   python poti-wandler5.py
