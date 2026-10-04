def check_short_circuit(pole1,pole2):

    status="SAFE"

    if pole1>0.9 or pole2>0.9:

        status="DANGER"

    elif pole1>0.6 or pole2>0.6:

        status="WARNING"

    return status