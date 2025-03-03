def analyze_log(fileName):
    ip_count = {}
    error_count = {}
    with open(fileName,"r") as file:
        for line in file:
            parts = line.split()
            ip = parts[0]
            if ip in ip_count:
                ip_count[ip] += 1
            else:
                ip_count[ip] = 1
            error = parts[-1]
            if error in error_count:
                error_count[error] += 1
            else:
                error_count[error] = 1
    return ip_count, error_count
    