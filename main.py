import math
import sys
from datetime import datetime
from typing import Dict, List, Tuple
import json
import csv
from colorama import Fore, Style, init

init(autoreset=True)

class PerformanceOracle:
    
    REFERENCE_EPOCH = {
        'cpu_sc': 2800,
        'cpu_mc': 18000,
        'gpu': 45000,
        'thermal': 150
    }

    PERFORMANCE_STRATA = [
        (140, "Titan Class", "Beyond cutting-edge systems", Fore.MAGENTA),
        (120, "Quantum Elite", "Flagship workstations", Fore.BLUE),
        (100, "Dragonfire", "Extreme gaming rigs", Fore.CYAN),
        (80, "Phoenix", "Enthusiast systems", Fore.GREEN),
        (60, "Griffin", "Premium devices", Fore.YELLOW),
        (40, "Basilisk", "Productivity systems", Fore.LIGHTRED_EX),
        (20, "Chimera", "Basic computing", Fore.RED),
        (0, "Ancient", "Legacy hardware", Fore.WHITE)
    ]

    def __init__(self):
        self.harmonic_weights = {
            'cpu_sc': 0.35,
            'cpu_mc': 0.35,
            'gpu': 0.25,
            'balance': 0.05
        }
        self.thermal_penalty = 0.0

    def _quantum_normalize(self, value: float, reference: float) -> float:
        x = value / reference
        return math.tanh(math.log(x + math.sqrt(x**2 + 1)))

    def _temporal_adjustment(self, component: str) -> float:
        tech_progression = {
            'cpu_sc': 1.18,
            'cpu_mc': 1.22,
            'gpu': 1.35
        }
        months_since_ref = (datetime.now().year - 2023) * 12
        return tech_progression.get(component, 1.0) ** (months_since_ref / 12)

    def _calculate_entanglement(self, components: Dict[str, float]) -> float:
        time_aware_refs = {
            k: v * self._temporal_adjustment(k)
            for k, v in self.REFERENCE_EPOCH.items()
            if k in ['cpu_sc', 'cpu_mc', 'gpu']
        }

        norms = {
            'cpu_sc': self._quantum_normalize(components['cpu_sc'], time_aware_refs['cpu_sc']),
            'cpu_mc': self._quantum_normalize(components['cpu_mc'], time_aware_refs['cpu_mc']),
            'gpu': self._quantum_normalize(components['gpu'], time_aware_refs['gpu']) ** 1.2
        }

        mean_norm = sum(norms.values()) / 3
        variance = sum((v - mean_norm)**2 for v in norms.values()) / 3
        entropy = math.sqrt(variance) / (mean_norm + 1e-9)
        balance = math.exp(-entropy * 3.5)

        tdp_ratio = components.get('thermal', 150) / self.REFERENCE_EPOCH['thermal']
        self.thermal_penalty = max(0, (tdp_ratio - 1) * 0.15)

        base_score = 100 * (
            (norms['cpu_sc'] ** self.harmonic_weights['cpu_sc']) *
            (norms['cpu_mc'] ** self.harmonic_weights['cpu_mc']) *
            (norms['gpu'] ** self.harmonic_weights['gpu']) *
            (balance ** self.harmonic_weights['balance'])
        )

        return base_score * (1 - self.thermal_penalty)

    def analyze(self, components: Dict[str, float]) -> Dict:
        score = self._calculate_entanglement(components)
        time_factor = self._temporal_adjustment('cpu_sc')
        adjusted_score = score * time_factor
        
        return {
            'base_score': round(score, 1),
            'temporal_score': round(adjusted_score, 1),
            'thermal_penalty': round(self.thermal_penalty * 100, 1),
            'stratum': self._classify_stratum(adjusted_score),
            'components': self._generate_component_report(components)
        }

    def _classify_stratum(self, score: float) -> Tuple[str, str, str]:
        for threshold, name, desc, color in self.PERFORMANCE_STRATA:
            if score >= threshold:
                return (f"{color}{name}{Style.RESET_ALL}", desc, color)
        return ("Unclassified", "Unknown category", Fore.WHITE)

    def _generate_component_report(self, components: Dict) -> List[Dict]:
        report = []
        for comp, value in components.items():
            if comp in self.REFERENCE_EPOCH:
                ratio = value / self.REFERENCE_EPOCH[comp]
                time_adj = self._temporal_adjustment(comp)
                modern_ratio = ratio / time_adj
                
                assessment = "Modern" if modern_ratio >= 1.0 else "Legacy"
                health = min(100, max(0, (modern_ratio ** 0.5) * 100))
                
                report.append({
                    'component': comp.upper(),
                    'value': value,
                    'modernity': f"{modern_ratio:.1%}",
                    'health': f"{health:.1f}%",
                    'assessment': assessment
                })
        return report

