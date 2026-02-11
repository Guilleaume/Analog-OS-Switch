#!/usr/bin/env python3
#
# Poti Simulator und Treble Bleed Rechner
# Copyright (C) 2024 (Dein Name oder Gemeinschaftsprojekt)
#
# Dieses Programm ist freie Software: Sie können es unter den Bedingungen der GNU
# General Public License, wie von der Free Software Foundation veröffentlicht,
# entweder Version 3 der Lizenz oder (nach Ihrer Wahl) jeder späteren Version,
# weiterverbreiten und/oder modifizieren.
#
# Dieses Programm wird in der Hoffnung verbreitet, dass es nützlich sein wird,
# aber OHNE JEGLICHE GEWÄHRLELEISTUNG, auch ohne die implizite Gewährleistung der
# MARKTGÄNGIGKEIT oder der EIGNUNG FÜR EINEN BESTIMMTEN ZWECK.
# Siehe die GNU General Public License für weitere Einzelheiten.
#
# Eine Kopie der GNU General Public License finden Sie unter <https://www.gnu.org/licenses/>.

import tkinter as tk
from tkinter import ttk, messagebox
import math

# Standard-Widerstandswerte der E24-Reihe (in kΩ)
E24_SERIES = [
    1.0, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.7, 3.0,
    3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8, 7.5, 8.2, 9.1,
    10, 11, 12, 13, 15, 16, 18, 20, 22, 24, 27, 30, 33, 36, 39, 
    43, 47, 51, 56, 62, 68, 75, 82, 91, 100, 110, 120, 130, 150,
    160, 180, 200, 220, 240, 270, 300, 330, 360, 390, 430, 470,
    510, 560, 620, 680, 750, 820, 910, 1000, 1100, 1200, 1300,
    1500, 1600, 1800, 2000, 2200, 2400, 2700, 3000, 3300, 3600,
    3900, 4300, 4700, 5100, 5600, 6200, 6800, 7500, 8200, 9100,
    10000, 11000, 12000, 13000, 15000, 16000, 18000, 20000, 22000, 
    24000, 27000, 30000, 33000, 36000, 39000, 43000, 47000, 51000, 
    56000, 62000, 68000, 75000, 82000, 91000, 100000, 110000, 120000, 
    130000, 150000, 160000, 180000, 200000, 220000, 240000, 270000, 
    300000, 330000, 360000, 390000, 430000, 470000, 510000, 560000, 
    620000, 680000, 750000, 820000, 910000, 1000000, 
] # Erweiterung bis 1 MΩ (1000 kΩ)

# Mapping der Kondensator-Codes (pF zu nF/µF)
CAP_CODES = {
    '102': 1.0, # 1000 pF = 1.0 nF
    '202': 2.0, # 2000 pF = 2.0 nF
    '472': 4.7, # 4700 pF = 4.7 nF
    '103': 10.0, # 10 nF (0.01 µF)
    '223': 22.0, # 22 nF (0.022 µF)
    '333': 33.0, # 33 nF (0.033 µF)
    '473': 47.0, # 47 nF (0.047 µF)
    '104': 100.0, # 100 nF (0.1 µF)
}

