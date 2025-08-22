def open_file():
    logFile = open("Log_file.txt", "r")
    return logFile
    
def read_logs(logFile):
    errors = 0
    criticals = 0   
    acceptance = 0  
    for line in logFile:
        if "ERROR" in line:
            errors = errors + 1
        elif "CRITICAL" in line:
            criticals = criticals + 1
        else:
            acceptance = acceptance + 1
    return errors, criticals, acceptance
    
def generate_report(errors, criticals, acceptance):
    print("After reviewing the logs the file displayed:")
    print("Errors:", errors)
    print("Criticals:", criticals)
    print("Passes:", acceptance)
    
def close_file(logFile):
    logFile.close()
    
def main():
    logFile = open_file()
    errors, criticals, acceptance = read_logs(logFile)
    generate_report(errors, criticals, acceptance)
    close_file(logFile)

main()