def main():
    print(f"\n{Fore.CYAN}=== Performance Evaluation Simplified ==={Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Understand your system's power at a glance{Style.RESET_ALL}\n")
    
    oracle = PerformanceOracle()
    
    try:
        components = {
            'cpu_sc': float(input(f"{Fore.WHITE}Single-Core Score: {Style.RESET_ALL}")),
            'cpu_mc': float(input(f"{Fore.WHITE}Multi-Core Score: {Style.RESET_ALL}")),
            'gpu': float(input(f"{Fore.WHITE}OpenCL Score: {Style.RESET_ALL}")),
            'thermal': float(input(f"{Fore.WHITE}TDP (Watts) [Default 150]: {Style.RESET_ALL}") or 150)
        }

        results = oracle.analyze(components)
        
        print(f"\n{Fore.YELLOW}═══════════════════════════════════════════════")
        print(f"{Fore.CYAN}✨  Instant Rating: {results['temporal_score']:.0f}/140  ✨")
        print(f"{Fore.YELLOW}═══════════════════════════════════════════════{Style.RESET_ALL}")
        
        print(f"\n{Fore.GREEN}=== Detailed Analysis ==={Style.RESET_ALL}")
        print(f"Base Score: {Fore.CYAN}{results['base_score']}{Style.RESET_ALL}")
        print(f"Future-Adjusted Score: {Fore.BLUE}{results['temporal_score']}{Style.RESET_ALL}")
        print(f"Efficiency Penalty: {Fore.RED}-{results['thermal_penalty']}%{Style.RESET_ALL}")
        
        stratum = results['stratum']
        print(f"\nPerformance Tier: {stratum[2]}{stratum[0]}{Style.RESET_ALL}")
        print(f"Description: {stratum[1]}")
        
        simplicity_score = 100 - abs(results['thermal_penalty'])
        print(f"\n{Fore.YELLOW}User Experience Score: {Fore.CYAN}{simplicity_score:.0f}/100{Style.RESET_ALL}")

        print(f"\n{Fore.YELLOW}=== Component Analysis ==={Style.RESET_ALL}")
        for comp in results['components']:
            color = Fore.GREEN if comp['assessment'] == "Modern" else Fore.RED
            print(
                f"{Fore.WHITE}{comp['component']}:{Style.RESET_ALL} "
                f"{comp['value']} → "
                f"{color}{comp['modernity']} Modern{Style.RESET_ALL} "
                f"({comp['health']} Health)"
            )

        export_choice = input(f"\n{Fore.WHITE}Export report? (JSON/CSV/TXT): {Style.RESET_ALL}").lower()
        if export_choice in ['json', 'csv', 'txt']:
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            filename = f"perf_report_{timestamp}.{export_choice}"
            
            with open(filename, 'w') as f:
                if export_choice == 'json':
                    json.dump(results, f, indent=2)
                elif export_choice == 'csv':
                    writer = csv.DictWriter(f, fieldnames=results.keys())
                    writer.writeheader()
                    writer.writerow(results)
                else:
                    f.write(str(results))
            
            print(f"{Fore.GREEN}Report saved to {filename}{Style.RESET_ALL}")

    except ValueError as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Evaluation cancelled{Style.RESET_ALL}")
        sys.exit(0)

if __name__ == "__main__":
    main()