class PotiSimulator:
    """Hauptklasse der Anwendung mit Notebook für verschiedene Tools."""
    def __init__(self, root):
        self.root = root
        self.root.title("Single-Coil Last- & Treble-Bleed Rechner")
        
        # Notebook für Tabs
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(pady=10, padx=10, expand=True, fill="both")
        
        # Tab 1: Poti Load Corrector
        self.load_corrector_frame = ttk.Frame(self.notebook, padding="10 10 12 12")
        self.notebook.add(self.load_corrector_frame, text='Lastkorrektur (Poti Loading)')
        self.setup_load_corrector(self.load_corrector_frame)

        # Tab 2: Treble Bleed Kombi-Finder
        self.treble_bleed_finder_frame = ttk.Frame(self.notebook, padding="10 10 12 12")
        self.notebook.add(self.treble_bleed_finder_frame, text='Treble Bleed Kombi')
        self.setup_treble_bleed_finder(self.treble_bleed_finder_frame)


    # --- Tab 1: Poti Load Corrector (Original-Funktionalität) ---
    
    def find_nearest_standard(self, value):
        """Findet die nächstgelegenen Standardwerte der E24-Reihe."""
        # Die nächsten 5 Standardwerte finden
        # Beachte: Die E24_SERIES ist in kΩ, der Eingabewert ist auch in kΩ
        differences = [(abs(val - value), val) for val in E24_SERIES]
        differences.sort()
        return [val for diff, val in differences[:5]]

    def setup_load_corrector(self, frame):
        """Einrichtung des Poti-Load-Correctors"""
        
        # Titel
        title = ttk.Label(frame, text="Poti-Lastkorrektur (R_parallel finden)", 
                          font=('Arial', 12, 'bold'))
        title.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Auswahl des Poti-Typs
        ttk.Label(frame, text="Wähle Poti-Typ (R_poti) [kΩ]:").grid(row=1, column=0, sticky=tk.W, pady=5)
        
        self.poti_var = tk.StringVar(value="500")
        poti_frame = ttk.Frame(frame)
        poti_frame.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Radiobutton(poti_frame, text="500 kΩ", variable=self.poti_var, value="500").pack(side=tk.LEFT)
        ttk.Radiobutton(poti_frame, text="250 kΩ", variable=self.poti_var, value="250").pack(side=tk.LEFT, padx=10)
        ttk.Radiobutton(poti_frame, text="Beliebig", variable=self.poti_var, value="custom").pack(side=tk.LEFT)
        
        # Custom Poti Eingabe
        self.custom_frame = ttk.Frame(frame)
        self.custom_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Label(self.custom_frame, text="Custom Poti (kΩ):").pack(side=tk.LEFT)
        self.custom_poti = tk.Entry(self.custom_frame, width=10)
        self.custom_poti.pack(side=tk.LEFT, padx=5)
        
        # Zielwert Eingabe
        ttk.Label(frame, text="Zielwiderstand (R_target) [kΩ]:").grid(row=3, column=0, sticky=tk.W, pady=10)
        self.target_entry = tk.Entry(frame, width=10)
        self.target_entry.grid(row=3, column=1, sticky=tk.W, pady=10)
        
        # Berechnen Button
        calc_btn = ttk.Button(frame, text="Parallelwiderstand berechnen", command=self.calculate_load)
        calc_btn.grid(row=4, column=0, columnspan=2, pady=15)
        
        # Ergebnis Anzeige
        self.result_var = tk.StringVar(value="Ergebnis erscheint hier...")
        result_label = ttk.Label(frame, textvariable=self.result_var, 
                                 font=('Arial', 11), foreground='blue')
        result_label.grid(row=5, column=0, columnspan=2, pady=10, sticky=tk.W)
        
        # Standardwerte Anzeige
        self.standard_var = tk.StringVar(value="Verfügbare Standardwerte erscheinen hier")
        standard_label = ttk.Label(frame, textvariable=self.standard_var,
                                     font=('Arial', 10), foreground='green')
        standard_label.grid(row=6, column=0, columnspan=2, pady=5, sticky=tk.W)
        
        # Bind Events
        self.poti_var.trace('w', lambda *args: self.toggle_custom(self.custom_frame, self.poti_var))
        self.toggle_custom(self.custom_frame, self.poti_var)


    def toggle_custom(self, frame, var, *args):
        """Blendet Custom-Eingabe ein/aus"""
        if var.get() == "custom":
            frame.grid()
        else:
            frame.grid_remove()

    def calculate_load(self):
        """Berechnet den benötigten Parallelwiderstand R_parallel."""
        try:
            # Poti-Wert bestimmen
            if self.poti_var.get() == "custom":
                poti_value = float(self.custom_poti.get().replace(',', '.'))
            else:
                poti_value = float(self.poti_var.get())
            
            # Zielwert auslesen
            target_value = float(self.target_entry.get().replace(',', '.'))
            
            # Validierung
            if poti_value <= 0 or target_value <= 0:
                messagebox.showerror("Fehler", "Werte müssen größer als 0 sein!")
                return
            
            if target_value >= poti_value:
                messagebox.showerror("Fehler", 
                    "Zielwert muss kleiner als Poti-Wert sein, um die Last zu reduzieren!")
                return
            
            # Berechnung: R_parallel = (R_poti * R_target) / (R_poti - R_target)
            R_parallel = (poti_value * target_value) / (poti_value - target_value)
            
            # Nächstgelegene Standardwerte finden
            nearest_standard = self.find_nearest_standard(R_parallel)
            
            # Ergebnis anzeigen
            self.result_var.set(
                f"Berechneter Parallelwiderstand (R_parallel): {R_parallel:,.2f} kΩ"
            )
            
            # Standardwerte anzeigen
            standard_text = "Nächstliegende E24-Standardwerte (R_parallel) [kΩ]:\n"
            
            for i, std_val in enumerate(nearest_standard, 1):
                # Tatsächlichen Gesamtwiderstand mit Standardwert berechnen
                actual_R = (poti_value * std_val) / (poti_value + std_val)
                difference = ((actual_R - target_value) / target_value) * 100
                
                # Formatierung für kΩ
                if std_val >= 1000:
                    std_val_str = f"{std_val / 1000:,.1f} MΩ"
                else:
                    std_val_str = f"{std_val:,.0f} kΩ"
                    
                standard_text += (
                    f"-> Wähle {std_val_str}: Gesamtwiderstand beträgt {actual_R:,.2f} kΩ "
                    f"({difference:+.2f}% Abweichung vom Ziel)\n"
                )
            
            self.standard_var.set(standard_text)
            
        except ValueError:
            messagebox.showerror("Fehler", "Bitte gültige Zahlen eingeben!")
        except ZeroDivisionError:
            messagebox.showerror("Fehler", "Ungültige Werte-Kombination!")

    # --- Tab 2: Treble Bleed Kombi-Finder (Neue Funktionalität) ---
    
    def setup_treble_bleed_finder(self, frame):
        """Einrichtung des Treble-Bleed-Kombi-Finders"""
        
        # Titel
        title = ttk.Label(frame, text="Treble Bleed Kombi-Finder (C & R)", 
                          font=('Arial', 12, 'bold'))
        title.grid(row=0, column=0, columnspan=2, pady=(0, 15))

        # Empfehlungen
        recommendation = ttk.Label(frame, text=(
            "Standard-Empfehlungen:\n"
            "- Lindy Fralin Stil: C = 2nF (Code 202) + R = 220 kΩ (Seriell)\n"
            "- Vintage Stil: C = 1nF (Code 102) ohne R\n"
            "- Fender Stil: C = 1.2nF (Code 122) + R = 150 kΩ (Parallel)"
        ), foreground='gray')
        recommendation.grid(row=1, column=0, columnspan=2, pady=(0, 15), sticky=tk.W)

        # C-Wert Eingabe
        ttk.Label(frame, text="Gewünschter Kondensator (Code z.B. 102):").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.cap_code_entry = tk.Entry(frame, width=10)
        self.cap_code_entry.grid(row=2, column=1, sticky=tk.W, pady=5)

        # R-Wert Eingabe
        ttk.Label(frame, text="Gewünschter Widerstand (R) [kΩ]:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.resistor_entry = tk.Entry(frame, width=10)
        self.resistor_entry.grid(row=3, column=1, sticky=tk.W, pady=5)

        # Poti-Wert für Treble Bleed
        ttk.Label(frame, text="Volume Poti [kΩ]:").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.tb_poti_var = tk.StringVar(value="250")
        poti_frame = ttk.Frame(frame)
        poti_frame.grid(row=4, column=1, sticky=(tk.W, tk.E), pady=5)
        ttk.Radiobutton(poti_frame, text="250 kΩ", variable=self.tb_poti_var, value="250").pack(side=tk.LEFT)
        ttk.Radiobutton(poti_frame, text="500 kΩ", variable=self.tb_poti_var, value="500").pack(side=tk.LEFT, padx=10)

        # Berechnen Button
        calc_btn = ttk.Button(frame, text="Kombination prüfen", command=self.calculate_treble_bleed)
        calc_btn.grid(row=5, column=0, columnspan=2, pady=15)
        
        # Ergebnis Anzeige
        self.tb_result_var = tk.StringVar(value="Ergebnis erscheint hier...")
        result_label = ttk.Label(frame, textvariable=self.tb_result_var, 
                                 font=('Arial', 11), foreground='blue')
        result_label.grid(row=6, column=0, columnspan=2, pady=10, sticky=tk.W)

    def capacitor_code_to_nf(self, code):
        """Konvertiert Kondensator-Code (z.B. '102') in nF."""
        if code in CAP_CODES:
            return CAP_CODES[code]
        
        if len(code) == 3 and code.isdigit():
            # Basiswert (erste 2 Ziffern) * 10^Multiplikator (dritte Ziffer)
            base = int(code[:2])
            multiplier = int(code[2])
            pF = base * (10 ** multiplier)
            # Konvertierung von pF zu nF (geteilt durch 1000)
            return pF / 1000.0
        
        return None

    def calculate_treble_bleed(self):
        """Analysiert die eingegebene Treble-Bleed-Kombination."""
        try:
            # Werte auslesen
            cap_code = self.cap_code_entry.get().strip()
            R_value_k = float(self.resistor_entry.get().replace(',', '.'))
            R_poti = float(self.tb_poti_var.get())
            
            C_nF = self.capacitor_code_to_nf(cap_code)
            
            if C_nF is None:
                messagebox.showerror("Fehler", f"Ungültiger Kondensator-Code: {cap_code}!")
                return
            
            if R_value_k < 0:
                messagebox.showerror("Fehler", "R-Wert muss >= 0 sein!")
                return

            # Nächstgelegenen E24 R-Wert finden
            nearest_R_standard = self.find_nearest_standard(R_value_k)[0]
            
            # --- Berechnung des Tiefpass-Frequenzschwerpunkts (nur für Info) ---
            # Dieser Schaltungsteil wirkt, wenn der Poti auf ca. 50% steht.
            # Für eine einfache Darstellung nehmen wir R_poti = 1/2 des Gesamtwerts
            R_eff_k = (R_value_k * R_poti) / (R_value_k + R_poti) if R_value_k > 0 else R_poti
            
            # Grenzfrequenz des Hochpasses (C in Serie mit R_poti/R_eff)
            C_Farad = C_nF * 1e-9
            R_Ohm = R_eff_k * 1000
            
            f_c = 1 / (2 * math.pi * R_Ohm * C_Farad)
            
            # Ausgabe zusammenstellen
            result_text = (
                f"Eingegebene Kombination:\n"
                f"  - Kondensator (C): {C_nF} nF (Code {cap_code})\n"
                f"  - Widerstand (R): {R_value_k:,.0f} kΩ\n\n"
                f"Nächstliegender E24 Widerstand (R): {nearest_R_standard:,.0f} kΩ\n\n"
            )
            
            # Berechnung des Gesamtwiderstands, wenn der Kondensator ignoriert wird (reiner DC-Load)
            # Dies ist relevant für den Ton bei Vol=10.
            R_total_k = (R_poti * nearest_R_standard) / (R_poti + nearest_R_standard)
            
            result_text += (
                f"Wenn R_poti ({R_poti:,.0f} kΩ) und R_Bleed ({nearest_R_standard:,.0f} kΩ) parallel geschaltet sind (Vol=10):\n"
                f"  - Resultierende DC-Last: {R_total_k:,.2f} kΩ\n\n"
                
            )
            
            self.tb_result_var.set(result_text)

        except ValueError:
            messagebox.showerror("Fehler", "Bitte gültige Zahlen (für R) eingeben!")
        except Exception as e:
            messagebox.showerror("Fehler", f"Ein unbekannter Fehler ist aufgetreten: {e}")

# Programm starten
if __name__ == "__main__":
    root = tk.Tk()
    app = PotiSimulator(root)
    root.mainloop()
