#file = open("test.txt", "r/w/a",)
#file.read()
#file.write()
#file.close()
import log_parser as logs
import repor_generator as generateRepor

log_file = "logs.txt"

result = logs.analyze_log(log_file)
generateRepor.generator_repor(result)
#generate_report()

#with open("file.txt","r",encoding="utf-8") as file: