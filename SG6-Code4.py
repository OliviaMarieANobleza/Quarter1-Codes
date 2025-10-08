    

def format_name(full_name):
   
    name_parts = full_name.split(',')
    
    
    first_name = name_parts[0].strip().title()
    middle_name = name_parts[1].strip().title() if len(name_parts) > 2 else ''
    last_name = name_parts[-1].strip().title()
    
    
    middle_initial = f" {middle_name[0]}." if middle_name else ''
    
 
    formatted_name = f"{last_name}, {first_name}{middle_initial}"
    
    return formatted_name

full_name = input("Enter your full name (First, Middle, Last): ")
formatted_name = format_name(full_name)
print(f"Formatted Name: {formatted_name}")
