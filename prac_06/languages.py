from prac_06.programming_language import ProgrammingLanguage

fields = []
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
fields.append(python)
fields.append(ruby)
fields.append(visual_basic)
print(python)
print('The dynamically typed languages are:')
for field in fields:
    if ProgrammingLanguage.is_dynamic(field):
        print(field.field)


