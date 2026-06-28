"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    if temperature<800 and neutrons_emitted>500 and (temperature*neutrons_emitted)<500000:
        return True
    else:
        return False

def reactor_efficiency(voltage, current, theoretical_max_power):
    power=current*voltage
    efficency =(power/theoretical_max_power)*100
    if efficency>=80:
        return "green"
    elif efficency>=60:
        return "orange"
    elif efficency>=30:
        return "red"
    elif efficency>=0:
        return "black"
def fail_safe(temperature, neutrons_produced_per_second, threshold):
    right_now=temperature*neutrons_produced_per_second
    danger=right_now/threshold
    danger = danger*100
    if danger<90:
        return "LOW"
    elif danger<= 110:
        return "NORMAL"
    else:
        return "DANGER"
