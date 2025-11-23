def calculate_risk(p):
    risk = []
    if p['bp_sys'] >= 140 or p['bp_dia'] >= 90:
        risk.append('High BP')
    if p['sugar'] >= 126:
        risk.append('High Sugar')
    if p['bmi'] >= 25:
        risk.append('Overweight')
    if len(risk) >= 2 or (p['age'] > 45 and 'High BP' in risk):
        return "HIGH RISK: " + ', '.join(risk)
    elif risk:
        return "Needs checkup: " + ', '.join(risk)
    else:
        return "Normal"
