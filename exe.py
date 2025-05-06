def convert(feets,inches):
    feets_in_inches = float(feets) * 12
    total_inches = feets_in_inches + float(inches)
    meters= total_inches * 0.0254
    return f"{meters}m"