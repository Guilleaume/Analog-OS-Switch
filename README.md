Introduction: The Concept of Analog-OS

Analog-OS was born from a pursuit of sonic perfection. The core mission was to fundamentally optimize the electronic infrastructure of the electric guitar. By utilizing high-quality copper wiring to minimize signal resistance and hand-selecting potentiometers through precise measurement, the goal was to provide the ideal electrical load for any given pickup.

To avoid constantly rebuilding the circuit for every test, I developed a wiring architecture that functions like a "Multi-Boot System"—allowing the player to switch between different "tonal operating systems" instantly.

The Analog-OS Switch & Modular Design

At the heart of this project is the Analog-OS Switch. Based on DPDT logic, this switch allows for an immediate toggle between 50s Wiring (for authentic, "woody" vintage frequency response) and Modern Wiring (for a stable signal when rolling back volume).

From this architecture, several modular extensions emerged, collectively known as Analog-OS-Design:

Integrated Treble-Bleed: From v1.1 onwards, the Treble-Bleed is hard-integrated into the Modern-Wiring mode. This results in an extremely effective Volume pot that maintains high-end clarity even at lower volumes.
     
Versatility for 2-Conductor Pickups: While complex switching often requires 4-conductor wiring, Analog-OS-Design brings modern sound-shaping to classic vintage pickups. Examples include the Capacitor Cascade (v1.2) or Series Switching.

The Stratocaster Application: Due to the efficiency of the Analog-OS Switch, a potentiometer slot was "freed up" in a standard Strat layout. This pot now serves as a Blending Control, allowing the Neck and Bridge pickups to be mixed continuously—even in series.

The v1.2p: Intelligent Load Correction
The evolution reached its peak with Version 1.2p. By utilizing an ON-OFF-ON toggle, I discovered a "physical gift":

In the center (OFF) position, the Tone potentiometer is completely isolated from the signal path. In a standard single-coil environment (250k pots), the parallel load of Volume and Tone usually creates an effective load of only 125k, which can "choke" the brilliance of a humbucker.

When switching two single-coils into series (Quasi-Humbucker) and using the v1.2p Bypass, the system suddenly sees a 250k load. This closely mimics the environment of a classic humbucker with the tone pot on "10." The result is a massive, open, and authentic humbucker sound.

The Analog-OS-Design is more than just a wiring diagram; it is a flexible, modular infrastructure for any guitarist looking to maximize their instrument's potential.

Planning & Hardware Constraints

The choice of version and module is naturally limited by the guitar's physical layout. Analog-OS is designed to be a flexible framework that adapts to your instrument:

Single-Cut Style (4-Pot System): These guitars are ideal for Versions 1.0 to 1.2. For 4-conductor humbuckers, you can easily implement modular additions like Spin-a-Split or Out-of-Phase. For 2-conductor pickups, the Capacitor Cascade is a powerful choice.

Telecaster Style (2-Pot System): Limited space on the control plate requires careful planning. Version 1.2p combined with Series Switching is highly effective here, provided the pickups are prepared for it (e.g., separate ground for the baseplate).

Stratocaster Style: As described above, the efficiency of the Analog-OS logic (especially when using mini-toggles) allows one of the existing tone controls in a standard Stratocaster layout to be repurposed as a versatile blending control, without adding or removing any hardware.

The Planning Workflow:
When designing your personal Analog-OS, consider these two factors:

1. Pickup Wiring: Are they 2-conductor or 4-conductor? For 2-conductor pickups, check if they are "series-ready" (isolated ground for metal covers/baseplates) or use traditional braided shield wiring.
    
2. Switching Hardware: Can you use Mini-Toggles (highly recommended for pickguard-mounted guitars) or do you need to use Push-Pull pots to preserve the original look?

The Bottom Line: While 4-conductor pickups remain the gold standard for versatility, Analog-OS finally brings advanced, switchable tone-shaping to the world of 2-conductor pickups.
--
A modular signal architecture for guitar pickups (CRTS technology).

Analog-OS (v1.2p) – Guitar Signal Architecture
"We don't change the pickup. We change the world the pickup lives in."
Analog-OS is a modular signal architecture for electric guitars. While traditional modifications often require physical intervention (such as converting vintage pickups to 4-conductor wire), Analog-OS optimizes the electrical environment—specifically the load and capacitance—surrounding the pickup.

Core System Logic
The system is based on a platform-independent wiring logic that scales across various potentiometer configurations:


Inclusive Logic: The design is specifically engineered to unlock the full potential of classic 2-conductor (braided shield) pickups without requiring physical modification.


Dual-Stack Engine (v1.1): Switchable via DPDT between Modern Wiring (including a calibrated Treble-Bleed) and 50s Wiring for maximum dynamics and vintage "woody" tones.


C-Cascade / Tone-Hack (v1.2): Dynamic capacitance management via DPDT fields, allowing users to toggle between different capacitor values (e.g., 22nF vs. 44nF) to shift the system's resonant peak.


True Bypass (v1.2p): Utilizing ON-OFF-ON switches, the center position offers a complete bypass of the tone potentiometer for an unfiltered, raw signal.

Intelligent Impedance Correction: Specialized logic for single-coil environments. When two coils are connected in series (quasi-humbucker), the system (in OFF mode) corrects the load from 125k to 250k, ensuring the sound retains its brilliance and doesn't "choke".

Documentation
This repository currently includes:


Logic Schematics: Detailed tabular pin assignments for versions 1.0 through 1.2p.


Implementation Guide: Descriptions for wire connections between DPDT switches and potentiometers.

License & Cardware
This project is licensed under the GNU General Public License v3.0 (GPL). You are free to copy, modify, and distribute it, provided that derivative works remain under the same license.

Special Clause for Commercial Users: Any party using Analog-OS for commercial purposes (e.g., installation in production instruments or sale of pre-wired harnesses) is required, in addition to the GPL, to send the author a postcard from their hometown (Legendary Cardware).

To obtain the mailing address for postcards, please contact me (markus_guilleaume@gmx.de) or via Private Message or by opening an "Issue" in this repository.

Integration Guide (English)

v1.0 & v1.1: Focuses on the switchable interaction between the Volume and Tone pots (50s vs. Modern) and the integration of the Treble-Bleed circuit.



v1.2: Introduces the Capacitor Cascade, allowing the user to toggle between two different capacitor values to shift the resonant peak.

v1.2p: Adds Intelligent Load Correction. In a single-coil environment, it prevents the signal from "choking" when coils are in series (quasi-humbucker) by correcting the parallel load from 125k back to 250k.

