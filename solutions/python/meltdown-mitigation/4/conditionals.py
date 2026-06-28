def is_criticality_balanced(temperature, neutrons_emitted):
    "hahahahah"
    return temperature<800 and neutrons_emitted>500 and (temperature*neutrons_emitted)<500000

def reactor_efficiency(voltage, current, theoretical_max_power):
    "hahahahah"
    power=current*voltage
    efficency =(power/theoretical_max_power)*100
    if efficency>=80:
        return "green"
    if efficency>=60:
        return "orange"
    if efficency>=30:
        return "red"
    return "black"
def fail_safe(temperature, neutrons_produced_per_second, threshold):
    "hahahahah"
    right_now=temperature*neutrons_produced_per_second
    danger=right_now/threshold
    danger = danger*100
    if danger<90:
        return "LOW"
    if danger<= 110:
        return "NORMAL"
    return "DANGER"
