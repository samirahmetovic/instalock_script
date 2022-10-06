def check_scaling(scaling):
    if (type(scaling) is not type(float)) or (type(scaling) is not type(int)):
        return 1.0

    return scaling
