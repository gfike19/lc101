sample_string = "%(name)s this should help you on your path %(other_name)s"

replacements = {"name" : "Gail", "other_name" : "-Coach Bombay"}

print(sample_string)
print(sample_string % replacements)
