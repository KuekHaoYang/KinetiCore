import math
import sys
from datetime import datetime
from typing import Dict, List, Tuple
import json
import csv
from colorama import Fore, Style, init

init(autoreset=True)

class KineticCore:
    
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
        """Enhanced normalization using relativistic velocity mapping"""
        x = value / reference
        return x / math.sqrt(1 + x**2)

    def _temporal_adjustment(self, component: str) -> float:
        """Hybrid growth model combining logistic and exponential components"""
        growth_params = {
            'cpu_sc': {'base': 1.18, 'k': 0.4, 'carrying_capacity': 2.8},
            'cpu_mc': {'base': 1.22, 'k': 0.35, 'carrying_capacity': 3.2},
            'gpu': {'base': 1.35, 'k': 0.3, 'carrying_capacity': 4.0}
        }
        params = growth_params.get(component, {'base': 1.0, 'k': 0.0, 'carrying_capacity': 1.0})
        
        years_since_ref = (datetime.now().year - 2023) + (datetime.now().month - 1)/12.0
        
        # Logistic component
        logistic = params['carrying_capacity'] / (1 + math.exp(-params['k'] * years_since_ref))
        
        # Exponential component
        exponential = params['base'] ** years_since_ref
        
        # Blending function with dynamic weighting
        blend_ratio = math.tanh(years_since_ref/4)
        return logistic * blend_ratio + exponential * (1 - blend_ratio)

    def _calculate_entanglement(self, components: Dict[str, float]) -> float:
        """Multi-dimensional performance synthesis with synergy factors"""
        time_aware_refs = {
            k: v * self._temporal_adjustment(k)
            for k, v in self.REFERENCE_EPOCH.items()
            if k in ['cpu_sc', 'cpu_mc', 'gpu']
        }

        # Component normalization with GPU-specific shaping
        norms = {
            'cpu_sc': self._quantum_normalize(components['cpu_sc'], time_aware_refs['cpu_sc']),
            'cpu_mc': self._quantum_normalize(components['cpu_mc'], time_aware_refs['cpu_mc']),
            'gpu': (self._quantum_normalize(components['gpu'], time_aware_refs['gpu'])) ** 1.3
        }

        # Balance calculation using geometric harmony index
        norms_list = list(norms.values())
        geomean = math.exp(sum(math.log(v + 1e-9) for v in norms_list) / 3)
        arithmean = sum(norms_list) / 3
        harmony = geomean / (arithmean + 1e-9)
        balance = math.exp(3.0 * (harmony - 1))

        # Thermal penalty with non-linear scaling
        tdp_ratio = components.get('thermal', 150) / self.REFERENCE_EPOCH['thermal']
        thermal_excess = max(0, tdp_ratio - 1)
        self.thermal_penalty = 0.12 * thermal_excess ** 1.7 / (1 + 0.5 * thermal_excess)

        # Composite score calculation with synergy factors
        synergy = 1.0 + 0.2 * math.tanh(5 * (min(norms.values()) - 0.6))
        base_score = 100 * synergy * (
            (norms['cpu_sc'] ** self.harmonic_weights['cpu_sc']) *
            (norms['cpu_mc'] ** self.harmonic_weights['cpu_mc']) *
            (norms['gpu'] ** self.harmonic_weights['gpu']) *
            (balance ** self.harmonic_weights['balance'])
        )

        return base_score * (1 - self.thermal_penalty)

    def analyze(self, components: Dict[str, float]) -> Dict:
        """Analyze system performance and generate detailed report"""
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
        """Classify performance into predefined strata"""
        for threshold, name, desc, color in self.PERFORMANCE_STRATA:
            if score >= threshold:
                return (f"{color}{name}{Style.RESET_ALL}", desc, color)
        return ("Unclassified", "Unknown category", Fore.WHITE)

    def _generate_component_report(self, components: Dict) -> List[Dict]:
        """Generate detailed component analysis report"""
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
    print(f"\n{Fore.CYAN}=== KineticCore Performance Evaluation ==={Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Understand your system's power at a glance{Style.RESET_ALL}\n")
    
    core = KineticCore()
    
    try:
        components = {
            'cpu_sc': float(input(f"{Fore.WHITE}Single-Core Score: {Style.RESET_ALL}")),
            'cpu_mc': float(input(f"{Fore.WHITE}Multi-Core Score: {Style.RESET_ALL}")),
            'gpu': float(input(f"{Fore.WHITE}OpenCL Score: {Style.RESET_ALL}")),
            'thermal': float(input(f"{Fore.WHITE}TDP (Watts) [Default 150]: {Style.RESET_ALL}") or 150)
        }

        results = core.analyze(components)
        
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
            filename = f"kineticcore_report_{timestamp}.{export_choice}"
            
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